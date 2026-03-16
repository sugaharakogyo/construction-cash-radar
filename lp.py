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
    max-width: 920px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}
.stApp{
    background: linear-gradient(180deg, #f8fbff 0%, #f6f7fb 100%);
}
.main-title{
    font-size: 48px;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 12px;
}
.subtext{
font-size:19px;
font-weight:700;
line-height:1.8;
color:white;
}
.mini{
    font-size: 15px;
    color: #dbeafe;
    font-weight: 600;
    line-height: 1.7;
}
.hero-wrap{
background: linear-gradient(135deg,#020617 0%,#0b3b74 40%,#0284c7 100%);
border-radius: 30px;
padding: 32px 24px;
box-shadow: 0 24px 50px rgba(0,0,0,0.35);
margin-bottom: 26px;
}
.badge{
    display:inline-block;
    background:#facc15;
    color:#111;
    font-weight:900;
    padding:8px 14px;
    border-radius:999px;
    font-size:14px;
    margin-bottom:14px;
}
.green-band{
    background:#eefcf3;
    border:3px solid #16a34a;
    border-radius:18px;
    padding:16px;
    text-align:center;
    font-size:20px;
    font-weight:900;
    color:#111;
    margin-bottom:20px;
}
.soft-card{
    background:white;
    border-radius:22px;
    padding:22px 18px;
    box-shadow:0 8px 20px rgba(15,23,42,0.05);
    border:1px solid #eef2f7;
    margin-top:18px;
}
.card-title{
    font-size:30px;
    font-weight:900;
    margin-bottom:12px;
    color:#111;
}
.price-box{
background:linear-gradient(180deg,#f0fff4,#dcfce7);
border:5px solid #16a34a;
border-radius:28px;
padding:28px 20px;
text-align:center;
margin-top:26px;
box-shadow:0 18px 36px rgba(22,163,74,0.25);
}

.price-big{
    font-size:54px;
    font-weight:900;
    color:#111;
}
.step-pill{
    display:inline-block;
    background:#1d4ed8;
    color:white;
    font-size:12px;
    font-weight:900;
    padding:5px 9px;
    border-radius:999px;
    margin-bottom:8px;
}
.visual-card{
    background:white;
    border-radius:22px;
    padding:16px;
    box-shadow:0 12px 24px rgba(0,0,0,0.16);
}
.visual-label{
    font-size:12px;
    font-weight:800;
    color:#64748b;
}
.visual-value{
    font-size:21px;
    font-weight:900;
    color:#111827;
}
.footer-note{
    text-align:center;
    color:#666;
    font-size:14px;
    margin-top:18px;
    line-height:1.8;
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
@media (max-width: 700px){
    .main-title{font-size:36px;}
    .subtext{font-size:17px;}
    .card-title{font-size:24px;}
    .price-big{font-size:42px;}
    div.stLinkButton > a{
        font-size:20px !important;
        padding:16px 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
st.markdown('<div class="badge">建設会社専用 / 最短30秒 無料診断</div>', unsafe_allow_html=True)

left, right = st.columns([1.15, 0.95], gap="large")

with left:
    st.markdown(
        '<div class="main-title" style="color:white;">'
        '建設会社は<br>'
        '<span style="color:#facc15;">黒字でも</span><br>'
        '<span style="color:#ff4d4f;">倒産します</span>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subtext" style="color:white;">'
        '<b>あなたの会社、あと何ヶ月持つか分かりますか？</b><br><br>'
        '売上・原価・固定費・現金を入れるだけで、<br>'
        '<b>資金ショート危険度</b> と <b>安全ライン不足額</b> を<br>'
        '最短30秒で診断します。'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="mini">'
        '会計ソフトでは見えない未来の資金を見える化。<br>'
        'スマホでもすぐ使えます。'
        '</div>',
        unsafe_allow_html=True
    )

    st.info("「利益は出ているのに、お金が残らない」そんな建設会社のための、未来の資金診断ツールです。")

with right:
    st.markdown('<div class="visual-card">', unsafe_allow_html=True)
    top1, top2 = st.columns([1, 0.7])
    with top1:
        st.markdown("**建設キャッシュレーダー**")
    with top2:
        st.markdown(
            '<div style="background:#fee2e2;color:#b91c1c;font-size:12px;font-weight:900;padding:6px 10px;border-radius:999px;text-align:center;">危険度 高</div>',
            unsafe_allow_html=True
        )

    chart = st.columns(6)
    heights = [0.92, 0.74, 0.58, 0.40, 0.22, 0.14]
    colors = ["#2563eb", "#2563eb", "#2563eb", "#2563eb", "#dc2626", "#dc2626"]
    for col, h, c in zip(chart, heights, colors):
        with col:
            st.markdown(
                f"""
                <div style="
                    height:120px;
                    display:flex;
                    align-items:flex-end;
                    justify-content:center;
                    border-bottom:2px solid #e5e7eb;
                    padding-bottom:8px;">
                    <div style="
                        width:18px;
                        height:{int(h*100)}px;
                        background:{c};
                        border-radius:8px 8px 0 0;">
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="visual-label">資金ショートまで</div>', unsafe_allow_html=True)
        st.markdown('<div class="visual-value">あと5ヶ月</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="visual-label">安全ライン不足</div>', unsafe_allow_html=True)
        st.markdown('<div class="visual-value">780万円</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>', unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)

# 30秒で分かること
st.markdown('<div class="soft-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
with p1:
    st.success("⏳ あと何ヶ月持つか\n\n資金ショートまでの目安がすぐ分かります。")
with p2:
    st.info("🛡️ 安全ラインとの差額\n\n安全に経営するために、あといくら必要か見えます。")
with p3:
    st.warning("📈 今やるべき改善\n\n売上・原価・固定費のどこを直すべきか整理できます。")
st.markdown('</div>', unsafe_allow_html=True)

# 警告
st.error("**売上があっても、現金が尽きたら終わりです。**\n\n利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。建設キャッシュレーダーは、その危険を先に見つけるためのツールです。")

# 悩み
st.markdown('<div class="soft-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)
st.markdown("""
- 売上はあるのに、お金が残らない
- 原価率が高い現場に後から気づく
- このままで本当に大丈夫か不安
- 銀行や税理士に数字をうまく説明できない
""")
st.markdown('</div>', unsafe_allow_html=True)

# 使い方
st.markdown('<div class="soft-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">使い方はかんたんです</div>', unsafe_allow_html=True)

f1, f2, f3, f4 = st.columns(4)
steps = [
    ("STEP 1", "数字を入れる", "売上・原価・固定費・現金を入力"),
    ("STEP 2", "結果を見る", "危険度・不足額・改善ポイントを確認"),
    ("STEP 3", "LINEで相談", "もっと詳しく使いたい方はLINEへ"),
    ("STEP 4", "Pro版で管理", "毎月の資金推移と危険アラートを確認")
]
for col, (s, t, d) in zip([f1, f2, f3, f4], steps):
    with col:
        st.markdown('<div style="background:#fff;border:2px solid #dbeafe;border-radius:18px;padding:16px 12px;text-align:center;height:100%;">', unsafe_allow_html=True)
        st.markdown(f'<div class="step-pill">{s}</div>', unsafe_allow_html=True)
        st.markdown(f"**{t}**")
        st.caption(d)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 価格
st.markdown('<div class="price-box">', unsafe_allow_html=True)
st.markdown('<div class="price-title">社長専用 Proダッシュボード</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text" style="text-align:center;font-weight:800;">'
    '12ヶ月資金推移・現場利益管理・銀行提出サマリー・<br>'
    '利益改善シミュレーターまで使えます。'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="price-big">月 9,800円</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-text" style="text-align:center;font-weight:800;">'
    'まずは無料診断。必要ならLINEから申込み。'
    '</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

st.markdown(
    '<div class="footer-note">'
    '※ スマホでも見やすく設計しています。<br>'
    '※ インスタ・QR・チラシからそのまま開けます。'
    '</div>',
    unsafe_allow_html=True
)
