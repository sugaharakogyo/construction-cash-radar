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
    "company_name": "株式会社○○",
    "cash": 500,
    "revenue": 500,
    "cost": 250,
    "fixed_cost": 130,
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
    c.drawString(46, height - 146, "今の状態は？")

    c.setFont(PDF_FONT_BOLD, 22)
    c.drawString(170, height - 148, status)

    c.setFont(PDF_FONT, 11)
    c.drawRightString(width - 46, height - 146, f"このままだと、あと {min(runway, 12):.1f}ヶ月もちます")

    card_top = height - 205
    left = 28
    card_w = width - 56
    c.setFillColor(white)
    c.roundRect(left, 150, card_w, card_top - 150, 18, fill=1, stroke=0)

    c.setFillColor(HexColor("#0f172a"))
    c.setFont(PDF_FONT_BOLD, 12)
    c.drawString(46, card_top - 22, "主要数値（社長目線）")

    y1 = card_top - 36
    draw_label_value(c, 46, y1, "今ある現金", f"{cash:,.0f} 万円", width=150)
    draw_label_value(c, 206, y1, "月の売上", f"{revenue:,.0f} 万円", width=150)
    draw_label_value(c, 366, y1, "外注・材料費", f"{cost:,.0f} 万円", width=150)

    y2 = y1 - 68
    draw_label_value(c, 46, y2, "人件費・家賃など", f"{fixed_cost:,.0f} 万円", width=150)
    draw_label_value(c, 206, y2, "借金の返済", f"{loan_pay:,.0f} 万円", width=150)
    draw_label_value(c, 366, y2, "税金の割合", f"{tax_rate * 100:.1f} %", width=150)

    y3 = y2 - 68
    draw_label_value(c, 46, y3, "手元に残る利益", f"{gross_profit:,.0f} 万円", width=150)
    draw_label_value(c, 206, y3, "税金の支払い", f"{estimated_tax:,.0f} 万円", width=150)
    
    balance_label = "毎月いくら増える？" if after_tax_balance >= 0 else "毎月いくら減る？"
    balance_value = f"+{after_tax_balance:,.0f}" if after_tax_balance >= 0 else f"{after_tax_balance:,.0f}"
    draw_label_value(c, 366, y3, balance_label, f"{balance_value} 万円", width=150)

    y4 = y3 - 68
    draw_label_value(c, 46, y4, "営業キャッシュ", f"{operating_balance:,.0f} 万円", width=150)
    
    if shortage_for_safety > 0:
        draw_label_value(c, 206, y4, "あといくら必要？", f"{shortage_for_safety:,.0f} 万円", width=150)
    else:
        draw_label_value(c, 206, y4, "安全ライン", "達成！", width=150)

    danger_text = f"{danger_month}ヶ月後" if danger_month is not None else "12ヶ月以内なし"
    draw_label_value(c, 366, y4, "お金が足りなくなる時期", danger_text, width=150)

    comment_y = y4 - 88
    c.setFillColor(HexColor("#e0f2fe"))
    c.roundRect(46, comment_y - 70, 470, 70, 14, fill=1, stroke=0)

    c.setFillColor(HexColor("#0f172a"))
    c.setFont(PDF_FONT_BOLD, 11)
    c.drawString(60, comment_y - 18, "今すぐやること")

    c.setFont(PDF_FONT, 10)
    if after_tax_balance < 0:
        c.drawString(60, comment_y - 38, f"- 売上をあと {needed_sales_up:,.0f} 万円 上げる")
        c.drawString(60, comment_y - 54, f"- 原価をあと {needed_cost_down:,.0f} 万円 下げる")
        c.drawString(280, comment_y - 38, "- 人件費や返済の見直し")
        c.drawString(280, comment_y - 54, "- 売掛金の回収を早める")
    else:
        c.drawString(60, comment_y - 38, "- 現金をもっと貯める")
        c.drawString(60, comment_y - 54, "- 利益率の高い仕事を優先する")
        c.drawString(280, comment_y - 38, "- 人を雇う・機械を買う判断に活用")
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
# Streamlitメニューを完全非表示
# =========================
hide_streamlit_style = """
<style>
    /* ヘッダー全体を非表示 */
    header {
        visibility: hidden !important;
        height: 0 !important;
    }
    
    /* ハンバーガーメニューを非表示 */
    #MainMenu {
        visibility: hidden !important;
    }
    
    /* フッターを非表示 */
    footer {
        visibility: hidden !important;
    }
    
    /* デプロイボタンを非表示 */
    .stDeployButton {
        display: none !important;
    }
    
    /* ツールバーを非表示 */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* ツールバー全体を削除 */
    .stApp > header {
        display: none !important;
    }
    
    /* 余白を調整 */
    .block-container {
        padding-top: 2rem !important;
    }
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
# CSS（スマホ対応強化版）
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

    /* その他のスタイルは省略 */

    /* ==================== */
    /* スマホ対応強化（640px以下） */
    /* ==================== */
    @media (max-width: 640px) {
        /* コンテナの余白調整 */
        .block-container {
            padding-top: 0.5rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            padding-bottom: 1rem !important;
        }
        
        /* カードの余白調整 */
        .card, .center-card { 
            padding: 15px !important; 
            border-radius: 14px !important;
            margin-bottom: 10px !important;
        }
        
        /* 大きなステータス文字を少し小さく */
        .big-status-font { 
            font-size: 2.5rem !important; 
        }
        
        /* サブタイトルも調整 */
        .sub-big {
            font-size: 1rem !important;
        }
        
        /* h1タイトルを小さく */
        h1 {
            font-size: 1.8rem !important;
        }
        
        /* h2サブタイトルを小さく */
        h2 {
            font-size: 1.4rem !important;
        }
        
        /* h3以下も調整 */
        h3 {
            font-size: 1.2rem !important;
        }
        
        h4 {
            font-size: 1.1rem !important;
        }
        
        /* 入力欄のラベルを見やすく */
        .stNumberInput label, .stTextInput label, .stSlider label {
            font-size: 0.95rem !important;
            font-weight: 700 !important;
        }
        
        /* 入力欄を大きく（指で押しやすく） */
        .stNumberInput input, .stTextInput input {
            font-size: 1.1rem !important;
            padding: 0.9rem 0.8rem !important;
            height: 3rem !important;
        }
        
        /* ボタンを大きく */
        .stButton > button {
            height: 3.5rem !important;
            font-size: 1.1rem !important;
            padding: 0.8rem 1rem !important;
        }
        
        /* メトリクスカードを調整 */
        .stMetric {
            padding: 12px !important;
            margin-bottom: 8px !important;
        }
        
        /* メトリクスのラベルを小さく */
        [data-testid="stMetricLabel"] {
            font-size: 0.85rem !important;
        }
        
        /* メトリクスの値を見やすく */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }
        
        /* アクションボックスの余白調整 */
        .action-box {
            padding: 12px !important;
            margin: 8px 0 !important;
        }
        
        /* アクションボックス内の文字サイズ */
        .action-box h4 {
            font-size: 1rem !important;
            line-height: 1.4 !important;
        }
        
        .action-box p {
            font-size: 0.9rem !important;
            line-height: 1.5 !important;
        }
        
        /* ダウンロードボタンを大きく */
        div[data-testid="stDownloadButton"] button {
            height: 3.5rem !important;
            font-size: 1.1rem !important;
        }
        
        /* 2カラムレイアウトを1カラムに */
        .row-widget.stHorizontal {
            flex-direction: column !important;
        }
        
        /* グラフの高さ調整 */
        .js-plotly-plot {
            max-height: 300px !important;
        }
        
        /* テーブルのフォントサイズ */
        .stDataFrame {
            font-size: 0.85rem !important;
        }
        
        /* エキスパンダー（折りたたみ）のタイトル */
        .streamlit-expanderHeader {
            font-size: 1rem !important;
        }
        
        /* リンクボタンを大きく */
        div[data-testid="stLinkButton"] a {
            font-size: 1.1rem !important;
            padding: 1rem !important;
            height: auto !important;
            min-height: 3.5rem !important;
        }
    }
    
    /* ==================== */
    /* さらに小さい画面（480px以下） */
    /* ==================== */
    @media (max-width: 480px) {
        .block-container {
            padding-left: 0.3rem !important;
            padding-right: 0.3rem !important;
        }
        
        .card, .center-card {
            padding: 12px !important;
        }
        
        .big-status-font {
            font-size: 2rem !important;
        }
        
        h1 {
            font-size: 1.5rem !important;
        }
        
        h2 {
            font-size: 1.3rem !important;
        }
        
        .stButton > button {
            font-size: 1rem !important;
        }
    }
    
    /* ==================== */
    /* タブレット（641px〜1024px） */
    /* ==================== */
    @media (min-width: 641px) and (max-width: 1024px) {
        .block-container {
            max-width: 700px !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        
        .big-status-font {
            font-size: 3.5rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# CSS（スマホ対応強化版 - ボタン＆12ヶ月表示改善）
# =========================
st.markdown("""
    <style>
    /* 既存のスタイル... */
    
    /* ==================== */
    /* +/- ボタンを大きく（スマホ対応） */
    /* ==================== */
    
    /* 数値入力欄全体のスタイル */
    .stNumberInput {
        position: relative;
    }
    
    /* +/- ボタンのコンテナ */
    .stNumberInput button {
        width: 2.5rem !important;
        height: 2.5rem !important;
        font-size: 1.3rem !important;
        padding: 0 !important;
        margin: 0 !important;
        border-radius: 8px !important;
        background: #2563eb !important;
        color: white !important;
        border: none !important;
        cursor: pointer !important;
    }
    
    /* +/- ボタンのホバー */
    .stNumberInput button:hover {
        background: #1d4ed8 !important;
    }
    
    /* +/- ボタンのアクティブ */
    .stNumberInput button:active {
        background: #1e40af !important;
        transform: scale(0.95);
    }
    
    /* 入力欄の右側の+/-ボタンエリア */
    .stNumberInput [data-baseweb="input"] > div {
        gap: 0.3rem !important;
    }
    
    /* ==================== */
    /* スマホでさらに大きく */
    /* ==================== */
    @media (max-width: 640px) {
        /* +/- ボタンをさらに大きく */
        .stNumberInput button {
            width: 3rem !important;
            height: 3rem !important;
            font-size: 1.5rem !important;
            border-radius: 10px !important;
        }
        
        /* 入力欄自体も大きく */
        .stNumberInput input {
            font-size: 1.2rem !important;
            padding: 0.9rem 1rem !important;
            height: 3.5rem !important;
        }
        
        /* 数値入力欄のラベル */
        .stNumberInput label {
            font-size: 1rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.5rem !important;
        }
    }
    
    /* ==================== */
    /* 「12ヶ月」表示を見やすく */
    /* ==================== */
    
    /* メーターグラフの数字部分 */
    .js-plotly-plot .plotly text {
        font-size: 1.8rem !important;
        font-weight: bold !important;
    }
    
    /* メーターグラフのタイトル */
    .js-plotly-plot .gtitle {
        font-size: 1.5rem !important;
        font-weight: bold !important;
    }
    
    /* グラフ内の数値 */
    .indicator-value {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
    }

    
    /* ==================== */
    /* スマホでグラフの文字を調整 */
    /* ==================== */
    @media (max-width: 640px) {
        /* メーターの数値を大きく */
        .js-plotly-plot .plotly text {
            font-size: 1.5rem !important;
        }
        
        /* メーターのタイトルを調整 */
        .js-plotly-plot .gtitle {
            font-size: 1.2rem !important;
        }
        
        /* グラフ全体の高さを調整 */
        .js-plotly-plot {
            max-height: 280px !important;
        }
    }
    
    @media (max-width: 480px) {
        /* さらに小さい画面 */
        .js-plotly-plot {
            max-height: 250px !important;
        }
        
        .js-plotly-plot .plotly text {
            font-size: 1.3rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* 既存のスタイル... */
    
    /* ==================== */
    /* グラフの見切れ防止 */
    /* ==================== */
    
    /* グラフコンテナの設定 */
    .js-plotly-plot {
        width: 100% !important;
        max-width: 100% !important;
        overflow: visible !important;
    }
    
    /* グラフ内のSVG */
    .js-plotly-plot .plotly svg {
        width: 100% !important;
        height: auto !important;
    }
    
    /* グラフを含むカードの余白調整 */
    .card:has(.js-plotly-plot) {
        padding: 10px !important;
        overflow: visible !important;
    }
    
    /* ==================== */
    /* スマホでのグラフ調整 */
    /* ==================== */
    @media (max-width: 640px) {
        /* グラフの高さを小さく */
        .js-plotly-plot {
            max-height: 320px !important;
        }
        
        /* グラフを含むカードの余白をさらに小さく */
        .card:has(.js-plotly-plot) {
            padding: 8px !important;
        }
        
        /* グラフのタイトルを小さく */
        .js-plotly-plot .gtitle {
            font-size: 1rem !important;
        }
        
        /* 軸のラベルを小さく */
        .js-plotly-plot .xtitle,
        .js-plotly-plot .ytitle {
            font-size: 0.9rem !important;
        }
        
        /* 目盛りの数字を小さく */
        .js-plotly-plot .xtick text,
        .js-plotly-plot .ytick text {
            font-size: 0.8rem !important;
        }
        
        /* 凡例を小さく */
        .js-plotly-plot .legend {
            font-size: 0.85rem !important;
        }
        
        /* 注釈を小さく */
        .js-plotly-plot .annotation {
            font-size: 0.75rem !important;
        }
    }
    
    /* ==================== */
    /* さらに小さい画面 */
    /* ==================== */
    @media (max-width: 480px) {
        .js-plotly-plot {
            max-height: 280px !important;
        }
        
        .card:has(.js-plotly-plot) {
            padding: 5px !important;
        }
        
        /* X軸の目盛りを間引く */
        .js-plotly-plot .xtick {
            display: none;
        }
        
        .js-plotly-plot .xtick:nth-child(2n) {
            display: block;
        }
    }
    
    /* ==================== */
    /* 横向き表示対応 */
    /* ==================== */
    @media (max-width: 640px) and (orientation: landscape) {
        .js-plotly-plot {
            max-height: 250px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)
# =========================
# タイトル
# =========================
st.title("🏗️ 建設キャッシュレーダー")
st.write("社長が3秒で分かる。あと何ヶ月もつか、今すぐやることが見える。")

st.markdown("""
<a href="https://buy.stripe.com/6oU28rarietE5gM6m87N600" target="_blank"
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
# 入力欄（通帳ベース版）
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("💰 今月の数字を入れてください")

# タブで切り替え
tab1, tab2 = st.tabs(["🎯 通帳ベース（実際の入出金）", "📊 利益ベース（従来）"])

with tab1:
    st.markdown("### 📌 実際のお金の動き")
    st.caption("利益ではなく、実際に通帳から出入りするお金を入れてください")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.number_input(
            "💵 今の通帳残高（万円）", 
            min_value=0, 
            step=100, 
            key="cash",
            help="💡 今、通帳にいくらありますか？",
            on_change=change_and_save if is_pro else None
        )
        
        st.number_input(
            "📥 今月入ってくるお金（万円）", 
            min_value=0, 
            step=50, 
            key="actual_income",
            help="💡 今月中に実際に振り込まれる予定の金額です。売掛金の回収予定を入れてください。",
            on_change=change_and_save if is_pro else None
        )
        
        st.number_input(
            "💰 まだ入ってない売上（万円）", 
            min_value=0, 
            step=50, 
            key="receivables",
            help="💡 請求済みだけど、まだ入金されていない金額（売掛金）",
            on_change=change_and_save if is_pro else None
        )
    
    with col2:
        st.number_input(
            "📤 今月出ていくお金（万円）", 
            min_value=0, 
            step=50, 
            key="actual_expense",
            help="💡 今月中に実際に払う予定の金額です。外注・材料・給料・家賃・返済の合計。",
            on_change=change_and_save if is_pro else None
        )
        
        st.number_input(
            "💳 まだ払ってない支払い（万円）", 
            min_value=0, 
            step=50, 
            key="payables",
            help="💡 請求されているけど、まだ払っていない金額（買掛金）",
            on_change=change_and_save if is_pro else None
        )
        
        st.slider(
            "📊 税金の割合（だいたい）", 
            min_value=0.0, 
            max_value=0.5, 
            step=0.01, 
            key="tax_rate",
            value=0.30,
            help="💡 利益の30%くらいが目安です。",
            on_change=change_and_save if is_pro else None
        )

with tab2:
    st.markdown("### 📊 利益ベース（参考）")
    st.caption("会計的な利益を計算する場合はこちら")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.number_input(
            "📈 月の売上（万円）", 
            min_value=0, 
            step=50, 
            key="revenue",
            help="💡 1ヶ月の売上高（発生ベース）",
            on_change=change_and_save if is_pro else None
        )
        
        st.number_input(
            "🔨 外注・材料費（万円）", 
            min_value=0, 
            step=10, 
            key="cost",
            help="💡 売上に対応する原価",
            on_change=change_and_save if is_pro else None
        )
    
    with col4:
        st.number_input(
            "🏢 人件費・家賃など（万円）", 
            min_value=0, 
            step=10, 
            key="fixed_cost",
            help="💡 毎月固定でかかる費用",
            on_change=change_and_save if is_pro else None
        )
        
        st.number_input(
            "💳 借金の返済（万円）", 
            min_value=0, 
            step=5, 
            key="loan_pay",
            help="💡 銀行への返済額（月）",
            on_change=change_and_save if is_pro else None
        )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 値取得
# =========================
cash = st.session_state.get("cash", 500)
actual_income = st.session_state.get("actual_income", 500)
actual_expense = st.session_state.get("actual_expense", 430)
receivables = st.session_state.get("receivables", 0)
payables = st.session_state.get("payables", 0)
tax_rate = st.session_state.get("tax_rate", 0.30)

# 従来の利益ベース計算（比較用）
revenue = st.session_state.get("revenue", 500)
cost = st.session_state.get("cost", 250)
fixed_cost = st.session_state.get("fixed_cost", 130)
loan_pay = st.session_state.get("loan_pay", 50)

gross_profit = revenue - cost
operating_balance = gross_profit - fixed_cost - loan_pay
estimated_tax_profit = max(0, operating_balance * tax_rate)
after_tax_balance_profit = operating_balance - estimated_tax_profit

# =========================
# 🆕 通帳ベースの計算
# =========================

# 今月の通帳増減（税金考慮前）
cash_flow_before_tax = actual_income - actual_expense

# 概算納税額（利益ベースで計算）
estimated_tax = estimated_tax_profit

# 税引後の通帳増減
cash_flow = cash_flow_before_tax - estimated_tax

# 来月末の通帳残高（予測）
next_month_cash = cash + cash_flow

# 実質的な現金（売掛金・買掛金考慮）
real_cash = cash + receivables - payables

# 資金余命（通帳ベース）
if cash_flow >= 0:
    runway = 12
else:
    runway = cash / abs(cash_flow) if cash_flow != 0 else 12

# 判定
if runway >= 6:
    status = "安全"
    color = "#15803d"
elif runway >= 3:
    status = "注意"
    color = "#d97706"
else:
    status = "危険"
    color = "#b91c1c"



# =========================
# 結果カード（通帳ベース版）
# =========================
st.markdown(f"""
    <div class="center-card" style="background:{color}; color:white;">
        <div class="sub-big">今の状態は？</div>
        <div class="big-status-font">{status}</div>
        <div style="font-size:1.15rem; color:white;">
            このままだと、あと {min(runway, 12):.1f} ヶ月もちます
        </div>
    </div>
""", unsafe_allow_html=True)

# メーター（既存のまま）
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=min(runway, 12),
    # ... 既存のコード
))
st.plotly_chart(fig, use_container_width=True)

# =========================
# 詳細データ（通帳ベース版）
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 詳しく見る（通帳ベース）")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.metric(
        "💰 今の通帳残高", 
        f"{cash:,.0f} 万円",
        help="現在の現預金"
    )
    
    st.metric(
        "📥 今月入ってくる", 
        f"{actual_income:,.0f} 万円",
        help="今月中に振り込まれる予定"
    )

with col_b:
    st.metric(
        "📤 今月出ていく", 
        f"{actual_expense:,.0f} 万円",
        help="今月中に支払う予定"
    )
    
    st.metric(
        "💸 税金の支払い", 
        f"{estimated_tax:,.0f} 万円",
        help="概算納税額"
    )

with col_c:
    if cash_flow >= 0:
        st.metric(
            "📈 今月の増減", 
            f"+{cash_flow:,.0f} 万円",
            delta="増えます",
            help="税金を払った後、今月これだけ増えます"
        )
    else:
        st.metric(
            "📉 今月の増減", 
            f"{cash_flow:,.0f} 万円",
            delta="減ります",
            delta_color="inverse",
            help="税金を払った後、今月これだけ減ります"
        )
    
    st.metric(
        "🔮 来月末の通帳", 
        f"{next_month_cash:,.0f} 万円",
        help="このままいくと来月末の残高"
    )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 売掛金・買掛金の状況
# =========================
if receivables > 0 or payables > 0:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📋 回収・支払いの状況")
    
    col_d, col_e, col_f = st.columns(3)
    
    with col_d:
        st.metric(
            "💰 まだ入ってない売上", 
            f"{receivables:,.0f} 万円",
            help="請求済みだけど未回収"
        )
    
    with col_e:
        st.metric(
            "💳 まだ払ってない支払い", 
            f"{payables:,.0f} 万円",
            help="請求されているけど未払い"
        )
    
    with col_f:
        diff = receivables - payables
        if diff >= 0:
            st.metric(
                "📊 実質的な現金力", 
                f"{real_cash:,.0f} 万円",
                delta=f"+{diff:,.0f} 万円",
                help="売掛金・買掛金を考慮した実質残高"
            )
        else:
            st.metric(
                "📊 実質的な現金力", 
                f"{real_cash:,.0f} 万円",
                delta=f"{diff:,.0f} 万円",
                delta_color="inverse",
                help="売掛金・買掛金を考慮した実質残高"
            )
    
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 利益ベースとの比較
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔍 通帳ベース vs 利益ベース")

compare_col1, compare_col2 = st.columns(2)

with compare_col1:
    st.markdown(f"""
    <div style="background: #f0f9ff; padding: 15px; border-radius: 12px; border-left: 4px solid #2563eb;">
        <h4 style="margin-top: 0; color: #1e40af;">💵 通帳ベース（現実）</h4>
        <p style="font-size: 1.1rem; margin: 5px 0;">
            今月の増減：<b>{cash_flow:+,.0f} 万円</b><br>
            来月末残高：<b>{next_month_cash:,.0f} 万円</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

with compare_col2:
    st.markdown(f"""
    <div style="background: #fef3f2; padding: 15px; border-radius: 12px; border-left: 4px solid #dc2626;">
        <h4 style="margin-top: 0; color: #991b1b;">📊 利益ベース（参考）</h4>
        <p style="font-size: 1.1rem; margin: 5px 0;">
            今月の増減：<b>{after_tax_balance_profit:+,.0f} 万円</b><br>
            粗利益：<b>{gross_profit:,.0f} 万円</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ズレの説明
gap = cash_flow - after_tax_balance_profit
if abs(gap) > 10:
    st.markdown(f"""
    <div style="background: #fef3c7; padding: 15px; border-radius: 12px; margin-top: 10px;">
        <p style="margin: 0; color: #78350f; font-weight: 600;">
            ⚠️ 通帳ベースと利益ベースに <b>{abs(gap):,.0f} 万円</b> のズレがあります。<br>
            これは入金サイトや先払いのタイミングのズレです。
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
# =========================
# CSV / PDF
# =========================
summary_rows = [
    {"出力日": today_str, "会社名": company_name, "分類": "基本情報", "項目名": "利用プラン", "数値・内容": plan, "単位": ""},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "今ある現金", "数値・内容": cash, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "月の売上", "数値・内容": revenue, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "外注・材料費", "数値・内容": cost, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "人件費・家賃など", "数値・内容": fixed_cost, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "借金の返済", "数値・内容": loan_pay, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "入力値", "項目名": "税金の割合", "数値・内容": round(tax_rate * 100, 1), "単位": "%"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "手元に残る利益", "数値・内容": gross_profit, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "営業キャッシュ", "数値・内容": operating_balance, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "税金の支払い", "数値・内容": estimated_tax, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "毎月の増減", "数値・内容": after_tax_balance, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "あと何ヶ月もつ？", "数値・内容": round(min(runway, 12), 1), "単位": "ヶ月"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "資金判定", "数値・内容": status, "単位": ""},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "あといくら必要？", "数値・内容": shortage_for_safety, "単位": "万円"},
    {"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "改善必要額", "数値・内容": needed_improvement, "単位": "万円"},
]

if danger_month is not None:
    summary_rows.append({"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "お金が足りなくなる時期", "数値・内容": danger_month, "単位": "ヶ月後"})
else:
    summary_rows.append({"出力日": today_str, "会社名": company_name, "分類": "計算結果", "項目名": "お金が足りなくなる時期", "数値・内容": "12ヶ月以内なし", "単位": ""})

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
# 結果カード（改善版）
# =========================
st.markdown(f"""
    <div class="center-card" style="background:{color}; color:white;">
        <div class="sub-big">今の状態は？</div>
        <div class="big-status-font">{status}</div>
        <div style="font-size:1.15rem; color:white;">
            このままだと、あと {min(runway, 12):.1f} ヶ月もちます
        </div>
    </div>
""", unsafe_allow_html=True)

# =========================
# メーター（改善版・スマホ対応）
# =========================
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=min(runway, 12),
    domain={"x": [0, 1], "y": [0, 1]},
    title={
        "text": "あと何ヶ月もつ？", 
        "font": {
            "size": 28,  # PCサイズ
            "color": "#111827",
            "family": "Noto Sans JP, sans-serif",
            "weight": 700
        }
    },
    number={
        "suffix": " ヶ月",
        "font": {
            "size": 48,  # 数字を大きく
            "color": "#0f172a",
            "family": "Noto Sans JP, sans-serif",
            "weight": 900
        }
    },
    gauge={
        "axis": {
            "range": [0, 12], 
            "tickwidth": 2,  # 目盛りを太く
            "tickcolor": "#334155",
            "tickfont": {
                "size": 14,  # 目盛りの数字を大きく
                "color": "#475569"
            }
        },
        "bar": {"color": color, "thickness": 0.6},  # バーを太く
        "bgcolor": "white",
        "borderwidth": 3,  # 枠を太く
        "bordercolor": "#94a3b8",
        "steps": [
            {"range": [0, 3], "color": "#fee2e2"},
            {"range": [3, 6], "color": "#fef3c7"},
            {"range": [6, 12], "color": "#dcfce7"}
        ],
        "threshold": {
            "line": {"color": "#7f1d1d", "width": 5},  # しきい値線を太く
            "thickness": 0.8,
            "value": min(runway, 12)
        }
    }
))

fig.update_layout(
    height=330,
    margin=dict(l=20, r=20, t=60, b=12),
    paper_bgcolor="#eef3f8",
    font=dict(
        family="Noto Sans JP, sans-serif",
        size=16,
        color="#111827"
    )
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# 詳細データ（改善版）
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 詳しく見る")

col_a, col_b = st.columns(2)

with col_a:
    st.metric(
        "💰 手元に残る利益", 
        f"{gross_profit:,.0f} 万円",
        help="売上 - 外注材料費"
    )
    
    # 最重要指標を強調
    if after_tax_balance >= 0:
        st.metric(
            "📈 毎月いくら増える？", 
            f"+{after_tax_balance:,.0f} 万円",
            delta="増えています",
            help="税金を払った後、毎月これだけ増えます"
        )
    else:
        st.metric(
            "📉 毎月いくら減る？", 
            f"{after_tax_balance:,.0f} 万円",
            delta="減っています",
            delta_color="inverse",
            help="税金を払った後、毎月これだけ減ります"
        )

with col_b:
    st.metric(
        "💸 税金の支払い", 
        f"{estimated_tax:,.0f} 万円",
        help="だいたいこれくらい税金がかかります"
    )
    
    if shortage_for_safety > 0:
        st.metric(
            "⚠️ あといくら必要？", 
            f"{shortage_for_safety:,.0f} 万円",
            help="6ヶ月安心して経営するために必要な金額"
        )
    else:
        st.metric(
            "✅ 安全ライン達成", 
            "OK！",
            help="6ヶ月分の余裕があります"
        )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 危険月表示（修正版）
# =========================
if danger_month is not None:
    st.markdown(f"""
    <div style="background: #fee2e2; padding: 20px; border-radius: 12px; border-left: 8px solid #b91c1c; margin: 15px 0;">
        <h3 style="color: #991b1b; margin-top: 0; margin-bottom: 10px;">
            🚨 このままだと危険です！
        </h3>
        <p style="font-size: 1.2rem; font-weight: bold; color: #7f1d1d; margin: 10px 0;">
            あと <span style="font-size: 2rem; color: #991b1b;">{danger_month}</span> ヶ月で現金が足りなくなります
        </p>
        <p style="color: #991b1b; margin: 10px 0;">
            今すぐ対策が必要です ↓
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="background: #dcfce7; padding: 20px; border-radius: 12px; border-left: 8px solid #15803d; margin: 15px 0;">
        <h3 style="color: #15803d; margin-top: 0; margin-bottom: 10px;">
            ✅ 安心してください
        </h3>
        <p style="font-size: 1.1rem; color: #166534; margin: 10px 0;">
            12ヶ月以内に現金が足りなくなる心配はありません
        </p>
        <p style="color: #15803d; margin: 10px 0;">
            この調子で経営を続けましょう！
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================
# 一撃アクション（完全修正版・分割方式）
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🎯 今すぐやること")

if after_tax_balance >= 0:
    # ========== 黒字の場合 ==========
    
    # ヘッダー部分
    st.markdown(f"""
    <div class="action-box" style="border-left: 8px solid #15803d; background: #f0fdf4;">
        <h4 style="color: #0f172a; margin-top: 0; margin-bottom: 10px;">
            😊 良いですね！毎月 <span style="color: #15803d; font-size: 1.3rem; font-weight: bold;">+{after_tax_balance:,.0f} 万円</span> 増えています
        </h4>
        <p style="font-weight: bold; font-size: 1.1rem; margin-top: 15px; margin-bottom: 15px; color: #0f172a;">
            今の良い状態を活かしましょう：
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ボックス1：現金をもっと貯める
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <p style="font-size: 1.05rem; margin: 0; line-height: 1.6; color: #0f172a;">
            💰 <b>現金をもっと貯める</b><br>
            <span style="color: #64748b;">→ 今の調子で貯金を増やせば、もっと安心できます</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ボックス2：利益の高い仕事を優先
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <p style="font-size: 1.05rem; margin: 0; line-height: 1.6; color: #0f172a;">
            📈 <b>利益の高い仕事を優先</b><br>
            <span style="color: #64748b;">→ 儲かる仕事を選んで受注しましょう</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ボックス3：会社を大きくする判断に使う
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <p style="font-size: 1.05rem; margin: 0; line-height: 1.6; color: #0f172a;">
            🚀 <b>会社を大きくする判断に使う</b><br>
            <span style="color: #64748b;">→ 人を雇う、機械を買う、などの判断材料にできます</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    # ========== 赤字の場合 ==========
    
    # ヘッダー部分
    st.markdown(f"""
    <div class="action-box" style="border-left: 8px solid #b91c1c; background: #fef2f2;">
        <h4 style="color: #0f172a; margin-top: 0; margin-bottom: 10px;">
            😰 今のままだと、毎月 <span style="color: #b91c1c; font-size: 1.3rem; font-weight: bold;">{abs(after_tax_balance):,.0f} 万円</span> ずつ減ります
        </h4>
        <p style="font-weight: bold; font-size: 1.1rem; margin-top: 15px; margin-bottom: 15px; color: #0f172a;">
            すぐに次のどれかをやりましょう：
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ボックス1：売上を増やす
    st.markdown(f"""
    <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <p style="font-size: 1.05rem; margin: 0; line-height: 1.6; color: #0f172a;">
            💡 <b>売上を増やす</b><br>
            → <span style="color: #2563eb; font-weight: bold;">あと {needed_sales_up:,.0f} 万円</span> 売上を上げれば安全圏<br>
            <span style="color: #64748b;">→ 例：月1件、{needed_sales_up:,.0f}万円の案件を追加</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ボックス2：コストを減らす
    st.markdown(f"""
    <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <p style="font-size: 1.05rem; margin: 0; line-height: 1.6; color: #0f172a;">
            💡 <b>コストを減らす</b><br>
            → <span style="color: #2563eb; font-weight: bold;">あと {needed_cost_down:,.0f} 万円</span> 原価を下げれば安全圏<br>
            <span style="color: #64748b;">→ 例：外注費を見直す、材料の仕入れ先を検討</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ボックス3：その他の対策
    st.markdown("""
    <div style="background: white; padding: 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <p style="font-size: 1.05rem; margin: 0; line-height: 1.6; color: #0f172a;">
            💡 <b>その他の対策</b><br>
            <span style="color: #64748b;">→ 人件費・家賃を見直せないか検討</span><br>
            <span style="color: #64748b;">→ 借金の返済額を相談できないか銀行に聞いてみる</span><br>
            <span style="color: #64748b;">→ 売掛金の回収を早められないか確認</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)




# =========================
# 改善ポイント（改善版・よりシンプル）
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("💡 状態別アドバイス")

if status == "危険":
    st.markdown("""
    <div style="background: #fee2e2; padding: 20px; border-radius: 12px; border-left: 6px solid #b91c1c;">
        <h4 style="color: #991b1b; margin-top: 0;">🚨 緊急対応が必要です</h4>
        <ul style="color: #7f1d1d; font-size: 1.05rem; line-height: 1.8;">
            <li><b>売掛金の回収を早める</b>（前倒し請求できないか交渉）</li>
            <li><b>外注費・材料費を見直す</b>（相見積もり、仕入れ先変更）</li>
            <li><b>人件費・家賃を圧縮できないか検討</b></li>
            <li><b>銀行に返済の相談</b>（リスケジュール）</li>
            <li><b>必要なら短期の資金調達も検討</b>（ビジネスローン等）</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
elif status == "注意":
    st.markdown("""
    <div style="background: #fef3c7; padding: 20px; border-radius: 12px; border-left: 6px solid #d97706;">
        <h4 style="color: #92400e; margin-top: 0;">⚠️ 注意が必要です</h4>
        <ul style="color: #78350f; font-size: 1.05rem; line-height: 1.8;">
            <li><b>利益をもう少し増やしたい</b>（売上UP or コストDOWN）</li>
            <li><b>現場ごとの利益を確認</b>（どの仕事が儲かってる？）</li>
            <li><b>3〜6ヶ月先の資金繰りを確認</b>（大きな支払い予定は？）</li>
            <li><b>利益が残る仕事を優先</b>（薄利の仕事は減らす）</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
else:
    st.markdown("""
    <div style="background: #dcfce7; padding: 20px; border-radius: 12px; border-left: 6px solid #15803d;">
        <h4 style="color: #15803d; margin-top: 0;">✅ 資金状況は安全です</h4>
        <ul style="color: #166534; font-size: 1.05rem; line-height: 1.8;">
            <li><b>安全圏を維持しながら事業拡大</b></li>
            <li><b>利益率の高い仕事を優先</b>（質の良い仕事を選ぶ）</li>
            <li><b>現金をもっと厚くする</b>（もっと安心できる）</li>
            <li><b>人を雇う、機械を買うなどの判断に活用</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# LINE誘導
# =========================
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
📱 LINEで友達追加！
</a>
</div>
""", unsafe_allow_html=True)

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
# =========================
# 12ヶ月推移グラフ（見切れ防止版）
# =========================
if is_pro:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 このままだと12ヶ月後いくら残る？")
    
    fig2 = go.Figure()
    
    # 税引後現預金（メイン）
    fig2.add_trace(go.Scatter(
        x=df_forecast["何ヶ月後"],
        y=df_forecast["税引後残高_万円"],
        mode="lines+markers",
        name="現金残高",
        line=dict(color="#2563eb", width=4),
        marker=dict(size=10),
        hovertemplate='%{x}ヶ月後: %{y:,.0f}万円<extra></extra>'
    ))
    
    # 0円ライン（危険ライン）
    fig2.add_hline(
        y=0,
        line_dash="dash",
        line_color="#b91c1c",
        line_width=3,
        annotation_text="⚠️ 0円",
        annotation_position="bottom right",
        annotation_font=dict(size=12, color="#b91c1c")
    )
    
    # 6ヶ月分の安全ライン
    safe_line = (fixed_cost + loan_pay) * 6
    if safe_line > 0:
        fig2.add_hline(
            y=safe_line,
            line_dash="dash",
            line_color="#15803d",
            line_width=3,
            annotation_text=f"✅ {safe_line:,.0f}万",
            annotation_position="top right",
            annotation_font=dict(size=12, color="#15803d")
        )
    
    # レイアウト設定（見切れ防止）
    fig2.update_layout(
        # X軸の設定
        xaxis=dict(
            title="何ヶ月後？",
            title_font=dict(size=16, weight=700, color="#111827"),
            tickfont=dict(size=14, color="#475569"),
            tickmode='linear',
            tick0=0,
            dtick=1,  # 1ヶ月刻み
            range=[-0.5, 12.5],  # 余白を持たせる
            fixedrange=False,  # ズーム可能
            showgrid=True,
            gridcolor="#e5e7eb",
            gridwidth=1
        ),
        
        # Y軸の設定
        yaxis=dict(
            title="現金残高（万円）",
            title_font=dict(size=16, weight=700, color="#111827"),
            tickfont=dict(size=14, color="#475569"),
            fixedrange=False,  # ズーム可能
            showgrid=True,
            gridcolor="#e5e7eb",
            gridwidth=1,
            zeroline=True,
            zerolinecolor="#cbd5e1",
            zerolinewidth=2
        ),
        
        # 全体の設定
        height=400,
        paper_bgcolor="white",
        plot_bgcolor="#f8fafc",
        font=dict(
            family="Noto Sans JP, sans-serif",
            size=14,
            color="#111827"
        ),
        
        # マージン設定（見切れ防止の重要ポイント）
        margin=dict(
            l=60,   # 左余白（Y軸ラベル用）
            r=40,   # 右余白
            t=40,   # 上余白
            b=60    # 下余白（X軸ラベル用）
        ),
        
        # ホバー設定
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Noto Sans JP, sans-serif"
        ),
        
        # 凡例設定
        showlegend=True,
        legend=dict(
            orientation="h",  # 横並び
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=14),
            bgcolor="rgba(255,255,255,0.8)"
        ),
        
        # レスポンシブ対応
        autosize=True
    )
    
    # グラフ表示（重要：use_container_width=True）
    st.plotly_chart(fig2, use_container_width=True, config={
        'displayModeBar': False,  # ツールバー非表示
        'responsive': True
    })
    
    st.markdown("</div>", unsafe_allow_html=True)





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
# 法的表記
# =========================
st.header("特定商取引法に基づく表記")
st.markdown("""
**サービス概要**

本サービスは、建設業の経営者向けに、
売上・原価・固定費・借入返済などを入力することで、
資金余命およびキャッシュフローを可視化し、
資金ショートリスクを把握できるサブスクリプション型デジタルツールです。

PRO版では以下の機能が利用可能です：

・12ヶ月キャッシュ予測
・資金ショート検知
・CSV出力
・PDFレポート出力
・データ保存機能

**販売事業者**  
菅原工業

**運営責任者**  
菅原大輔

**電話番号**  
メールにてお問合せください。

**メールアドレス**  
ds62823@gmail.com

**販売価格**  
PROプラン：月額9,800円（税込）（サブスクリプション）

**商品以外の必要料金**  
インターネット接続に必要な通信費

**支払い方法**  
クレジットカード（Stripe決済）

**支払い時期**  
申込時に決済

**サービス提供時期**  
決済完了後すぐに利用可能

**キャンセル・返金について**  
デジタルサービスの特性上、決済後の返金は原則不可とします。
ただし、サービスに重大な不具合がある場合は個別に対応いたします。

キャンセルについて  
サブスクリプションはいつでも解約可能です。  
解約後、次回請求は発生しません。

*解約は次回更新日前までに行ってください。
""")

st.header("利用規約")
st.markdown("""
本サービスは、経営判断の参考情報を提供するものであり、
正確性・完全性を保証するものではありません。

本サービスの利用によって生じたいかなる損害についても、
運営者は一切の責任を負いません。

本サービスは予告なく内容を変更・停止する場合があります。

ユーザーは自己責任において本サービスを利用するものとします。
""")

st.header("プライバシーポリシー")
st.markdown("""
本サービスでは、ユーザーの個人情報を適切に管理し、
第三者に開示することはありません。

取得した情報は、サービス提供および改善のためにのみ利用します。

法令に基づく場合を除き、ユーザーの同意なく情報を第三者に提供することはありません。
""")

# =========================
# フッター
# =========================
if not is_pro:
    remain = max(0, DEMO_LIMIT - st.session_state.get("calc_count", 0))
    st.info(f"デモ版の残り計算回数：{remain} / {DEMO_LIMIT}")
else:
    st.success(f"Pro版をご利用中です。ログインユーザー: {st.session_state['auth_user']}")

