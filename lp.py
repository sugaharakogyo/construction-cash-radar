import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

st.markdown("""
<style>
.block-container{
    max-width: 920px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

html, body, [class*="css"]{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background:#f6f7fb;
}

/* hero */
.hero{
    background: linear-gradient(135deg, #0f172a 0%, #0b3d6e 45%, #0369a1 100%);
    border-radius: 28px;
    padding: 34px 24px 28px 24px;
    color: white;
    margin-bottom: 26px;
    box-shadow: 0 14px 32px rgba(0,0,0,0.18);
}

.hero-badge{
    display:inline-block;
    background:#facc15;
    color:#111111 !important;
    font-size:14px;
    font-weight:900;
    padding:8px 14px;
    border-radius:999px;
    margin-bottom:16px;
}

.hero-title{
    font-size:44px;
    line-height:1.15;
    font-weight:900;
    color:#ffffff !important;
    margin-bottom:18px;
}

.hero-title .yellow{
    color:#facc15 !important;
}

.hero-title .red{
    color:#ef4444 !important;
}

.hero-text{
    font-size:18px;
    line-height:1.9;
    color:#ffffff !important;
    margin-bottom:14px;
    font-weight:700;
}

.hero-mini{
    font-size:15px;
    line-height:1.8;
    color:#dbeafe !important;
    font-weight:600;
    margin-bottom:18px;
}

/* visual card */
.visual{
    background:#ffffff;
    border-radius:22px;
    padding:18px;
    margin-top:16px;
    box-shadow:0 8px 22px rgba(0,0,0,0.14);
    border:1px solid rgba(255,255,255,0.4);
}

.visual-head{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:12px;
}

.visual-logo{
    font-size:15px;
    font-weight:900;
    color:#0f172a !important;
}

.visual-status{
    background:#fee2e2;
    color:#b91c1c !important;
    font-size:12px;
    font-weight:900;
    padding:6px 10px;
    border-radius:999px;
}

.chart{
    display:flex;
    align-items:flex-end;
    gap:8px;
    height:120px;
    margin:16px 0 14px 0;
    padding:6px 4px 0 4px;
    border-bottom:2px solid #e5e7eb;
}

.bar{
    width:18px;
    background:linear-gradient(180deg,#38bdf8,#2563eb);
    border-radius:8px 8px 0 0;
}

.bar.red{
    background:linear-gradient(180deg,#fb7185,#dc2626);
}

.card-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
}

.card{
    background:#f8fafc;
    border:1px solid #e2e8f0;
    border-radius:14px;
    padding:12px;
}

.card-label{
    font-size:12px;
    color:#475569 !important;
    font-weight:800;
    margin-bottom:4px;
}

.card-value{
    font-size:20px;
    color:#111827 !important;
    font-weight:900;
}

/* counter */
.counter-box{
    background:#e9f7ee;
    border:3px solid #16a34a;
    border-radius:18px;
    padding:16px;
    margin-bottom:20px;
    text-align:center;
    font-size:18px;
    font-weight:900;
    color:#111111 !important;
}

/* buttons */
div.stLinkButton > a{
    background:#16a34a !important;
    color:white !important;
    border:none !important;
    border-radius:16px !important;
    font-weight:900 !important;
    font-size:22px !important;
    padding:18px 14px !important;
    text-align:center !important;
    display:block !important;
    text-decoration:none !important;
    box-shadow:0 10px 22px rgba(22,163,74,0.22) !important;
}

div.stLinkButton > a:hover{
    background:#15803d !important;
    color:white !important;
}

/* section */
.section{
    background:#ffffff;
    border-radius:22px;
    padding:24px 20px;
    margin-top:20px;
    box-shadow:0 6px 18px rgba(0,0,0,0.05);
    border:1px solid #ececec;
}

.section h2{
    font-size:28px;
    font-weight:900;
    color:#111111 !important;
    margin-bottom:14px;
    line-height:1.4;
}

.section ul{
    font-size:18px;
    line-height:2.0;
    color:#1f2937 !important;
    margin:0;
    padding-left:22px;
}

/* flow */
.flow{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:12px;
    margin-top:12px;
}

.flowbox{
    background:#ffffff;
    border:2px solid #dbeafe;
    border-radius:16px;
    padding:14px 10px;
    text-align:center;
}

.step{
    display:inline-block;
    background:#1d4ed8;
    color:#ffffff !important;
    font-size:12px;
    font-weight:900;
    padding:4px 8px;
    border-radius:999px;
    margin-bottom:8px;
}

.flow-title{
    font-size:18px;
    font-weight:900;
    color:#111827 !important;
    margin-bottom:6px;
}

.flow-text{
    font-size:14px;
    line-height:1.6;
    color:#475569 !important;
}

/* price */
.price{
    background:#e9f7ee;
    border:4px solid #16a34a;
    border-radius:24px;
    padding:24px;
    text-align:center;
    margin-top:24px;
    box-shadow:0 14px 30px rgba(34,197,94,0.14);
}

.price h3{
    font-size:38px;
    font-weight:900;
    color:#111111 !important;
    margin-bottom:10px;
}

.price-text{
    font-size:18px;
    line-height:1.9;
    color:#111111 !important;
    font-weight:700;
}

.price-main{
    font-size:52px;
    font-weight:900;
    color:#111111 !important;
    margin-top:10px;
    margin-bottom:10px;
}

/* footer */
.footer{
    font-size:14px;
    text-align:center;
    margin-top:20px;
    color:#666666 !important;
    line-height:1.8;
}

@media(max-width:700px){
    .hero-title{
        font-size:34px;
    }

    .hero-text{
        font-size:16px;
    }

    .section h2{
        font-size:24px;
    }

    .section ul{
        font-size:16px;
    }

    .flow{
        grid-template-columns:1fr;
    }

    .card-grid{
        grid-template-columns:1fr;
    }

    .price-main{
        font-size:40px;
    }

    div.stLinkButton > a{
        font-size:20px !important;
        padding:16px 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

    <div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>

    <div class="hero-title">
        建設会社は<br>
        <span class="yellow">黒字でも</span><br>
        <span class="red">倒産します</span>
    </div>

    <div class="hero-text">
        <b>あなたの会社、あと何ヶ月持つか分かりますか？</b><br><br>
        売上・原価・固定費・現金を入れるだけで、<br>
        <b>資金ショート危険度</b> と <b>安全ライン不足額</b> を<br>
        最短30秒で診断します。
    </div>

    <div class="hero-mini">
        会計ソフトでは見えない未来の資金を見える化。<br>
        スマホでもすぐ使えます。
    </div>

    <div class="visual">
        <div class="visual-head">
            <div class="visual-logo">建設キャッシュレーダー</div>
            <div class="visual-status">危険度 高</div>
        </div>

        <div class="chart">
            <div class="bar" style="height:90px;"></div>
            <div class="bar" style="height:72px;"></div>
            <div class="bar" style="height:56px;"></div>
            <div class="bar" style="height:38px;"></div>
            <div class="bar red" style="height:22px;"></div>
            <div class="bar red" style="height:14px;"></div>
        </div>

        <div class="card-grid">
            <div class="card">
                <div class="card-label">資金ショートまで</div>
                <div class="card-value">あと5ヶ月</div>
            </div>

            <div class="card">
                <div class="card-label">安全ライン不足</div>
                <div class="card-value">780万円</div>
            </div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="counter-box">
建設会社専用 / 資金ショート危険度を無料診断
</div>
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)

st.markdown("""
<div class="section">
    <h2>30秒でこの3つが分かります</h2>
    <ul>
        <li>あと何ヶ月で資金ショートする可能性があるか</li>
        <li>安全ラインまでいくら不足しているか</li>
        <li>今やるべき改善ポイント</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>こんなお悩みありませんか？</h2>
    <ul>
        <li>売上はあるのにお金が残らない</li>
        <li>原価率が高い現場に後から気づく</li>
        <li>このままで本当に大丈夫か不安</li>
        <li>銀行や税理士に数字をうまく説明できない</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>使い方はかんたんです</h2>

    <div class="flow">
        <div class="flowbox">
            <div class="step">STEP 1</div>
            <div class="flow-title">数字を入れる</div>
            <div class="flow-text">売上・原価・固定費・現金を入力</div>
        </div>

        <div class="flowbox">
            <div class="step">STEP 2</div>
            <div class="flow-title">結果を見る</div>
            <div class="flow-text">危険度・不足額・改善ポイントを確認</div>
        </div>

        <div class="flowbox">
            <div class="step">STEP 3</div>
            <div class="flow-title">LINEで相談</div>
            <div class="flow-text">もっと詳しく使いたい方はLINEへ</div>
        </div>

        <div class="flowbox">
            <div class="step">STEP 4</div>
            <div class="flow-title">Pro版で管理</div>
            <div class="flow-text">毎月の資金推移と危険アラートを確認</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="price">
    <h3>社長専用 Proダッシュボード</h3>

    <div class="price-text">
        12ヶ月資金推移・現場利益管理・銀行提出サマリー・<br>
        利益改善シミュレーターまで使えます。
    </div>

    <div class="price-main">月 9,800円</div>

    <div class="price-text">
        まずは無料診断。必要ならLINEから申込み。
    </div>
</div>
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

st.markdown("""
<div class="footer">
スマホでも利用できます。<br>
QRコード・SNSからそのまま診断可能
</div>
""", unsafe_allow_html=True)
