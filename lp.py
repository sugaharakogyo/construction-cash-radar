import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

# Google Analytics
st.components.v1.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-V96H2R41TL"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-V96H2R41TL');
    </script>
    """,
    height=0,
)

st.markdown(
    """
<style>
.block-container{
    max-width: 860px;
    padding-top: 0.8rem;
    padding-bottom: 3rem;
}

html, body, [class*="css"]{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background: linear-gradient(180deg, #f7f8fc 0%, #f3f5fa 100%);
}

/* 共通見出し */
.section-title{
    font-size: 30px;
    font-weight: 900;
    color: #111827 !important;
    line-height: 1.35;
    margin: 10px 0 12px 0;
}

/* ヒーロー */
.hero{
    width: 100%;
    box-sizing: border-box;
    background: linear-gradient(135deg, #041126 0%, #0a2e63 45%, #0a78c9 100%);
    border-radius: 28px;
    padding: 26px 22px 24px 22px;
    box-shadow: 0 18px 40px rgba(5, 18, 38, 0.25);
    color: white;
    overflow: hidden;
    margin-bottom: 18px;
}

.hero-badge{
    display: inline-block;
    background: #facc15;
    color: #111111 !important;
    font-size: 14px;
    font-weight: 900;
    padding: 8px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
}

.hero-appname{
    font-size: 14px;
    font-weight: 800;
    color: #dbeafe !important;
    margin-bottom: 12px;
    letter-spacing: 0.2px;
}

.hero-title{
    font-size: 54px;
    line-height: 1.05;
    font-weight: 900;
    margin: 0 0 18px 0;
    color: white !important;
}

.yellow{ color: #facc15 !important; }
.red{ color: #ff5c66 !important; }

.hero-sub{
    font-size: 21px;
    line-height: 1.85;
    font-weight: 800;
    color: white !important;
    margin-bottom: 12px;
}

.hero-mini{
    font-size: 16px;
    line-height: 1.8;
    font-weight: 700;
    color: #e0ecff !important;
}

/* 緑帯 */
.green-band{
    width: 100%;
    box-sizing: border-box;
    background: #eef9f1;
    border: 3px solid #16a34a;
    border-radius: 18px;
    padding: 14px 16px;
    text-align: center;
    font-size: 19px;
    font-weight: 900;
    color: #111827 !important;
    margin: 18px 0 18px 0;
}

/* ボタン */
div.stLinkButton > a{
    background: linear-gradient(180deg, #1fb44f 0%, #16a34a 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 22px !important;
    padding: 18px 14px !important;
    text-align: center !important;
    display: block !important;
    text-decoration: none !important;
    box-shadow: 0 12px 22px rgba(22,163,74,0.20) !important;
}

div.stLinkButton > a:hover{
    background: linear-gradient(180deg, #18a848 0%, #15803d 100%) !important;
    color: #ffffff !important;
}

/* 説明カード */
.info-card{
    width: 100%;
    box-sizing: border-box;
    border-radius: 18px;
    padding: 18px 16px;
    margin: 0 0 14px 0;
}

.info-card h3{
    margin: 0 0 8px 0;
    font-size: 24px;
    line-height: 1.4;
    font-weight: 900;
}

.info-card p{
    margin: 0;
    font-size: 17px;
    line-height: 1.8;
    font-weight: 700;
}

.card-green{
    background: #dcf4e3;
    border-left: 6px solid #16a34a;
}
.card-green h3, .card-green p{
    color: #166534 !important;
}

.card-blue{
    background: #dbeafe;
    border-left: 6px solid #2563eb;
}
.card-blue h3, .card-blue p{
    color: #1d4ed8 !important;
}

.card-yellow{
    background: #fff7cc;
    border-left: 6px solid #d97706;
}
.card-yellow h3, .card-yellow p{
    color: #9a6700 !important;
}

.warning-box{
    width: 100%;
    box-sizing: border-box;
    background: #ffe3e3;
    border-left: 6px solid #ef4444;
    border-radius: 18px;
    padding: 18px 16px;
    margin: 18px 0;
}

.warning-box h3{
    margin: 0 0 10px 0;
    font-size: 24px;
    font-weight: 900;
    color: #dc2626 !important;
    line-height: 1.4;
}

.warning-box p{
    margin: 0;
    font-size: 17px;
    line-height: 1.85;
    font-weight: 700;
    color: #b91c1c !important;
}

/* リスト風カード */
.list-card{
    width: 100%;
    box-sizing: border-box;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 16px 14px;
    margin: 0 0 12px 0;
}

.list-card b{
    display: block;
    font-size: 19px;
    color: #111827 !important;
    margin-bottom: 6px;
}

.list-card span{
    display: block;
    font-size: 15px;
    line-height: 1.75;
    color: #475569 !important;
    font-weight: 700;
}

/* Pro */
.price-box{
    width: 100%;
    box-sizing: border-box;
    background: linear-gradient(180deg, #effcf2 0%, #dcfce7 100%);
    border: 5px solid #16a34a;
    border-radius: 24px;
    padding: 24px 18px;
    text-align: center;
    box-shadow: 0 14px 28px rgba(22,163,74,0.14);
    margin: 22px 0 18px 0;
}

.price-title{
    font-size: 36px;
    font-weight: 900;
    color: #111827 !important;
    line-height: 1.35;
    margin-bottom: 10px;
}

.price-text{
    font-size: 18px;
    line-height: 1.85;
    font-weight: 800;
    color: #111827 !important;
}

.price-main{
    font-size: 56px;
    line-height: 1.1;
    font-weight: 900;
    color: #111827 !important;
    margin: 12px 0;
}

/* フッター */
.small-note{
    text-align: center;
    color: #6b7280 !important;
    font-size: 14px;
    line-height: 1.8;
    margin-top: 18px;
}

/* スマホ */
@media (max-width: 768px){
    .hero{
        padding: 22px 18px 20px 18px;
        border-radius: 22px;
    }

    .hero-badge{
        font-size: 13px;
        padding: 8px 12px;
    }

    .hero-appname{
        font-size: 13px;
    }

    .hero-title{
        font-size: 34px;
        line-height: 1.08;
        margin-bottom: 14px;
    }

    .hero-sub{
        font-size: 16px;
        line-height: 1.8;
    }

    .hero-mini{
        font-size: 14px;
        line-height: 1.75;
    }

    .green-band{
        font-size: 16px;
        padding: 12px 14px;
    }

    .section-title{
        font-size: 22px;
    }

    .info-card{
        padding: 16px 14px;
    }

    .info-card h3{
        font-size: 18px;
    }

    .info-card p{
        font-size: 15px;
    }

    .warning-box h3{
        font-size: 20px;
    }

    .warning-box p{
        font-size: 15px;
    }

    .list-card b{
        font-size: 17px;
    }

    .list-card span{
        font-size: 14px;
    }

    .price-title{
        font-size: 24px;
    }

    .price-main{
        font-size: 42px;
    }

    .price-text{
        font-size: 15px;
    }

    div.stLinkButton > a{
        font-size: 20px !important;
        padding: 16px 12px !important;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# ヒーロー
st.markdown(
    """
<div class="hero">
    <div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>
    <div class="hero-appname">建設キャッシュレーダー</div>

    <div class="hero-title">
        <span class="yellow">黒字でも</span><br>
        <span class="red">倒産します</span>
    </div>

    <div class="hero-sub">
        あなたの会社、あと何ヶ月持つか分かりますか？<br><br>
        売上・原価・固定費・現金を入れるだけで、<br>
        資金ショート危険度 と 安全ライン不足額 を<br>
        最短30秒で診断します。
    </div>

    <div class="hero-mini">
        会計ソフトでは見えない未来の資金を見える化。<br>
        スマホでもすぐ使えます。
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>',
    unsafe_allow_html=True,
)

st.link_button("30秒で無料診断する", APP_URL)

# 3つ
st.markdown('<div class="section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="info-card card-green">
    <h3>⏳ あと何ヶ月持つか</h3>
    <p>資金ショートまでの目安がすぐ分かります。</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card card-blue">
    <h3>🛡️ 安全ラインとの差額</h3>
    <p>安全に経営するために、あといくら必要か見えます。</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="info-card card-yellow">
    <h3>📈 今やるべき改善</h3>
    <p>売上・原価・固定費のどこを優先して直すべきか整理できます。</p>
</div>
""",
    unsafe_allow_html=True,
)

# 警告
st.markdown(
    """
<div class="warning-box">
    <h3>売上があっても、現金が尽きたら終わりです。</h3>
    <p>
        利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。<br>
        建設キャッシュレーダーは、その危険を先に見つけるためのツールです。
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# 悩み
st.markdown('<div class="section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="list-card">
    <b>売上はあるのに、お金が残らない</b>
    <span>黒字なのに不安が消えない会社向けです。</span>
</div>
<div class="list-card">
    <b>原価率が高い現場に後から気づく</b>
    <span>現場の数字が見えにくい会社向けです。</span>
</div>
<div class="list-card">
    <b>このままで本当に大丈夫か不安</b>
    <span>未来の資金が読めず、判断に迷う会社向けです。</span>
</div>
<div class="list-card">
    <b>銀行や税理士に数字をうまく説明できない</b>
    <span>見える化して説明材料を持ちたい会社向けです。</span>
</div>
""",
    unsafe_allow_html=True,
)

# 向いている会社
st.markdown('<div class="section-title">このサービスが向いている会社</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="list-card">
    <b>月ごとの資金繰りを先に把握したい会社</b>
    <span>「今月は大丈夫」ではなく、数ヶ月先まで見たい会社に向いています。</span>
</div>
<div class="list-card">
    <b>社長が数字判断を早くしたい会社</b>
    <span>売上・原価・固定費・現金を入れて、すぐ判断したい会社に向いています。</span>
</div>
<div class="list-card">
    <b>税理士・銀行との会話を強くしたい会社</b>
    <span>感覚ではなく、数字で話したい会社に向いています。</span>
</div>
""",
    unsafe_allow_html=True,
)

# 使い方
st.markdown('<div class="section-title">使い方はかんたんです</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="list-card">
    <b>STEP 1　数字を入れる</b>
    <span>売上・原価・固定費・現金を入力します。</span>
</div>
<div class="list-card">
    <b>STEP 2　結果を見る</b>
    <span>危険度・不足額・改善ポイントを確認します。</span>
</div>
<div class="list-card">
    <b>STEP 3　LINEで相談</b>
    <span>もっと詳しく使いたい方はLINEへ進みます。</span>
</div>
<div class="list-card">
    <b>STEP 4　Pro版で管理</b>
    <span>毎月の資金推移と危険アラートを確認します。</span>
</div>
""",
    unsafe_allow_html=True,
)

# Pro
st.markdown(
    """
<div class="price-box">
    <div class="price-title">社長専用 Proダッシュボード</div>
    <div class="price-text">
        12ヶ月資金推移・現場利益管理・銀行提出サマリー・<br>
        利益改善シミュレーターまで使えます。
    </div>
    <div class="price-main">月 9,800円</div>
    <div class="price-text">
        まずは無料診断。必要ならLINEから申込み。
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.link_button("30秒で無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

# FAQ
st.markdown('<div class="section-title">よくある質問</div>', unsafe_allow_html=True)

with st.expander("Q. まずは無料で使えますか？"):
    st.write("はい。まずは無料診断で危険度と安全ライン不足額を確認できます。")

with st.expander("Q. 入力は難しいですか？"):
    st.write("売上・原価・固定費・現金など、社長が分かる数字から始められるように作っています。")

with st.expander("Q. どんな会社に向いていますか？"):
    st.write("資金繰りを先に読みたい建設会社、数字判断を早くしたい社長に向いています。")

with st.expander("Q. Pro版では何が増えますか？"):
    st.write("12ヶ月資金推移、現場利益管理、銀行提出サマリー、利益改善シミュレーターまで使えます。")

st.markdown(
    '<div class="small-note">※ スマホでも見やすく設計しています。<br>※ インスタ・QR・チラシからそのまま開けます。</div>',
    unsafe_allow_html=True,
)
