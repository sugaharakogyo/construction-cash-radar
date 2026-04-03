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
    max-width: 980px;
    padding-top: 0.8rem;
    padding-bottom: 2.5rem;
}

.stApp{
    background: #f8fafc;
    color: #0f172a;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* 共通 */
.section-label{
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    font-weight: 800;
    font-size: 13px;
    padding: 6px 12px;
    border-radius: 999px;
    margin-bottom: 12px;
}

.section-title{
    font-size: 34px;
    font-weight: 900;
    line-height: 1.3;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin: 10px 0 10px;
}

.section-sub{
    font-size: 17px;
    line-height: 1.9;
    color: #475569;
    font-weight: 600;
    margin-bottom: 20px;
}

.card{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(15,23,42,0.05);
    margin-bottom: 14px;
}

.mini-card{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 20px rgba(15,23,42,0.05);
    margin-bottom: 12px;
}

.feature-title{
    font-size: 20px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 8px;
}

.feature-text{
    color: #475569;
    line-height: 1.85;
    font-weight: 600;
}

.divider-space{
    height: 10px;
}

/* hero */
.hero-wrap{
    background: linear-gradient(135deg,#ffffff 0%,#eff6ff 100%);
    border: 1px solid #dbeafe;
    border-radius: 28px;
    padding: 34px 28px;
    box-shadow: 0 16px 40px rgba(15,23,42,0.06);
    margin-bottom: 18px;
}

.hero-badge{
    display: inline-block;
    background: #1d4ed8;
    color: white;
    font-weight: 800;
    font-size: 13px;
    padding: 7px 13px;
    border-radius: 999px;
    margin-bottom: 16px;
}

.hero-title{
    font-size: 52px;
    font-weight: 900;
    line-height: 1.14;
    letter-spacing: -0.03em;
    color: #0f172a;
    margin-bottom: 14px;
}

.hero-title .blue{
    color: #1d4ed8;
}

.hero-title .red{
    color: #dc2626;
}

.hero-sub{
    font-size: 18px;
    line-height: 1.95;
    color: #334155;
    font-weight: 600;
    margin-bottom: 18px;
}

.hero-points{
    background: white;
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 18px;
    color: #0f172a;
    line-height: 1.9;
    font-weight: 700;
    margin-top: 12px;
}

.hero-points b{
    color: #1d4ed8;
}

.cta-row-note{
    text-align: center;
    color: #64748b;
    font-size: 14px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 2px;
}

/* buttons */
.cta-primary{
    display: block;
    width: 100%;
    text-align: center;
    background: linear-gradient(135deg,#2563eb 0%,#1d4ed8 100%);
    color: white !important;
    text-decoration: none !important;
    padding: 16px 18px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 900;
    box-shadow: 0 12px 24px rgba(37,99,235,0.24);
    margin: 10px 0;
}

.cta-secondary{
    display: block;
    width: 100%;
    text-align: center;
    background: white;
    color: #0f172a !important;
    text-decoration: none !important;
    padding: 16px 18px;
    border-radius: 14px;
    font-size: 17px;
    font-weight: 800;
    border: 2px solid #d1d5db;
    margin: 10px 0;
}

.cta-line{
    display: block;
    width: 100%;
    text-align: center;
    background: #16a34a;
    color: white !important;
    text-decoration: none !important;
    padding: 16px 18px;
    border-radius: 14px;
    font-size: 17px;
    font-weight: 900;
    box-shadow: 0 10px 22px rgba(22,163,74,0.20);
    margin: 10px 0;
}

/* 3 benefits */
.benefit-grid{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-top: 12px;
    margin-bottom: 8px;
}

.benefit-box{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 22px 18px;
    box-shadow: 0 8px 20px rgba(15,23,42,0.05);
}

.benefit-box .num{
    color: #1d4ed8;
    font-size: 14px;
    font-weight: 900;
    margin-bottom: 8px;
}

.benefit-box .ttl{
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 8px;
    color: #0f172a;
}

.benefit-box .txt{
    color: #475569;
    line-height: 1.8;
    font-weight: 600;
}

/* alert */
.alert{
    background: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 6px solid #ef4444;
    border-radius: 18px;
    padding: 22px;
    color: #0f172a;
    line-height: 1.9;
    font-weight: 700;
    margin: 28px 0 8px;
}

.alert b{
    font-size: 22px;
}

/* sample */
.sample-wrap{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 12px 26px rgba(15,23,42,0.05);
}

.sample-top{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 14px;
}

.sample-box{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 18px;
    font-weight: 700;
    color: #334155;
    line-height: 1.9;
}

.sample-result{
    background: linear-gradient(135deg,#eff6ff 0%,#eef2ff 100%);
    border: 1px solid #c7d2fe;
    border-radius: 18px;
    padding: 20px;
    color: #0f172a;
    line-height: 2.0;
    font-weight: 700;
}

.sample-result .big{
    font-size: 26px;
    font-weight: 900;
    color: #1d4ed8;
}

/* problem list */
.problem-list{
    display: grid;
    gap: 10px;
}

.problem-item{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 16px 18px;
    box-shadow: 0 6px 16px rgba(15,23,42,0.04);
    font-weight: 700;
    color: #0f172a;
}

/* steps */
.step-list{
    display: grid;
    gap: 12px;
}

.step-item{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 16px rgba(15,23,42,0.04);
}

.step-item b{
    color: #1d4ed8;
    font-size: 15px;
}

/* price */
.price-wrap{
    background: linear-gradient(135deg,#f0fdf4 0%,#dcfce7 100%);
    border: 2px solid #16a34a;
    border-radius: 26px;
    padding: 30px 24px;
    text-align: center;
    box-shadow: 0 18px 38px rgba(22,163,74,0.10);
}

.price-label{
    display: inline-block;
    background: #166534;
    color: white;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 900;
    margin-bottom: 14px;
}

.price-title{
    font-size: 34px;
    font-weight: 900;
    line-height: 1.4;
    color: #0f172a;
    margin-bottom: 10px;
}

.price-text{
    font-size: 17px;
    line-height: 1.95;
    color: #1f2937;
    font-weight: 700;
}

.price-main{
    font-size: 58px;
    font-weight: 900;
    color: #166534;
    letter-spacing: -0.03em;
    margin: 14px 0 10px;
}

.price-sub{
    font-size: 14px;
    color: #475569;
    font-weight: 700;
}

/* footer */
.footer-box{
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    color: #64748b;
    line-height: 1.85;
    font-size: 14px;
    margin-top: 18px;
}

/* responsive */
@media (max-width: 768px){
    .block-container{
        padding-left: 0.8rem;
        padding-right: 0.8rem;
        padding-top: 0.5rem;
    }

    .hero-wrap{
        padding: 24px 18px;
        border-radius: 22px;
    }

    .hero-title{
        font-size: 35px;
        line-height: 1.2;
    }

    .hero-sub{
        font-size: 16px;
        line-height: 1.8;
    }

    .section-title{
        font-size: 26px;
    }

    .benefit-grid{
        grid-template-columns: 1fr;
        gap: 12px;
    }

    .sample-top{
        grid-template-columns: 1fr;
    }

    .price-title{
        font-size: 26px;
    }

    .price-main{
        font-size: 42px;
    }

    .cta-primary,
    .cta-secondary,
    .cta-line{
        font-size: 16px;
        padding: 15px 14px;
    }
}
</style>
""", unsafe_allow_html=True)

# ヒーロー
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>

    <div class="hero-title">
        <span class="blue">資金あと何ヶ月もつか</span><br>
        一発で分かる
    </div>

    <div class="hero-sub">
        売上・原価・固定費・現金を入れるだけで、<br>
        あなたの会社の <b>資金ショート危険度</b> と
        <b>安全ライン不足額</b> を<br>
        その場で見える化します。
    </div>

    <div class="hero-points">
        ・黒字でも現金が尽きる理由が見える<br>
        ・あと何ヶ月持つかが分かる<br>
        ・次に何を直せばいいかが分かる
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a href="{APP_URL}" target="_self" class="cta-primary">30秒で無料診断する</a>',
    unsafe_allow_html=True
)
st.markdown('<div class="cta-row-note">登録不要ですぐ使えます</div>', unsafe_allow_html=True)

# 3つ分かること
st.markdown('<div class="section-label">FEATURES</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">社長が知りたい数字だけを、できるだけ分かりやすく表示します。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="benefit-grid">
    <div class="benefit-box">
        <div class="num">01</div>
        <div class="ttl">資金ショートまでの期間</div>
        <div class="txt">あと何ヶ月持つかを、その場で把握できます。</div>
    </div>
    <div class="benefit-box">
        <div class="num">02</div>
        <div class="ttl">安全ラインとの差額</div>
        <div class="txt">あといくら足りないかが明確になります。</div>
    </div>
    <div class="benefit-box">
        <div class="num">03</div>
        <div class="ttl">改善ポイント</div>
        <div class="txt">どこを直せばいいか、優先順位が見えます。</div>
    </div>
</div>
""", unsafe_allow_html=True)

# アラート
st.markdown("""
<div class="alert">
    <b>売上があっても、現金が尽きたら終わりです。</b><br><br>
    利益が出ていても、入金サイト・原価率・固定費のズレで、
    突然お金が回らなくなることがあります。<br>
    会計ソフトや試算表だけでは見えない
    <b>“未来の資金繰り”</b> を先に確認するためのサービスです。
</div>
""", unsafe_allow_html=True)

# 診断イメージ
st.markdown('<div class="section-label">SAMPLE</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">診断結果のイメージ</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">入力した数字から、危険度と改善の方向性をすぐ確認できます。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="sample-wrap">
    <div class="sample-top">
        <div class="sample-box">
            売上　900万円<br>
            原価　620万円<br>
            固定費　260万円<br>
            現金　180万円
        </div>
        <div class="sample-result">
            <b>診断結果</b><br><br>
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

# 悩み
st.markdown('<div class="section-label">PROBLEMS</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">建設会社の社長が、よく感じる不安を前提に作っています。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="problem-list">
    <div class="problem-item">売上はあるのにお金が残らない</div>
    <div class="problem-item">原価率が高い現場に後から気づく</div>
    <div class="problem-item">このままで本当に大丈夫か不安</div>
    <div class="problem-item">銀行や税理士に数字を説明しづらい</div>
</div>
""", unsafe_allow_html=True)

# 向いてる会社
st.markdown('<div class="section-label">FOR WHO</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">このサービスが向いている会社</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">特に、数字判断を早くしたい会社に向いています。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="problem-list">
    <div class="problem-item">月ごとの資金繰りを先に把握したい会社</div>
    <div class="problem-item">社長が数字判断を早くしたい会社</div>
    <div class="problem-item">税理士・銀行との会話を強くしたい会社</div>
</div>
""", unsafe_allow_html=True)

# 使い方
st.markdown('<div class="section-label">FLOW</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">使い方はかんたんです</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">むずかしい設定はありません。数字を入れるだけです。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="step-list">
    <div class="step-item"><b>STEP 1</b><br>売上・原価・固定費・現金を入力</div>
    <div class="step-item"><b>STEP 2</b><br>危険度と不足額を確認</div>
    <div class="step-item"><b>STEP 3</b><br>改善ポイントを確認</div>
    <div class="step-item"><b>STEP 4</b><br>必要ならLINE相談 / Pro版で継続管理</div>
</div>
""", unsafe_allow_html=True)

# 価格
st.markdown('<div class="section-label">PLAN</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">社長専用 Proダッシュボード</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">無料診断で確認したあと、継続管理したい方はPro版をご利用ください。</div>', unsafe_allow_html=True)

st.markdown("""
<div class="price-wrap">
    <div class="price-label">おすすめ</div>
    <div class="price-title">毎月の資金判断を、もっと早く・分かりやすく</div>
    <div class="price-text">
        12ヶ月資金推移<br>
        現場利益管理<br>
        銀行提出サマリー<br>
        利益改善シミュレーター
    </div>
    <div class="price-main">月 9,800円</div>
    <div class="price-sub">まずは無料診断から始められます</div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a href="{APP_URL}" target="_self" class="cta-primary">30秒で無料診断する</a>',
    unsafe_allow_html=True
)
st.markdown(
    f'<a href="{STRIPE_URL}" target="_blank" class="cta-secondary">PRO版を始める（月額9,800円）</a>',
    unsafe_allow_html=True
)
st.markdown(
    f'<a href="{LINE_URL}" target="_blank" class="cta-line">LINEで問い合わせる</a>',
    unsafe_allow_html=True
)

# フッター
st.markdown("""
<div class="footer-box">
    建設会社の資金不安を、数字で見える化。<br>
    会計ソフトでは見えない「未来のキャッシュ」を、すぐ確認できます。
</div>
""", unsafe_allow_html=True)
