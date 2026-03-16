import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

# Google Analytics
st.components.v1.html("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-V96H2R41TL"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-V96H2R41TL');
</script>
""", height=0)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

st.markdown("""
<style>
.block-container{
    max-width:950px;
    padding-top:1rem;
    padding-bottom:3rem;
}

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background:#f6f7fb;
}

/* HERO */
.hero{
    background:linear-gradient(135deg,#0f172a 0%,#0b3b66 45%,#0369a1 100%);
    border-radius:28px;
    padding:34px 24px 28px 24px;
    color:white;
    margin-bottom:24px;
    box-shadow:0 16px 34px rgba(0,0,0,0.18);
    position:relative;
    overflow:hidden;
}

.hero:before{
    content:"";
    position:absolute;
    top:-40px;
    right:-40px;
    width:180px;
    height:180px;
    background:rgba(250,204,21,0.12);
    border-radius:50%;
}

.hero:after{
    content:"";
    position:absolute;
    bottom:-55px;
    left:-55px;
    width:220px;
    height:220px;
    background:rgba(239,68,68,0.10);
    border-radius:50%;
}

.hero-badge{
    position:relative;
    z-index:1;
    background:#facc15;
    color:#111 !important;
    font-weight:900;
    display:inline-block;
    padding:8px 14px;
    border-radius:999px;
    margin-bottom:16px;
    font-size:14px;
    box-shadow:0 6px 16px rgba(250,204,21,0.25);
}

.hero-grid{
    position:relative;
    z-index:1;
    display:grid;
    grid-template-columns:1.35fr 0.9fr;
    gap:18px;
    align-items:center;
}

.hero-title{
    font-size:44px;
    font-weight:900;
    line-height:1.18;
    margin-bottom:16px;
    color:white !important;
    letter-spacing:0.3px;
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
    opacity:0.98;
    margin-bottom:14px;
    color:white !important;
}

.hero-mini{
    font-size:15px;
    opacity:0.92;
    color:white !important;
    line-height:1.8;
}

.hero-visual{
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:24px;
    padding:16px;
    backdrop-filter:blur(3px);
}

.visual-screen{
    background:#ffffff;
    border-radius:18px;
    padding:14px;
    box-shadow:0 10px 24px rgba(0,0,0,0.15);
}

.visual-top{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:12px;
}

.visual-logo{
    font-size:14px;
    font-weight:900;
    color:#0f172a !important;
}

.visual-status{
    font-size:12px;
    font-weight:800;
    color:#16a34a !important;
    background:#dcfce7;
    border-radius:999px;
    padding:5px 10px;
}

.visual-chart{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:6px;
    align-items:end;
    height:120px;
    margin:14px 0 10px 0;
}

.bar{
    border-radius:10px 10px 4px 4px;
    background:linear-gradient(180deg,#38bdf8,#1d4ed8);
}

.bar.red{
    background:linear-gradient(180deg,#fb7185,#dc2626);
}

.visual-cards{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

.v-card{
    background:#f8fafc;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:10px;
}

.v-label{
    font-size:11px;
    font-weight:800;
    color:#64748b !important;
    margin-bottom:4px;
}

.v-value{
    font-size:17px;
    font-weight:900;
    color:#111827 !important;
}

/* Counter / Sub CTA */
.counter-box{
    background:#e9f7ee;
    border:3px solid #16a34a;
    border-radius:18px;
    padding:16px;
    margin-top:2px;
    margin-bottom:18px;
    text-align:center;
    font-size:18px;
    font-weight:900;
    color:#111 !important;
}

.cta-sub{
    text-align:center;
    font-size:17px;
    color:#374151 !important;
    line-height:1.8;
    margin-top:14px;
    margin-bottom:8px;
    font-weight:700;
}

/* Buttons */
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
    box-shadow:0 10px 20px rgba(22,163,74,0.20) !important;
}

div.stLinkButton > a:hover{
    background:#15803d !important;
    color:white !important;
}

/* Common cards */
.section-card{
    background:#ffffff;
    border-radius:22px;
    padding:24px 20px;
    margin-top:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.05);
    border:1px solid #ececec;
}

.section-title{
    font-size:30px;
    font-weight:900;
    color:#111 !important;
    margin-bottom:14px;
    line-height:1.4;
}

.section-text{
    font-size:18px;
    line-height:1.9;
    color:#222 !important;
}

/* 3 points */
.point-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:14px;
    margin-top:6px;
}

.point-box{
    background:linear-gradient(180deg,#f8fafc,#eef6ff);
    border:2px solid #dbeafe;
    border-radius:18px;
    padding:18px 14px;
    text-align:center;
}

.point-icon{
    font-size:30px;
    margin-bottom:10px;
}

.point-title{
    font-size:19px;
    font-weight:900;
    color:#111827 !important;
    margin-bottom:8px;
}

.point-text{
    font-size:15px;
    line-height:1.7;
    color:#475569 !important;
}

/* Warning */
.warning-box{
    background:#fff1f2;
    border:3px solid #ef4444;
    border-radius:20px;
    padding:22px;
    margin-top:30px;
}

.warning-title{
    font-size:24px;
    font-weight:900;
    color:#b91c1c !important;
    margin-bottom:10px;
}

.warning-text{
    font-size:18px;
    line-height:1.9;
    color:#4c0519 !important;
}

/* Problems */
.problem-list{
    margin:0;
    padding-left:22px;
    font-size:18px;
    line-height:2.0;
    color:#1f2937 !important;
}

.problem-list li{
    margin-bottom:8px;
}

/* Features */
.feature-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px;
    margin-top:8px;
}

.feature-box{
    background:#f8fafc;
    border:2px solid #e5e7eb;
    border-radius:18px;
    padding:16px;
}

.feature-num{
    display:inline-block;
    background:#111827;
    color:white !important;
    font-size:12px;
    font-weight:900;
    border-radius:999px;
    padding:4px 9px;
    margin-bottom:10px;
}

.feature-title{
    font-size:20px;
    font-weight:900;
    color:#111827 !important;
    margin-bottom:6px;
}

.feature-text{
    font-size:16px;
    line-height:1.8;
    color:#334155 !important;
}

/* Flow */
.flow{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:12px;
    margin-top:10px;
}

.flow-box{
    background:#ffffff;
    border:2px solid #dbeafe;
    border-radius:18px;
    padding:14px 12px;
    text-align:center;
}

.flow-step{
    display:inline-block;
    background:#1d4ed8;
    color:white !important;
    font-size:12px;
    font-weight:900;
    border-radius:999px;
    padding:4px 9px;
    margin-bottom:10px;
}

.flow-title{
    font-size:18px;
    font-weight:900;
    color:#111827 !important;
    margin-bottom:6px;
}

.flow-text{
    font-size:14px;
    color:#475569 !important;
    line-height:1.6;
}

/* Price */
.price-box{
    background:#e9f7ee;
    border:4px solid #16a34a;
    border-radius:26px;
    padding:26px 20px;
    margin-top:26px;
    text-align:center;
    box-shadow:0 14px 30px rgba(34,197,94,0.14);
    color:#111 !important;
}

.price-box *{
    color:#111 !important;
}

.price-box h3{
    font-size:40px;
    font-weight:900;
    margin:0 0 10px 0;
}

.price-main{
    font-size:52px;
    font-weight:900;
    margin:10px 0;
    line-height:1.2;
}

.price-text{
    font-size:18px;
    line-height:1.9;
}

/* Footer */
.small-note{
    color:#666 !important;
    font-size:14px;
    line-height:1.8;
    margin-top:20px;
    text-align:center;
}

/* Mobile */
@media(max-width:700px){

    .block-container{
        padding-top:0.6rem;
        padding-bottom:2rem;
    }

    .hero{
        padding:26px 18px;
    }

    .hero-grid{
        grid-template-columns:1fr;
    }

    .hero-title{
        font-size:34px;
    }

    .hero-text{
        font-size:16px;
    }

    .hero-mini{
        font-size:15px;
    }

    .section-title{
        font-size:25px;
    }

    .section-text,
    .problem-list{
        font-size:16px;
    }

    .point-grid{
        grid-template-columns:1fr;
    }

    .feature-grid{
        grid-template-columns:1fr;
    }

    .price-main{
        font-size:40px;
    }

    .flow{
        grid-template-columns:1fr;
    }

    div.stLinkButton > a{
        font-size:20px !important;
        padding:16px 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>
    <div class="hero-grid">
        <div>
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
                会計ソフトでは見えない、未来の資金を見える化。<br>
                スマホでもすぐ使えます。
            </div>
        </div>

        <div class="hero-visual">
            <div class="visual-screen">
                <div class="visual-top">
                    <div class="visual-logo">建設キャッシュレーダー™</div>
                    <div class="visual-status">危険度 高</div>
                </div>

                <div class="visual-chart">
                    <div class="bar" style="height:86px;"></div>
                    <div class="bar" style="height:72px;"></div>
                    <div class="bar" style="height:58px;"></div>
                    <div class="bar" style="height:42px;"></div>
                    <div class="bar red" style="height:24px;"></div>
                    <div class="bar red" style="height:14px;"></div>
                </div>

                <div class="visual-cards">
                    <div class="v-card">
                        <div class="v-label">資金ショートまで</div>
                        <div class="v-value">あと5ヶ月</div>
                    </div>
                    <div class="v-card">
                        <div class="v-label">安全ライン不足</div>
                        <div class="v-value">780万円</div>
                    </div>
                </div>
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
<div class="cta-sub">
    未来の資金を見える化して、危険を先に把握してください。
</div>
""", unsafe_allow_html=True)

# 3 points
st.markdown("""
<div class="section-card">
    <div class="section-title">30秒でこの3つが分かります</div>
    <div class="point-grid">
        <div class="point-box">
            <div class="point-icon">⏳</div>
            <div class="point-title">あと何ヶ月持つか</div>
            <div class="point-text">資金ショートまでの目安がすぐ分かります。</div>
        </div>
        <div class="point-box">
            <div class="point-icon">🛡️</div>
            <div class="point-title">安全ラインとの差額</div>
            <div class="point-text">安全に経営するために、あといくら必要か見えます。</div>
        </div>
        <div class="point-box">
            <div class="point-icon">📈</div>
            <div class="point-title">今やるべき改善</div>
            <div class="point-text">売上・原価・固定費のどこを直すべきか整理できます。</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Warning
st.markdown("""
<div class="warning-box">
    <div class="warning-title">売上があっても、現金が尽きたら終わりです。</div>
    <div class="warning-text">
        利益が出ていても、入金サイト・原価率・固定費のズレで<br>
        <b>突然お金が回らなくなる</b>ことがあります。<br>
        建設キャッシュレーダーは、その危険を先に見つけるためのツールです。
    </div>
</div>
""", unsafe_allow_html=True)

# Problems
st.markdown("""
<div class="section-card">
    <div class="section-title">こんなお悩みありませんか？</div>
    <ul class="problem-list">
        <li>売上はあるのに、お金が残らない</li>
        <li>原価率が高い現場に後から気づく</li>
        <li>このままで本当に大丈夫か不安</li>
        <li>銀行や税理士に数字をうまく説明できない</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Features
st.markdown("""
<div class="section-card">
    <div class="section-title">建設キャッシュレーダーで分かること</div>
    <div class="feature-grid">
        <div class="feature-box">
            <div class="feature-num">STEP 1</div>
            <div class="feature-title">あと何ヶ月持つか分かる</div>
            <div class="feature-text">このままだと、いつ危ないかが見えます。</div>
        </div>
        <div class="feature-box">
            <div class="feature-num">STEP 2</div>
            <div class="feature-title">安全ラインとの差額が分かる</div>
            <div class="feature-text">安全にするために、あといくら必要か見えます。</div>
        </div>
        <div class="feature-box">
            <div class="feature-num">STEP 3</div>
            <div class="feature-title">今やるべき改善が分かる</div>
            <div class="feature-text">売上・固定費・原価のどこを直すべきか整理できます。</div>
        </div>
        <div class="feature-box">
            <div class="feature-num">PRO</div>
            <div class="feature-title">毎月使える経営ダッシュボード</div>
            <div class="feature-text">12ヶ月資金推移、現場利益、銀行提出サマリーまで使えます。</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Flow
st.markdown("""
<div class="section-card">
    <div class="section-title">使い方はかんたんです</div>
    <div class="flow">
        <div class="flow-box">
            <div class="flow-step">STEP 1</div>
            <div class="flow-title">数字を入れる</div>
            <div class="flow-text">売上・原価・固定費・現金を入力</div>
        </div>
        <div class="flow-box">
            <div class="flow-step">STEP 2</div>
            <div class="flow-title">結果を見る</div>
            <div class="flow-text">危険度・不足額・改善ポイントを確認</div>
        </div>
        <div class="flow-box">
            <div class="flow-step">STEP 3</div>
            <div class="flow-title">LINEで相談</div>
            <div class="flow-text">もっと詳しく使いたい方はLINEへ</div>
        </div>
        <div class="flow-box">
            <div class="flow-step">STEP 4</div>
            <div class="flow-title">Pro版で管理</div>
            <div class="flow-text">毎月の資金推移と危険アラートを確認</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Price
st.markdown("""
<div class="price-box">
    <h3>社長専用 Proダッシュボード</h3>
    <div class="price-text">
        Pro版では<br>
        <b>12ヶ月資金推移</b>・<b>現場利益管理</b>・<b>銀行提出サマリー</b><br>
        ・<b>利益改善シミュレーター</b> まで使えます。
    </div>
    <div class="price-main">月 9,800円</div>
    <div class="price-text">
        まずは無料診断。必要ならLINEから申込み。
    </div>
</div>
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

# Footer
st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ インスタ・QR・チラシからそのまま開けます。
</div>
""", unsafe_allow_html=True)
