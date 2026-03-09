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
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

html, body, [class*="css"]  {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background: #f7f7f7;
}

.hero{
    background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 55%, #06b6d4 100%);
    color: white !important;
    border-radius: 24px;
    padding: 28px 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    margin-bottom: 22px;
}

.hero h1{
    font-size: 48px;
    line-height: 1.2;
    margin: 0 0 14px 0;
    font-weight: 900;
    color: white !important;
}

.hero p{
    font-size: 20px;
    line-height: 1.8;
    margin: 0;
    color: white !important;
}

.hero-badge{
    display:inline-block;
    background:#facc15;
    color:#111 !important;
    font-weight:800;
    font-size:14px;
    border-radius:999px;
    padding:8px 14px;
    margin-bottom:16px;
}

.section-card{
    background:#ffffff;
    border-radius:22px;
    padding:24px 20px;
    margin-top:18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
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

.problem-list{
    margin:0;
    padding-left:22px;
    font-size:18px;
    line-height:2.0;
    color:#222 !important;
}

.point-box{
    background:#f8fafc;
    border:2px solid #e5e7eb;
    border-radius:18px;
    padding:16px;
    margin-top:12px;
}

.point-title{
    font-size:20px;
    font-weight:800;
    margin-bottom:6px;
    color:#111 !important;
}

.price-box{
    background:#eef9f0;
    border:4px solid #2e7d32;
    border-radius:22px;
    padding:24px 20px;
    margin-top:18px;
    text-align:center;
}

.price-box h3{
    font-size:40px;
    font-weight:900;
    margin:0 0 10px 0;
    color:#111 !important;
}

.price-box p{
    font-size:18px;
    line-height:1.9;
    color:#111 !important;
    margin:0;
}

.cta-sub{
    text-align:center;
    font-size:18px;
    line-height:1.8;
    color:#333 !important;
    margin-top:14px;
}

.small-note{
    color:#666 !important;
    font-size:14px;
    line-height:1.8;
    margin-top:20px;
}

div.stLinkButton > a{
    display:block !important;
    text-align:center !important;
    background:#ef4444 !important;
    color:#ffffff !important;
    border:0 !important;
    border-radius:16px !important;
    padding:18px 20px !important;
    font-size:22px !important;
    font-weight:900 !important;
    text-decoration:none !important;
    box-shadow:0 8px 20px rgba(239,68,68,0.30) !important;
}

div.stLinkButton > a:hover{
    background:#dc2626 !important;
    color:#ffffff !important;
}

@media (max-width: 768px){
    .block-container{
        padding-top: 0.8rem;
        padding-bottom: 2rem;
    }

    .hero{
        padding:22px 16px;
        border-radius:20px;
    }

    .hero h1{
        font-size:34px;
    }

    .hero p{
        font-size:17px;
        line-height:1.8;
    }

    .section-title{
        font-size:24px;
    }

    .section-text,
    .problem-list{
        font-size:16px;
    }

    .price-box h3{
        font-size:34px;
    }

    div.stLinkButton > a{
        font-size:20px !important;
        padding:16px 14px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =====================================
# ヒーロー
# =====================================
st.markdown("""
<div class="hero">
    <div class="hero-badge">建設会社向け / スマホで30秒診断</div>
    <h1>建設会社は<br>黒字でも潰れます</h1>
    <p>
        原因は <b>資金ショート</b>。<br>
        売上・原価・固定費・現金を入れるだけで、<br>
        <b>いつ危ないか</b> と <b>安全にするには月いくら必要か</b> がすぐ分かります。
    </p>
</div>
""", unsafe_allow_html=True)

st.link_button("無料で診断する", APP_URL)

st.markdown("""
<div class="cta-sub">
    まずは無料で、あなたの会社のキャッシュ状況を確認してください。
</div>
""", unsafe_allow_html=True)

# =====================================
# 悩み
# =====================================
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

# =====================================
# 解決
# =====================================
st.markdown("""
<div class="section-card">
    <div class="section-title">建設キャッシュレーダーで分かること</div>
    <div class="point-box">
        <div class="point-title">① 資金ショート時期</div>
        <div class="section-text">このままだと、あと何ヶ月で危ないかが分かります。</div>
    </div>
    <div class="point-box">
        <div class="point-title">② 安全ラインまでの不足額</div>
        <div class="section-text">安全にするには、月いくら改善が必要かが見えます。</div>
    </div>
    <div class="point-box">
        <div class="point-title">③ 今やるべき打ち手</div>
        <div class="section-text">売上・入金・固定費・原価のどこを優先すべきか整理できます。</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# Pro案内
# =====================================
st.markdown("""
<div class="price-box">
    <h3>続きは Pro版へ</h3>
    <p>
        Pro版では<br>
        <b>12ヶ月資金推移</b>・<b>現場利益管理</b>・<b>銀行提出サマリー</b><br>
        ・<b>利益改善シミュレーター</b> まで使えます。
    </p>
    <p style="font-size:48px; font-weight:900; margin-top:14px;">月 9,800円</p>
    <p style="margin-top:8px;">まずは無料診断 → 気に入ったらLINEから申込み</p>
</div>
""", unsafe_allow_html=True)

st.link_button("無料で診断する", APP_URL)

# =====================================
# LINE案内
# =====================================
st.markdown("""
<div class="section-card">
    <div class="section-title">Proをご希望の方へ</div>
    <div class="section-text">
        無料診断のあと、もっと詳しく使いたい方はLINEからお申し込みください。<br>
        Pro版コードをお送りします。
    </div>
</div>
""", unsafe_allow_html=True)

st.link_button("LINEで問い合わせる", LINE_URL)

# =====================================
# フッター
# =====================================
st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ トラック広告・チラシ・プロフィールQRからそのまま開けます。
</div>
""", unsafe_allow_html=True)
