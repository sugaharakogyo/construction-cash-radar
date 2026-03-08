import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="建設キャッシュレーダー",
    layout="wide"
)

# ===============================
# 関数
# ===============================
def yen(n):
    return f"{int(round(n)):,}円"


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

.cta-link {
    display: block;
    width: 100%;
    text-align: center;
    padding: 16px 18px;
    background: #ff4d4f;
    color: #ffffff !important;
    border-radius: 14px;
    text-decoration: none !important;
    font-weight: 900;
    font-size: 20px;
    margin: 10px 0 18px 0;
    box-sizing: border-box;
}

.cta-link:hover {
    background: #e63b3d;
    color: #ffffff !important;
}

.diagnosis-box {
    background: #f7faf7;
    border: 4px solid #2e7d32;
    border-radius: 24px;
    padding: 26px;
    margin-top: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.result-danger {
    background: #fff4f4;
    border-left: 12px solid #d62828;
    border-radius: 18px;
    padding: 20px;
    margin-top: 18px;
}

.result-warn {
    background: #fff9e8;
    border-left: 12px solid #f4b400;
    border-radius: 18px;
    padding: 20px;
    margin-top: 18px;
}

.result-safe {
    background: #f2fbf3;
    border-left: 12px solid #2e7d32;
    border-radius: 18px;
    padding: 20px;
    margin-top: 18px;
}

.kpi-big {
    font-size: 42px;
    font-weight: 900;
    line-height: 1.3;
}

.kpi-mid {
    font-size: 26px;
    font-weight: 900;
    line-height: 1.5;
}

.badge {
    display: inline-block;
    background: #fff3c9;
    color: #111;
    font-weight: 900;
    padding: 8px 12px;
    border-radius: 999px;
    margin-bottom: 10px;
}

.example-box {
    background: #ffffff;
    border: 3px solid #d62828;
    border-radius: 20px;
    padding: 22px;
    margin-top: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}

.example-title {
    font-size: 24px;
    font-weight: 900;
    color: #d62828;
    margin-bottom: 10px;
}

div[data-testid="stNumberInput"] label {
    font-weight: 800 !important;
}

div[data-testid="stButton"] > button {
    border-radius: 14px;
    font-weight: 800;
    min-height: 52px;
    font-size: 18px;
    background: #ff4d4f;
    color: white;
    border: none;
}

div[data-testid="stButton"] > button:hover {
    background: #e63b3d;
    color: white;
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

    .cta-link {
        font-size: 18px;
        padding: 14px 16px;
    }

    .kpi-big {
        font-size: 34px;
    }

    .kpi-mid {
        font-size: 22px;
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
    <div class="badge">建設会社向け 30秒無料診断</div>
    <div class="hero-title">
        忙しい建設社長でも<br>
        資金不足を防ぐ
    </div>
    <div class="hero-sub">
        売上1億〜5億の建設会社に刺さる<br>
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

st.link_button(
    "無料で試してみる",
    "https://construction-cash-check.streamlit.app",
    use_container_width=True
)

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

st.markdown(
    '<a href="#diagnosis" class="cta-link">30秒無料診断をする</a>',
    unsafe_allow_html=True
)

# ===============================
# 理由
# ===============================
st.markdown('<div class="section-title">このツールを作った理由</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card-red">
<div class="story-title">
原価85%で、<br>
潰れかけました。
</div>
<div class="card-body">
売上はありました。<br>
仕事もありました。<br>
忙しかったです。<br><br>

でも、お金が残らない。<br>
家族もいる。借入もある。<br><br>

<span style="font-weight:900;">「このままだと終わる」</span><br>
本気でそう思いました。<br><br>

だから作ったのが、<br>
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
# 実例
# ===============================
st.markdown('<div class="section-title">実際のイメージ</div>', unsafe_allow_html=True)

st.markdown("""
<div class="example-box">
<div class="example-title">たとえばこんな会社</div>
<div class="card-body">
売上　950万円 / 月<br>
原価　610万円 / 月<br>
固定費　400万円 / 月<br>
現金　680万円<br><br>

これを入れるだけで、<br>
<span class="red">あと何ヶ月で危ないか</span><br>
<span class="green">安全にするには売上がいくら必要か</span><br>
がすぐ分かります。
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
        お試しは6回まで。<br>
        その後は有料で、しっかり業務に使える。
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("※ 今後レーダーシリーズ展開予定")

# ===============================
# CTA
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

st.markdown(
    '<a href="#diagnosis" class="cta-link">今すぐ30秒無料診断をする</a>',
    unsafe_allow_html=True
)

# ===============================
# 30秒無料診断
# ===============================
st.markdown('<div id="diagnosis"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">30秒無料診断</div>', unsafe_allow_html=True)

st.markdown("""
<div class="diagnosis-box">
    <div class="card-title">売上・原価・固定費・現金を入れるだけ</div>
    <div class="card-body">
        いまの会社が安全か、危ないかをすぐに確認できます。
    </div>
</div>
""", unsafe_allow_html=True)

d1, d2 = st.columns(2)

with d1:
    sales = st.number_input("売上（月）", min_value=0, step=100000, value=9500000, key="lp_sales")
    cost = st.number_input("原価（月）", min_value=0, step=100000, value=6100000, key="lp_cost")

with d2:
    fixed_cost = st.number_input("固定費（月）", min_value=0, step=100000, value=4000000, key="lp_fixed")
    cash_on_hand = st.number_input("現在の現金残高", min_value=0, step=100000, value=6800000, key="lp_cash")

tax_rate = 0.30

gross = sales - cost
delta_pre = gross - fixed_cost
tax_est = delta_pre * tax_rate if delta_pre > 0 else 0
delta_after = delta_pre - tax_est

runway_months = None
if delta_after < 0 and abs(delta_after) > 0:
    runway_months = cash_on_hand / abs(delta_after)

safe_cash = fixed_cost * 6
lack_cash = max(0, safe_cash - cash_on_hand)
need_after_per_month = (lack_cash / 6) if lack_cash > 0 else 0

cost_rate_now = (cost / sales) if sales > 0 else 0.65
gross_margin_rate = max(0.01, 1.0 - cost_rate_now)
denom = gross_margin_rate * max(0.01, (1.0 - tax_rate))
need_sales_safe = (need_after_per_month / denom) if denom > 0 else 0

calc = st.button("診断する", use_container_width=True, key="lp_diagnosis_btn")

if calc:
    if runway_months is None:
        st.markdown(f"""
<div class="result-safe">
    <div class="kpi-big">🟢 いまは安全です</div>
    <div class="card-body">
        税後でも黒字で、資金ショートの心配は小さい状態です。<br>
        安全ライン（6ヶ月分の固定費）: <b>{yen(safe_cash)}</b>
    </div>
</div>
""", unsafe_allow_html=True)
    else:
        months_left = max(0, int(runway_months))
        st.markdown(f"""
<div class="result-danger">
    <div class="kpi-big">⚠ 資金ショートまで<br>あと {months_left} ヶ月</div>
    <div class="card-body">
        このままだと毎月 <b>{yen(abs(delta_after))}</b> ずつ現金が減ります。<br>
        年間では <b>{yen(abs(delta_after) * 12)}</b> のキャッシュ減少です。
    </div>
</div>
""", unsafe_allow_html=True)

    if lack_cash > 0:
        st.markdown(f"""
<div class="result-warn">
    <div class="kpi-mid">安全ラインまで不足<br>{yen(lack_cash)}</div>
    <div class="card-body">
        安全にするには、ざっくり<br>
        <b>売上 +{yen(need_sales_safe)} / 月</b><br>
        を目安に見直す必要があります。
    </div>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
<div class="result-safe">
    <div class="kpi-mid">安全ラインクリア</div>
    <div class="card-body">
        現在の現金は、6ヶ月安全ラインを超えています。
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="cta-box">
    <div style="font-size:30px; font-weight:900; line-height:1.5;">
        続きを見るには Pro版へ
    </div>
    <div class="card-body" style="margin-top:10px;">
        現場利益、12ヶ月予測、銀行提出サマリーまで使えます。<br>
        お試しは6回、その後は月9,800円です。
    </div>
</div>
""", unsafe_allow_html=True)

# ===============================
# Pro申込み
# ===============================

st.markdown("## Pro版（月9800円）")

st.markdown("""
Pro版では以下の機能が使えます

・12ヶ月資金推移グラフ  
・現場利益管理  
・銀行提出サマリー  
""")

st.link_button(
"Pro版を申し込む（LINE）",
"https://lin.ee/7m28VAs"
)

st.markdown("## 無料で資金ショート診断")

st.link_button(
"無料診断を試す",
"https://construction-cash-check.streamlit.app"
)


st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ ホーム画面に追加すればアプリのように使えます。
</div>
""", unsafe_allow_html=True)
