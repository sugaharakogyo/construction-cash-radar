import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# 基本設定
# =========================
APP_DIR = Path(".")
USERS_FILE = APP_DIR / "pro_users.json"
USER_DATA_DIR = APP_DIR / "user_data"
USER_DATA_DIR.mkdir(exist_ok=True)

DEMO_LIMIT = 6
LINE_URL = "https://lin.ee/7m28VAs"

DEFAULT_STATE = {
    "company_name": "株式会社サンプル建設",
    "cash": 1000,
    "revenue": 900,
    "cost": 558,
    "fixed_cost": 260,
    "loan_pay": 50,
    "tax_rate": 0.30,
    "plan": "デモ（無料）",
    "calc_count": 0
}

# =========================
# PDFフォント
# =========================
try:
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
    PDF_FONT_BOLD = "HeiseiKakuGo-W5"
    PDF_FONT = "HeiseiMin-W3"
except Exception:
    PDF_FONT_BOLD = "Helvetica-Bold"
    PDF_FONT = "Helvetica"

# =========================
# 認証まわり
# =========================
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def load_users():
    if USERS_FILE.exists():
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def ensure_default_admin():
    users = load_users()
    if "admin" not in users:
        users["admin"] = {
            "password_hash": hash_password("admin1234"),
            "display_name": "管理者",
            "role": "admin"
        }
        save_users(users)

def register_user_by_admin(username: str, password: str, display_name: str = ""):
    users = load_users()
    if username in users:
        return False, "このPro IDはすでに使われています。"
    users[username] = {
        "password_hash": hash_password(password),
        "display_name": display_name or username,
        "role": "user"
    }
    save_users(users)
    return True, "Proユーザーを発行しました。"

def authenticate_user(username: str, password: str):
    users = load_users()
    user = users.get(username)
    if not user:
        return False
    return user.get("password_hash") == hash_password(password)

def get_user_info(username: str):
    users = load_users()
    return users.get(username, {})

def update_password(username: str, current_password: str, new_password: str):
    users = load_users()
    user = users.get(username)
    if not user:
        return False, "ユーザーが見つかりません。"
    if user.get("password_hash") != hash_password(current_password):
        return False, "現在のパスワードが違います。"
    users[username]["password_hash"] = hash_password(new_password)
    save_users(users)
    return True, "パスワードを変更しました。"

def admin_reset_user_password(target_username: str, new_password: str):
    users = load_users()
    if target_username not in users:
        return False, "対象ユーザーが見つかりません。"
    users[target_username]["password_hash"] = hash_password(new_password)
    save_users(users)
    return True, "パスワードを再設定しました。"

def get_user_state_file(username: str) -> Path:
    safe_name = re.sub(r'[\\/:*?"<>| ]', "_", username)
    return USER_DATA_DIR / f"{safe_name}_state.json"

# =========================
# ユーザー別 保存・読込
# =========================
def load_state_for_user(username=None):
    if username:
        save_file = get_user_state_file(username)
    else:
        save_file = APP_DIR / "demo_state.json"

    if save_file.exists():
        try:
            with open(save_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            merged = DEFAULT_STATE.copy()
            merged.update(data)
            return merged
        except Exception:
            return DEFAULT_STATE.copy()
    return DEFAULT_STATE.copy()

def save_state_for_user(username=None):
    if username:
        save_file = get_user_state_file(username)
    else:
        save_file = APP_DIR / "demo_state.json"

    data = {
        "company_name": st.session_state.get("company_name", DEFAULT_STATE["company_name"]),
        "cash": st.session_state.get("cash", DEFAULT_STATE["cash"]),
        "revenue": st.session_state.get("revenue", DEFAULT_STATE["revenue"]),
        "cost": st.session_state.get("cost", DEFAULT_STATE["cost"]),
        "fixed_cost": st.session_state.get("fixed_cost", DEFAULT_STATE["fixed_cost"]),
        "loan_pay": st.session_state.get("loan_pay", DEFAULT_STATE["loan_pay"]),
        "tax_rate": st.session_state.get("tax_rate", DEFAULT_STATE["tax_rate"]),
        "plan": st.session_state.get("plan", DEFAULT_STATE["plan"]),
        "calc_count": st.session_state.get("calc_count", DEFAULT_STATE["calc_count"])
    }
    try:
        with open(save_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def reset_state_for_user(username=None):
    for key, value in DEFAULT_STATE.items():
        st.session_state[key] = value
    save_state_for_user(username)

def change_and_save():
    username = st.session_state.get("auth_user")
    if st.session_state.get("is_pro_logged_in"):
        save_state_for_user(username)
    else:
        save_state_for_user(None)

def count_demo_use():
    if st.session_state.get("plan") == "デモ（無料）":
        current = st.session_state.get("calc_count", 0)
        st.session_state["calc_count"] = current + 1
        save_state_for_user(None)

# =========================
# 補助
# =========================
def sanitize_filename(text: str) -> str:
    text = text.strip()
    if not text:
        return "company"
    text = re.sub(r'[\\/:*?"<>|]', "_", text)
    text = text.replace(" ", "_")
    return text[:50]

# =========================
# PDF作成
# =========================
def draw_label_value(c, x, y, label, value, width=230, height=54):
    c.setFillColor(white)
    c.roundRect(x, y - height, width, height, 10, fill=1, stroke=0)
    c.setFillColor(HexColor("#475569"))
    c.setFont(PDF_FONT_BOLD, 9)
    c.drawString(x + 12, y - 16, label)
    c.setFillColor(HexColor("#0f172a"))
    c.setFont(PDF_FONT_BOLD, 16)
    c.drawString(x + 12, y - 38, value)

def create_pdf_report(
    company_name,
    today_str,
    status,
    color,
    runway,
    cash,
    revenue,
    cost,
    fixed_cost,
    loan_pay,
    tax_rate,
    gross_profit,
    operating_balance,
    estimated_tax,
    after_tax_balance,
    shortage_for_safety,
    danger_month,
    needed_sales_up,
    needed_cost_down
):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFillColor(HexColor("#eef3f8"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    c.setFillColor(HexColor("#0f172a"))
    c.roundRect(28, height - 105, width - 56, 78, 18, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont(PDF_FONT_BOLD, 20)
    c.drawString(46, height - 55, "建設キャッシュレーダー レポート")

    c.setFont(PDF_FONT, 11)
    c.drawString(46, height - 76, company_name)

    c.setFont(PDF_FONT, 9)
    c.drawRightString(width - 46, height - 76, f"出力日: {today_str}")

    c.setFillColor(HexColor(color))
    c.roundRect(28, height - 180, width - 56, 58, 16, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont(PDF_FONT_BOLD, 12)
    c.drawString(46, height - 146, "現在の資金状況")

    c.setFont(PDF_FONT_BOLD, 22)
    c.drawString(170, height - 148, status)

    c.setFont(PDF_FONT, 11)
    c.drawRightString(width - 46, height - 146, f"資金余命の目安: {min(runway, 12):.1f}ヶ月")

    card_top = height - 205
    left = 28
    card_w = width - 56
    c.setFillColor(white)
    c.roundRect(left, 150, card_w, card_top - 150, 18, fill=1, stroke=0)

    c.setFillColor(HexColor("#0f172a"))
    c.setFont(PDF_FONT_BOLD, 12)
    c.drawString(46, card_top - 22, "主要数値サマリー")

    y1 = card_top - 36
    draw_label_value(c, 46, y1, "現在の現預金残高", f"{cash:,.0f} 万円", width=150)
    draw_label_value(c, 206, y1, "月平均売上高", f"{revenue:,.0f} 万円", width=150)
    draw_label_value(c, 366, y1, "月平均原価", f"{cost:,.0f} 万円", width=150)

    y2 = y1 - 68
    draw_label_value(c, 46, y2, "月平均固定費", f"{fixed_cost:,.0f} 万円", width=150)
    draw_label_value(c, 206, y2, "月間借入返済額", f"{loan_pay:,.0f} 万円", width=150)
    draw_label_value(c, 366, y2, "概算税率", f"{tax_rate * 100:.1f} %", width=150)

    y3 = y2 - 68
    draw_label_value(c, 46, y3, "粗利益", f"{gross_profit:,.0f} 万円", width=150)
    draw_label_value(c, 206, y3, "概算納税額", f"{estimated_tax:,.0f} 万円", width=150)
    draw_label_value(c, 366, y3, "税引後月次増減額", f"{after_tax_balance:,.0f} 万円", width=150)

    y4 = y3 - 68
    draw_label_value(c, 46, y4, "営業ベース月次増減額", f"{operating_balance:,.0f} 万円", width=150)
    draw_label_value(c, 206, y4, "6ヶ月安全ライン不足額", f"{shortage_for_safety:,.0f} 万円", width=150)

    danger_text = f"{danger_month}ヶ月後" if danger_month is not None else "12ヶ月以内なし"
    draw_label_value(c, 366, y4, "資金ショート想定時期", danger_text, width=150)

    comment_y = y4 - 88
    c.setFillColor(HexColor("#e0f2fe"))
    c.roundRect(46, comment_y - 70, 470, 70, 14, fill=1, stroke=0)

    c.setFillColor(HexColor("#0f172a"))
    c.setFont(PDF_FONT_BOLD, 11)
    c.drawString(60, comment_y - 18, "経営アクションの目安")

    c.setFont(PDF_FONT, 10)
    if after_tax_balance < 0:
        c.drawString(60, comment_y - 38, f"- 売上をあと {needed_sales_up:,.0f} 万円 上げる")
        c.drawString(60, comment_y - 54, f"- 原価をあと {needed_cost_down:,.0f} 万円 下げる")
        c.drawString(280, comment_y - 38, "- 固定費や返済の見直し")
        c.drawString(280, comment_y - 54, "- 回収サイト短縮・前倒し請求")
    else:
        c.drawString(60, comment_y - 38, "- 現預金をさらに積み増す")
        c.drawString(60, comment_y - 54, "- 利益率の高い受注を優先する")
        c.drawString(280, comment_y - 38, "- 採用・設備投資判断に活用")
        c.drawString(280, comment_y - 54, "- 安全圏を維持しながら拡大")

    c.setFillColor(HexColor("#64748b"))
    c.setFont(PDF_FONT, 8)
    c.drawString(32, 26, "本レポートは建設キャッシュレーダーに基づく簡易試算です。税務・融資判断は専門家確認を推奨します。")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()

# =========================
# 初期化
# =========================
ensure_default_admin()

if "is_pro_logged_in" not in st.session_state:
    st.session_state["is_pro_logged_in"] = False
if "auth_user" not in st.session_state:
    st.session_state["auth_user"] = ""
if "auth_role" not in st.session_state:
    st.session_state["auth_role"] = ""

if "app_initialized" not in st.session_state:
    loaded = load_state_for_user(None)
    for key, value in loaded.items():
        if key not in st.session_state:
            st.session_state[key] = value
    st.session_state["app_initialized"] = True

# =========================
# CSS
# =========================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500;700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Noto Sans JP', sans-serif;
        color: #111827 !important;
    }

    .stApp { background: #eef3f8; }
    .main { background: #eef3f8; }

    .block-container {
        max-width: 900px;
        padding-top: 1rem;
        padding-bottom: 1.2rem;
    }

    .card {
        background: #ffffff;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.10);
        margin-bottom: 14px;
        border: 1px solid #dbe4ee;
    }

    .center-card {
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.14);
        margin-bottom: 14px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.25);
    }

    .big-status-font {
        font-size: 4.0rem !important;
        font-weight: 900 !important;
        margin-top: 0.3rem;
        margin-bottom: 0.3rem;
        line-height: 1;
        color: white !important;
    }

    .sub-big {
        font-size: 1.15rem;
        font-weight: 700;
        color: white !important;
    }

    .action-box {
        background: #f8fbff;
        border-left: 8px solid #2563eb;
        padding: 18px;
        border-radius: 12px;
        margin-top: 8px;
        margin-bottom: 8px;
        color: #0f172a !important;
    }

    .pro-box {
        background: linear-gradient(135deg, #111827, #1f2937);
        color: white !important;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
        margin-bottom: 12px;
        text-align: center;
    }

    .demo-box {
        background: #fff4cc;
        color: #5b4300 !important;
        padding: 16px;
        border-radius: 14px;
        border: 2px solid #f4c542;
        margin-bottom: 12px;
        text-align: center;
        font-weight: 700;
    }

    .locked-box {
        background: linear-gradient(135deg, #7c2d12, #b91c1c);
        color: white !important;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.14);
        margin-bottom: 12px;
        text-align: center;
        font-weight: 700;
    }

    .line-box {
        background: linear-gradient(135deg, #06c755, #03a84a);
        color: white !important;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.14);
        margin-bottom: 12px;
        text-align: center;
        font-weight: 700;
    }

    .csv-box {
        background: linear-gradient(135deg, #0f766e, #0f4c81);
        color: white !important;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.14);
        margin-bottom: 12px;
        text-align: center;
        font-weight: 700;
    }

    .pdf-box {
        background: linear-gradient(135deg, #7c2d12, #b91c1c);
        color: white !important;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.14);
        margin-bottom: 12px;
        text-align: center;
        font-weight: 700;
    }

    .auth-box {
        background: linear-gradient(135deg, #0f172a, #334155);
        color: white !important;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.14);
        margin-bottom: 12px;
        text-align: center;
        font-weight: 700;
    }

    .input-highlight {
        background: #f8fafc;
        border: 2px solid #cbd5e1;
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 10px;
    }

    .stMetric {
        background: #ffffff;
        padding: 14px;
        border-radius: 14px;
        border: 1px solid #d9e2ec;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        text-align: center;
        margin-bottom: 10px;
    }

    .stTextInput label, .stNumberInput label, .stSlider label {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
    }

    .stTextInput input, .stNumberInput input {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 2px solid #94a3b8 !important;
        border-radius: 12px !important;
        padding: 0.7rem 0.9rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }

    .stTextInput input:focus, .stNumberInput input:focus {
        border: 2px solid #2563eb !important;
        box-shadow: 0 0 0 1px #2563eb !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3.1rem;
        font-size: 1rem;
        font-weight: 700;
        background: #2563eb;
        color: white;
        border: none;
        box-shadow: 0 6px 14px rgba(37, 99, 235, 0.22);
    }

    .stButton > button:hover {
        background: #1d4ed8;
        color: white;
    }

    div[data-testid="stLinkButton"] a {
        width: 100%;
        display: inline-block;
        text-align: center;
        border-radius: 12px;
        padding: 0.85rem 1rem;
        background: #06c755;
        color: white !important;
        font-weight: 700;
        text-decoration: none;
        border: none;
    }

    div[data-testid="stDownloadButton"] button {
        width: 100%;
        border-radius: 12px;
        height: 3.1rem;
        font-size: 0.98rem;
        font-weight: 700;
        background: #0f766e;
        color: white;
        border: none;
    }

    .stAlert {
        margin-top: 0.3rem !important;
        margin-bottom: 0.6rem !important;
    }

    hr {
        display: none !important;
    }

    [data-testid="stVerticalBlock"] > div:empty {
        display: none !important;
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 0.8rem;
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }
        .card, .center-card { padding: 16px; border-radius: 16px; }
        .big-status-font { font-size: 3.0rem !important; }
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# タイトル
# =========================
st.title("🏗️ 建設キャッシュレーダー")
st.write("社長のための資金余命ダッシュボード。危険・注意・安定を一瞬で見える化。")
st.markdown("""
<a href="https://buy.stripe.com/あなたのURL" target="_blank"
style="
display:block;
text-align:center;
background:linear-gradient(135deg,#6366f1,#4f46e5);
color:white;
padding:18px;
border-radius:16px;
text-decoration:none;
font-weight:bold;
font-size:18px;
margin-top:10px;
">
まずは無料でお試し！🚀 気に入ったら月額9,800円
</a>
""", unsafe_allow_html=True)
# =========================
# Proログイン
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔐 Proログイン")

if st.session_state["is_pro_logged_in"]:
    st.markdown(f"""
        <div class="auth-box">
            ログイン中: <b>{st.session_state["auth_user"]}</b>
            {" / 管理者" if st.session_state["auth_role"] == "admin" else ""}
        </div>
    """, unsafe_allow_html=True)

    col_auth1, col_auth2 = st.columns(2)
    with col_auth1:
        if st.button("🔓 Proとして使う"):
            st.session_state["plan"] = "Pro（月9,800円）"
            loaded = load_state_for_user(st.session_state["auth_user"])
            for key, value in loaded.items():
                st.session_state[key] = value
            st.rerun()
    with col_auth2:
        if st.button("🚪 ログアウト"):
            st.session_state["is_pro_logged_in"] = False
            st.session_state["auth_user"] = ""
            st.session_state["auth_role"] = ""
            st.session_state["plan"] = "デモ（無料）"
            loaded = load_state_for_user(None)
            for key, value in loaded.items():
                st.session_state[key] = value
            st.rerun()
else:
    st.markdown("<div class='input-highlight'>", unsafe_allow_html=True)
    st.text_input("Pro ID を入力", key="login_id")
    st.text_input("パスワードを入力", type="password", key="login_pw")
    if st.button("🔑 ログインする"):
        login_id = st.session_state.get("login_id", "").strip()
        login_pw = st.session_state.get("login_pw", "").strip()
        if authenticate_user(login_id, login_pw):
            user_info = get_user_info(login_id)
            st.session_state["is_pro_logged_in"] = True
            st.session_state["auth_user"] = login_id
            st.session_state["auth_role"] = user_info.get("role", "user")
            st.session_state["plan"] = "Pro（月9,800円）"
            loaded = load_state_for_user(login_id)
            for key, value in loaded.items():
                st.session_state[key] = value
            st.success("ログインしました。")
            st.rerun()
        else:
            st.error("Pro ID かパスワードが違います。")
    st.markdown("</div>", unsafe_allow_html=True)
    st.caption("管理者が発行したPro IDでログインしてください。")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 管理者だけのユーザー発行
# =========================
if st.session_state.get("is_pro_logged_in") and st.session_state.get("auth_role") == "admin":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🛠️ 管理者専用：Proユーザー発行")

    st.markdown("<div class='input-highlight'>", unsafe_allow_html=True)
    st.text_input("新しいPro ID", key="admin_new_id")
    st.text_input("表示名", key="admin_new_name")
    st.text_input("初期パスワード", type="password", key="admin_new_pw")

    if st.button("👤 Proユーザーを発行"):
        new_id = st.session_state.get("admin_new_id", "").strip()
        new_name = st.session_state.get("admin_new_name", "").strip()
        new_pw = st.session_state.get("admin_new_pw", "").strip()

        if not new_id or not new_pw:
            st.warning("Pro ID と初期パスワードを入れてください。")
        elif len(new_pw) < 4:
            st.warning("初期パスワードは4文字以上にしてください。")
        else:
            ok, msg = register_user_by_admin(new_id, new_pw, new_name)
            if ok:
                st.success(msg)
            else:
                st.error(msg)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='input-highlight'>", unsafe_allow_html=True)
    st.subheader("🔁 管理者専用：ユーザーパスワード再設定")
    st.text_input("対象Pro ID", key="admin_reset_id")
    st.text_input("新しいパスワード", type="password", key="admin_reset_pw")

    if st.button("🔧 パスワード再設定"):
        target_id = st.session_state.get("admin_reset_id", "").strip()
        new_pw = st.session_state.get("admin_reset_pw", "").strip()

        if not target_id or not new_pw:
            st.warning("対象Pro IDと新しいパスワードを入れてください。")
        elif len(new_pw) < 4:
            st.warning("新しいパスワードは4文字以上にしてください。")
        else:
            ok, msg = admin_reset_user_password(target_id, new_pw)
            if ok:
                st.success(msg)
            else:
                st.error(msg)
    st.markdown("</div>", unsafe_allow_html=True)

    users = load_users()
    rows = []
    for uid, info in users.items():
        rows.append({
            "Pro ID": uid,
            "表示名": info.get("display_name", ""),
            "権限": info.get("role", "user")
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# ログインユーザーのパスワード変更
# =========================
if st.session_state.get("is_pro_logged_in"):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔑 パスワード変更")

    st.markdown("<div class='input-highlight'>", unsafe_allow_html=True)
    st.text_input("現在のパスワード", type="password", key="change_current_pw")
    st.text_input("新しいパスワード", type="password", key="change_new_pw")
    st.text_input("新しいパスワード（確認）", type="password", key="change_new_pw_confirm")

    if st.button("✅ パスワードを変更する"):
        current_pw = st.session_state.get("change_current_pw", "").strip()
        new_pw = st.session_state.get("change_new_pw", "").strip()
        confirm_pw = st.session_state.get("change_new_pw_confirm", "").strip()

        if not current_pw or not new_pw or not confirm_pw:
            st.warning("全部入力してください。")
        elif len(new_pw) < 4:
            st.warning("新しいパスワードは4文字以上にしてください。")
        elif new_pw != confirm_pw:
            st.warning("新しいパスワードが一致していません。")
        else:
            ok, msg = update_password(st.session_state["auth_user"], current_pw, new_pw)
            if ok:
                st.success(msg)
            else:
                st.error(msg)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 会社名入力
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🏢 会社情報")
st.text_input("会社名", key="company_name", on_change=change_and_save)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# プラン
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🎫 プラン")

if st.session_state["is_pro_logged_in"]:
    st.session_state["plan"] = "Pro（月9,800円）"
    st.markdown("""
        <div class="pro-box">
            <b>Pro版</b><br>
            保存 / CSV / PDF / 12ヶ月推移 / LINE導線 が使えます
        </div>
    """, unsafe_allow_html=True)
else:
    st.session_state["plan"] = "デモ（無料）"
    remain = max(0, DEMO_LIMIT - st.session_state.get("calc_count", 0))
    st.markdown(f"""
        <div class="demo-box">
            <b>デモ版</b><br>
            残り計算回数：<b>{remain} / {DEMO_LIMIT}</b>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

is_pro = st.session_state["is_pro_logged_in"]

# =========================
# デモ上限
# =========================
if not is_pro and st.session_state.get("calc_count", 0) >= DEMO_LIMIT:
    st.error("⚠️ デモ版の利用回数は上限に達しました。")
    st.info("Pro版では計算回数が無制限になります。ログインするとPro機能が開きます。")
    col_stop1, col_stop2 = st.columns(2)
    with col_stop1:
        st.button("🔒 Proログインして続ける", disabled=True)
    with col_stop2:
        st.button("🔄 初期値に戻す", on_click=lambda: reset_state_for_user(None))
    st.stop()

# =========================
# 入力欄
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("💰 月次入力")

col1, col2 = st.columns(2)

with col1:
    st.number_input("現在の現預金 (万円)", min_value=0, step=100, key="cash", on_change=change_and_save if is_pro else None)
    st.number_input("月平均売上 (万円)", min_value=0, step=50, key="revenue", on_change=change_and_save if is_pro else None)
    st.number_input("月平均原価 (万円)", min_value=0, step=10, key="cost", on_change=change_and_save if is_pro else None)

with col2:
    st.number_input("月平均固定費 (万円)", min_value=0, step=10, key="fixed_cost", on_change=change_and_save if is_pro else None)
    st.number_input("月の借入返済 (万円)", min_value=0, step=5, key="loan_pay", on_change=change_and_save if is_pro else None)
    st.slider("税率（概算）", min_value=0.0, max_value=0.5, step=0.01, key="tax_rate", on_change=change_and_save if is_pro else None)

col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if is_pro:
        st.button("📊 計算する")
    else:
        st.button("📊 計算する", on_click=count_demo_use)
with col_btn2:
    if is_pro:
        if st.button("💾 保存"):
            save_state_for_user(st.session_state["auth_user"])
            st.success("保存しました。")
    else:
        st.button("🔒 保存（Pro）", disabled=True)
with col_btn3:
    if is_pro:
        st.button("🔄 初期値に戻す", on_click=lambda: reset_state_for_user(st.session_state["auth_user"]))
    else:
        st.button("🔄 初期値に戻す", on_click=lambda: reset_state_for_user(None))

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 値取得
# =========================
company_name = st.session_state["company_name"].strip()
cash = st.session_state["cash"]
revenue = st.session_state["revenue"]
cost = st.session_state["cost"]
fixed_cost = st.session_state["fixed_cost"]
loan_pay = st.session_state["loan_pay"]
tax_rate = st.session_state["tax_rate"]
plan = st.session_state["plan"]

safe_company_name = sanitize_filename(company_name)
today_str = datetime.now().strftime("%Y-%m-%d")

# =========================
# 計算
# =========================
gross_profit = revenue - cost
operating_balance = gross_profit - fixed_cost - loan_pay
estimated_tax = max(0, operating_balance * tax_rate)
after_tax_balance = operating_balance - estimated_tax

if after_tax_balance >= 0:
    runway = 12
else:
    runway = cash / abs(after_tax_balance) if after_tax_balance != 0 else 12

if runway >= 6:
    status = "安全"
    color = "#15803d"
elif runway >= 3:
    status = "注意"
    color = "#d97706"
else:
    status = "危険"
    color = "#b91c1c"

if after_tax_balance < 0:
    shortage_for_safety = max(0, abs(after_tax_balance) * 6 - cash)
else:
    shortage_for_safety = 0

needed_improvement = max(0, abs(after_tax_balance))
needed_sales_up = needed_improvement
needed_cost_down = needed_improvement

# =========================
# 12ヶ月推移データ
# =========================
months = list(range(13))
cash_before_tax = []
cash_after_tax = []

current_before_tax = cash
current_after_tax = cash
danger_month = None

for m in months:
    cash_before_tax.append(current_before_tax)
    cash_after_tax.append(current_after_tax)
    current_before_tax += operating_balance
    current_after_tax += after_tax_balance

for i, v in enumerate(cash_after_tax):
    if v < 0:
        danger_month = i
        break

df_forecast = pd.DataFrame({
    "会社名": [company_name] * len(months),
    "経過月": months,
    "税引前現預金残高_万円": cash_before_tax,
    "税引後現預金残高_万円": cash_after_tax
})

# =========================
# CSV / PDF
# =========================
summary_rows = [
    {"出力日": today_str, "会社名": company_name, "分類": "基本情報", "項目名": "利用プラン", "数値・内容": plan, "単位": ""},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "現在の現預金残高", "数値・内容": cash, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "月平均売上高", "数値・内容": revenue, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "月平均原価", "数値・内容": cost, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "月平均固定費", "数値・内容": fixed_cost, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "月間借入返済額", "数値・内容": loan_pay, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "概算税率", "数値・内容": round(tax_rate * 100, 1), "単位": "%"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "粗利益", "数値・内容": gross_profit, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "営業ベース月次増減額", "数値・内容": operating_balance, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "概算納税額", "数値・内容": estimated_tax, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "税引後月次増減額", "数値・内容": after_tax_balance, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "資金余命目安", "数値・内容": round(min(runway, 12), 1), "単位": "ヶ月"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "資金判定", "数値・内容": status, "単位": ""},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "6ヶ月安全ライン不足額", "数値・内容": shortage_for_safety, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "改善必要額", "数値・内容": needed_improvement, "単位": "万円"},
]

if danger_month is not None:
    summary_rows.append({"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "資金ショート想定時期", "数値・内容": danger_month, "単位": "ヶ月後"})
else:
    summary_rows.append({"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "資金ショート想定時期", "数値・内容": "12ヶ月以内なし", "単位": ""})

df_summary = pd.DataFrame(summary_rows)
summary_csv = df_summary.to_csv(index=False).encode("utf-8-sig")
forecast_csv = df_forecast.to_csv(index=False).encode("utf-8-sig")

pdf_bytes = create_pdf_report(
    company_name=company_name,
    today_str=today_str,
    status=status,
    color=color,
    runway=runway,
    cash=cash,
    revenue=revenue,
    cost=cost,
    fixed_cost=fixed_cost,
    loan_pay=loan_pay,
    tax_rate=tax_rate,
    gross_profit=gross_profit,
    operating_balance=operating_balance,
    estimated_tax=estimated_tax,
    after_tax_balance=after_tax_balance,
    shortage_for_safety=shortage_for_safety,
    danger_month=danger_month,
    needed_sales_up=needed_sales_up,
    needed_cost_down=needed_cost_down
)

# =========================
# 結果カード
# =========================
st.markdown(f"""
    <div class="center-card" style="background:{color}; color:white;">
        <div class="sub-big">現在の資金状況</div>
        <div class="big-status-font">{status}</div>
        <div style="font-size:1.15rem; color:white;">資金余命の目安：{min(runway, 12):.1f} ヶ月</div>
    </div>
""", unsafe_allow_html=True)

# =========================
# メーター
# =========================
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=min(runway, 12),
    domain={"x": [0, 1], "y": [0, 1]},
    title={"text": "資金余命（目安）", "font": {"size": 26, "color": "#111827"}},
    gauge={
        "axis": {"range": [0, 12], "tickwidth": 1, "tickcolor": "#334155"},
        "bar": {"color": color},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "#94a3b8",
        "steps": [
            {"range": [0, 3], "color": "#fee2e2"},
            {"range": [3, 6], "color": "#fef3c7"},
            {"range": [6, 12], "color": "#dcfce7"}
        ],
        "threshold": {
            "line": {"color": "#7f1d1d", "width": 4},
            "thickness": 0.75,
            "value": min(runway, 12)
        }
    }
))
fig.update_layout(height=330, margin=dict(l=20, r=20, t=60, b=12), paper_bgcolor="#eef3f8")
st.plotly_chart(fig, use_container_width=True)

# =========================
# 詳細データ
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 詳細データ")

col_a, col_b = st.columns(2)
with col_a:
    st.metric("粗利益", f"{gross_profit:,.0f} 万円")
    st.metric("固定費", f"{fixed_cost:,.0f} 万円")
    st.metric("概算納税額", f"{estimated_tax:,.0f} 万円")
with col_b:
    st.metric("借入返済", f"{loan_pay:,.0f} 万円")
    st.metric("税引後 月次増減額", f"{after_tax_balance:,.0f} 万円")
    st.metric("6ヶ月安全ライン不足額", f"{shortage_for_safety:,.0f} 万円")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Pro限定 / デモ一部表示
# =========================
if is_pro:
    st.markdown("""
        <div class="csv-box">
            <b>📄 税理士・銀行向けCSV出力</b><br>
            会社名入りで提出や共有に使いやすい形で出力できます
        </div>
    """, unsafe_allow_html=True)

    csv_col1, csv_col2 = st.columns(2)
    with csv_col1:
        st.download_button(
            label="⬇️ サマリーCSV出力",
            data=summary_csv,
            file_name=f"{safe_company_name}_cash_summary_{today_str}.csv",
            mime="text/csv"
        )
    with csv_col2:
        st.download_button(
            label="⬇️ 12ヶ月推移CSV出力",
            data=forecast_csv,
            file_name=f"{safe_company_name}_cash_forecast_{today_str}.csv",
            mime="text/csv"
        )

    st.markdown("""
        <div class="pdf-box">
            <b>🧾 1枚レポートPDF出力</b><br>
            税理士・銀行・社内共有向けの見やすい1ページ資料です
        </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="⬇️ 1枚レポートPDF出力",
        data=pdf_bytes,
        file_name=f"{safe_company_name}_cash_report_{today_str}.pdf",
        mime="application/pdf"
    )

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=df_forecast["経過月"],
        y=df_forecast["税引前現預金残高_万円"],
        mode="lines+markers",
        name="税引前現預金"
    ))
    fig2.add_trace(go.Scatter(
        x=df_forecast["経過月"],
        y=df_forecast["税引後現預金残高_万円"],
        mode="lines+markers",
        name="税引後現預金"
    ))
    fig2.update_layout(
        title="📈 12ヶ月 現預金推移（予測）",
        xaxis_title="経過月",
        yaxis_title="現預金残高（万円）",
        height=390,
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#111827"),
        margin=dict(l=20, r=20, t=60, b=20)
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
        <div class="line-box">
            <b>相談・最新情報はLINEから</b><br>
            気になることがあればLINE追加してください
        </div>
    """, unsafe_allow_html=True)
    st.link_button("📱 LINE追加ボタン", LINE_URL)

else:
    st.markdown("""
        <div class="locked-box">
            <b>🔒 ここから先はPro版の機能です</b><br>
            保存 / CSV / PDF / 12ヶ月推移 / LINE相談導線 が使えます
        </div>
    """, unsafe_allow_html=True)

    preview_col1, preview_col2 = st.columns(2)
    with preview_col1:
        st.metric("12ヶ月後の税引後現預金（プレビュー）", f"{cash_after_tax[-1]:,.0f} 万円")
    with preview_col2:
        preview_text = f"{danger_month}ヶ月後" if danger_month is not None else "12ヶ月以内なし"
        st.metric("資金ショート想定時期（プレビュー）", preview_text)

    lock_col1, lock_col2 = st.columns(2)
    with lock_col1:
        st.button("🔒 CSV出力（Pro）", disabled=True)
    with lock_col2:
        st.button("🔒 PDF出力（Pro）", disabled=True)

    st.info("Pro版では、12ヶ月推移グラフ・提出用CSV・1枚レポートPDF・保存機能が使えます。")

# =========================
# 危険月表示
# =========================
if danger_month is not None:
    st.error(f"⚠️ このままだと **{danger_month}ヶ月後** に資金ショートの可能性があります。")
else:
    st.success("✅ 12ヶ月以内の資金ショートリスクは低いです。")

# =========================
# 一撃アクション
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🎯 一撃アクション")

if after_tax_balance < 0:
    st.markdown(f"""
    <div class="action-box">
        <b>今月のままだと毎月 {abs(after_tax_balance):,.0f} 万円ずつ減る計算です。</b><br><br>
        安全ラインに近づけるには、まず次のどれかをやるのが最短です。<br>
        ・売上を <b>あと {needed_sales_up:,.0f} 万円</b> 上げる<br>
        ・原価を <b>あと {needed_cost_down:,.0f} 万円</b> 下げる<br>
        ・固定費や返済を見直して、月の支出を圧縮する
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="action-box">
        <b>今月は税引後でも {after_tax_balance:,.0f} 万円プラスです。</b><br><br>
        今の状態はかなり良いです。<br>
        ・現預金をさらに積み増す<br>
        ・利益率の高い受注を増やす<br>
        ・採用・設備投資の判断材料としてこの数字を使う
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 改善ポイント
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("💡 改善ポイント")

if status == "危険":
    st.error("**緊急対応が必要です！**")
    st.write("- 売上の前倒し請求、回収サイト短縮を検討")
    st.write("- 原価を最優先で見直す")
    st.write("- 固定費と借入返済の圧縮余地を確認")
    st.write("- 必要なら短期資金の確保も視野に入れる")
elif status == "注意":
    st.warning("**注意が必要です。**")
    st.write("- 黒字幅をもう一段上げたい状態です")
    st.write("- 現場ごとの粗利バラつきを確認")
    st.write("- 数ヶ月先の資金繰りを先回りで見る")
    st.write("- 利益が残る案件構成に寄せる")
else:
    st.success("**資金状況は安全です！**")
    st.write("- 安全圏を維持しながら事業拡大を検討")
    st.write("- 利益率の高い受注を優先")
    st.write("- 現預金を厚くしてさらに安定化")
    st.write("- 採用や設備投資の判断に活用")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("""
<div style='margin-top:10px;'>
<a href="https://lin.ee/7m28VAs" target="_blank"
style="
display:block;
text-align:center;
background:#06c755;
color:white;
padding:16px;
border-radius:14px;
text-decoration:none;
font-weight:bold;
font-size:18px;
">
📱 LINEで相談する
</a>
</div>
""", unsafe_allow_html=True)

# =========================
# フッター
# =========================
if not is_pro:
    remain = max(0, DEMO_LIMIT - st.session_state.get("calc_count", 0))
    st.info(f"デモ版の残り計算回数：{remain} / {DEMO_LIMIT}")
else:
    st.success(f"Pro版をご利用中です。ログインユーザー: {st.session_state['auth_user']}")
