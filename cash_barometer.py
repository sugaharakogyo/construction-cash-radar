import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="建設キャッシュレーダー")

# =========================
# CSS（iPhoneレベル）
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #eef2ff, #f8fafc);
}

.block-container {
    padding-top: 1rem;
    max-width: 850px;
}

/* ガラスカード */
.card {
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 22px;
    margin-bottom: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* メイン表示 */
.hero {
    padding: 30px;
    border-radius: 28px;
    text-align: center;
    color: white;
    font-weight: bold;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.big {
    font-size: 4.5rem;
    font-weight: 900;
}

.mid {
    font-size: 1.3rem;
    opacity: 0.9;
}

/* 数字カード */
.metric {
    background: white;
    border-radius: 18px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 6px 14px rgba(0,0,0,0.08);
}

/* 入力 */
input {
    border-radius: 12px !important;
    border: 2px solid #cbd5e1 !important;
}

/* ボタン */
.stButton button {
    border-radius: 14px;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: white;
    border: none;
}

/* LINE */
.line a {
    display:block;
    text-align:center;
    background: linear-gradient(135deg, #06c755, #00a843);
    color:white;
    padding:16px;
    border-radius:16px;
    text-decoration:none;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🏗️ 建設キャッシュレーダー")

# =========================
# 入力
# =========================
cash = st.number_input("現預金", value=1000)
revenue = st.number_input("売上", value=900)
cost = st.number_input("原価", value=500)
fixed = st.number_input("固定費", value=200)
loan = st.number_input("返済", value=50)

# =========================
# 計算
# =========================
gross = revenue - cost
balance = gross - fixed - loan
tax = max(0, balance * 0.3)
after = balance - tax

if after >= 0:
    runway = 12
else:
    runway = cash / abs(after)

if runway >= 6:
    status = "安全"
    color = "linear-gradient(135deg,#16a34a,#22c55e)"
elif runway >= 3:
    status = "注意"
    color = "linear-gradient(135deg,#f59e0b,#fbbf24)"
else:
    status = "危険"
    color = "linear-gradient(135deg,#dc2626,#ef4444)"

# =========================
# ヒーロー（iPhone感）
# =========================
st.markdown(f"""
<div class='hero' style='background:{color}'>
<div class='mid'>資金状況</div>
<div class='big'>{status}</div>
<div class='mid'>あと {runway:.1f} ヶ月</div>
</div>
""", unsafe_allow_html=True)

# =========================
# アクション
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

if after < 0:
    st.error(f"毎月 {abs(after):,.0f} 万円減る")
    st.write(f"👉 売上 +{abs(after):,.0f} / 原価 -{abs(after):,.0f}")
else:
    st.success(f"毎月 {after:,.0f} 万円増えてる")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# メーター
# =========================
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=min(runway, 12),
    gauge={'axis': {'range': [0, 12]}}
))
fig.update_layout(height=250)
st.plotly_chart(fig, use_container_width=True)

# =========================
# 数字カード
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div class='metric'>粗利<br><b>{gross}</b></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric'>税金<br><b>{tax}</b></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='metric'>返済<br><b>{loan}</b></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric'>最終<br><b>{after}</b></div>", unsafe_allow_html=True)

# =========================
# LINE
# =========================
st.markdown(f"""
<div class='card line'>
<a href="https://lin.ee/7m28VAs" target="_blank">
📱 LINEで相談する
</a>
</div>
""", unsafe_allow_html=True)
