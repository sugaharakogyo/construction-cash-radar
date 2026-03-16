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
    max-width: 960px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at 10% 10%, rgba(59,130,246,0.08), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(239,68,68,0.08), transparent 20%),
        linear-gradient(180deg, #f8fbff 0%, #f6f7fb 100%);
}

/* 全体共通 */
h1,h2,h3,p,div,span{
    box-sizing: border-box;
}

/* ヒーロー */
.hero{
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #081224 0%, #0c3d73 45%, #0a7ac2 100%);
    border-radius: 30px;
    padding: 34px 26px 28px 26px;
    color: #fff;
    margin-bottom: 28px;
    box-shadow: 0 20px 45px rgba(2, 24, 58, 0.25);
    border: 1px solid rgba(255,255,255,0.08);
}

.hero:before{
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    background: rgba(250,204,21,0.12);
    border-radius: 50%;
    top: -90px;
    right: -70px;
}

.hero:after{
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    background: rgba(239,68,68,0.12);
    border-radius: 50%;
    bottom: -100px;
    left: -70px;
}

.hero-inner{
    position: relative;
    z-index: 2;
}

.hero-badge{
    display: inline-block;
    background: #facc15;
    color: #111 !important;
    font-weight: 900;
    font-size: 14px;
    border-radius: 999px;
    padding: 9px 16px;
    margin-bottom: 16px;
    box-shadow: 0 10px 20px rgba(250,204,21,0.22);
}

.hero-grid{
    display: grid;
    grid-template-columns: 1.2fr 0.95fr;
    gap: 20px;
    align-items: center;
}

.hero-title{
    font-size: 50px;
    line-height: 1.08;
    font-weight: 900;
    margin: 0 0 18px 0;
    letter-spacing: 0.5px;
    color: #fff !important;
}

.yellow{
    color: #facc15 !important;
}

.red{
    color: #ff4d4f !important;
}

.hero-sub{
    font-size: 20px;
    line-height: 1.85;
    font-weight: 800;
    margin-bottom: 14px;
    color: #fff !important;
}

.hero-mini{
    font-size: 15px;
    line-height: 1.9;
    color: #dbeafe !important;
    font-weight: 700;
}

.hero-highlight{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 12px 14px;
    margin-top: 18px;
    font-size: 15px;
    line-height: 1.8;
    color: #fff !important;
    font-weight: 800;
}

/* 右のビジュアル */
.visual-wrap{
    background: linear-gradient(180deg, rgba(255,255,255,0.16), rgba(255,255,255,0.08));
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 26px;
    padding: 14px;
    backdrop-filter: blur(3px);
}

.visual{
    background: #ffffff;
    border-radius: 22px;
    padding: 16px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.16);
}

.visual-top{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
}

.visual-logo{
    font-size: 15px;
    font-weight: 900;
    color: #0f172a !important;
}

.visual-pill{
    font-size: 12px;
    font-weight: 900;
    color: #b91c1c !important;
    background: #fee2e2;
    border-radius: 999px;
    padding: 6px 10px;
}

.visual-chart{
    height: 126px;
    display: flex;
    align-items: end;
    gap: 9px;
    padding: 6px 4px 10px 4px;
    border-bottom: 2px solid #e5e7eb;
    margin-bottom: 14px;
}

.bar{
    width: 18px;
    border-radius: 8px 8px 0 0;
    background: linear-gradient(180deg, #3b82f6 0%, #2563eb 100%);
    box-shadow: 0 6px 10px rgba(37,99,235,0.18);
}

.bar.red{
    background: linear-gradient(180deg, #fb7185 0%, #dc2626 100%);
    box-shadow: 0 6px 10px rgba(220,38,38,0.16);
}

.visual-cards{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}

.v-card{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 12px;
}

.v-label{
    font-size: 12px;
    font-weight: 800;
    color: #64748b !important;
    margin-bottom: 5px;
}

.v-value{
    font-size: 21px;
    font-weight: 900;
    color: #111827 !important;
}

/* 緑帯 */
.counter-box{
    background: linear-gradient(180deg, #eefcf3 0%, #e7f9ed 100%);
    border: 3px solid #16a34a;
    border-radius: 20px;
    padding: 16px;
    margin-top: 2px;
    margin-bottom: 20px;
    text-align: center;
    font-size: 20px;
    font-weight: 900;
    color: #111 !important;
    box-shadow: 0 8px 16px rgba(22,163,74,0.08);
}

/* ボタン */
div.stLinkButton > a{
    background: linear-gradient(180deg, #18b24c 0%, #16a34a 100%) !important;
    color: #fff !important;
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
    color: #fff !important;
}

/* セクション */
.section-card{
    background: #fff;
    border-radius: 24px;
    padding: 24px 22px;
    margin-top: 20px;
    box-shadow: 0 10px 24px rgba(15,23,42,0.05);
    border: 1px solid #eef2f7;
}

.section-title{
    font-size: 31px;
    line-height: 1.4;
    font-weight: 900;
    color: #111 !important;
    margin-bottom: 14px;
}

.section-text{
    font-size: 18px;
    line-height: 1.9;
    color: #1f2937 !important;
}

/* 3つの特徴 */
.point-grid{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-top: 6px;
}

.point-box{
    background: linear-gradient(180deg, #fcfdff 0%, #f3f8ff 100%);
    border: 2px solid #dbeafe;
    border-radius: 18px;
    padding: 18px 16px;
    text-align: center;
}

.point-icon{
    font-size: 32px;
    margin-bottom: 10px;
}

.point-title{
    font-size: 20px;
    font-weight: 900;
    color: #111827 !important;
    margin-bottom: 8px;
}

.point-text{
    font-size: 15px;
    line-height: 1.8;
    color: #475569 !important;
    font-weight: 700;
}

/* 警告 */
.warning-box{
    background: linear-gradient(180deg, #fff3f3 0%, #fff1f2 100%);
    border: 3px solid #ef4444;
    border-radius: 22px;
    padding: 22px;
    margin-top: 30px;
    box-shadow: 0 10px 20px rgba(239,68,68,0.08);
}

.warning-title{
    font-size: 25px;
    font-weight: 900;
    color: #b91c1c !important;
    margin-bottom: 10px;
}

.warning-text{
    font-size: 18px;
    line-height: 1.9;
    color: #4c0519 !important;
    font-weight: 700;
}

/* リスト */
.problem-list{
    margin: 0;
    padding-left: 22px;
    font-size: 18px;
    line-height: 2;
    color: #1f2937 !important;
    font-weight: 700;
}

.problem-list li{
    margin-bottom: 8px;
}

/* flow */
.flow{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 12px;
}

.flowbox{
    background: #fff;
    border: 2px solid #dbeafe;
    border-radius: 18px;
    padding: 16px 12px;
    text-align: center;
}

.step{
    display: inline-block;
    background: #1d4ed8;
    color: #fff !important;
    font-size: 12px;
    font-weight: 900;
    border-radius: 999px;
    padding: 4px 9px;
    margin-bottom: 10px;
}

.flow-title{
    font-size: 18px;
    font-weight: 900;
    color: #111827 !important;
    margin-bottom: 6px;
}

.flow-text{
    font-size: 14px;
    line-height: 1.7;
    color: #475569 !important;
    font-weight: 700;
}

/* price */
.price-box{
    background: linear-gradient(180deg, #eefcf3 0%, #e8f9ee 100%);
    border: 4px solid #16a34a;
    border-radius: 28px;
    padding: 28px 20px;
    margin-top: 26px;
    text-align: center;
    box-shadow: 0 16px 30px rgba(22,163,74,0.12);
}

.price-title{
    font-size: 42px;
    font-weight: 900;
    color: #111 !important;
    margin-bottom: 10px;
}

.price-text{
    font-size: 18px;
    line-height: 1.9;
    color: #111 !important;
    font-weight: 800;
}

.price-main{
    font-size: 56px;
    font-weight: 900;
    color: #111 !important;
    margin: 10px 0;
}

/* note */
.small-note{
    color: #666 !important;
    font-size: 14px;
    line-height: 1.8;
    margin-top: 22px;
    text-align: center;
    font-weight: 700;
}

/* モバイル */
@media(max-width:700px){
    .block-container{
        padding-top: 0.7rem;
        padding-bottom: 2rem;
    }

    .hero{
        padding: 26px 18px;
    }

    .hero-grid{
        grid-template-columns: 1fr;
    }

    .hero-title{
        font-size: 36px;
    }

    .hero-sub{
        font-size: 17px;
    }

    .hero-mini{
        font-size: 14px;
    }

    .section-title{
        font-size: 25px;
    }

    .section-text,
    .problem-list{
        font-size: 16px;
    }

    .point-grid{
        grid-template-columns: 1fr;
    }

    .flow{
        grid-template-columns: 1fr;
    }

    .visual-cards{
        grid-template-columns: 1fr;
    }

    .price-main{
        font-size: 42px;
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

st.markdown(
    """
<div class="hero">
  <div class="hero-inner">
    <div class="hero-badge">建設会社専用 / 最短30秒 無料診断</div>

    <div class="hero-grid">
      <div>
        <div class="hero-title">
          建設会社は<br>
          <span class="yellow">黒字でも</span><br>
          <span class="red">倒産します</span>
        </div>

        <div class="hero-sub">
          <b>あなたの会社、あと何ヶ月持つか分かりますか？</b><br><br>
          売上・原価・固定費・現金を入れるだけで、<br>
          <b>資金ショート危険度</b> と <b>安全ライン不足額</b> を<br>
          最短30秒で診断します。
        </div>

        <div class="hero-mini">
          会計ソフトでは見えない未来の資金を見える化。<br>
          スマホでもすぐ使えます。
        </div>

        <div class="hero-highlight">
          「利益は出ているのに、お金が残らない」<br>
          そんな建設会社のための、未来の資金診断ツールです。
        </div>
      </div>

      <div class="visual-wrap">
        <div class="visual">
          <div class="visual-top">
            <div class="visual-logo">建設キャッシュレーダー</div>
            <div class="visual-pill">危険度 高</div>
          </div>

          <div class="visual-chart">
            <div class="bar" style="height:92px;"></div>
            <div class="bar" style="height:74px;"></div>
            <div class="bar" style="height:58px;"></div>
            <div class="bar" style="height:40px;"></div>
            <div class="bar red" style="height:22px;"></div>
            <div class="bar red" style="height:14px;"></div>
          </div>

          <div class="visual-cards">
            <div class="v-card">
              <div class="v-label">資金ショートまで</div>
              <div class="v-value">あと5ヶ月</div>
            </div>
            <div class="v-card">
              <div class="v-label">安全ライン不足</div>
              <div class="v-value">780万円</div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="counter-box">
建設会社専用 / 資金ショート危険度を無料診断
</div>
""",
    unsafe_allow_html=True,
)

st.link_button("30秒で無料診断する", APP_URL)

st.markdown(
    """
<div class="section-card">
  <div class="section-title">30秒でこの3つが分かります</div>
  <div class="point-grid">
    <div class="point-box">
      <div class="point-icon">⏳</div>
      <div class="point-title">あと何ヶ月持つか</div>
      <div class="point-text">資金ショートまでの目安がすぐ分かります。</div>
    </div>
    <div class="point-box">
      <div class="point-icon">🛡️</div>
      <div class="point-title">安全ラインとの差額</div>
      <div class="point-text">安全に経営するために、あといくら必要か見えます。</div>
    </div>
    <div class="point-box">
      <div class="point-icon">📈</div>
      <div class="point-title">今やるべき改善</div>
      <div class="point-text">売上・原価・固定費のどこを直すべきか整理できます。</div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="warning-box">
  <div class="warning-title">売上があっても、現金が尽きたら終わりです。</div>
  <div class="warning-text">
    利益が出ていても、入金サイト・原価率・固定費のズレで<br>
    <b>突然お金が回らなくなる</b>ことがあります。<br>
    建設キャッシュレーダーは、その危険を先に見つけるためのツールです。
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section-card">
  <div class="section-title">こんなお悩みありませんか？</div>
  <ul class="problem-list">
    <li>売上はあるのに、お金が残らない</li>
    <li>原価率が高い現場に後から気づく</li>
    <li>このままで本当に大丈夫か不安</li>
    <li>銀行や税理士に数字をうまく説明できない</li>
  </ul>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section-card">
  <div class="section-title">使い方はかんたんです</div>

  <div class="flow">
    <div class="flowbox">
      <div class="step">STEP 1</div>
      <div class="flow-title">数字を入れる</div>
      <div class="flow-text">売上・原価・固定費・現金を入力</div>
    </div>

    <div class="flowbox">
      <div class="step">STEP 2</div>
      <div class="flow-title">結果を見る</div>
      <div class="flow-text">危険度・不足額・改善ポイントを確認</div>
    </div>

    <div class="flowbox">
      <div class="step">STEP 3</div>
      <div class="flow-title">LINEで相談</div>
      <div class="flow-text">もっと詳しく使いたい方はLINEへ</div>
    </div>

    <div class="flowbox">
      <div class="step">STEP 4</div>
      <div class="flow-title">Pro版で管理</div>
      <div class="flow-text">毎月の資金推移と危険アラートを確認</div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

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

st.markdown(
    """
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ インスタ・QR・チラシからそのまま開けます。
</div>
""",
    unsafe_allow_html=True,
)
