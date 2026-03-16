import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

# Google Analytics
st.components.v1.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-V96H2R41TL"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-V96H2R41TL');
    </script>
    """,
    height=0,
)

st.markdown("""
<style>
.block-container{
    max-width: 900px;
    padding-top: 0.8rem;
    padding-bottom: 3rem;
}
.stApp{
    background: linear-gradient(180deg, #f8fbff 0%, #f6f7fb 100%);
}
h1,h2,h3,p,div,span{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.hero-box{
    background: linear-gradient(135deg, #020617 0%, #0b3b74 42%, #0284c7 100%);
    border-radius: 28px;
    padding: 24px 22px 22px 22px;
    box-shadow: 0 24px 52px rgba(0,0,0,0.28);
    margin-bottom: 18px;
}
.hero-badge{
    display:inline-block;
    background:#facc15;
    color:#111111 !important;
    font-weight:900;
    font-size:14px;
    border-radius:999px;
    padding:8px 14px;
    margin-bottom:16px;
}
.hero-title{
    font-size:50px;
    line-height:1.08;
    font-weight:900;
    margin:0;
    color:#ffffff !important;
}
.hero-sub{
    font-size:19px;
    line-height:1.85;
    font-weight:800;
    color:#ffffff !important;
}
.hero-mini{
    font-size:15px;
    line-height:1.8;
    font-weight:700;
    color:#dbeafe !important;
}
.yellow{
    color:#facc15 !important;
}
.red{
    color:#ff4d4f !important;
}
.green-band{
    background:#ecfdf3;
    border:3px solid #16a34a;
    border-radius:18px;
    padding:14px;
    text-align:center;
    font-size:19px;
    font-weight:900;
    color:#111 !important;
    margin-bottom:18px;
}
.section-card{
    background:#ffffff;
    border:1px solid #edf2f7;
    border-radius:22px;
    padding:22px 20px;
    box-shadow:0 10px 24px rgba(15,23,42,0.05);
    margin-top:18px;
}
.section-title{
    font-size:30px;
    font-weight:900;
    color:#111 !important;
    margin-bottom:10px;
}
.price-card{
    background: linear-gradient(180deg, #f0fff4 0%, #dcfce7 100%);
    border:5px solid #16a34a;
    border-radius:24px;
    padding:26px 18px;
    box-shadow:0 18px 34px rgba(22,163,74,0.18);
    text-align:center;
    margin-top:22px;
}
.price-title{
    font-size:36px;
    font-weight:900;
    color:#111 !important;
    margin-bottom:8px;
}
.price-main{
    font-size:56px;
    font-weight:900;
    color:#111 !important;
    line-height:1.1;
    margin:10px 0;
}
.price-text{
    font-size:18px;
    line-height:1.8;
    font-weight:800;
    color:#111 !important;
}
.small-note{
    text-align:center;
    color:#666 !important;
    font-size:14px;
    line-height:1.8;
    margin-top:18px;
}
div.stLinkButton > a{
    background: linear-gradient(180deg, #18b24c 0%, #16a34a 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 22px !important;
    padding: 18px 14px !important;
    text-align: center !important;
    display: block !important;
    text-decoration: none !important;
    box-shadow: 0 12px 22px rgba(22,163,74,0.22) !important;
}
div.stLinkButton > a:hover{
    background: linear-gradient(180deg, #16a34a 0%, #15803d 100%) !important;
    color: white !important;
}
@media (max-width: 700px){
    .hero-title{font-size:36px;}
    .hero-sub{font-size:17px;}
    .section-title{font-size:24px;}
    .price-main{font-size:42px;}
    div.stLinkButton > a{
        font-size:20px !important;
        padding:16px 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown('<div class="hero-box">', unsafe_allow_html=True)
st.markdown('<div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-title">
    <span class="yellow">黒字でも</span><br>
    <span class="red">倒産します</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.markdown(
    """
    <div class="hero-sub">
    あなたの会社、あと何ヶ月持つか分かりますか？<br><br>
    売上・原価・固定費・現金を入れるだけで、<br>
    資金ショート危険度 と 安全ライン不足額 を<br>
    最短30秒で診断します。
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.markdown(
    """
    <div class="hero-mini">
    会計ソフトでは見えない未来の資金を見える化。<br>
    スマホでもすぐ使えます。
    </div>
    """,
    unsafe_allow_html=True
)

st.info("「利益は出ているのに、お金が残らない」そんな建設会社のための、未来の資金診断ツールです。")
st.markdown('</div>', unsafe_allow_html=True)

# 緑帯
st.markdown(
    '<div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>',
    unsafe_allow_html=True
)

# CTA
st.link_button("30秒で無料診断する", APP_URL)

# 3つ分かること
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.success("⏳ あと何ヶ月持つか\n\n資金ショートまでの目安がすぐ分かります。")
with c2:
    st.info("🛡️ 安全ラインとの差額\n\n安全に経営するために、あといくら必要か見えます。")
with c3:
    st.warning("📈 今やるべき改善\n\n売上・原価・固定費のどこを直すべきか整理できます。")

st.markdown('</div>', unsafe_allow_html=True)

# 警告
st.error(
    "**売上があっても、現金が尽きたら終わりです。**\n\n"
    "利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。"
    "建設キャッシュレーダーは、その危険を先に見つけるためのツールです。"
)

# 悩み
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)
st.markdown("""
- 売上はあるのに、お金が残らない
- 原価率が高い現場に後から気づく
- このままで本当に大丈夫か不安
- 銀行や税理士に数字をうまく説明できない
""")
st.markdown('</div>', unsafe_allow_html=True)

# 使い方
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">使い方はかんたんです</div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)
steps = [
    ("STEP 1", "数字を入れる", "売上・原価・固定費・現金を入力"),
    ("STEP 2", "結果を見る", "危険度・不足額・改善ポイントを確認"),
    ("STEP 3", "LINEで相談", "もっと詳しく使いたい方はLINEへ"),
    ("STEP 4", "Pro版で管理", "毎月の資金推移と危険アラートを確認"),
]

for col, item in zip([s1, s2, s3, s4], steps):
    step, title, desc = item
    with col:
        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border:2px solid #dbeafe;
                border-radius:18px;
                padding:16px 12px;
                text-align:center;
                height:100%;
            ">
                <div style="
                    display:inline-block;
                    background:#1d4ed8;
                    color:#ffffff;
                    font-size:12px;
                    font-weight:900;
                    padding:5px 9px;
                    border-radius:999px;
                    margin-bottom:8px;
                ">{step}</div>
                <div style="font-size:18px;font-weight:900;color:#111827;margin-bottom:6px;">{title}</div>
                <div style="font-size:14px;line-height:1.7;color:#475569;font-weight:700;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# 価格
st.markdown('<div class="price-card">', unsafe_allow_html=True)
st.markdown('<div class="price-title">社長専用 Proダッシュボード</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="price-text">12ヶ月資金推移・現場利益管理・銀行提出サマリー・<br>利益改善シミュレーターまで使えます。</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="price-main">月 9,800円</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="price-text">まずは無料診断。必要ならLINEから申込み。</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# CTA
st.link_button("30秒で無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

st.markdown(
    '<div class="small-note">※ スマホでも見やすく設計しています。<br>※ インスタ・QR・チラシからそのまま開けます。</div>',
    unsafe_allow_html=True
)
