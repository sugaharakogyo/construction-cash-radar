import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

APP_URL="https://construction-cash-radar.streamlit.app"
LINE_URL="https://lin.ee/7m28VAs"

st.markdown("""
<style>

.block-container{
max-width:900px;
padding-top:1rem;
}

.stApp{
background:#f3f4f6;
}

/* HERO */

.hero{
background:linear-gradient(135deg,#041126 0%,#0b2f66 40%,#0b7cc8 100%);
border-radius:24px;
padding:28px;
color:white;
margin-bottom:20px;
box-shadow:0 15px 35px rgba(0,0,0,0.25);
}

.hero-badge{
background:#facc15;
color:black;
padding:6px 14px;
border-radius:999px;
font-weight:800;
display:inline-block;
margin-bottom:12px;
}

.hero-appname{
font-size:15px;
font-weight:800;
margin-bottom:10px;
color:#e0ecff;
}

.hero-title{
font-size:52px;
font-weight:900;
line-height:1.1;
margin-bottom:12px;
}

.yellow{color:#facc15;}
.red{color:#ff5c66;}

.hero-sub{
font-size:20px;
font-weight:700;
line-height:1.8;
}

.hero-mini{
margin-top:12px;
color:#dbeafe;
}

/* CTA */

.green-band{
background:#dcfce7;
border:3px solid #16a34a;
border-radius:14px;
padding:10px;
font-weight:800;
text-align:center;
margin:18px 0;
}

/* SECTION */

.section-title{
font-size:28px;
font-weight:900;
margin:30px 0 10px;
}

/* CARDS */

.card{
background:white;
border-radius:14px;
padding:16px;
margin-bottom:12px;
box-shadow:0 2px 6px rgba(0,0,0,0.05);
}

.card-green{
border-left:6px solid #16a34a;
background:#dcfce7;
}

.card-blue{
border-left:6px solid #2563eb;
background:#dbeafe;
}

.card-yellow{
border-left:6px solid #eab308;
background:#fef9c3;
}

/* WARNING */

.warning{
background:#fee2e2;
border-left:6px solid #ef4444;
border-radius:14px;
padding:18px;
margin:20px 0;
}

/* LIST */

.list{
background:white;
border-radius:14px;
padding:16px;
margin-bottom:10px;
box-shadow:0 2px 5px rgba(0,0,0,0.05);
}

/* PRICE */

.price{
background:#dcfce7;
border:4px solid #16a34a;
border-radius:24px;
padding:28px;
text-align:center;
margin:30px 0;
}

.price-title{
font-size:30px;
font-weight:900;
}

.price-main{
font-size:52px;
font-weight:900;
margin:10px 0;
}

/* MOBILE */

@media(max-width:768px){

.hero-title{
font-size:34px;
}

.hero-sub{
font-size:16px;
}

.price-main{
font-size:38px;
}

.section-title{
font-size:22px;
}

}

</style>
""",unsafe_allow_html=True)


# HERO

st.markdown("""
<div class="hero">

<div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>

<div class="hero-appname">建設キャッシュレーダー</div>

<div class="hero-title">
<span class="yellow">黒字でも</span><br>
<span class="red">倒産します</span>
</div>

<div class="hero-sub">

あなたの会社、あと何ヶ月持つか分かりますか？<br><br>

売上・原価・固定費・現金を入れるだけで<br>

資金ショート危険度 と 安全ライン不足額 を<br>

最短30秒で診断します。

</div>

<div class="hero-mini">
会計ソフトでは見えない未来の資金を見える化。<br>
スマホでもすぐ使えます。
</div>

</div>
""",unsafe_allow_html=True)


st.markdown('<div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>',unsafe_allow_html=True)

st.link_button("30秒で無料診断する",APP_URL)


# 3つ

st.markdown('<div class="section-title">30秒でこの3つが分かります</div>',unsafe_allow_html=True)

st.markdown('<div class="card card-green"><b>⏳ あと何ヶ月持つか</b><br>資金ショートまでの目安がすぐ分かります。</div>',unsafe_allow_html=True)

st.markdown('<div class="card card-blue"><b>🛡️ 安全ラインとの差額</b><br>安全に経営するために、あといくら必要か見えます。</div>',unsafe_allow_html=True)

st.markdown('<div class="card card-yellow"><b>📈 今やるべき改善</b><br>売上・原価・固定費のどこを優先して直すべきか整理できます。</div>',unsafe_allow_html=True)


# WARNING

st.markdown("""
<div class="warning">

<b style="font-size:22px">売上があっても、現金が尽きたら終わりです。</b><br><br>

利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。  

建設キャッシュレーダーは、その危険を先に見つけるためのツールです。

</div>
""",unsafe_allow_html=True)


# 悩み

st.markdown('<div class="section-title">こんなお悩みありませんか？</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>売上はあるのに、お金が残らない</b></div>',unsafe_allow_html=True)
st.markdown('<div class="list"><b>原価率が高い現場に後から気づく</b></div>',unsafe_allow_html=True)
st.markdown('<div class="list"><b>このままで本当に大丈夫か不安</b></div>',unsafe_allow_html=True)
st.markdown('<div class="list"><b>銀行や税理士に数字をうまく説明できない</b></div>',unsafe_allow_html=True)


# 向いてる会社

st.markdown('<div class="section-title">このサービスが向いている会社</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>月ごとの資金繰りを先に把握したい会社</b><br>「今月は大丈夫」ではなく、数ヶ月先まで見たい会社に向いています。</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>社長が数字判断を早くしたい会社</b><br>売上・原価・固定費・現金を入れて、すぐ判断したい会社に向いています。</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>税理士・銀行との会話を強くしたい会社</b><br>感覚ではなく、数字で話したい会社に向いています。</div>',unsafe_allow_html=True)


# 使い方

st.markdown('<div class="section-title">使い方はかんたんです</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>STEP1　数字を入れる</b><br>売上・原価・固定費・現金を入力します。</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>STEP2　結果を見る</b><br>危険度・不足額・改善ポイントを確認します。</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>STEP3　LINEで相談</b><br>もっと詳しく使いたい方はLINEへ進みます。</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>STEP4　Pro版で管理</b><br>毎月の資金推移と危険アラートを確認します。</div>',unsafe_allow_html=True)


# 価格

st.markdown("""
<div class="price">

<div class="price-title">社長専用 Proダッシュボード</div>

12ヶ月資金推移・現場利益管理・銀行提出サマリー<br>
利益改善シミュレーターまで使えます。

<div class="price-main">月 9,800円</div>

まずは無料診断。必要ならLINEから申込み。

</div>
""",unsafe_allow_html=True)


st.link_button("30秒で無料診断する",APP_URL)
st.link_button("LINEで問い合わせる",LINE_URL)


st.markdown("""
<div style="text-align:center;color:#6b7280;font-size:14px;margin-top:20px">
※ スマホでも見やすく設計しています。<br>
※ インスタ・QR・チラシからそのまま開けます。
</div>
""",unsafe_allow_html=True)
