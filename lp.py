import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

st.markdown("""
<style>

.block-container{
max-width:900px;
padding-top:1rem;
padding-bottom:3rem;
}

.stApp{
background:#f6f7fb;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
}

/* HERO */

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
color:#111;
font-weight:900;
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
}

.yellow{color:#facc15;}
.red{color:#ef4444;}

.hero-text{
font-size:18px;
line-height:1.9;
margin-bottom:16px;
}

.hero-mini{
font-size:15px;
opacity:0.9;
}

/* chart visual */

.visual{
background:white;
border-radius:20px;
padding:16px;
margin-top:20px;
box-shadow:0 6px 18px rgba(0,0,0,0.1);
}

.chart{
display:flex;
align-items:flex-end;
gap:6px;
height:120px;
margin-top:10px;
}

.bar{
width:16px;
background:#3b82f6;
border-radius:6px 6px 0 0;
}

.bar.red{
background:#ef4444;
}

.card-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:8px;
margin-top:10px;
}

.card{
background:#f1f5f9;
border-radius:10px;
padding:8px;
font-size:14px;
}

.card strong{
font-size:16px;
}

/* counter */

.counter-box{
background:#e9f7ee;
border:3px solid #16a34a;
border-radius:18px;
padding:16px;
margin-bottom:20px;
text-align:center;
font-size:18px;
font-weight:900;
}

/* buttons */

div.stLinkButton>a{
background:#16a34a;
color:white;
border-radius:16px;
font-weight:900;
font-size:22px;
padding:18px;
text-align:center;
display:block;
text-decoration:none;
}

/* cards */

.section{
background:white;
border-radius:20px;
padding:22px;
margin-top:20px;
box-shadow:0 6px 18px rgba(0,0,0,0.05);
}

.section h2{
font-size:28px;
margin-bottom:12px;
}

.section ul{
font-size:18px;
line-height:2;
}

/* flow */

.flow{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:10px;
margin-top:12px;
}

.flowbox{
border:2px solid #dbeafe;
border-radius:16px;
padding:12px;
text-align:center;
}

.step{
background:#1d4ed8;
color:white;
font-size:12px;
padding:4px 8px;
border-radius:999px;
display:inline-block;
margin-bottom:6px;
}

/* price */

.price{
background:#e9f7ee;
border:4px solid #16a34a;
border-radius:24px;
padding:24px;
text-align:center;
margin-top:24px;
}

.price h3{
font-size:40px;
margin-bottom:8px;
}

.price-main{
font-size:52px;
font-weight:900;
}

.footer{
font-size:14px;
text-align:center;
margin-top:20px;
color:#666;
}

@media(max-width:700px){

.hero-title{font-size:32px;}

.flow{
grid-template-columns:1fr;
}

}

</style>
""", unsafe_allow_html=True)

# HERO

st.markdown("""
<div class="hero">

<div class="hero-badge">
建設会社専用 / 最短30秒 無料診断
</div>

<div class="hero-title">
建設会社は<br>
<span class="yellow">黒字でも</span><br>
<span class="red">倒産します</span>
</div>

<div class="hero-text">
<b>あなたの会社、あと何ヶ月持つか分かりますか？</b><br><br>

売上・原価・固定費・現金を入れるだけで<br>

<b>資金ショート危険度</b> と  
<b>安全ライン不足額</b> を  
最短30秒で診断します。
</div>

<div class="hero-mini">
会計ソフトでは見えない未来の資金を見える化
</div>

<div class="visual">

<strong>建設キャッシュレーダー</strong>

<div class="chart">

<div class="bar" style="height:90px"></div>
<div class="bar" style="height:70px"></div>
<div class="bar" style="height:55px"></div>
<div class="bar" style="height:35px"></div>
<div class="bar red" style="height:20px"></div>
<div class="bar red" style="height:12px"></div>

</div>

<div class="card-grid">

<div class="card">
資金ショートまで<br>
<strong>あと5ヶ月</strong>
</div>

<div class="card">
安全ライン不足<br>
<strong>780万円</strong>
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="counter-box">
建設会社専用 / 資金ショート危険度を無料診断
</div>
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)

# section

st.markdown("""
<div class="section">
<h2>30秒でこの3つが分かります</h2>

<ul>
<li>あと何ヶ月で資金ショートする可能性があるか</li>
<li>安全ラインまでいくら不足しているか</li>
<li>今やるべき改善ポイント</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
<h2>こんなお悩みありませんか？</h2>

<ul>
<li>売上はあるのにお金が残らない</li>
<li>原価率が高い現場に後から気づく</li>
<li>このままで本当に大丈夫か不安</li>
<li>銀行や税理士に数字を説明できない</li>
</ul>

</div>
""", unsafe_allow_html=True)

# flow

st.markdown("""
<div class="section">

<h2>使い方</h2>

<div class="flow">

<div class="flowbox">
<div class="step">STEP1</div><br>
数字入力
</div>

<div class="flowbox">
<div class="step">STEP2</div><br>
診断結果
</div>

<div class="flowbox">
<div class="step">STEP3</div><br>
改善確認
</div>

<div class="flowbox">
<div class="step">STEP4</div><br>
Pro利用
</div>

</div>

</div>
""", unsafe_allow_html=True)

# price

st.markdown("""
<div class="price">

<h3>Pro版</h3>

12ヶ月資金推移  
現場利益管理  
銀行提出サマリー  
利益改善シミュレーター  

<div class="price-main">
月 9,800円
</div>

</div>
""", unsafe_allow_html=True)

st.link_button("無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

st.markdown("""
<div class="footer">

スマホでも利用できます<br>
QRコード・SNSからそのまま診断可能

</div>
""", unsafe_allow_html=True)
