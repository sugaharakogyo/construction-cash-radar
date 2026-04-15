import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"
STRIPE_URL = "https://buy.stripe.com/6oU28rarietE5gM6m87N600"
TOKUSHO_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"
TERMS_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"
PRIVACY_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"

st.markdown("""
<style>
.block-container {
    max-width: 980px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}
.stApp {
    background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
}
.hero {
    background: linear-gradient(135deg, #ffffff 0%, #eaf2ff 55%, #dbeafe 100%);
    border: 1px solid #dbeafe;
    border-radius: 28px;
    padding: 32px 24px;
    box-shadow: 0 18px 40px rgba(15,23,42,0.06);
    margin-bottom: 18px;
}
.badge {
    display: inline-block;
    background: #2563eb;
    color: white;
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
}
.hero-title {
    font-size: 42px;
    font-weight: 900;
    line-height: 1.2;
    color: #0f172a;
    margin-bottom: 12px;
}
.hero-title .blue {
    color: #1d4ed8;
}
.hero-sub {
    font-size: 17px;
    line-height: 1.9;
    color: #334155;
    margin-bottom: 18px;
    font-weight: 600;
}
.card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 22px;
    padding: 22px 20px;
    box-shadow: 0 10px 24px rgba(15,23,42,0.05);
    margin-bottom: 16px;
}
.card-title {
    font-size: 24px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 10px;
}
.card-text {
    font-size: 16px;
    line-height: 1.85;
    color: #475569;
    font-weight: 600;
}
.notice {
    background: linear-gradient(180deg, #fff1f2 0%, #ffe4e6 100%);
    border: 1px solid #fecdd3;
    border-left: 6px solid #ef4444;
    border-radius: 22px;
    padding: 22px 20px;
    margin-bottom: 16px;
}
.notice-title {
    font-size: 28px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 10px;
}
.notice-text {
    font-size: 16px;
    line-height: 1.9;
    color: #374151;
    font-weight: 700;
}
.price {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 2px solid #16a34a;
    border-radius: 24px;
    padding: 28px 20px;
    text-align: center;
    margin-bottom: 16px;
}
.price-main {
    font-size: 48px;
    font-weight: 900;
    color: #166534;
    margin: 10px 0 6px;
}
.footer-box {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    color: #64748b;
    font-size: 14px;
    line-height: 1.9;
    margin-top: 16px;
}
@media (max-width: 768px) {
    .hero-title {
        font-size: 32px;
    }
    .hero-sub {
        font-size: 15px;
    }
    .card-title {
        font-size: 21px;
    }
    .notice-title {
        font-size: 23px;
    }
    .price-main {
        font-size: 40px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="badge">建設会社専用 / 最短30秒 無料診断</div>
    <div class="hero-title">
        <span class="blue">資金あと何ヶ月もつか</span><br>
        一発で分かる
    </div>
    <div class="hero-sub">
        売上・原価・固定費・現金を入れるだけで、<br>
        あなたの会社の資金ショート危険度と安全ライン不足額を見える化します。
    </div>
</div>
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL, use_container_width=True)
st.caption("登録不要ですぐ使えます")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">資金ショートまでの期間</div>
        <div class="card-text">あと何ヶ月持つかを、その場で把握できます。</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">安全ラインとの差額</div>
        <div class="card-text">あといくら足りないかが明確になります。</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">改善ポイント</div>
        <div class="card-text">どこを直せばいいか、優先順位が見えます。</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="notice">
    <div class="notice-title">売上があっても、現金が尽きたら終わりです。</div>
    <div class="notice-text">
        利益が出ていても、入金サイト・原価率・固定費のズレで、
        突然お金が回らなくなることがあります。<br>
        会計ソフトや試算表だけでは見えない未来の資金繰りを先に確認するためのサービスです。
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="card-title">こんなお悩みありませんか？</div>
    <div class="card-text">
        ・売上はあるのにお金が残らない<br>
        ・原価率が高い現場に後から気づく<br>
        ・このままで本当に大丈夫か不安<br>
        ・銀行や税理士に数字を説明しづらい
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="card-title">このサービスが向いている会社</div>
    <div class="card-text">
        ・月ごとの資金繰りを先に把握したい会社<br>
        ・社長が数字判断を早くしたい会社<br>
        ・税理士、銀行との会話を強くしたい会社
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="price">
    <div style="font-size:13px;font-weight:900;color:#166534;">おすすめ</div>
    <div style="font-size:30px;font-weight:900;color:#0f172a;line-height:1.45;margin-top:10px;">
        社長専用 Proダッシュボード
    </div>
    <div style="font-size:16px;line-height:1.9;color:#1f2937;font-weight:700;margin-top:10px;">
        12ヶ月資金推移<br>
        現場利益管理<br>
        銀行提出サマリー<br>
        利益改善シミュレーター
    </div>
    <div class="price-main">月 9,800円</div>
    <div style="font-size:14px;color:#475569;font-weight:700;">まずは無料診断から始められます</div>
</div>
""", unsafe_allow_html=True)

st.link_button("PRO版を始める（月額9,800円）", STRIPE_URL, use_container_width=True)
st.link_button("LINEで問い合わせる", LINE_URL, use_container_width=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("特定商取引法に基づく表記", TOKUSHO_URL, use_container_width=True)
with c2:
    st.link_button("利用規約", TERMS_URL, use_container_width=True)
with c3:
    st.link_button("プライバシーポリシー", PRIVACY_URL, use_container_width=True)

st.markdown("""
<div class="footer-box">
    建設会社の資金不安を、数字で見える化。<br>
    会計ソフトでは見えない未来のキャッシュを、すぐ確認できます。
</div>
""", unsafe_allow_html=True)
