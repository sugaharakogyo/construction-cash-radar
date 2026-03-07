import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="建設キャッシュレーダー",
    layout="wide"
)

# ===============================
# CSS
# ===============================
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

html, body, [class*="css"] {
    color: #111 !important;
}

.main {
    background: #07101f;
}

h1, h2, h3, h4, p, div, span, label {
    color: inherit;
}

.section-title {
    font-size: 32px;
    font-weight: 900;
    color: #ffffff;
    margin-top: 28px;
    margin-bottom: 10px;
    line-height: 1.4;
}

.hero-box {
    background: #f7faf7;
    border: 4px solid #1f7a1f;
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.10);
}

.hero-title {
    font-size: 48px;
    font-weight: 900;
    line-height: 1.25;
    color: #111;
}

.hero-sub {
    font-size: 22px;
    font-weight: 700;
    color: #333;
    margin-top: 12px;
    line-height: 1.6;
}

.hero-note {
    font-size: 20px;
    line-height: 1.9;
    color: #222;
    margin-top: 18px;
}

.red {
    color: #d62828;
    font-weight: 900;
}

.yellow {
    color: #f4b400;
    font-weight: 900;
}

.green {
    color: #2e7d32;
    font-weight: 900;
}

.card-red {
    background: #fff4f4;
    border-left: 12px solid #d62828;
    border-radius: 18px;
    padding: 20px;
    margin: 14px 0;
    color: #111 !important;
}

.card-yellow {
    background: #fff9e8;
    border-left: 12px solid #f4b400;
    border-radius: 18px;
    padding: 20px;
    margin: 14px 0;
    color: #111 !important;
}

.card-green {
    background: #f2fbf3;
    border-left: 12px solid #2e7d32;
    border-radius: 18px;
    padding: 20px;
    margin: 14px 0;
    color: #111 !important;
}

.card-title {
    font-size: 24px;
    font-weight: 900;
    line-height: 1.5;
    color: #111 !important;
}

.card-body {
    font-size: 17px;
    line-height: 1.8;
    margin-top: 10px;
    color: #222 !important;
}

.story-title {
    font-size: 34px;
    font-weight: 900;
    line-height: 1.5;
    color: #d62828;
    margin-bottom: 14px;
}

.screen-box {
    background: #f7faf7;
    border: 4px solid #2e7d32;
    border-radius: 24px;
    padding: 26px;
    margin: 18px 0 28px 0;
    color: #111 !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.price-box {
    background: #fff3c9;
    border: 4px solid #f4b400;
    border-radius: 22px;
    padding: 28px;
    text-align: center;
    margin-top: 10px;
    color: #111 !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.price-main {
    font-size: 52px;
    font-weight: 900;
    color: #111 !important;
    margin: 12px 0;
}

.cta-box {
    background: #eef9f0;
    border: 4px solid #2e7d32;
    border-radius: 24px;
    padding: 28px;
    margin-top: 22px;
    text-align: center;
    color: #111 !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.small-note {
    color: #d6d6d6;
    font-size: 14px;
    line-height: 1.8;
    margin-top: 12px;
}

.logo-wrap {
    text-align: center;
    margin-bottom: 12px;
}

div[data-testid="stButton"] > button {
    border-radius: 14px;
    font-weight: 800;
    min-height: 52px;
    font-size: 18px;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 0.9rem;
        padding-right: 0.9rem;
    }

    .section-title {
        font-size: 24px;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-sub {
        font-size: 18px;
    }

    .hero-note {
        font-size: 17px;
    }

    .card-title {
        font-size: 20px;
    }

    .card-body {
        font-size: 15px;
    }

    .story-title {
        font-size: 28px;
    }

    .price-main {
        font-size: 40px;
    }
}
</style>
""", unsafe_allow_html=True)

# ===============================
# HERO
# ===============================
left, right = st.columns([1.1, 2])

with left:
    st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)
    if Path("logo.png").exists():
        st.image("logo.png", width=280)
    else:
        st.markdown("## 建設キャッシュレーダー")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">
            忙しい建設社長でも<br>
            資金不足を防ぐ
        </div>
        <div class="hero-sub">
            建設会社のための<br>
            経営ダッシュボード
        </div>
        <div class="hero-note">
            売上と原価を入れるだけで<br>
            <span class="red">資金ショート</span>、
            <span class="yellow">安全ライン</span>、
            <span class="green">必要な売上</span><br>
            が一瞬で見える。
        </div>
    </div>
    """, unsafe_allow_html=True)

st.button("無料で試してみる", use_container_width=True, type="primary", key="cta_top")

# ===============================
# 悩み
# ===============================
st.markdown('<div class="section-title">そんな悩みはありませんか？</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card-red">
        <div class="card-title">仕事はあるのに<br>お金が残らない</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card-yellow">
        <div class="card-title">原価率が高いのに<br>気づくのが遅い</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card-green">
        <div class="card-title">このままで<br>本当に大丈夫か不安</div>
    </div>
    """, unsafe_allow_html=True)

st.button("無料で試してみる", use_container_width=True, type="primary", key="cta_mid")

# ===============================
# 理由
# ===============================
st.markdown("""
<div class="card-red">

<div class="story-title">
原価85%で、<br>
潰れかけました。
</div>

<div class="card-body">

売上はありました。  
仕事もありました。  
忙しかったです。  

でも、お金が残らない。  
家族もいる。借入もある。  

<b>「このままだと終わる」</b>  
本気でそう思いました。  

だから作ったのが、  
<span class="green">建設キャッシュレーダー</span>です。

</div>

</div>
""", unsafe_allow_html=True)

# ===============================
# できること
# ===============================
st.markdown('<div class="section-title">建設キャッシュレーダーでできること</div>', unsafe_allow_html=True)

f1, f2 = st.columns(2)

with f1:
    st.markdown("""
    <div class="card-green">
        <div class="card-title">✅ 資金ショート時期がわかる</div>
        <div class="card-body">
            このままだと何年何月に危ないか見える
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-yellow">
        <div class="card-title">✅ 安全ラインがわかる</div>
        <div class="card-body">
            今の現金で足りているかすぐ分かる
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="card-red">
        <div class="card-title">✅ 必要な売上・利益がわかる</div>
        <div class="card-body">
            あとどれだけ必要か一瞬で見える
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-green">
        <div class="card-title">✅ 現場利益がわかる</div>
        <div class="card-body">
            儲かる現場・危ない現場がわかる
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# 画面イメージ
# ===============================
st.markdown('<div class="section-title">社長が最初に見る画面</div>', unsafe_allow_html=True)

st.markdown("""
<div class="screen-box">
    <div style="font-size:22px; font-weight:900; color:#d62828;">⚠ このままだと</div>
    <div style="font-size:46px; font-weight:900; line-height:1.25; margin-top:10px; color:#111;">
        2027年2月<br>
        資金ショート
    </div>
    <hr style="margin:18px 0;">
    <div style="font-size:28px; font-weight:900; color:#2e7d32;">
        安全にするには
    </div>
    <div style="font-size:30px; font-weight:900; margin-top:12px; color:#111; line-height:1.7;">
        売上 +800万円 / 月<br>
        利益 +120万円 / 月
    </div>
</div>
""", unsafe_allow_html=True)

# ===============================
# 料金
# ===============================
st.markdown('<div class="section-title">料金</div>', unsafe_allow_html=True)

st.markdown("""
<div class="price-box">
    <div style="font-size:22px; font-weight:800; color:#111;">
        建設キャッシュレーダー
    </div>
    <div class="price-main">
        月 9,800円
    </div>
    <div class="card-body">
        忙しい建設社長でも、<br>
        未来の資金が見える。
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("※ 今後レーダーシリーズ展開予定")

# ===============================
# 最後CTA
# ===============================
st.markdown("""
<div class="cta-box">
    <div style="font-size:36px; font-weight:900; line-height:1.5;">
        建設キャッシュレーダーで<br>
        未来の資金を見える化する
    </div>
    <div class="card-body" style="margin-top:14px;">
        忙しいのに儲からない経営から、抜け出すために。
    </div>
</div>
""", unsafe_allow_html=True)

st.button("今すぐ試してみる", use_container_width=True, type="primary", key="cta_bottom")

st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ ホーム画面に追加すればアプリのように使えます。
</div>
""", unsafe_allow_html=True)