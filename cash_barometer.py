import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import json
from pathlib import Path

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
# 保存ファイル設定
# =========================
SAVE_FILE = Path("cash_radar_state.json")

DEFAULT_STATE = {
    "cash": 1000,
    "revenue": 900,
    "cost": 558,
    "fixed_cost": 260,
    "loan_pay": 50,
    "tax_rate": 0.30,
    "plan": "デモ（無料）",
    "calc_count": 0
}

DEMO_LIMIT = 6

# =========================
# 保存・読込関数
# =========================
def load_state():
    if SAVE_FILE.exists():
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {**DEFAULT_STATE, **data}
        except Exception:
            return DEFAULT_STATE.copy()
    return DEFAULT_STATE.copy()

def save_state():
    data = {
        "cash": st.session_state.get("cash", DEFAULT_STATE["cash"]),
        "revenue": st.session_state.get("revenue", DEFAULT_STATE["revenue"]),
        "cost": st.session_state.get("cost", DEFAULT_STATE["cost"]),
        "fixed_cost": st.session_state.get("fixed_cost", DEFAULT_STATE["fixed_cost"]),
        "loan_pay": st.session_state.get("loan_pay", DEFAULT_STATE["loan_pay"]),
        "tax_rate": st.session_state.get("tax_rate", DEFAULT_STATE["tax_rate"]),
        "plan": st.session_state.get("plan", DEFAULT_STATE["plan"]),
        "calc_count": st.session_state.get("calc_count", DEFAULT_STATE["calc_count"])
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def reset_state():
    for key, value in DEFAULT_STATE.items():
        st.session_state[key] = value
    save_state()

def count_demo_use():
    if st.session_state.get("plan") == "デモ（無料）":
        st.session_state["calc_count"] = st.session_state.get("calc_count", 0) + 1
        save_state()

# =========================
# 初期読込
# =========================
loaded = load_state()

for key, value in loaded.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================
# CSS
# =========================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Noto Sans JP', sans-serif;
    }

    .main {
        background-color: #f0f2f6;
    }

    .stNumberInput label, .stSlider label, .stRadio label {
        font-size: 1.05rem !important;
        font-weight: bold;
        color: #333333;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.12);
        margin-bottom: 20px;
    }

    .center-card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.12);
        margin-bottom: 20px;
        text-align: center;
    }

    .big-status-font {
        font-size: 4.2rem !important;
        font-weight: 900 !important;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        line-height: 1;
    }

    .sub-big {
        font-size: 1.2rem;
        font-weight: bold;
    }

    .action-box {
        background: #f8f9fa;
        border-left: 8px solid #007bff;
        padding: 18px;
        border-radius: 12px;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .pro-box {
        background: linear-gradient(135deg, #1f2937, #111827);
        color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.18);
        margin-bottom: 20px;
        text-align: center;
    }

    .demo-box {
        background: #fff8e1;
        color: #333333;
        padding: 18px;
        border-radius: 14px;
        border: 2px solid #ffe082;
        margin-bottom: 20px;
        text-align: center;
    }

    .stMetric {
        background-color: white;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        text-align: center;
        margin-bottom: 16px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.2rem;
        font-size: 1.05rem;
        font-weight: bold;
        background-color: #007bff;
        color: white;
        border: none;
    }

    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# タイトル
# =========================
st.title("🏗️ 建設キャッシュレーダー")
st.write("社長のための資金余命ダッシュボード。危険・注意・安定を一瞬で見える化。")

# =========================
# プラン選択
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🎫 プラン")

st.radio(
    "プランを選んでください",
    ["デモ（無料）", "Pro（月9,800円）"],
    key="plan",
    horizontal=True,
    on_change=save_state
)

if st.session_state["plan"] == "デモ（無料）":
    remain = max(0, DEMO_LIMIT - st.session_state.get("calc_count", 0))
    st.markdown(f"""
        <div class="demo-box">
            <b>デモ版</b><br>
            残り計算回数：<b>{remain} / {DEMO_LIMIT}</b>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="pro-box">
            <b>Pro版</b><br>
            計算回数 無制限 / 将来の追加機能も拡張しやすい状態です
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# デモ制限チェック
# =========================
if st.session_state["plan"] == "デモ（無料）" and st.session_state.get("calc_count", 0) >= DEMO_LIMIT:
    st.error("⚠️ デモ版の利用回数は上限に達しました。Pro版をご利用ください。")
    st.info("Pro版では、計算回数が無制限になります。")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if st.button("💎 Proに切り替える"):
            st.session_state["plan"] = "Pro（月9,800円）"
            save_state()
            st.rerun()
    with col_p2:
        if st.button("🔄 初期化する"):
            reset_state()
            st.rerun()
    st.stop()

# =========================
# 入力欄
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("💰 月次入力")

    col1, col2 = st.columns(2)

    with col1:
        st.number_input(
            "現在の現預金 (万円)",
            min_value=0,
            step=100,
            key="cash",
            on_change=save_state
        )
        st.number_input(
            "月平均売上 (万円)",
            min_value=0,
            step=50,
            key="revenue",
            on_change=save_state
        )
        st.number_input(
            "月平均原価 (万円)",
            min_value=0,
            step=10,
            key="cost",
            on_change=save_state
        )

    with col2:
        st.number_input(
            "月平均固定費 (万円)",
            min_value=0,
            step=10,
            key="fixed_cost",
            on_change=save_state
        )
        st.number_input(
            "月の借入返済 (万円)",
            min_value=0,
            step=5,
            key="loan_pay",
            on_change=save_state
        )
        st.slider(
            "税率（概算）",
            min_value=0.0,
            max_value=0.5,
            step=0.01,
            key="tax_rate",
            on_change=save_state
        )

    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("📊 計算する"):
            count_demo_use()
            st.rerun()
    with col_btn2:
        if st.button("💾 保存"):
            save_state()
            st.success("保存しました。")
    with col_btn3:
        if st.button("🔄 初期値に戻す"):
            reset_state()
            st.success("初期値に戻しました。")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 値取得
# =========================
cash = st.session_state["cash"]
revenue = st.session_state["revenue"]
cost = st.session_state["cost"]
fixed_cost = st.session_state["fixed_cost"]
loan_pay = st.session_state["loan_pay"]
tax_rate = st.session_state["tax_rate"]

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
    color = "#28a745"
elif runway >= 3:
    status = "注意"
    color = "#ffc107"
else:
    status = "危険"
    color = "#dc3545"

if after_tax_balance < 0:
    shortage_for_safety = max(0, abs(after_tax_balance) * 6 - cash)
else:
    shortage_for_safety = 0

needed_improvement = max(0, abs(after_tax_balance))
needed_sales_up = needed_improvement
needed_cost_down = needed_improvement

# =========================
# 結果カード
# =========================
st.markdown(f"""
    <div class="center-card" style="background-color:{color}; color:white;">
        <div class="sub-big">現在の資金状況</div>
        <div class="big-status-font">{status}</div>
        <div style="font-size:1.2rem;">資金余命の目安：{min(runway, 12):.1f} ヶ月</div>
    </div>
""", unsafe_allow_html=True)

# =========================
# メーター
# =========================
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=min(runway, 12),
    domain={"x": [0, 1], "y": [0, 1]},
    title={"text": "資金余命（目安）", "font": {"size": 28, "color": "#333333"}},
    gauge={
        "axis": {"range": [0, 12], "tickwidth": 1, "tickcolor": "#555555"},
        "bar": {"color": color},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 3], "color": "#ffe0e0"},
            {"range": [3, 6], "color": "#fff8e0"},
            {"range": [6, 12], "color": "#e0ffe0"}
        ],
        "threshold": {
            "line": {"color": "red", "width": 4},
            "thickness": 0.75,
            "value": min(runway, 12)
        }
    }
))
fig.update_layout(
    height=350,
    margin=dict(l=20, r=20, t=60, b=20),
    paper_bgcolor="#f0f2f6"
)
st.plotly_chart(fig, use_container_width=True)

# =========================
# 詳細データ
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 詳細データ")

col_a, col_b = st.columns(2)
with col_a:
    st.metric("粗利", f"{gross_profit:,.0f} 万円")
    st.metric("固定費", f"{fixed_cost:,.0f} 万円")
    st.metric("概算税金", f"{estimated_tax:,.0f} 万円")
with col_b:
    st.metric("借入返済", f"{loan_pay:,.0f} 万円")
    st.metric("税引後 月次増減", f"{after_tax_balance:,.0f} 万円")
    st.metric("安全ラインまでの不足額", f"{shortage_for_safety:,.0f} 万円")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 12ヶ月推移
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

df = pd.DataFrame({
    "月": months,
    "税前キャッシュ": cash_before_tax,
    "税後キャッシュ": cash_after_tax
})

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df["月"],
    y=df["税前キャッシュ"],
    mode="lines+markers",
    name="税前キャッシュ"
))
fig2.add_trace(go.Scatter(
    x=df["月"],
    y=df["税後キャッシュ"],
    mode="lines+markers",
    name="税後キャッシュ"
))

fig2.update_layout(
    title="📈 12ヶ月 現金推移（予測）",
    xaxis_title="月",
    yaxis_title="現金残高（万円）",
    height=420,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

st.plotly_chart(fig2, use_container_width=True)

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
        ・利益率の高い現場を増やす<br>
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

# =========================
# フッター
# =========================
if st.session_state["plan"] == "デモ（無料）":
    remain = max(0, DEMO_LIMIT - st.session_state.get("calc_count", 0))
    st.info(f"デモ版の残り計算回数：{remain} / {DEMO_LIMIT}")
else:
    st.success("Pro版をご利用中です。計算回数は無制限です。")
