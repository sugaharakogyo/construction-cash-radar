import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="📊",
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
st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)


APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

st.markdown("""
<style>

/* 全体 */
.block-container{
    max-width:900px;
    padding-top:1rem;
    padding-bottom:3rem;
}

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background:#f6f7fb;
}

/* ヒーロー */
.hero{
    background:linear-gradient(135deg,#0f172a,#0369a1);
    border-radius:26px;
    padding:32px 24px;
    color:white;
    margin-bottom:28px;
    box-shadow:0 10px 30px rgba(0,0,0,0.18);
}

.hero-badge{
    background:#facc15;
    color:#111 !important;
    font-weight:800;
    display:inline-block;
    padding:7px 14px;
    border-radius:999px;
    margin-bottom:14px;
    font-size:14px;
}

.hero-title{
    font-size:42px;
    font-weight:900;
    line-height:1.2;
    margin-bottom:16px;
    color:white !important;
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
    opacity:0.97;
    margin-bottom:16px;
    color:white !important;
}

.hero-mini{
    font-size:16px;
    opacity:0.9;
    color:white !important;
}

/* カウンター */
.counter-box{
    background:#e9f7ee;
    border:3px solid #16a34a;
    border-radius:18px;
    padding:16px;
    margin-top:6px;
    margin-bottom:20px;
    text-align:center;
    font-size:18px;
    font-weight:800;
    color:#111 !important;
}

/* CTAサブ */
.cta-sub{
    text-align:center;
    font-size:17px;
    color:#374151 !important;
    line-height:1.8;
    margin-top:14px;
    margin-bottom:8px;
    font-weight:700;
}

/* ボタン */
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

/* セクション共通 */
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

/* 警告 */
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

/* 悩みリスト */
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

/* 特徴 */
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

/* 価格 */
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

/* 導線 */
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

/* フッター */
.small-note{
    color:#666 !important;
    font-size:14px;
    line-height:1.8;
    margin-top:20px;
    text-align:center;
}

/* スマホ */
@media(max-width:700px){

    .block-container{
        padding-top:0.6rem;
        padding-bottom:2rem;
    }

    .hero{
        padding:26px 18px;
    }

    .hero-title{
        font-size:32px;
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

# ヒーロー
st.markdown("""
<div class="hero">
    <div class="hero-badge">建設会社向け / 30秒無料診断</div>
    <div class="hero-title">
        建設会社は<br>
        <span class="yellow">黒字でも</span><br>
        <span class="red">潰れます</span>
    </div>
    <div class="hero-text">
        原因は <b>資金ショート</b>。<br>
        売上・原価・固定費・現金を入れるだけで、<br>
        <b>いつ危ないか</b> と <b>安全にするには月いくら必要か</b> がすぐ分かる。
    </div>
    <div class="hero-mini">
        まずは無料で診断。<br>
        スマホでもすぐ使えます。
    </div>
</div>
""", unsafe_allow_html=True)

# カウンター
st.markdown("""
<div class="counter-box">
現在 多くの建設会社が診断しています
</div>
""", unsafe_allow_html=True)

# CTA
st.link_button("無料で診断する", APP_URL)

st.markdown("""
<div class="cta-sub">
    あなたの会社のキャッシュ状況を、今すぐ見える化してください。
</div>
""", unsafe_allow_html=True)

# 警告
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

# 悩み
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

# 特徴
st.markdown("""
<div class="section-card">
    <div class="section-title">建設キャッシュレーダーで分かること</div>
    <div class="feature-grid">
        <div class="feature-box">
            <div class="feature-num">STEP 1</div>
            <div class="feature-title">資金ショート時期</div>
            <div class="feature-text">このままだと、あと何ヶ月で危ないかが分かります。</div>
        </div>
        <div class="feature-box">
            <div class="feature-num">STEP 2</div>
            <div class="feature-title">安全ライン不足額</div>
            <div class="feature-text">安全にするために、月いくら改善が必要か見えます。</div>
        </div>
        <div class="feature-box">
            <div class="feature-num">STEP 3</div>
            <div class="feature-title">今日やる打ち手</div>
            <div class="feature-text">売上・入金・固定費・原価のどこを優先すべきか整理できます。</div>
        </div>
        <div class="feature-box">
            <div class="feature-num">PRO</div>
            <div class="feature-title">さらに深く改善</div>
            <div class="feature-text">12ヶ月資金推移、銀行提出サマリー、利益改善シミュレーターまで使えます。</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 導線
st.markdown("""
<div class="section-card">
    <div class="section-title">使い方はかんたんです</div>
    <div class="flow">
        <div class="flow-box">
            <div class="flow-step">STEP 1</div>
            <div class="flow-title">無料診断</div>
            <div class="flow-text">売上・原価・固定費・現金を入力</div>
        </div>
        <div class="flow-box">
            <div class="flow-step">STEP 2</div>
            <div class="flow-title">結果確認</div>
            <div class="flow-text">危険時期と不足額をチェック</div>
        </div>
        <div class="flow-box">
            <div class="flow-step">STEP 3</div>
            <div class="flow-title">LINE申込み</div>
            <div class="flow-text">もっと詳しく使いたい方はLINEへ</div>
        </div>
        <div class="flow-box">
            <div class="flow-step">STEP 4</div>
            <div class="flow-title">Pro利用</div>
            <div class="flow-text">資金推移・利益管理まで使える</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 価格
st.markdown("""
<div class="price-box">
    <h3>続きは Pro版へ</h3>
    <div class="price-text">
        Pro版では<br>
        <b>12ヶ月資金推移</b>・<b>現場利益管理</b>・<b>銀行提出サマリー</b><br>
        ・<b>利益改善シミュレーター</b> まで使えます。
    </div>
    <div class="price-main">月 9,800円</div>
    <div class="price-text">
        まずは無料診断 → 気に入ったらLINEから申込み
    </div>
</div>
""", unsafe_allow_html=True)

st.link_button("無料で診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

# フッター
st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ インスタ・QR・チラシからそのまま開けます。
</div>
""", unsafe_allow_html=True)
