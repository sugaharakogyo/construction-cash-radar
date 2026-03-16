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

st.markdown("""
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
    background: linear-gradient(180deg, #f8fbff 0%, #f6f7fb 100%);
}

.section-card{
    background:#ffffff;
    border:1px solid #edf2f7;
    border-radius:22px;
    padding:22px 18px;
    box-shadow:0 10px 24px rgba(15,23,42,0.05);
    margin-top:18px;
}

.section-title{
    font-size:30px;
    font-weight:900;
    color:#111 !important;
    margin-bottom:12px;
    line-height:1.4;
}

.green-band{
    background:#ecfdf3;
    border:3px solid #16a34a;
    border-radius:18px;
    padding:14px 16px;
    text-align:center;
    font-size:18px;
    font-weight:900;
    color:#111 !important;
    margin-top:18px;
    margin-bottom:18px;
}

.points-stack{
    display:flex;
    flex-direction:column;
    gap:14px;
}

.point-box{
    border-radius:18px;
    padding:18px 16px;
    font-weight:700;
}

.point-box h3{
    margin:0 0 8px 0;
    font-size:24px;
    line-height:1.4;
}

.point-box p{
    margin:0;
    font-size:17px;
    line-height:1.8;
}

.point-green{
    background:#dcfce7;
    color:#166534;
}

.point-blue{
    background:#dbeafe;
    color:#1d4ed8;
}

.point-yellow{
    background:#fef9c3;
    color:#a16207;
}

.warning-box{
    background:#fee2e2;
    border:2px solid #ef4444;
    border-radius:20px;
    padding:20px 16px;
    margin-top:18px;
}

.warning-box h3{
    margin:0 0 10px 0;
    font-size:22px;
    font-weight:900;
    color:#dc2626;
}

.warning-box p{
    margin:0;
    font-size:17px;
    line-height:1.85;
    color:#b91c1c;
    font-weight:700;
}

.simple-list{
    display:flex;
    flex-direction:column;
    gap:12px;
}

.simple-item{
    background:#f8fafc;
    border:1px solid #e5e7eb;
    border-radius:16px;
    padding:16px 14px;
}

.simple-item b{
    display:block;
    font-size:19px;
    color:#111827;
    margin-bottom:6px;
}

.simple-item span{
    font-size:15px;
    line-height:1.7;
    color:#475569;
    font-weight:700;
}

.price-box{
    background: linear-gradient(180deg, #f0fff4 0%, #dcfce7 100%);
    border:5px solid #16a34a;
    border-radius:24px;
    padding:24px 18px;
    box-shadow:0 18px 34px rgba(22,163,74,0.18);
    text-align:center;
    margin-top:22px;
}

.price-title{
    font-size:34px;
    font-weight:900;
    color:#111 !important;
    line-height:1.3;
    margin-bottom:10px;
}

.price-main{
    font-size:54px;
    font-weight:900;
    color:#111 !important;
    line-height:1.1;
    margin:10px 0;
}

.price-text{
    font-size:18px;
    line-height:1.8;
    font-weight:800;
    color:#111 !important;
}

.faq-box{
    background:#ffffff;
    border:1px solid #e5e7eb;
    border-radius:16px;
    padding:16px 14px;
    margin-top:12px;
}

.faq-q{
    font-size:18px;
    font-weight:900;
    color:#111827;
    margin-bottom:6px;
}

.faq-a{
    font-size:15px;
    line-height:1.8;
    color:#475569;
    font-weight:700;
}

.small-note{
    text-align:center;
    color:#666 !important;
    font-size:14px;
    line-height:1.8;
    margin-top:18px;
}

div.stLinkButton > a{
    background: linear-gradient(180deg, #18b24c 0%, #16a34a 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 22px !important;
    padding: 18px 14px !important;
    text-align: center !important;
    display: block !important;
    text-decoration: none !important;
    box-shadow: 0 12px 22px rgba(22,163,74,0.22) !important;
}

div.stLinkButton > a:hover{
    background: linear-gradient(180deg, #16a34a 0%, #15803d 100%) !important;
    color: white !important;
}

@media (max-width: 768px){
    .section-card{
        padding:18px 14px;
    }

    .section-title{
        font-size:22px;
    }

    .point-box h3{
        font-size:19px;
    }

    .point-box p{
        font-size:15px;
    }

    .warning-box h3{
        font-size:20px;
    }

    .warning-box p{
        font-size:15px;
    }

    .simple-item b{
        font-size:17px;
    }

    .simple-item span{
        font-size:14px;
    }

    .price-title{
        font-size:24px;
    }

    .price-main{
        font-size:40px;
    }

    .price-text{
        font-size:15px;
    }

    .faq-q{
        font-size:16px;
    }

    .faq-a{
        font-size:14px;
    }

    .green-band{
        font-size:16px;
        padding:12px 14px;
    }

    div.stLinkButton > a{
        font-size:20px !important;
        padding:16px 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# 青ヒーロー（スマホ優先で独立表示）
st.components.v1.html(
    """
    <style>
      body{
        margin:0;
        background:transparent;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      .hero{
        background: linear-gradient(135deg, #020617 0%, #0b3b74 42%, #0284c7 100%);
        border-radius: 28px;
        padding: 28px 22px 24px 22px;
        box-shadow: 0 24px 52px rgba(0,0,0,0.28);
        color: white;
      }
      .badge{
        display:inline-block;
        background:#facc15;
        color:#111;
        font-weight:900;
        font-size:14px;
        border-radius:999px;
        padding:8px 14px;
        margin-bottom:16px;
      }
      .hero-title{
        font-size:54px;
        line-height:1.06;
        font-weight:900;
        margin:0 0 16px 0;
        color:#ffffff;
      }
      .yellow{ color:#facc15; }
      .red{ color:#ff4d4f; }
      .hero-sub{
        font-size:21px;
        line-height:1.85;
        font-weight:800;
        color:#ffffff;
        margin-bottom:14px;
      }
      .hero-mini{
        font-size:16px;
        line-height:1.8;
        font-weight:700;
        color:#dbeafe;
      }
      @media (max-width:768px){
        .hero{
          padding:24px 18px 20px 18px;
          border-radius:24px;
        }
        .hero-title{
          font-size:34px;
        }
        .hero-sub{
          font-size:16px;
          line-height:1.8;
        }
        .hero-mini{
          font-size:14px;
        }
      }
    </style>

    <div class="hero">
      <div class="badge">建設会社専用 / 最短30秒 無料診断</div>

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
    height=430,
    scrolling=False,
)

st.markdown(
    '<div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>',
    unsafe_allow_html=True
)

st.link_button("30秒で無料診断する", APP_URL)

# 3つ分かること（縦積み）
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)
st.markdown("""
<div class="points-stack">
    <div class="point-box point-green">
        <h3>⏳ あと何ヶ月持つか</h3>
        <p>資金ショートまでの目安がすぐ分かります。</p>
    </div>

    <div class="point-box point-blue">
        <h3>🛡️ 安全ラインとの差額</h3>
        <p>安全に経営するために、あといくら必要か見えます。</p>
    </div>

    <div class="point-box point-yellow">
        <h3>📈 今やるべき改善</h3>
        <p>売上・原価・固定費のどこを優先して直すべきか整理できます。</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 警告
st.markdown("""
<div class="warning-box">
    <h3>売上があっても、現金が尽きたら終わりです。</h3>
    <p>
    利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。<br>
    建設キャッシュレーダーは、その危険を先に見つけるためのツールです。
    </p>
</div>
""", unsafe_allow_html=True)

# 悩み
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)
st.markdown("""
<div class="simple-list">
    <div class="simple-item">
        <b>売上はあるのに、お金が残らない</b>
        <span>黒字なのに不安が消えない会社向けです。</span>
    </div>
    <div class="simple-item">
        <b>原価率が高い現場に後から気づく</b>
        <span>現場の数字が見えにくい会社向けです。</span>
    </div>
    <div class="simple-item">
        <b>このままで本当に大丈夫か不安</b>
        <span>未来の資金が読めず、判断に迷う会社向けです。</span>
    </div>
    <div class="simple-item">
        <b>銀行や税理士に数字をうまく説明できない</b>
        <span>見える化して説明材料を持ちたい会社向けです。</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 追加1：向いている会社
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">このサービスが向いている会社</div>', unsafe_allow_html=True)
st.markdown("""
<div class="simple-list">
    <div class="simple-item">
        <b>月ごとの資金繰りを先に把握したい会社</b>
        <span>「今月は大丈夫」ではなく、数ヶ月先まで見たい会社に向いています。</span>
    </div>
    <div class="simple-item">
        <b>社長が数字判断を早くしたい会社</b>
        <span>売上・原価・固定費・現金を入れて、すぐ判断したい会社に向いています。</span>
    </div>
    <div class="simple-item">
        <b>税理士・銀行との会話を強くしたい会社</b>
        <span>感覚ではなく、数字で話したい会社に向いています。</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 使い方
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">使い方はかんたんです</div>', unsafe_allow_html=True)
st.markdown("""
<div class="simple-list">
    <div class="simple-item">
        <b>STEP 1　数字を入れる</b>
        <span>売上・原価・固定費・現金を入力します。</span>
    </div>
    <div class="simple-item">
        <b>STEP 2　結果を見る</b>
        <span>危険度・不足額・改善ポイントを確認します。</span>
    </div>
    <div class="simple-item">
        <b>STEP 3　LINEで相談</b>
        <span>もっと詳しく使いたい方はLINEへ進みます。</span>
    </div>
    <div class="simple-item">
        <b>STEP 4　Pro版で管理</b>
        <span>毎月の資金推移と危険アラートを確認します。</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Pro
st.markdown("""
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
""", unsafe_allow_html=True)

st.link_button("30秒で無料診断する", APP_URL)
st.link_button("LINEで問い合わせる", LINE_URL)

# 追加2：FAQ
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">よくある質問</div>', unsafe_allow_html=True)
st.markdown("""
<div class="faq-box">
    <div class="faq-q">Q. まずは無料で使えますか？</div>
    <div class="faq-a">はい。まずは無料診断で危険度と安全ライン不足額を確認できます。</div>
</div>

<div class="faq-box">
    <div class="faq-q">Q. 入力は難しいですか？</div>
    <div class="faq-a">売上・原価・固定費・現金など、社長が分かる数字から始められるように作っています。</div>
</div>

<div class="faq-box">
    <div class="faq-q">Q. どんな会社に向いていますか？</div>
    <div class="faq-a">資金繰りを先に読みたい建設会社、数字判断を早くしたい社長に向いています。</div>
</div>

<div class="faq-box">
    <div class="faq-q">Q. Pro版では何が増えますか？</div>
    <div class="faq-a">12ヶ月資金推移、現場利益管理、銀行提出サマリー、利益改善シミュレーターまで使えます。</div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="small-note">※ スマホでも見やすく設計しています。<br>※ インスタ・QR・チラシからそのまま開けます。</div>',
    unsafe_allow_html=True
)
