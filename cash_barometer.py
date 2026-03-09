import streamlit as st
import pandas as pd
import altair as alt
import json
from pathlib import Path
import datetime
st.markdown("""
<style>
.result-danger{
    background:#ffe5e5 !important;
    color:#111 !important;
    border-left:12px solid #ff4d4f !important;
    border-radius:18px !important;
    padding:20px !important;
    margin-top:18px !important;
}
.result-danger .kpi-big,
.result-danger .kpi-mid,
.result-danger .card-body,
.result-danger div,
.result-danger span,
.result-danger b{
    color:#111 !important;
}

.result-warn{
    background:#fff3cd !important;
    color:#111 !important;
    border-left:12px solid #f4b400 !important;
    border-radius:18px !important;
    padding:20px !important;
    margin-top:18px !important;
}
.result-warn .kpi-big,
.result-warn .kpi-mid,
.result-warn .card-body,
.result-warn div,
.result-warn span,
.result-warn b{
    color:#111 !important;
}

.result-safe{
    background:#e6f7e6 !important;
    color:#111 !important;
    border-left:12px solid #2e7d32 !important;
    border-radius:18px !important;
    padding:20px !important;
    margin-top:18px !important;
}
.result-safe .kpi-big,
.result-safe .kpi-mid,
.result-safe .card-body,
.result-safe div,
.result-safe span,
.result-safe b{
    color:#111 !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 設定・保存
# ===============================
SAVE_PATH = Path("cash_barometer_state.json")


def load_state() -> dict:
    if SAVE_PATH.exists():
        try:
            return json.loads(SAVE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state():
    data = {
        "sales": st.session_state.get("sales", 0),
        "cost": st.session_state.get("cost", 0),
        "fixed_total": st.session_state.get("fixed_total", 0),
        "cash_on_hand": st.session_state.get("cash_on_hand", 0),
        "plan": st.session_state.get("plan", "デモ（無料）"),
        "tax_rate": st.session_state.get("tax_rate", 0.30),
        "safety_months": st.session_state.get("safety_months", 6),
        "scenario_pct": st.session_state.get("scenario_pct", 0),
        "calc_count": st.session_state.get("calc_count", 0),
        "pro_unlocked": st.session_state.get("pro_unlocked", False),
        "projects": st.session_state.get("projects", []),
    }
    SAVE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def yen(n: float) -> str:
    try:
        return f"{int(round(float(n))):,}円"
    except Exception:
        return "0円"


def safe_div(a: float, b: float, default: float = 0.0) -> float:
    try:
        if float(b) == 0:
            return default
        return float(a) / float(b)
    except Exception:
        return default


# ===============================
# ページ設定
# ===============================
st.set_page_config(page_title="建設キャッシュレーダー", layout="wide")

# ===============================
# スマホ用レイアウト調整（上のほうでOK）
# ===============================
st.markdown(
    """
<style>
@media (max-width: 768px) {
  h1 { font-size: 26px !important; }
  h2 { font-size: 22px !important; }
  h3 { font-size: 20px !important; }

  .block-container {
    padding-top: 1rem;
    padding-left: 0.9rem;
    padding-right: 0.9rem;
  }

  div[data-testid="stMetricValue"] { font-size: 22px !important; }
  div[data-testid="stMetricLabel"] { font-size: 13px !important; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ===============================
# 初期値
# ===============================
defaults = {
    "sales": 9_500_000,
    "cost": 6_100_000,
    "fixed_total": 4_000_000,  # 固定費ぜんぶ（人件費/家賃/リース/返済/その他）
    "cash_on_hand": 6_800_000,
    "plan": "デモ（無料）",
    "tax_rate": 0.30,
    "safety_months": 6,
    "scenario_pct": -10,
    "calc_count": 0,
    "pro_unlocked": False,
    "projects": [],
}

saved = load_state()
for k, v in defaults.items():
    st.session_state.setdefault(k, saved.get(k, v))

# ===============================
# デモ / Pro
# ===============================
DEMO_LIMIT = 6

with st.sidebar:
    st.header("📌 入力（ざっくりでOK）")

    st.markdown("## 🔐 プラン")
    plan= "デモ（無料）"
    if "is_pro" not in st.session_state:
        st.session_state.is_pro = False

    if plan == "デモ（無料）":
        st.session_state.is_pro = False
        st.caption("※ デモは一部制限あり（計算ボタン6回まで）")
    else:
        if st.session_state.pro_unlocked:
            st.session_state.is_pro = True
            st.success("Pro 解放中")
        else:
            pro_key = st.text_input("Proキー", type="password")
            if pro_key == "9800":
                st.session_state.pro_unlocked = True
                st.session_state.is_pro = True
                save_state()
                st.success("Pro 解放！")
            elif pro_key:
                st.session_state.is_pro = False
                st.error("キーが違うよ")

    is_pro = st.session_state.is_pro
    demo_locked = (not is_pro) and (st.session_state.calc_count >= DEMO_LIMIT)

    st.subheader("📊 月次入力")
    st.number_input(
        "売上（月）",
        min_value=0,
        step=100000,
        key="sales",
        disabled=(not is_pro),  # デモは固定
        on_change=save_state,
    )
    st.number_input(
        "原価（月）※材料+外注など",
        min_value=0,
        step=100000,
        key="cost",
        disabled=(not is_pro),  # デモは固定
        on_change=save_state,
    )
    st.number_input(
        "固定費（全部）※人件費/家賃/返済/リース/その他",
        min_value=0,
        step=100000,
        key="fixed_total",
        on_change=save_state,
    )
    st.number_input(
        "現在の現金残高",
        min_value=0,
        step=100000,
        key="cash_on_hand",
        on_change=save_state,
    )

    st.divider()
    st.subheader("⚙️ 設定（ざっくり）")
    st.slider("税率（概算）", 0.0, 0.5, float(st.session_state.tax_rate), 0.01, key="tax_rate", on_change=save_state)
    st.slider("安全ライン（月）", 3, 12, int(st.session_state.safety_months), 1, key="safety_months", on_change=save_state)

    st.divider()
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("💾 保存"):
            save_state()
            st.success("保存しました！")
    with col_s2:
        if st.button("🧹 保存を初期化"):
            if SAVE_PATH.exists():
                SAVE_PATH.unlink()
            st.session_state.clear()
            st.rerun()

# ===============================
# タイトル
# ===============================
left, right = st.columns([1, 7])
with left:
    if Path("logo.png").exists():
        st.image("logo.png", width=120)
with right:
    st.markdown(
        """# 建設キャッシュレーダー
売上と現場コストを入れるだけ。 **「いつ資金ショートするか」「安全にするには月いくら必要か」** が一発で見える。"""
    )

# ===============================
# 計算（共通）
# ===============================
sales = float(st.session_state.sales)
cost = float(st.session_state.cost)
fixed_total = float(st.session_state.fixed_total)
cash_on_hand = float(st.session_state.cash_on_hand)
tax_rate = float(st.session_state.tax_rate)
safety_months = int(st.session_state.safety_months)

gross = sales - cost
burn = fixed_total
delta_pre = gross - burn
tax_est = delta_pre * tax_rate if delta_pre > 0 else 0
delta_after = delta_pre - tax_est  # 税後の月次増減

# 資金余命（税後がマイナスのときだけ）
runway_months = None
if delta_after < 0:
    runway_months = cash_on_hand / abs(delta_after) if abs(delta_after) > 0 else 0

# 資金ショート日（ざっくり 30日=1ヶ月換算）
today = datetime.date.today()
short_date = None
if runway_months is not None:
    months_left = max(0, int(runway_months))
    short_date = today + datetime.timedelta(days=months_left * 30)

# 安全ライン（手元目標）
target_cash = burn * safety_months
need_cash = max(0.0, target_cash - cash_on_hand)

# 月あたり必要な税後利益
need_after_per_month = None
if safety_months > 0 and need_cash > 0:
    need_after_per_month = need_cash / safety_months

# 売上アップ目安（原価率を現状維持の前提で逆算）
cost_rate_now = (cost / sales) if sales > 0 else 0.65
gross_margin_rate = max(0.01, 1.0 - cost_rate_now)

need_sales_per_month = None
if need_after_per_month is not None:
    denom = gross_margin_rate * max(0.01, (1.0 - tax_rate))
    need_sales_per_month = need_after_per_month / denom if denom > 0 else None

SALES_BUFFER = 1.3
need_sales_safe = None
if need_sales_per_month is not None:
    need_sales_safe = need_sales_per_month * SALES_BUFFER

# 固定費を下げるなら（税後の必要利益を税前に戻すイメージ）
need_cost_cut = None
if need_after_per_month is not None:
    need_cost_cut = need_after_per_month / max(0.01, (1.0 - tax_rate))
    need_cost_cut *= SALES_BUFFER

# ===============================
# 計算ボタン（デモ回数管理）
# ===============================
is_pro = st.session_state.is_pro
demo_locked = (not is_pro) and (st.session_state.calc_count >= DEMO_LIMIT)
can_calculate = is_pro or (st.session_state.calc_count < DEMO_LIMIT)

col_btn1, col_btn2 = st.columns([1, 3])
with col_btn1:
    calc = st.button("計算する", type="primary", disabled=not can_calculate)
with col_btn2:
    st.caption("※ デモは計算ボタンが6回まで。Proは無制限。")

if calc and (not is_pro):
    st.session_state.calc_count += 1
    save_state()
    st.rerun()

if demo_locked:
    st.error("⛔ デモは6回までです。続きはProでご利用ください。")


if calc:
    # ===============================
    # 共通計算
    # ===============================
    months_left = 0
    if runway_months is not None:
        months_left = max(0, int(runway_months))

    # ===============================
    # ① 資金ショート結果カード
    # ===============================
    if runway_months is None:
        st.markdown(f"""
        <div style="
            background:#e6f7e6;
            border-left:12px solid #2e7d32;
            border-radius:18px;
            padding:22px;
            margin-top:18px;
            color:#111;
            box-shadow:0 4px 14px rgba(0,0,0,0.06);
        ">
            <div style="font-size:40px; font-weight:900; line-height:1.3; color:#111;">
                🟢 いまは安全です
            </div>
            <div style="font-size:18px; line-height:1.8; margin-top:10px; color:#111;">
                税後でも黒字で、資金ショートの心配は小さい状態です。<br>
                安全ライン（6ヶ月分の固定費）: <b>{yen(safe_cash)}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="
            background:#ffe5e5;
            border-left:12px solid #ff4d4f;
            border-radius:18px;
            padding:22px;
            margin-top:18px;
            color:#111;
            box-shadow:0 4px 14px rgba(0,0,0,0.06);
        ">
            <div style="font-size:42px; font-weight:900; line-height:1.3; color:#111;">
                ⚠ 資金ショートまで<br>あと {months_left} ヶ月
            </div>
            <div style="font-size:18px; line-height:1.8; margin-top:10px; color:#111;">
                このままだと毎月 <b>{yen(abs(delta_after))}</b> ずつ現金が減ります。<br>
                年間では <b>{yen(abs(delta_after) * 12)}</b> のキャッシュ減少です。
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ===============================
    # ② 安全ラインカード
    # ===============================
    if lack_cash > 0:
        st.markdown(f"""
        <div style="
            background:#fff3cd;
            border-left:12px solid #f4b400;
            border-radius:18px;
            padding:22px;
            margin-top:18px;
            color:#111;
            box-shadow:0 4px 14px rgba(0,0,0,0.06);
        ">
            <div style="font-size:30px; font-weight:900; line-height:1.4; color:#111;">
                安全ラインまで不足<br>{yen(lack_cash)}
            </div>
            <div style="font-size:18px; line-height:1.8; margin-top:10px; color:#111;">
                安全にするには、ざっくり<br>
                <b>売上 +{yen(need_sales_safe)} / 月</b><br>
                を目安に見直す必要があります。
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="
            background:#e6f7e6;
            border-left:12px solid #2e7d32;
            border-radius:18px;
            padding:22px;
            margin-top:18px;
            color:#111;
            box-shadow:0 4px 14px rgba(0,0,0,0.06);
        ">
            <div style="font-size:30px; font-weight:900; line-height:1.4; color:#111;">
                安全ラインクリア
            </div>
            <div style="font-size:18px; line-height:1.8; margin-top:10px; color:#111;">
                現在の現金は、6ヶ月安全ラインを超えています。
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ===============================
    # ③ 今すぐ分かる結論
    # ===============================
    urgency = "危険"
    urgency_msg = f"資金余命は約 {months_left} ヶ月。今月中に改善が必要です。"

    if runway_months is None:
        urgency = "安全"
        urgency_msg = "税後でも黒字です。まずは今の水準維持を優先してください。"
    elif months_left >= 12:
        urgency = "注意"
        urgency_msg = f"まだ余裕はありますが、放置すると {months_left} ヶ月後に危険です。"

    st.markdown(f"""
    <div style="
        background:#ffffff;
        border:3px solid #ececec;
        border-radius:18px;
        padding:22px;
        margin-top:20px;
        color:#111;
        box-shadow:0 4px 14px rgba(0,0,0,0.04);
    ">
        <div style="font-size:20px; font-weight:900; color:#111;">⚡ 今すぐ分かる結論</div>
        <div style="margin-top:10px; font-size:17px; line-height:1.8; color:#111;">
            <b>{urgency}</b>。{urgency_msg}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===============================
    # ④ 今日やる打ち手
    # ===============================
    actions = []

    if lack_cash > 0:
        actions.append(f"まず <b>売上 +{yen(need_sales_safe)} / 月</b> を目安に改善する")
    if delta_after < 0:
        actions.append("入金を早くする（請求締め・入金サイト短縮）")
        actions.append("固定費と返済額を見直す")
        actions.append("原価率の高い現場を洗い出す")

    if not actions:
        actions.append("今の利益率と現金残高を維持する")
        actions.append("原価率が高い現場だけ毎月チェックする")

    actions_html = "".join([f"<li style='margin-bottom:8px;'>{a}</li>" for a in actions[:4]])

    st.markdown(f"""
    <div style="
        background:#ffffff;
        border:3px solid #ececec;
        border-radius:18px;
        padding:22px;
        margin-top:20px;
        color:#111;
        box-shadow:0 4px 14px rgba(0,0,0,0.04);
    ">
        <div style="font-size:20px; font-weight:900; color:#111;">✅ 今日やる打ち手（最短で効く順）</div>
        <div style="margin-top:10px; font-size:17px; line-height:1.8; color:#111;">
            <ul style="padding-left:22px; margin:0;">
                {actions_html}
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===============================
    # ⑤ 12ヶ月資金推移グラフ
    # ===============================
    months = list(range(1, 13))
    cash_list = []
    current_cash = cash_on_hand

    for _ in months:
        current_cash = current_cash + delta_after
        cash_list.append(current_cash)

    df_cash = pd.DataFrame({
        "月": months,
        "現金残高": cash_list
    })

    st.markdown("""
    <div style="
        background:#ffffff;
        border:3px solid #ececec;
        border-radius:18px;
        padding:22px;
        margin-top:20px;
        color:#111;
        box-shadow:0 4px 14px rgba(0,0,0,0.04);
    ">
        <div style="font-size:20px; font-weight:900; color:#111;">📈 Proで見える12ヶ月資金推移</div>
        <div style="margin-top:10px; font-size:16px; line-height:1.8; color:#111;">
            今の条件のまま進んだ場合、現金が12ヶ月でどう動くかを確認できます。
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.line_chart(df_cash.set_index("月"))

    # ===============================
    # ⑥ Pro申込み導線
    # ===============================
    st.markdown("""
    <div style="
        background:#eef9f0;
        border:4px solid #2e7d32;
        border-radius:20px;
        padding:24px;
        margin-top:22px;
        text-align:center;
        color:#111;
        box-shadow:0 4px 14px rgba(0,0,0,0.05);
    ">
        <div style="font-size:34px; font-weight:900; line-height:1.4; color:#111;">
            続きは Pro版へ
        </div>
        <div style="font-size:18px; line-height:1.9; margin-top:12px; color:#111;">
            Pro版では<br>
            <b>12ヶ月資金推移</b>・<b>現場利益管理</b>・<b>銀行提出サマリー</b><br>
            まで使えます。
        </div>
        <div style="font-size:44px; font-weight:900; margin-top:16px; color:#111;">
            月 9,800円
        </div>
        <div style="font-size:16px; margin-top:8px; color:#111;">
            デモは6回まで / Proは無制限
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🚀 Proを申し込む（LINE）",
        "https://lin.ee/7m28VAs",
        use_container_width=True
    )



