import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app/"
LINE_URL = "https://lin.ee/7m28VAs"
STRIPE_URL = "https://buy.stripe.com/6oU28rarietE5gM6m87N600"

TOKUSHO_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"
TERMS_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"
PRIVACY_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"


def render(html: str) -> None:
    st.markdown(html, unsafe_allow_html=True)


render("""
<style>
.block-container{
    max-width:1040px;
    padding-top:0.8rem;
    padding-bottom:3rem;
}
.stApp{
    background:
      radial-gradient(circle at top right, rgba(37,99,235,0.05), transparent 22%),
      linear-gradient(180deg,#f8fbff 0%,#f4f7fb 45%,#eef3f8 100%);
    color:#0f172a;
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
}
.kcr-section-label{
    display:inline-block;
    background:#e0f2fe;
    color:#0369a1;
    font-size:12px;
    font-weight:900;
    letter-spacing:.05em;
    padding:7px 12px;
    border-radius:999px;
    margin-bottom:12px;
}
.kcr-section-title{
    font-size:38px;
    font-weight:900;
    color:#0f172a;
    line-height:1.28;
    letter-spacing:-0.03em;
    margin:0 0 10px 0;
}
.kcr-section-sub{
    font-size:17px;
    line-height:1.95;
    color:#475569;
    font-weight:600;
    margin-bottom:20px;
}
.kcr-hero{
    position:relative;
    overflow:hidden;
    background:linear-gradient(135deg,#ffffff 0%,#eff6ff 55%,#dbeafe 100%);
    border:1px solid #dbeafe;
    border-radius:30px;
    padding:34px 30px;
    box-shadow:0 20px 48px rgba(15,23,42,0.06);
    margin-bottom:18px;
}
.kcr-hero:before{
    content:"";
    position:absolute;
    top:-80px;
    right:-50px;
    width:220px;
    height:220px;
    background:rgba(37,99,235,0.08);
    border-radius:999px;
}
.kcr-hero:after{
    content:"";
    position:absolute;
    bottom:-80px;
    left:-60px;
    width:180px;
    height:180px;
    background:rgba(14,165,233,0.08);
    border-radius:999px;
}
.kcr-hero-inner{
    position:relative;
    z-index:2;
}
.kcr-badge{
    display:inline-block;
    background:linear-gradient(135deg,#2563eb 0%,#1d4ed8 100%);
    color:#fff;
    font-size:13px;
    font-weight:900;
    padding:8px 14px;
    border-radius:999px;
    margin-bottom:16px;
    box-shadow:0 10px 20px rgba(37,99,235,0.20);
}
.kcr-app-name{
    color:#1e40af;
    font-size:15px;
    font-weight:900;
    letter-spacing:.04em;
    margin-bottom:10px;
}
.kcr-hero-title{
    font-size:56px;
    line-height:1.08;
    font-weight:900;
    letter-spacing:-0.04em;
    color:#0f172a;
    margin-bottom:16px;
}
.kcr-hero-title .blue{color:#1d4ed8;}
.kcr-hero-title .dark{color:#0f172a;}
.kcr-hero-sub{
    font-size:19px;
    line-height:1.95;
    color:#334155;
    font-weight:700;
    margin-bottom:16px;
}
.kcr-hero-sub b{color:#1d4ed8;}
.kcr-hero-points{
    background:rgba(255,255,255,0.88);
    border:1px solid #dbeafe;
    border-radius:18px;
    padding:18px 20px;
    color:#0f172a;
    font-size:16px;
    line-height:1.95;
    font-weight:700;
}
.kcr-cta-primary,.kcr-cta-secondary,.kcr-cta-line{
    display:block;
    width:100%;
    text-align:center;
    text-decoration:none !important;
    padding:17px 18px;
    border-radius:16px;
    font-weight:900;
    margin:10px 0;
}
.kcr-cta-primary{
    background:linear-gradient(135deg,#2563eb 0%,#1d4ed8 100%);
    color:#fff !important;
    font-size:19px;
    box-shadow:0 14px 28px rgba(37,99,235,0.24);
}
.kcr-cta-secondary{
    background:#fff;
    color:#0f172a !important;
    font-size:17px;
    border:2px solid #cbd5e1;
    box-shadow:0 10px 22px rgba(15,23,42,0.05);
}
.kcr-cta-line{
    background:linear-gradient(135deg,#16a34a 0%,#15803d 100%);
    color:#fff !important;
    font-size:17px;
    box-shadow:0 12px 24px rgba(22,163,74,0.20);
}
.kcr-cta-subnote{
    text-align:center;
    color:#64748b;
    font-size:14px;
    font-weight:700;
    margin-bottom:18px;
}
.kcr-grid-3{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:16px;
    margin-top:10px;
}
.kcr-box{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:20px;
    padding:24px 20px;
    box-shadow:0 10px 24px rgba(15,23,42,0.05);
}
.kcr-num{
    color:#2563eb;
    font-size:14px;
    font-weight:900;
    margin-bottom:10px;
}
.kcr-box-title{
    font-size:23px;
    font-weight:900;
    line-height:1.45;
    color:#0f172a;
    margin-bottom:10px;
}
.kcr-box-text{
    color:#475569;
    font-size:16px;
    line-height:1.9;
    font-weight:600;
}
.kcr-alert{
    background:linear-gradient(180deg,#fff1f2 0%,#ffe4e6 100%);
    border:1px solid #fecdd3;
    border-left:6px solid #ef4444;
    border-radius:20px;
    padding:24px 22px;
    margin:28px 0 10px;
    box-shadow:0 10px 24px rgba(239,68,68,0.08);
}
.kcr-alert-title{
    font-size:30px;
    font-weight:900;
    color:#111827;
    line-height:1.5;
    margin-bottom:10px;
}
.kcr-alert-text{
    color:#374151;
    font-size:17px;
    line-height:1.95;
    font-weight:700;
}
.kcr-sample{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:24px;
    padding:24px;
    box-shadow:0 14px 30px rgba(15,23,42,0.05);
}
.kcr-sample-top{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
}
.kcr-sample-input{
    background:#f8fafc;
    border:1px solid #e2e8f0;
    border-radius:18px;
    padding:20px;
    font-size:16px;
    line-height:2;
    color:#334155;
    font-weight:800;
}
.kcr-sample-result{
    background:linear-gradient(135deg,#eff6ff 0%,#eef2ff 100%);
    border:1px solid #c7d2fe;
    border-radius:18px;
    padding:20px;
    font-size:16px;
    line-height:2;
    color:#0f172a;
    font-weight:800;
}
.kcr-sample-result .big{
    font-size:30px;
    line-height:1.4;
    font-weight:900;
    color:#1d4ed8;
}
.kcr-list{
    display:grid;
    gap:12px;
}
.kcr-list-item{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:17px 18px;
    box-shadow:0 8px 18px rgba(15,23,42,0.04);
    color:#0f172a;
    font-size:17px;
    font-weight:800;
    line-height:1.8;
}
.kcr-faq-wrap{
    display:grid;
    gap:12px;
}
.kcr-faq-item{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:20px;
    box-shadow:0 8px 18px rgba(15,23,42,0.04);
}
.kcr-faq-q{
    font-size:18px;
    font-weight:900;
    color:#0f172a;
    margin-bottom:8px;
    line-height:1.7;
}
.kcr-faq-a{
    color:#475569;
    font-size:16px;
    line-height:1.95;
    font-weight:600;
}
.kcr-price{
    background:linear-gradient(135deg,#f0fdf4 0%,#dcfce7 100%);
    border:2px solid #16a34a;
    border-radius:28px;
    padding:32px 24px;
    text-align:center;
    box-shadow:0 18px 40px rgba(22,163,74,0.10);
}
.kcr-price-badge{
    display:inline-block;
    background:#166534;
    color:#fff;
    font-size:13px;
    font-weight:900;
    padding:7px 12px;
    border-radius:999px;
    margin-bottom:14px;
}
.kcr-price-title{
    font-size:36px;
    font-weight:900;
    line-height:1.45;
    color:#0f172a;
    margin-bottom:12px;
    letter-spacing:-0.03em;
}
.kcr-price-text{
    color:#1f2937;
    font-size:17px;
    line-height:1.95;
    font-weight:700;
}
.kcr-price-main{
    font-size:60px;
    font-weight:900;
    color:#166534;
    letter-spacing:-0.04em;
    margin:14px 0 8px;
}
.kcr-price-sub{
    color:#475569;
    font-size:14px;
    font-weight:700;
}
.kcr-footer-links{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:12px;
    margin-top:18px;
    margin-bottom:12px;
}
.kcr-footer-link{
    display:inline-block;
    text-decoration:none !important;
    background:#fff;
    color:#0f172a !important;
    border:1px solid #d1d5db;
    padding:11px 14px;
    border-radius:12px;
    font-size:14px;
    font-weight:800;
    box-shadow:0 6px 16px rgba(15,23,42,0.04);
}
.kcr-footer{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:18px;
    padding:18px;
    text-align:center;
    color:#64748b;
    font-size:14px;
    line-height:1.9;
    margin-top:18px;
}
@media (max-width:768px){
    .block-container{
        padding-left:.85rem;
        padding-right:.85rem;
        padding-top:.45rem;
    }
    .kcr-hero{padding:24px 18px;border-radius:22px;}
    .kcr-hero-title{font-size:36px;line-height:1.18;}
    .kcr-hero-sub{font-size:16px;}
    .kcr-section-title{font-size:28px;}
    .kcr-section-sub{font-size:15px;}
    .kcr-grid-3{grid-template-columns:1fr;gap:12px;}
    .kcr-box-title{font-size:20px;}
    .kcr-sample-top{grid-template-columns:1fr;}
    .kcr-alert-title{font-size:23px;}
    .kcr-alert-text{font-size:15px;}
    .kcr-price-title{font-size:28px;}
    .kcr-price-main{font-size:44px;}
    .kcr-cta-primary,.kcr-cta-secondary,.kcr-cta-line{
        font-size:16px;
        padding:15px 14px;
    }
}
</style>
""")

render("""
<div class="kcr-hero">
  <div class="kcr-hero-inner">
    <div class="kcr-badge">建設会社専用 / 最短30秒 無料診断</div>
    <div class="kcr-app-name">建設キャッシュレーダー</div>
    <div class="kcr-hero-title">
      <span class="blue">資金あと何ヶ月もつか</span><br>
      <span class="dark">一発で分かる</span>
    </div>
    <div class="kcr-hero-sub">
      売上・原価・固定費・現金を入れるだけで、<br>
      あなたの会社の <b>資金ショート危険度</b> と
      <b>安全ライン不足額</b> を<br>
      その場で見える化します。
    </div>
    <div class="kcr-hero-points">
      ・黒字でも現金が尽きる理由が見える<br>
      ・あと何ヶ月持つかが分かる<br>
      ・次に何を直せばいいかが分かる
    </div>
  </div>
</div>
""")

render(f'<a href="{APP_URL}" target="_self" class="kcr-cta-primary">30秒で無料診断する</a>')
render('<div class="kcr-cta-subnote">登録不要ですぐ使えます</div>')

render('<div class="kcr-section-label">FEATURES</div>')
render('<div class="kcr-section-title">30秒でこの3つが分かります</div>')
render('<div class="kcr-section-sub">社長が知りたい数字だけを、できるだけ分かりやすく表示します。</div>')

render("""
<div class="kcr-grid-3">
  <div class="kcr-box">
    <div class="kcr-num">01</div>
    <div class="kcr-box-title">資金ショートまでの期間</div>
    <div class="kcr-box-text">あと何ヶ月持つかを、その場で把握できます。</div>
  </div>
  <div class="kcr-box">
    <div class="kcr-num">02</div>
    <div class="kcr-box-title">安全ラインとの差額</div>
    <div class="kcr-box-text">あといくら足りないかが明確になります。</div>
  </div>
  <div class="kcr-box">
    <div class="kcr-num">03</div>
    <div class="kcr-box-title">改善ポイント</div>
    <div class="kcr-box-text">どこを直せばいいか、優先順位が見えます。</div>
  </div>
</div>
""")

render('<div class="kcr-section-label">BENEFITS</div>')
render('<div class="kcr-section-title">導入メリット</div>')
render('<div class="kcr-section-sub">数字が見えるようになるだけで、社長の判断スピードが変わります。</div>')

render("""
<div class="kcr-grid-3">
  <div class="kcr-box">
    <div class="kcr-box-title">判断が早くなる</div>
    <div class="kcr-box-text">資金が何ヶ月持つか見えるので、攻めるか守るかの判断が早くなります。</div>
  </div>
  <div class="kcr-box">
    <div class="kcr-box-title">銀行・税理士との会話が強くなる</div>
    <div class="kcr-box-text">現状と不足額を数字で把握できるため、説明しやすくなります。</div>
  </div>
  <div class="kcr-box">
    <div class="kcr-box-title">改善ポイントが明確になる</div>
    <div class="kcr-box-text">原価・固定費・現金のどこを見直すべきか、優先順位が見えます。</div>
  </div>
</div>
""")

render("""
<div class="kcr-alert">
  <div class="kcr-alert-title">売上があっても、現金が尽きたら終わりです。</div>
  <div class="kcr-alert-text">
    利益が出ていても、入金サイト・原価率・固定費のズレで、突然お金が回らなくなることがあります。<br>
    会計ソフトや試算表だけでは見えない <b>“未来の資金繰り”</b> を先に確認するためのサービスです。
  </div>
</div>
""")

render('<div class="kcr-section-label">SAMPLE</div>')
render('<div class="kcr-section-title">診断結果のイメージ</div>')
render('<div class="kcr-section-sub">入力した数字から、危険度と改善の方向性をその場で確認できます。</div>')

render("""
<div class="kcr-sample">
  <div class="kcr-sample-top">
    <div class="kcr-sample-input">
      売上　900万円<br>
      原価　620万円<br>
      固定費　260万円<br>
      現金　180万円
    </div>
    <div class="kcr-sample-result">
      診断結果<br><br>
      資金ショートまで<br>
      <span class="big">3.4ヶ月</span><br><br>
      安全ライン不足額<br>
      <span class="big">あと380万円不足</span><br><br>
      改善ポイント<br>
      <span class="big">原価率 −3%</span>
    </div>
  </div>
</div>
""")

render('<div class="kcr-section-label">PROBLEMS</div>')
render('<div class="kcr-section-title">こんなお悩みありませんか？</div>')
render('<div class="kcr-section-sub">建設会社の社長が感じやすい不安を前提に作っています。</div>')

render("""
<div class="kcr-list">
  <div class="kcr-list-item">売上はあるのにお金が残らない</div>
  <div class="kcr-list-item">原価率が高い現場に後から気づく</div>
  <div class="kcr-list-item">このままで本当に大丈夫か不安</div>
  <div class="kcr-list-item">銀行や税理士に数字を説明しづらい</div>
</div>
""")

render('<div class="kcr-section-label">FOR WHO</div>')
render('<div class="kcr-section-title">このサービスが向いている会社</div>')
render('<div class="kcr-section-sub">特に、数字判断を早くしたい会社に向いています。</div>')

render("""
<div class="kcr-list">
  <div class="kcr-list-item">月ごとの資金繰りを先に把握したい会社</div>
  <div class="kcr-list-item">社長が数字判断を早くしたい会社</div>
  <div class="kcr-list-item">税理士・銀行との会話を強くしたい会社</div>
</div>
""")

render('<div class="kcr-section-label">FLOW</div>')
render('<div class="kcr-section-title">使い方はかんたんです</div>')
render('<div class="kcr-section-sub">むずかしい設定はありません。数字を入れるだけです。</div>')

render("""
<div class="kcr-list">
  <div class="kcr-list-item"><b>STEP 1</b>　売上・原価・固定費・現金を入力</div>
  <div class="kcr-list-item"><b>STEP 2</b>　危険度と不足額を確認</div>
  <div class="kcr-list-item"><b>STEP 3</b>　改善ポイントを確認</div>
  <div class="kcr-list-item"><b>STEP 4</b>　必要ならLINE相談 / Pro版で継続管理</div>
</div>
""")

render('<div class="kcr-section-label">FAQ</div>')
render('<div class="kcr-section-title">よくある質問</div>')
render('<div class="kcr-section-sub">導入前によく聞かれる内容をまとめています。</div>')

render("""
<div class="kcr-faq-wrap">
  <div class="kcr-faq-item">
    <div class="kcr-faq-q">Q. 会計ソフトがなくても使えますか？</div>
    <div class="kcr-faq-a">はい。売上・原価・固定費・現金などの数字が分かれば使えます。</div>
  </div>
  <div class="kcr-faq-item">
    <div class="kcr-faq-q">Q. 無料診断だけでも使えますか？</div>
    <div class="kcr-faq-a">はい。まずは無料診断だけで、今の資金状況を確認できます。</div>
  </div>
  <div class="kcr-faq-item">
    <div class="kcr-faq-q">Q. Pro版では何ができますか？</div>
    <div class="kcr-faq-a">12ヶ月資金推移、現場利益管理、銀行提出サマリー、利益改善シミュレーターなどが使えます。</div>
  </div>
  <div class="kcr-faq-item">
    <div class="kcr-faq-q">Q. サブスクはいつでも解約できますか？</div>
    <div class="kcr-faq-a">はい。解約後は次回請求が発生しません。詳細は特定商取引法に基づく表記をご確認ください。</div>
  </div>
</div>
""")

render('<div class="kcr-section-label">PLAN</div>')
render('<div class="kcr-section-title">社長専用 Proダッシュボード</div>')
render('<div class="kcr-section-sub">無料診断で確認したあと、継続管理したい方はPro版をご利用ください。</div>')

render("""
<div class="kcr-price">
  <div class="kcr-price-badge">おすすめ</div>
  <div class="kcr-price-title">毎月の資金判断を、もっと早く・分かりやすく</div>
  <div class="kcr-price-text">
    12ヶ月資金推移<br>
    現場利益管理<br>
    銀行提出サマリー<br>
    利益改善シミュレーター
  </div>
  <div class="kcr-price-main">月 9,800円</div>
  <div class="kcr-price-sub">まずは無料診断から始められます</div>
</div>
""")

render(f'<a href="{APP_URL}" target="_self" class="kcr-cta-primary">30秒で無料診断する</a>')
render(f'<a href="{STRIPE_URL}" target="_blank" class="kcr-cta-secondary">PRO版を始める（月額9,800円）</a>')
render(f'<a href="{LINE_URL}" target="_blank" class="kcr-cta-line">LINEで問い合わせる</a>')

render(f"""
<div class="kcr-footer-links">
  <a href="{TOKUSHO_URL}" target="_blank" class="kcr-footer-link">特定商取引法に基づく表記</a>
  <a href="{TERMS_URL}" target="_blank" class="kcr-footer-link">利用規約</a>
  <a href="{PRIVACY_URL}" target="_blank" class="kcr-footer-link">プライバシーポリシー</a>
</div>
""")

render("""
<div class="kcr-footer">
  建設会社の資金不安を、数字で見える化。<br>
  会計ソフトでは見えない「未来のキャッシュ」を、すぐ確認できます。
</div>
""")
