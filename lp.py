import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

st.markdown("""
<style>
.block-container{
    max-width: 980px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(255,215,0,0.15), transparent 25%),
        radial-gradient(circle at top right, rgba(0,191,255,0.18), transparent 25%),
        linear-gradient(180deg, #0b1020 0%, #10182f 35%, #f6f7fb 35%, #f6f7fb 100%);
}

/* ヒーロー */
.hero{
    background:
        linear-gradient(135deg, rgba(255,196,0,0.18) 0%, rgba(255,196,0,0.02) 20%),
        linear-gradient(135deg, #081223 0%, #0f1d3a 45%, #0ea5e9 100%);
    border: 2px solid rgba(255,255,255,0.08);
    border-radius: 28px;
    padding: 34px 24px 30px 24px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.30);
    margin-bottom: 18px;
    position: relative;
    overflow: hidden;
}

.hero:before{
    content:"";
    position:absolute;
    top:-80px;
    right:-80px;
    width:220px;
    height:220px;
    background: radial-gradient(circle, rgba(255,215,0,0.35), transparent 70%);
    border-radius:50%;
}

.hero-badge{
    display:inline-block;
    background: linear-gradient(90deg, #facc15, #fde047);
    color:#111 !important;
    font-size:14px;
    font-weight:900;
    border-radius:999px;
    padding:8px 14px;
    margin-bottom:14px;
    box-shadow:0 6px 16px rgba(250,204,21,0.35);
}

.hero-title{
    font-size:54px;
    line-height:1.12;
    font-weight:900;
    color:white !important;
    margin:0 0 14px 0;
    letter-spacing: -1px;
}

.hero-title .red{
    color:#ff5b5b !important;
    text-shadow:0 0 20px rgba(255,91,91,0.25);
}

.hero-title .yellow{
    color:#ffd84d !important;
    text-shadow:0 0 20px rgba(255,216,77,0.25);
}

.hero-text{
    font-size:19px;
    line-height:1.9;
    color:#f5f7ff !important;
    margin:0;
}

.hero-mini{
    margin-top:16px;
    font-size:15px;
    color:#dbeafe !important;
    line-height:1.8;
}

/* CTA */
.cta-wrap{
    margin-top:18px;
    margin-bottom:8px;
}

div.stLinkButton > a{
    display:block !important;
    text-align:center !important;
    background: linear-gradient(90deg, #ff4b4b 0%, #ff2d55 100%) !important;
    color:#ffffff !important;
    border:0 !important;
    border-radius:18px !important;
    padding:18px 18px !important;
    font-size:24px !important;
    font-weight:900 !important;
    text-decoration:none !important;
    box-shadow:0 12px 26px rgba(255,59,92,0.35) !important;
    letter-spacing:0.5px !important;
}

div.stLinkButton > a:hover{
    background: linear-gradient(90deg, #ef4444 0%, #e11d48 100%) !important;
    color:#ffffff !important;
}

.cta-sub{
    text-align:center;
    font-size:17px;
    color:#374151 !important;
    line-height:1.8;
    margin-top:12px;
    margin-bottom:10px;
    font-weight:700;
}

/* カード */
.section-card{
    background:#ffffff;
    border-radius:24px;
    padding:24px 20px;
    margin-top:18px;
    border:1px solid #e5e7eb;
    box-shadow:0 8px 22px rgba(15,23,42,0.06);
}

.section-title{
    font-size:32px;
    line-height:1.35;
    font-weight:900;
    color:#111827 !important;
    margin-bottom:14px;
}

.section-text{
    font-size:18px;
    line-height:1.9;
    color:#1f2937 !important;
}

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

.em{
    color:#dc2626 !important;
    font-weight:900;
}

.highlight{
    color:#1d4ed8 !important;
    font-weight:900;
}

.feature-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px;
}

.feature-box{
    background:linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    border:2px solid #e5e7eb;
    border-radius:20px;
    padding:16px;
}

.feature-num{
    display:inline-block;
    background:#111827;
    color:white !important;
    font-size:13px;
    font-weight:900;
    border-radius:999px;
    padding:5px 10px;
    margin-bottom:10px;
}

.feature-title{
    font-size:21px;
    font-weight:900;
    color:#111827 !important;
    margin-bottom:6px;
}

.feature-text{
    font-size:16px;
    line-height:1.8;
    color:#334155 !important;
}

/* 強い訴求 */
.warning-box{
    background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%);
    border:3px solid #fb7185;
    border-radius:24px;
    padding:22px 20px;
    margin-top:18px;
    box-shadow:0 10px 22px rgba(251,113,133,0.15);
}

.warning-title{
    font-size:30px;
    font-weight:900;
    color:#9f1239 !important;
    line-height:1.4;
    margin-bottom:10px;
}

.warning-text{
    font-size:18px;
    line-height:1.9;
    color:#4c0519 !important;
}

/* 価格 */
.price-box{
    background:
      linear-gradient(135deg, rgba(34,197,94,0.15), rgba(34,197,94,0.02)),
      #f0fdf4;
    border:4px solid #16a34a;
    border-radius:26px;
    padding:26px 20px;
    margin-top:18px;
    text-align:center;
    box-shadow:0 14px 30px rgba(34,197,94,0.14);
}

.price-box h3{
    font-size:42px;
    font-weight:900;
    color:#111827 !important;
    margin:0 0 10px 0;
}

.price-main{
    font-size:58px;
    font-weight:900;
    color:#111827 !important;
    line-height:1.2;
    margin-top:12px;
    margin-bottom:8px;
}

.price-text{
    font-size:19px;
    line-height:1.9;
    color:#111827 !important;
}

/* 導線 */
.flow{
    display:grid;
    grid-template-columns:repeat(4, 1fr);
    gap:12px;
}

.flow-box{
    background:#ffffff;
    border:2px solid #dbeafe;
    border-radius:18px;
    padding:16px 12px;
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
    color:#6b7280 !important;
    font-size:14px;
    line-height:1.9;
    margin-top:22px;
    text-align:center;
}

/* スマホ */
@media (max-width: 768px){
    .block-container{
        padding-top: 0.6rem;
        padding-bottom: 2rem;
    }

    .hero{
        padding:24px 16px 22px 16px;
        border-radius:22px;
    }

    .hero-title{
        font-size:36px;
        line-height:1.15;
    }

    .hero-text{
        font-size:17px;
        line-height:1.85;
    }

    .hero-mini{
        font-size:14px;
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

    .flow{
        grid-template-columns:1fr;
    }

    .price-box h3{
        font-size:32px;
    }

    .price-main{
        font-size:46px;
    }

    div.stLinkButton > a{
        font-size:21px !important;
        padding:16px 14px !important;
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
st.markdown("""
<div style="
background:#f3fff5;
border:3px solid #2e7d32;
border-radius:16px;
padding:12px;
margin-bottom:20px;
text-align:center;
font-size:18px;
font-weight:700;
">
現在 <span style="font-size:24px;">多くの建設会社</span> が診断しています
</div>
""", unsafe_allow_html=True)
# 警告
st.markdown("""
<div class="warning-box">
    <div class="warning-title">売上があっても、現金が尽きたら終わりです。</div>
    <div class="warning-text">
        利益が出ていても、入金サイト・原価率・固定費のズレで<br>
        <span class="em">突然お金が回らなくなる</span> ことがあります。<br>
        建設キャッシュレーダーは、その危険を先に見つけるためのツールです。
    </div>
</div>
""", unsafe_allow_html=True)

# 悩み
st.markdown("""
<div class="section-card">
    <div class="section-title">こんなお悩みありませんか？</div>
    <ul class="problem-list">
        <li>売上はあるのに、なぜかお金が残らない</li>
        <li>原価率の高い現場に、後から気づく</li>
        <li>このままで本当に大丈夫か不安</li>
        <li>銀行や税理士に、数字をうまく説明できない</li>
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

# 導線説明
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
※ トラック広告・チラシ・プロフィールQRからそのまま開けます。
</div>
""", unsafe_allow_html=True)
