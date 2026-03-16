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

# 全体CSS
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
.section-title{
    font-size: 30px;
    font-weight: 900;
    color: #111 !important;
    margin-top: 6px;
    margin-bottom: 8px;
    line-height: 1.4;
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
    .section-title{
        font-size: 22px;
    }
    div.stLinkButton > a{
        font-size: 20px !important;
        padding: 16px 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ヒーロー（独立表示）
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

# 緑帯（独立表示）
st.components.v1.html(
    """
    <style>
      body{
        margin:0;
        background:transparent;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      .green-band{
        background:#ecfdf3;
        border:3px solid #16a34a;
        border-radius:18px;
        padding:14px;
        text-align:center;
        font-size:19px;
        font-weight:900;
        color:#111;
      }
      @media (max-width:768px){
        .green-band{
          font-size:16px;
          padding:12px 14px;
        }
      }
    </style>
    <div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>
    """,
    height=72,
    scrolling=False,
)

st.write("")
st.link_button("30秒で無料診断する", APP_URL)

# 3つ分かること
st.markdown('<div class="section-title">30秒でこの3つが分かります</div>', unsafe_allow_html=True)
st.success("⏳ あと何ヶ月持つか\n\n資金ショートまでの目安がすぐ分かります。")
st.info("🛡️ 安全ラインとの差額\n\n安全に経営するために、あといくら必要か見えます。")
st.warning("📈 今やるべき改善\n\n売上・原価・固定費のどこを優先して直すべきか整理できます。")

# 警告
st.error(
    "**売上があっても、現金が尽きたら終わりです。**\n\n"
    "利益が出ていても、入金サイト・原価率・固定費のズレで突然お金が回らなくなることがあります。"
    "建設キャッシュレーダーは、その危険を先に見つけるためのツールです。"
)

# 悩み
st.markdown('<div class="section-title">こんなお悩みありませんか？</div>', unsafe_allow_html=True)
st.markdown("""
- 売上はあるのに、お金が残らない  
- 原価率が高い現場に後から気づく  
- このままで本当に大丈夫か不安  
- 銀行や税理士に数字をうまく説明できない  
""")

# 向いている会社
st.markdown('<div class="section-title">このサービスが向いている会社</div>', unsafe_allow_html=True)
st.markdown("""
- 月ごとの資金繰りを先に把握したい会社  
- 社長が数字判断を早くしたい会社  
- 税理士や銀行と数字で話したい会社  
""")

# 使い方
st.markdown('<div class="section-title">使い方はかんたんです</div>', unsafe_allow_html=True)
st.info("STEP 1　数字を入れる\n\n売上・原価・固定費・現金を入力します。")
st.info("STEP 2　結果を見る\n\n危険度・不足額・改善ポイントを確認します。")
st.info("STEP 3　LINEで相談\n\nもっと詳しく使いたい方はLINEへ進みます。")
st.info("STEP 4　Pro版で管理\n\n毎月の資金推移と危険アラートを確認します。")

# Pro価格（独立表示）
st.components.v1.html(
    """
    <style>
      body{
        margin:0;
        background:transparent;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      .price-card{
        background: linear-gradient(180deg, #f0fff4 0%, #dcfce7 100%);
        border:5px solid #16a34a;
        border-radius:24px;
        padding:26px 18px;
        box-shadow:0 18px 34px rgba(22,163,74,0.18);
        text-align:center;
      }
      .price-title{
        font-size:36px;
        font-weight:900;
        color:#111;
        margin-bottom:8px;
        line-height:1.3;
      }
      .price-main{
        font-size:56px;
        font-weight:900;
        color:#111;
        line-height:1.1;
        margin:10px 0;
      }
      .price-text{
        font-size:18px;
        line-height:1.8;
        font-weight:800;
        color:#111;
      }
      @media (max-width:768px){
        .price-title{font-size:24px;}
        .price-main{font-size:40px;}
        .price-text{font-size:15px;}
      }
    </style>

    <div class="price-card">
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
    height=260,
    scrolling=False,
)

st.write("")
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
    unsafe_allow_html=True
)
