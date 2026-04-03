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
    max-width: 1040px;
    padding-top: 0.8rem;
    padding-bottom: 3rem;
}

.stApp{
    background:
        radial-gradient(circle at top right, rgba(37,99,235,0.05), transparent 22%),
        linear-gradient(180deg, #f8fbff 0%, #f4f7fb 45%, #eef3f8 100%);
    color:#0f172a;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* ------- 共通 ------- */
.kcr-section-label{
    display:inline-block;
    background:#e0f2fe;
    color:#0369a1;
    font-size:12px;
    font-weight:900;
    letter-spacing:0.05em;
    padding:7px 12px;
    border-radius:999px;
    margin-bottom:12px;
}

.kcr-section-title{
    font-size:38px;
    font-weight:900;
    color:#0f172a;
    line-height:1.28;
    letter-spacing:-0.03em;
    margin:0 0 10px 0;
}

.kcr-section-sub{
    font-size:17px;
    line-height:1.95;
    color:#475569;
    font-weight:600;
    margin-bottom:20px;
}

.kcr-card{
    background:#ffffff;
    border:1px solid #e5e7eb;
    border-radius:20px;
    box-shadow:0 12px 30px rgba(15,23,42,0.05);
}

.kcr-spacer{
    height:10px;
}

/* ------- HERO ------- */
.kcr-hero{
    position:relative;
    overflow:hidden;
    background:linear-gradient(135deg,#ffffff 0%,#eff6ff 55%,#dbeafe 100%);
    border:1px solid #dbeafe;
    border-radius:30px;
    padding:34px 30px;
    box-shadow:0 20px 48px rgba(15,23,42,0.06);
    margin-bottom:18px;
}

.kcr-hero:before{
    content:"";
    position:absolute;
    top:-80px;
    right:-50px;
    width:220px;
    height:220px;
    background:rgba(37,99,235,0.08);
    border-radius:999px;
}

.kcr-hero:after{
    content:"";
    position:absolute;
    bottom:-80px;
    left:-60px;
    width:180px;
    height:180px;
    background:rgba(14,165,233,0.08);
    border-radius:999px;
}

.kcr-hero-inner{
    position:relative;
    z-index:2;
}

.kcr-badge{
    display:inline-block;
    background:linear-gradient(135deg,#2563eb 0%,#1d4ed8 100%);
    color:#fff;
    font-size:13px;
    font-weight:900;
    padding:8px 14px;
    border-radius:999px;
    margin-bottom:16px;
    box-shadow:0 10px 20px rgba(37,99,235,0.20);
}

.kcr-app-name{
    color:#1e40af;
    font-size:15px;
    font-weight:900;
    letter-spacing:0.04em;
    margin-bottom:10px;
}

.kcr-hero-title{
    font-size:56px;
    line-height:1.08;
    font-weight:900;
    letter-spacing:-0.04em;
    color:#0f172a;
    margin-bottom:16px;
}

.kcr-hero-title .blue{
    color:#1d4ed8;
}

.kcr-hero-title .dark{
    color:#0f172a;
}

.kcr-hero-sub{
    font-size:19px;
    line-height:1.95;
    color:#334155;
    font-weight:700;
    margin-bottom:16px;
}

.kcr-hero-sub b{
    color:#1d4ed8;
}

.kcr-hero-points{
    background:rgba(255,255,255,0.88);
    backdrop-filter: blur(6px);
    border:1px solid #dbeafe;
    border-radius:18px;
    padding:18px 20px;
    color:#0f172a;
    font-size:16px;
    line-height:1.95;
    font-weight:700;
}

.kcr-hero-points b{
    color:#1d4ed8;
}

/* ------- CTA ------- */
.kcr-cta-primary{
    display:block;
    width:100%;
    text-align:center;
    text-decoration:none !important;
    background:linear-gradient(135deg,#2563eb 0%,#1d4ed8 100%);
    color:#ffffff !important;
    padding:17px 18px;
    border-radius:16px;
    font-size:19px;
    font-weight:900;
    box-shadow:0 14px 28px rgba(37,99,235,0.24);
    margin:12px 0 8px 0;
}

.kcr-cta-primary:hover{
    filter:brightness(1.02);
}

.kcr-cta-subnote{
    text-align:center;
    color:#64748b;
    font-size:14px;
    font-weight:700;
    margin-bottom:18px;
}

.kcr-cta-secondary{
    display:block;
    width:100%;
    text-align:center;
    text-decoration:none !important;
    background:#ffffff;
    color:#0f172a !important;
    padding:16px 18px;
    border-radius:16px;
    font-size:17px;
    font-weight:900;
    border:2px solid #cbd5e1;
    margin:10px 0;
    box-shadow:0 10px 22px rgba(15,23,42,0.05);
}

.kcr-cta-line{
    display:block;
    width:100%;
    text-align:center;
    text-decoration:none !important;
    background:linear-gradient(135deg,#16a34a 0%,#15803d 100%);
    color:#ffffff !important;
    padding:16px 18px;
    border-radius:16px;
    font-size:17px;
    font-weight:900;
    margin:10px 0;
    box-shadow:0 12px 24px rgba(22,163,74,0.20);
}

/* ------- 3つ分かる ------- */
.kcr-feature-grid{
    display:grid;
    grid-template-columns:repeat(3, 1fr);
    gap:16px;
    margin-top:10px;
}

.kcr-feature-box{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:20px;
    padding:24px 20px;
    box-shadow:0 10px 24px rgba(15,23,42,0.05);
}

.kcr-feature-num{
    color:#2563eb;
    font-size:14px;
    font-weight:900;
    margin-bottom:10px;
}

.kcr-feature-title{
    font-size:23px;
    font-weight:900;
    line-height:1.45;
    color:#0f172a;
    margin-bottom:10px;
}

.kcr-feature-text{
    color:#475569;
    font-size:16px;
    line-height:1.9;
    font-weight:600;
}

/* ------- warning ------- */
.kcr-alert{
    background:linear-gradient(180deg,#fff1f2 0%,#ffe4e6 100%);
    border:1px solid #fecdd3;
    border-left:6px solid #ef4444;
    border-radius:20px;
    padding:24px 22px;
    margin:28px 0 10px;
    box-shadow:0 10px 24px rgba(239,68,68,0.08);
}

.kcr-alert-title{
    font-size:30px;
    font-weight:900;
    color:#111827;
    line-height:1.5;
    margin-bottom:10px;
}

.kcr-alert-text{
    color:#374151;
    font-size:17px;
    line-height:1.95;
    font-weight:700;
}

/* ------- sample ------- */
.kcr-sample{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:24px;
    padding:24px;
    box-shadow:0 14px 30px rgba(15,23,42,0.05);
}

.kcr-sample-top{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
}

.kcr-sample-input{
    background:#f8fafc;
    border:1px solid #e2e8f0;
    border-radius:18px;
    padding:20px;
    font-size:16px;
    line-height:2.0;
    color:#334155;
    font-weight:800;
}

.kcr-sample-result{
    background:linear-gradient(135deg,#eff6ff 0%,#eef2ff 100%);
    border:1px solid #c7d2fe;
    border-radius:18px;
    padding:20px;
    font-size:16px;
    line-height:2.0;
    color:#0f172a;
    font-weight:800;
}

.kcr-sample-result .big{
    font-size:30px;
    line-height:1.4;
    font-weight:900;
    color:#1d4ed8;
}

/* ------- list ------- */
.kcr-list{
    display:grid;
    gap:12px;
}

.kcr-list-item{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:17px 18px;
    box-shadow:0 8px 18px rgba(15,23,42,0.04);
    color:#0f172a;
    font-size:17px;
    font-weight:800;
    line-height:1.8;
}

/* ------- steps ------- */
.kcr-step-grid{
    display:grid;
    gap:12px;
}

.kcr-step-item{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:19px 18px;
    box-shadow:0 8px 18px rgba(15,23,42,0.04);
    color:#0f172a;
    line-height:1.8;
    font-size:17px;
    font-weight:800;
}

.kcr-step-item b{
    color:#2563eb;
}

/* ------- price ------- */
.kcr-price{
    background:linear-gradient(135deg,#f0fdf4 0%,#dcfce7 100%);
    border:2px solid #16a34a;
    border-radius:28px;
    padding:32px 24px;
    text-align:center;
    box-shadow:0 18px 40px rgba(22,163,74,0.10);
}

.kcr-price-badge{
    display:inline-block;
    background:#166534;
    color:#fff;
    font-size:13px;
    font-weight:900;
    padding:7px 12px;
    border-radius:999px;
    margin-bottom:14px;
}

.kcr-price-title{
    font-size:36px;
    font-weight:900;
    line-height:1.45;
    color:#0f172a;
    margin-bottom:12px;
    letter-spacing:-0.03em;
}

.kcr-price-text{
    color:#1f2937;
    font-size:17px;
    line-height:1.95;
    font-weight:700;
}

.kcr-price-main{
    font-size:60px;
    font-weight:900;
    color:#166534;
    letter-spacing:-0.04em;
    margin:14px 0 8px;
}

.kcr-price-sub{
    color:#475569;
    font-size:14px;
    font-weight:700;
}

/* ------- footer ------- */
.kcr-footer{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:18px;
    text-align:center;
    color:#64748b;
    font-size:14px;
    line-height:1.9;
    margin-top:18px;
}

/* ------- mobile ------- */
@media (max-width: 768px){
    .block-container{
        padding-left:0.85rem;
        padding-right:0.85rem;
        padding-top:0.45rem;
    }

    .kcr-hero{
        padding:24px 18px;
        border-radius:22px;
    }

    .kcr-hero-title{
        font-size:36px;
        line-height:1.18;
    }

    .kcr-hero-sub{
        font-size:16px;
    }

    .kcr-hero-points{
        font-size:15px;
        padding:16px;
    }

    .kcr-section-title{
        font-size:28px;
    }

    .kcr-section-sub{
        font-size:15px;
    }

    .kcr-feature-grid{
        grid-template-columns:1fr;
        gap:12px;
    }

    .kcr-feature-title{
        font-size:20px;
    }

    .kcr-sample-top{
        grid-template-columns:1fr;
    }

    .kcr-alert-title{
        font-size:23px;
    }

    .kcr-alert-text{
        font-size:15px;
    }

    .kcr-price-title{
        font-size:28px;
    }

    .kcr-price-main{
        font-size:44px;
    }

    .kcr-cta-primary,
    .kcr-cta-secondary,
    .kcr-cta-line{
        font-size:16px;
        padding:15px 14px;
    }
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="kcr-hero">
    <div class="kcr-hero-inner">
        <div class="kcr-badge">建設会社専用 / 最短30秒 無料診断</div>

        <div class="kcr-app-name">建設キャッシュレーダー</div>

        <div class="kcr-hero-title">
            <span class="blue">資金あと何ヶ月もつか</span><br>
            <span class="dark">一発で分かる</span>
        </div>

        <div class="kcr-hero-sub">
            売上・原価・固定費・現金を入れるだけで、<br>
            あなたの会社の <b>資金ショート危険度</b> と
            <b>安全ライン不足額</b> を<br>
            その場で見える化します。
        </div>

        <div class="kcr-hero-points">
            ・黒字でも現金が尽きる理由が見える<br>
            ・あと何ヶ月持つかが分かる<br>
            ・次に何を直せばいいかが分かる
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a href="{APP_URL}" target="_self" class="kcr-cta-primary">30秒で無料診断する</a>',
    unsafe_allow_html=True
)
st.markdown('<div class="kcr-cta-subnote">登録不要ですぐ使えます</div>', unsafe_allow_html=True)

# FEATURES
st.markdown('<div class="kcr-section-label">FEATURES</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-sub">社長が知りたい数字だけを、できるだけ分かりやすく表示します。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kcr-feature-grid">
    <div class="kcr-feature-box">
        <div class="kcr-feature-num">01</div>
        <div class="kcr-feature-title">資金ショートまでの期間</div>
        <div class="kcr-feature-text">あと何ヶ月持つかを、その場で把握できます。</div>
    </div>

    <div class="kcr-feature-box">
        <div class="kcr-feature-num">02</div>
        <div class="kcr-feature-title">安全ラインとの差額</div>
        <div class="kcr-feature-text">あといくら足りないかが明確になります。</div>
    </div>

    <div class="kcr-feature-box">
        <div class="kcr-feature-num">03</div>
        <div class="kcr-feature-title">改善ポイント</div>
        <div class="kcr-feature-text">どこを直せばいいか、優先順位が見えます。</div>
    </div>
</div>
""", unsafe_allow_html=True)

# WARNING
st.markdown("""
<div class="kcr-alert">
    <div class="kcr-alert-title">売上があっても、現金が尽きたら終わりです。</div>
    <div class="kcr-alert-text">
        利益が出ていても、入金サイト・原価率・固定費のズレで、突然お金が回らなくなることがあります。<br>
        会計ソフトや試算表だけでは見えない <b>“未来の資金繰り”</b> を先に確認するためのサービスです。
    </div>
</div>
""", unsafe_allow_html=True)

# SAMPLE
st.markdown('<div class="kcr-section-label">SAMPLE</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-title">診断結果のイメージ</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-sub">入力した数字から、危険度と改善の方向性をその場で確認できます。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kcr-sample">
    <div class="kcr-sample-top">
        <div class="kcr-sample-input">
            売上　900万円<br>
            原価　620万円<br>
            固定費　260万円<br>
            現金　180万円
        </div>

        <div class="kcr-sample-result">
            診断結果<br><br>
            資金ショートまで<br>
            <span class="big">3.4ヶ月</span><br><br>
            安全ライン不足額<br>
            <span class="big">あと380万円不足</span><br><br>
            改善ポイント<br>
            <span class="big">原価率 −3%</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# PROBLEMS
st.markdown('<div class="kcr-section-label">PROBLEMS</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-sub">建設会社の社長が感じやすい不安を前提に作っています。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kcr-list">
    <div class="kcr-list-item">売上はあるのにお金が残らない</div>
    <div class="kcr-list-item">原価率が高い現場に後から気づく</div>
    <div class="kcr-list-item">このままで本当に大丈夫か不安</div>
    <div class="kcr-list-item">銀行や税理士に数字を説明しづらい</div>
</div>
""", unsafe_allow_html=True)

# FOR WHO
st.markdown('<div class="kcr-section-label">FOR WHO</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-title">このサービスが向いている会社</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-sub">特に、数字判断を早くしたい会社に向いています。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kcr-list">
    <div class="kcr-list-item">月ごとの資金繰りを先に把握したい会社</div>
    <div class="kcr-list-item">社長が数字判断を早くしたい会社</div>
    <div class="kcr-list-item">税理士・銀行との会話を強くしたい会社</div>
</div>
""", unsafe_allow_html=True)

# FLOW
st.markdown('<div class="kcr-section-label">FLOW</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-title">使い方はかんたんです</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-sub">むずかしい設定はありません。数字を入れるだけです。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kcr-step-grid">
    <div class="kcr-step-item"><b>STEP 1</b><br>売上・原価・固定費・現金を入力</div>
    <div class="kcr-step-item"><b>STEP 2</b><br>危険度と不足額を確認</div>
    <div class="kcr-step-item"><b>STEP 3</b><br>改善ポイントを確認</div>
    <div class="kcr-step-item"><b>STEP 4</b><br>必要ならLINE相談 / Pro版で継続管理</div>
</div>
""", unsafe_allow_html=True)

# PLAN
st.markdown('<div class="kcr-section-label">PLAN</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-title">社長専用 Proダッシュボード</div>', unsafe_allow_html=True)
st.markdown('<div class="kcr-section-sub">無料診断で確認したあと、継続管理したい方はPro版をご利用ください。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kcr-price">
    <div class="kcr-price-badge">おすすめ</div>
    <div class="kcr-price-title">毎月の資金判断を、もっと早く・分かりやすく</div>
    <div class="kcr-price-text">
        12ヶ月資金推移<br>
        現場利益管理<br>
        銀行提出サマリー<br>
        利益改善シミュレーター
    </div>
    <div class="kcr-price-main">月 9,800円</div>
    <div class="kcr-price-sub">まずは無料診断から始められます</div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a href="{APP_URL}" target="_self" class="kcr-cta-primary">30秒で無料診断する</a>',
    unsafe_allow_html=True
)
st.markdown(
    f'<a href="{STRIPE_URL}" target="_blank" class="kcr-cta-secondary">PRO版を始める（月額9,800円）</a>',
    unsafe_allow_html=True
)
st.markdown(
    f'<a href="{LINE_URL}" target="_blank" class="kcr-cta-line">LINEで問い合わせる</a>',
    unsafe_allow_html=True
)

# FOOTER
st.markdown("""
<div class="kcr-footer">
    建設会社の資金不安を、数字で見える化。<br>
    会計ソフトでは見えない「未来のキャッシュ」を、すぐ確認できます。
</div>
""", unsafe_allow_html=True)
