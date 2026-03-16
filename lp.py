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
padding-top:0.5rem;
}

.stApp{
background:linear-gradient(180deg,#f6f8fc 0%,#eef2f8 100%);
}

/* hero */

.hero{
background:linear-gradient(135deg,#041126 0%,#0b2f66 40%,#0b7cc8 100%);
border-radius:28px;
padding:28px;
color:white;
box-shadow:0 20px 40px rgba(0,0,0,0.25);
margin-bottom:20px;
}

.hero-badge{
display:inline-block;
background:#facc15;
color:black;
padding:8px 14px;
border-radius:999px;
font-weight:800;
font-size:14px;
margin-bottom:10px;
}

.hero-appname{
font-size:15px;
font-weight:800;
margin-bottom:12px;
color:#e0ecff;
}

.hero-title{
font-size:56px;
font-weight:900;
line-height:1.05;
margin-bottom:16px;
}

.yellow{color:#facc15;}
.red{color:#ff5c66;}

.hero-sub{
font-size:20px;
line-height:1.8;
font-weight:700;
margin-bottom:12px;
}

.hero-mini{
font-size:16px;
line-height:1.7;
color:#dbeafe;
}

/* band */

.green-band{
background:#ecfdf5;
border:3px solid #16a34a;
border-radius:16px;
padding:12px;
text-align:center;
font-weight:800;
margin:20px 0;
}

/* cards */

.section-title{
font-size:28px;
font-weight:900;
margin:20px 0 10px 0;
}

.info-card{
border-radius:16px;
padding:18px;
margin-bottom:12px;
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

.warning-box{
background:#fee2e2;
border-left:6px solid #ef4444;
border-radius:16px;
padding:18px;
margin:18px 0;
}

.list-card{
background:white;
border:1px solid #e5e7eb;
border-radius:16px;
padding:16px;
margin-bottom:10px;
}

.price-box{
background:linear-gradient(180deg,#ecfdf5,#dcfce7);
border:4px solid #16a34a;
border-radius:24px;
padding:24px;
text-align:center;
margin:20px 0;
}

.price-title{
font-size:34px;
font-weight:900;
margin-bottom:8px;
}

.price-main{
font-size:52px;
font-weight:900;
margin:10px 0;
}

.small-note{
text-align:center;
font-size:14px;
color:#6b7280;
margin-top:20px;
}

/* mobile */

@media(max-width:768px){

.hero-title{font-size:34px;}

.hero-sub{font-size:16px;}

.price-main{font-size:40px;}

.section-title{font-size:22px;}

}

</style>
""",unsafe_allow_html=True)


# hero

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

st.markdown("""
<div class="info-card card-green">
<b>⏳ あと何ヶ月持つか</b><br>
資金ショートまでの目安がすぐ分かります。
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="info-card card-blue">
<b>🛡️ 安全ラインとの差額</b><br>
安全に経営するために、あといくら必要か見えます。
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="info-card card-yellow">
<b>📈 今やるべき改善</b><br>
売上・原価・固定費のどこを優先して直すべきか整理できます。
</div>
""",unsafe_allow_html=True)


# warning

st.markdown("""
<div class="warning-box">

<b style="font-size:22px">売上があっても、現金が尽きたら終わりです。</b><br><br>

利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。  

建設キャッシュレーダーは、その危険を先に見つけるためのツールです。

</div>
""",unsafe_allow_html=True)


# 悩み

st.markdown('<div class="section-title">こんなお悩みありませんか？</div>',unsafe_allow_html=True)

st.markdown("""
<div class="list-card">
<b>売上はあるのに、お金が残らない</b>
</div>

<div class="list-card">
<b>原価率が高い現場に後から気づく</b>
</div>

<div class="list-card">
<b>このままで本当に大丈夫か不安</b>
</div>

<div class="list-card">
<b>銀行や税理士に数字を説明できない</b>
</div>
""",unsafe_allow_html=True)


# Pro

st.markdown("""
<div class="price-box">

<div class="price-title">社長専用 Proダッシュボード</div>

12ヶ月資金推移・現場利益管理・銀行提出サマリー・<br>
利益改善シミュレーターまで使えます。

<div class="price-main">月 9,800円</div>

まずは無料診断。必要ならLINEから申込み。

</div>
""",unsafe_allow_html=True)

st.link_button("30秒で無料診断する",APP_URL)
st.link_button("LINEで問い合わせる",LINE_URL)


# footer

st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ インスタ・QR・チラシからそのまま開けます。
</div>
""",unsafe_allow_html=True)
