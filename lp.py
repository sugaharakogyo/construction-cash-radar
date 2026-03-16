import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

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

html = """
<style>
.block-container{
    max-width: 920px;
    padding-top: 0.8rem;
    padding-bottom: 3rem;
}
.stApp{
    background: linear-gradient(180deg, #f8fbff 0%, #f6f7fb 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a{
    text-decoration: none;
}
.lp-wrap{
    display: flex;
    flex-direction: column;
    gap: 18px;
}
.hero{
    background: linear-gradient(135deg, #020617 0%, #0b3b74 42%, #0284c7 100%);
    border-radius: 30px;
    padding: 28px 24px;
    box-shadow: 0 24px 52px rgba(0,0,0,0.30);
    color: white;
}
.badge{
    display: inline-block;
    background: #facc15;
    color: #111 !important;
    font-weight: 900;
    font-size: 14px;
    padding: 8px 14px;
    border-radius: 999px;
    margin-bottom: 16px;
}
.hero-grid{
    display: grid;
    grid-template-columns: 1.15fr 0.95fr;
    gap: 20px;
    align-items: center;
}
.hero-title{
    font-size: 52px;
    line-height: 1.06;
    font-weight: 900;
    margin: 0 0 16px 0;
    color: #fff !important;
}
.hero-sub{
    font-size: 20px;
    line-height: 1.8;
    font-weight: 800;
    color: #fff !important;
    margin-bottom: 14px;
}
.hero-mini{
    font-size: 15px;
    line-height: 1.8;
    font-weight: 700;
    color: #dbeafe !important;
    margin-bottom: 14px;
}
.yellow{
    color: #facc15 !important;
}
.red{
    color: #ff4d4f !important;
}
.hero-note{
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 12px 14px;
    font-size: 15px;
    line-height: 1.7;
    font-weight: 700;
    color: #fff !important;
}
.green-band{
    background: #ecfdf3;
    border: 3px solid #16a34a;
    border-radius: 18px;
    padding: 14px;
    text-align: center;
    font-size: 19px;
    font-weight: 900;
    color: #111 !important;
}
.visual{
    background: #ffffff;
    border-radius: 22px;
    padding: 16px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.16);
}
.visual-top{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
}
.visual-logo{
    font-size: 15px;
    font-weight: 900;
    color: #0f172a !important;
}
.visual-pill{
    background: #fee2e2;
    color: #b91c1c !important;
    font-size: 12px;
    font-weight: 900;
    padding: 6px 10px;
    border-radius: 999px;
}
.visual-cards{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 12px;
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
    margin-bottom: 4px;
}
.v-value{
    font-size: 22px;
    font-weight: 900;
    color: #111827 !important;
}
.chart{
    height: 120px;
    display: flex;
    align-items: end;
    gap: 8px;
    padding: 4px 4px 10px 4px;
    border-bottom: 2px solid #e5e7eb;
}
.bar{
    width: 18px;
    border-radius: 8px 8px 0 0;
    background: linear-gradient(180deg, #3b82f6 0%, #2563eb 100%);
}
.bar.red{
    background: linear-gradient(180deg, #fb7185 0%, #dc2626 100%);
}
.primary-btn{
    display: block;
    width: 100%;
    text-align: center;
    background: linear-gradient(180deg, #18b24c 0%, #16a34a 100%);
    color: #fff !important;
    font-weight: 900;
    font-size: 22px;
    padding: 18px 14px;
    border-radius: 18px;
    box-shadow: 0 12px 22px rgba(22,163,74,0.22);
}
.secondary-btn{
    display: block;
    width: 100%;
    text-align: center;
    background: linear-gradient(180deg, #15a34a 0%, #15803d 100%);
    color: #fff !important;
    font-weight: 900;
    font-size: 22px;
    padding: 18px 14px;
    border-radius: 18px;
    box-shadow: 0 12px 22px rgba(22,163,74,0.20);
}
.card{
    background: #fff;
    border: 1px solid #edf2f7;
    border-radius: 22px;
    padding: 22px 20px;
    box-shadow: 0 10px 24px rgba(15,23,42,0.05);
}
.card-title{
    font-size: 30px;
    font-weight: 900;
    color: #111 !important;
    margin-bottom: 12px;
}
.points{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
}
.point{
    background: linear-gradient(180deg, #fcfdff 0%, #f3f8ff 100%);
    border: 2px solid #dbeafe;
    border-radius: 18px;
    padding: 18px 16px;
}
.point-emoji{
    font-size: 30px;
    margin-bottom: 8px;
}
.point-title{
    font-size: 20px;
    font-weight: 900;
    color: #111827 !important;
    margin-bottom: 8px;
}
.point-text{
    font-size: 15px;
    line-height: 1.75;
    font-weight: 700;
    color: #475569 !important;
}
.warning{
    background: linear-gradient(180deg, #fff3f3 0%, #fff1f2 100%);
    border: 3px solid #ef4444;
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 10px 20px rgba(239,68,68,0.08);
}
.warning-title{
    font-size: 25px;
    font-weight: 900;
    color: #b91c1c !important;
    margin-bottom: 8px;
}
.warning-text{
    font-size: 18px;
    line-height: 1.85;
    font-weight: 700;
    color: #4c0519 !important;
}
.list{
    margin: 0;
    padding-left: 22px;
}
.list li{
    font-size: 18px;
    line-height: 2;
    font-weight: 700;
    color: #1f2937 !important;
}
.flow{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}
.flow-item{
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
    padding: 5px 9px;
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
    font-weight: 700;
    color: #475569 !important;
}
.price{
    background: linear-gradient(180deg, #f0fff4 0%, #dcfce7 100%);
    border: 5px solid #16a34a;
    border-radius: 26px;
    padding: 26px 20px;
    text-align: center;
    box-shadow: 0 18px 34px rgba(22,163,74,0.18);
}
.price-title{
    font-size: 40px;
    font-weight: 900;
    color: #111 !important;
    margin-bottom: 10px;
}
.price-text{
    font-size: 18px;
    line-height: 1.85;
    font-weight: 800;
    color: #111 !important;
}
.price-main{
    font-size: 56px;
    font-weight: 900;
    color: #111 !important;
    margin: 10px 0;
}
.footer{
    text-align: center;
    color: #666 !important;
    font-size: 14px;
    line-height: 1.8;
    margin-top: 4px;
}
.cta-stack{
    display: flex;
    flex-direction: column;
    gap: 12px;
}
@media (max-width: 700px){
    .hero-grid{
        grid-template-columns: 1fr;
    }
    .hero-title{
        font-size: 38px;
    }
    .hero-sub{
        font-size: 17px;
    }
    .card-title{
        font-size: 24px;
    }
    .points{
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
    .primary-btn,.secondary-btn{
        font-size: 20px;
        padding: 16px 12px;
    }
}
</style>

<div class="lp-wrap">

  <div class="hero">
    <div class="badge">建設会社専用 / 最短30秒 無料診断</div>

    <div class="hero-grid">
      <div>
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

        <div class="hero-note">
          「利益は出ているのに、お金が残らない」<br>
          そんな建設会社のための、未来の資金診断ツールです。
        </div>
      </div>

      <div class="visual">
        <div class="visual-top">
          <div class="visual-logo">建設キャッシュレーダー</div>
          <div class="visual-pill">危険度 高</div>
        </div>

        <div class="chart">
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

  <div class="green-band">建設会社専用 / 資金ショート危険度を無料診断</div>

  <a class="primary-btn" href="APP_URL" target="_self">30秒で無料診断する</a>

  <div class="card">
    <div class="card-title">30秒でこの3つが分かります</div>
    <div class="points">
      <div class="point">
        <div class="point-emoji">⏳</div>
        <div class="point-title">あと何ヶ月持つか</div>
        <div class="point-text">資金ショートまでの目安がすぐ分かります。</div>
      </div>
      <div class="point">
        <div class="point-emoji">🛡️</div>
        <div class="point-title">安全ラインとの差額</div>
        <div class="point-text">安全に経営するために、あといくら必要か見えます。</div>
      </div>
      <div class="point">
        <div class="point-emoji">📈</div>
        <div class="point-title">今やるべき改善</div>
        <div class="point-text">売上・原価・固定費のどこを直すべきか整理できます。</div>
      </div>
    </div>
  </div>

  <div class="warning">
    <div class="warning-title">売上があっても、現金が尽きたら終わりです。</div>
    <div class="warning-text">
      利益が出ていても、入金サイト・原価率・固定費のズレで<br>
      突然お金が回らなくなることがあります。<br>
      建設キャッシュレーダーは、その危険を先に見つけるためのツールです。
    </div>
  </div>

  <div class="card">
    <div class="card-title">こんなお悩みありませんか？</div>
    <ul class="list">
      <li>売上はあるのに、お金が残らない</li>
      <li>原価率が高い現場に後から気づく</li>
      <li>このままで本当に大丈夫か不安</li>
      <li>銀行や税理士に数字をうまく説明できない</li>
    </ul>
  </div>

  <div class="card">
    <div class="card-title">使い方はかんたんです</div>
    <div class="flow">
      <div class="flow-item">
        <div class="step">STEP 1</div>
        <div class="flow-title">数字を入れる</div>
        <div class="flow-text">売上・原価・固定費・現金を入力</div>
      </div>
      <div class="flow-item">
        <div class="step">STEP 2</div>
        <div class="flow-title">結果を見る</div>
        <div class="flow-text">危険度・不足額・改善ポイントを確認</div>
      </div>
      <div class="flow-item">
        <div class="step">STEP 3</div>
        <div class="flow-title">LINEで相談</div>
        <div class="flow-text">もっと詳しく使いたい方はLINEへ</div>
      </div>
      <div class="flow-item">
        <div class="step">STEP 4</div>
        <div class="flow-title">Pro版で管理</div>
        <div class="flow-text">毎月の資金推移と危険アラートを確認</div>
      </div>
    </div>
  </div>

  <div class="price">
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

  <div class="cta-stack">
    <a class="primary-btn" href="APP_URL" target="_self">30秒で無料診断する</a>
    <a class="secondary-btn" href="LINE_URL" target="_blank">LINEで問い合わせる</a>
  </div>

  <div class="footer">
    ※ スマホでも見やすく設計しています。<br>
    ※ インスタ・QR・チラシからそのまま開けます。
  </div>

</div>
"""

html = html.replace("APP_URL", APP_URL).replace("LINE_URL", LINE_URL)

st.markdown(html, unsafe_allow_html=True)
