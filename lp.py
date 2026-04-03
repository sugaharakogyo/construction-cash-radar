import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app/"
LINE_URL = "https://lin.ee/7m28VAs"
STRIPE_URL = "https://buy.stripe.com/6oU28rarietE5gM6m87N600"

st.markdown("""
<style>
.block-container{
    max-width: 920px;
    padding-top: 0.8rem;
    padding-bottom: 2rem;
}

.stApp{
    background: linear-gradient(180deg,#f8fafc 0%,#eef2f7 100%);
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    color:#111827;
}

/* hero */
.hero{
    background: linear-gradient(135deg,#07111f 0%,#0b2f66 42%,#0ea5e9 100%);
    border-radius: 28px;
    padding: 34px 28px 30px 28px;
    color: white;
    margin-bottom: 18px;
    box-shadow: 0 24px 48px rgba(2,8,23,0.22);
    position: relative;
    overflow: hidden;
}

.hero::after{
    content:"";
    position:absolute;
    right:-60px;
    top:-60px;
    width:180px;
    height:180px;
    background: rgba(255,255,255,0.08);
    border-radius: 999px;
}

.hero-badge{
    background:#facc15;
    color:#111827;
    padding:7px 14px;
    border-radius:999px;
    font-size:14px;
    font-weight:800;
    display:inline-block;
    margin-bottom:14px;
}

.hero-app{
    font-size:15px;
    font-weight:800;
    margin-bottom:10px;
    color:#dbeafe;
    letter-spacing:0.03em;
}

.hero-title{
    font-size:54px;
    font-weight:900;
    line-height:1.05;
    margin-bottom:18px;
    letter-spacing:-0.02em;
}

.yellow{color:#facc15;}
.red{color:#ff6b74;}

.hero-sub{
    font-size:20px;
    line-height:1.8;
    font-weight:700;
    color:#f8fafc;
}

.hero-mini{
    margin-top:14px;
    color:#dbeafe;
    font-size:15px;
    line-height:1.7;
    font-weight:600;
}

/* cta */
.cta-band{
    background:#dcfce7;
    border:2px solid #16a34a;
    border-radius:16px;
    padding:12px 14px;
    font-weight:900;
    text-align:center;
    margin:14px 0 16px;
    color:#166534;
    box-shadow:0 6px 18px rgba(22,163,74,0.08);
}

.sub-cta{
    text-align:center;
    color:#475569;
    font-size:14px;
    margin-top:-4px;
    margin-bottom:10px;
    font-weight:600;
}

/* section title */
.section-title{
    font-size:30px;
    font-weight:900;
    margin:34px 0 14px;
    color:#0f172a;
    letter-spacing:-0.02em;
}

/* cards */
.card{
    background:white;
    border-radius:18px;
    padding:20px 18px;
    margin-bottom:12px;
    box-shadow:0 8px 20px rgba(15,23,42,0.06);
    border:1px solid #e5e7eb;
    color:#111827;
    line-height:1.75;
}

.card strong,
.card b{
    font-size:18px;
}

.card-green{
    background:linear-gradient(180deg,#f0fdf4 0%,#dcfce7 100%);
    border-left:6px solid #16a34a;
}

.card-blue{
    background:linear-gradient(180deg,#eff6ff 0%,#dbeafe 100%);
    border-left:6px solid #2563eb;
}

.card-yellow{
    background:linear-gradient(180deg,#fefce8 0%,#fef9c3 100%);
    border-left:6px solid #eab308;
}

/* alert */
.warning{
    background:linear-gradient(180deg,#fff1f2 0%,#fee2e2 100%);
    border-left:6px solid #ef4444;
    border-radius:18px;
    padding:22px;
    margin:26px 0;
    color:#111827;
    box-shadow:0 8px 20px rgba(239,68,68,0.08);
    line-height:1.8;
}

/* sample */
.sample{
    background:linear-gradient(180deg,#eef2ff 0%,#e0e7ff 100%);
    border-left:6px solid #4f46e5;
    border-radius:18px;
    padding:22px;
    margin:24px 0;
    color:#111827;
    box-shadow:0 8px 20px rgba(79,70,229,0.08);
    line-height:1.9;
}

/* list */
.list{
    background:white;
    border-radius:16px;
    padding:16px 18px;
    margin-bottom:10px;
    box-shadow:0 6px 16px rgba(15,23,42,0.05);
    border:1px solid #e5e7eb;
    color:#111827;
    font-weight:700;
}

/* price */
.price{
    background:linear-gradient(180deg,#f0fdf4 0%,#dcfce7 100%);
    border:4px solid #16a34a;
    border-radius:28px;
    padding:30px 22px;
    text-align:center;
    margin:34px 0 18px;
    color:#111827;
    box-shadow:0 18px 40px rgba(22,163,74,0.10);
}

.price-title{
    font-size:32px;
    font-weight:900;
    line-height:1.3;
    margin-bottom:10px;
}

.price-body{
    font-size:18px;
    line-height:1.9;
    font-weight:700;
    color:#1f2937;
}

.price-main{
    font-size:56px;
    font-weight:900;
    margin:14px 0 10px;
    color:#166534;
    letter-spacing:-0.03em;
}

.price-mini{
    font-size:15px;
    color:#374151;
    font-weight:700;
}

/* footer box */
.footer-note{
    background:#ffffff;
    border-radius:16px;
    padding:18px;
    margin-top:20px;
    border:1px solid #e5e7eb;
    color:#475569;
    text-align:center;
    font-size:14px;
    line-height:1.8;
}

/* Streamlit buttons */
div[data-testid="stLinkButton"] a{
    width:100%;
    display:inline-block;
    text-align:center;
    padding:0.95rem 1rem;
    border-radius:14px;
    font-weight:900;
    font-size:1rem;
    text-decoration:none !important;
    transition:all .2s ease;
    box-shadow:0 10px 20px rgba(15,23,42,0.08);
}

div[data-testid="stLinkButton"] a:hover{
    transform:translateY(-1px);
}

/* first button */
[data-testid="stLinkButton"] + div[data-testid="stLinkButton"] a{
    background:#ffffff !important;
    color:#0f172a !important;
    border:2px solid #d1d5db !important;
}

/* mobile */
@media(max-width:768px){
    .block-container{
        padding-top:0.5rem;
        padding-left:0.8rem;
        padding-right:0.8rem;
    }

    .hero{
        padding:24px 18px 22px 18px;
        border-radius:22px;
    }

    .hero-title{
        font-size:36px;
        line-height:1.12;
    }

    .hero-sub{
        font-size:16px;
        line-height:1.7;
    }

    .hero-mini{
        font-size:14px;
    }

    .section-title{
        font-size:23px;
        margin:28px 0 12px;
    }

    .card,
    .warning,
    .sample,
    .list{
        border-radius:14px;
        padding:16px 14px;
    }

    .price{
        border-radius:22px;
        padding:24px 16px;
    }

    .price-title{
        font-size:24px;
    }

    .price-main{
        font-size:42px;
    }

    .price-body{
        font-size:16px;
    }

    div[data-testid="stLinkButton"] a{
        font-size:0.95rem;
        padding:0.9rem 0.85rem;
        border-radius:12px;
    }
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>

    <div class="hero-app">建設キャッシュレーダー</div>

    <div class="hero-title">
        <span class="yellow">黒字でも</span><br>
        <span class="red">倒産します</span>
    </div>

    <div class="hero-sub">
        原因は <b>資金ショート</b> です。<br><br>
        売上・原価・固定費・現金を入れるだけで<br>
        あなたの会社の<br>
        <b>資金ショート危険度</b> と
        <b>安全ライン不足額</b> が<br>
        30秒で分かります。
    </div>

    <div class="hero-mini">
        会計ソフトでは見えない未来の資金繰りを見える化。
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="cta-band">建設会社専用 / 資金ショート危険度を無料診断</div>', unsafe_allow_html=True)
st.link_button("30秒で無料診断する", APP_URL)
st.markdown('<div class="sub-cta">登録不要ですぐ使えます</div>', unsafe_allow_html=True)

# 3つ
st.markdown('<div class="section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)

st.markdown('<div class="card card-green"><b>資金ショートまでの期間</b><br>あと何ヶ月持つかが一発で分かります。</div>', unsafe_allow_html=True)
st.markdown('<div class="card card-blue"><b>安全ラインとの差額</b><br>あといくら必要かが明確になります。</div>', unsafe_allow_html=True)
st.markdown('<div class="card card-yellow"><b>改善ポイント</b><br>どこを直せばいいかがその場で分かります。</div>', unsafe_allow_html=True)

# WARNING
st.markdown("""
<div class="warning">
    <b style="font-size:22px">売上があっても、現金が尽きたら終わりです。</b><br><br>
    利益が出ていても、
    入金サイト・原価率・固定費のズレで
    突然お金が回らなくなることがあります。
</div>
""", unsafe_allow_html=True)

# sample
st.markdown('<div class="section-title">診断結果のイメージ</div>', unsafe_allow_html=True)

st.markdown("""
<div class="sample">
    売上　900万円<br>
    原価　620万円<br>
    固定費　260万円<br>
    現金　180万円<br><br>

    <b>診断結果</b><br><br>

    資金ショートまで <b>3.4ヶ月</b><br><br>
    安全ライン <b>あと380万円不足</b><br><br>
    改善ポイント <b>原価率 −3%</b>
</div>
""", unsafe_allow_html=True)

# 悩み
st.markdown('<div class="section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)

st.markdown('<div class="list">売上はあるのにお金が残らない</div>', unsafe_allow_html=True)
st.markdown('<div class="list">原価率が高い現場に後から気づく</div>', unsafe_allow_html=True)
st.markdown('<div class="list">このままで本当に大丈夫か不安</div>', unsafe_allow_html=True)
st.markdown('<div class="list">銀行や税理士に数字を説明できない</div>', unsafe_allow_html=True)

# 向いてる会社
st.markdown('<div class="section-title">このサービスが向いている会社</div>', unsafe_allow_html=True)

st.markdown('<div class="list">月ごとの資金繰りを先に把握したい会社</div>', unsafe_allow_html=True)
st.markdown('<div class="list">社長が数字判断を早くしたい会社</div>', unsafe_allow_html=True)
st.markdown('<div class="list">税理士・銀行との会話を強くしたい会社</div>', unsafe_allow_html=True)

# 使い方
st.markdown('<div class="section-title">使い方はかんたんです</div>', unsafe_allow_html=True)

st.markdown('<div class="list"><b>STEP1</b> 数字を入力</div>', unsafe_allow_html=True)
st.markdown('<div class="list"><b>STEP2</b> 診断結果を見る</div>', unsafe_allow_html=True)
st.markdown('<div class="list"><b>STEP3</b> LINEで相談</div>', unsafe_allow_html=True)
st.markdown('<div class="list"><b>STEP4</b> Pro版で継続管理</div>', unsafe_allow_html=True)

# price
st.markdown("""
<div class="price">
    <div class="price-title">社長専用 Proダッシュボード</div>

    <div class="price-body">
        12ヶ月資金推移<br>
        現場利益管理<br>
        銀行提出サマリー<br>
        利益改善シミュレーター
    </div>

    <div class="price-main">月 9,800円</div>
    <div class="price-mini">まずは無料診断から始められます</div>
</div>
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)
st.link_button("PRO版を始める（月額9,800円）", STRIPE_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

st.markdown("""
<div class="footer-note">
    建設会社の資金不安を、数字で見える化。<br>
    会計ソフトでは見えない「未来のキャッシュ」をすぐ確認できます。
</div>
""", unsafe_allow_html=True)
