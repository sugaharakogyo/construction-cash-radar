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
font-family:sans-serif;
}

/* HERO */

.hero{
background:linear-gradient(135deg,#041126 0%,#0b2f66 40%,#0b7cc8 100%);
border-radius:24px;
padding:28px;
color:white;
margin-bottom:20px;
box-shadow:0 20px 40px rgba(0,0,0,0.25);
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

.hero-app{
font-weight:800;
margin-bottom:10px;
color:#dbeafe;
}

.hero-title{
font-size:52px;
font-weight:900;
line-height:1.1;
margin-bottom:14px;
}

.yellow{color:#facc15;}
.red{color:#ff5c66;}

.hero-sub{
font-size:20px;
line-height:1.8;
font-weight:700;
}

.hero-mini{
margin-top:12px;
color:#dbeafe;
font-size:16px;
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
color:#111827;
}

/* section */

.section-title{
font-size:28px;
font-weight:900;
margin:30px 0 10px;
color:#111827;
}

/* cards */

.card{
background:white;
border-radius:14px;
padding:18px;
margin-bottom:12px;
box-shadow:0 3px 6px rgba(0,0,0,0.05);
color:#111827;
}

.card-green{
background:#dcfce7;
border-left:6px solid #16a34a;
}

.card-blue{
background:#dbeafe;
border-left:6px solid #2563eb;
}

.card-yellow{
background:#fef9c3;
border-left:6px solid #eab308;
}

/* warning */

.warning{
background:#fee2e2;
border-left:6px solid #ef4444;
border-radius:14px;
padding:20px;
margin:24px 0;
color:#111827;
}

/* list */

.list{
background:white;
border-radius:14px;
padding:16px;
margin-bottom:10px;
box-shadow:0 2px 5px rgba(0,0,0,0.05);
color:#111827;
}

/* result sample */

.sample{
background:#eef2ff;
border-left:6px solid #4f46e5;
border-radius:14px;
padding:20px;
margin:25px 0;
color:#111827;
}

/* price */

.price{
background:#bbf7d0;
border:4px solid #16a34a;
border-radius:24px;
padding:28px;
text-align:center;
margin:30px 0;
color:#111827;
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

/* mobile */

@media(max-width:768px){

.hero-title{font-size:34px;}

.hero-sub{font-size:16px;}

.section-title{font-size:22px;}

.price-main{font-size:40px;}

}

</style>
""",unsafe_allow_html=True)

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
<b>安全ライン不足額</b> が  

30秒で分かります。

</div>

<div class="hero-mini">

会計ソフトでは見えない  
未来の資金繰りを見える化。

</div>

</div>
""",unsafe_allow_html=True)

st.markdown('<div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>',unsafe_allow_html=True)

st.link_button("30秒で無料診断する",APP_URL)

# 3つ

st.markdown('<div class="section-title">30秒でこの3つが分かります</div>',unsafe_allow_html=True)

st.markdown('<div class="card card-green"><b>資金ショートまでの期間</b><br>あと何ヶ月持つか分かります。</div>',unsafe_allow_html=True)

st.markdown('<div class="card card-blue"><b>安全ラインとの差額</b><br>あといくら必要か見えます。</div>',unsafe_allow_html=True)

st.markdown('<div class="card card-yellow"><b>改善ポイント</b><br>どこを直せばいいか分かります。</div>',unsafe_allow_html=True)

# WARNING

st.markdown("""
<div class="warning">

<b style="font-size:22px">売上があっても、現金が尽きたら終わりです。</b><br><br>

利益が出ていても  

入金サイト・原価率・固定費のズレで  

突然お金が回らなくなることがあります。

</div>
""",unsafe_allow_html=True)

# sample result

st.markdown('<div class="section-title">診断結果のイメージ</div>',unsafe_allow_html=True)

st.markdown("""
<div class="sample">

売上　900万円<br>
原価　620万円<br>
固定費　260万円<br>
現金　180万円<br><br>

<b>診断結果</b><br><br>

資金ショートまで  
<b>3.4ヶ月</b><br><br>

安全ライン  
<b>あと380万円不足</b><br><br>

改善ポイント  
<b>原価率 −3%</b>

</div>
""",unsafe_allow_html=True)

# 悩み

st.markdown('<div class="section-title">こんなお悩みありませんか？</div>',unsafe_allow_html=True)

st.markdown('<div class="list">売上はあるのにお金が残らない</div>',unsafe_allow_html=True)
st.markdown('<div class="list">原価率が高い現場に後から気づく</div>',unsafe_allow_html=True)
st.markdown('<div class="list">このままで本当に大丈夫か不安</div>',unsafe_allow_html=True)
st.markdown('<div class="list">銀行や税理士に数字を説明できない</div>',unsafe_allow_html=True)

# 向いてる会社

st.markdown('<div class="section-title">このサービスが向いている会社</div>',unsafe_allow_html=True)

st.markdown('<div class="list">月ごとの資金繰りを先に把握したい会社</div>',unsafe_allow_html=True)
st.markdown('<div class="list">社長が数字判断を早くしたい会社</div>',unsafe_allow_html=True)
st.markdown('<div class="list">税理士・銀行との会話を強くしたい会社</div>',unsafe_allow_html=True)

# 使い方

st.markdown('<div class="section-title">使い方はかんたんです</div>',unsafe_allow_html=True)

st.markdown('<div class="list"><b>STEP1</b> 数字を入力</div>',unsafe_allow_html=True)
st.markdown('<div class="list"><b>STEP2</b> 診断結果を見る</div>',unsafe_allow_html=True)
st.markdown('<div class="list"><b>STEP3</b> LINEで相談</div>',unsafe_allow_html=True)
st.markdown('<div class="list"><b>STEP4</b> Pro版で管理</div>',unsafe_allow_html=True)

# price

st.markdown("""
<div class="price">

<div class="price-title">社長専用 Proダッシュボード</div>

12ヶ月資金推移<br>
現場利益管理<br>
銀行提出サマリー<br>
利益改善シミュレーター

<div class="price-main">月 9,800円</div>

まずは無料診断

</div>
""",unsafe_allow_html=True)

st.link_button("30秒で無料診断する",APP_URL)
st.link_button("LINEで問い合わせる",LINE_URL)
