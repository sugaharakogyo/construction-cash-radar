import streamlit as st

st.components.v1.html(
    """
    <style>
      .hero{
        background: linear-gradient(135deg, #020617 0%, #0b3b74 42%, #0284c7 100%);
        border-radius: 30px;
        padding: 28px 24px;
        box-shadow: 0 24px 52px rgba(0,0,0,0.30);
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      .badge{
        display: inline-block;
        background: #facc15;
        color: #111;
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
        color: #fff;
      }
      .hero-sub{
        font-size: 20px;
        line-height: 1.8;
        font-weight: 800;
        color: #fff;
        margin-bottom: 14px;
      }
      .hero-mini{
        font-size: 15px;
        line-height: 1.8;
        font-weight: 700;
        color: #dbeafe;
        margin-bottom: 14px;
      }
      .yellow{ color: #facc15; }
      .red{ color: #ff4d4f; }
      .hero-note{
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 16px;
        padding: 12px 14px;
        font-size: 15px;
        line-height: 1.7;
        font-weight: 700;
        color: #fff;
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
        color: #0f172a;
      }
      .visual-pill{
        background: #fee2e2;
        color: #b91c1c;
        font-size: 12px;
        font-weight: 900;
        padding: 6px 10px;
        border-radius: 999px;
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
        color: #64748b;
        margin-bottom: 4px;
      }
      .v-value{
        font-size: 22px;
        font-weight: 900;
        color: #111827;
      }
      @media (max-width: 700px){
        .hero-grid{ grid-template-columns: 1fr; }
        .hero-title{ font-size: 38px; }
        .hero-sub{ font-size: 17px; }
        .visual-cards{ grid-template-columns: 1fr; }
      }
    </style>

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
    """,
    height=520,
    scrolling=False,
)


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
