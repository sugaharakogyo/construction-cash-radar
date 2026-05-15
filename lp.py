import streamlit as st

# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="建設キャッシュレーダー - 資金あと何ヶ月もつか一発で分かる",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# Streamlitメニューを完全非表示
# =========================
hide_streamlit_style = """
<style>
    header {
        visibility: hidden !important;
        height: 0 !important;
    }
    #MainMenu {
        visibility: hidden !important;
    }
    footer {
        visibility: hidden !important;
    }
    .stDeployButton {
        display: none !important;
    }
    header[data-testid="stHeader"] {
        display: none !important;
    }
    .stApp > header {
        display: none !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# =========================
# URL設定
# =========================
APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"
STRIPE_URL = "https://buy.stripe.com/6oU28rarietE5gM6m87N600"
TOKUSHO_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"
TERMS_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"
PRIVACY_URL = "https://wool-athlete-ae3.notion.site/333953f89b848056818cf44d9a9dbea9"

# =========================
# CSS（改善版）
# =========================
st.markdown("""
<style>
/* 基本設定 */
.block-container {
    max-width: 980px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.stApp {
    background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
}

/* ヒーローセクション */
.hero {
    background: linear-gradient(135deg, #ffffff 0%, #eaf2ff 55%, #dbeafe 100%);
    border: 1px solid #dbeafe;
    border-radius: 28px;
    padding: 40px 32px;
    box-shadow: 0 18px 40px rgba(15,23,42,0.08);
    margin-bottom: 24px;
    text-align: center;
}

.badge {
    display: inline-block;
    background: #2563eb;
    color: white;
    padding: 8px 16px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 16px;
}

.hero-title {
    font-size: 48px;
    font-weight: 900;
    line-height: 1.2;
    color: #0f172a;
    margin-bottom: 16px;
}

.hero-title .blue {
    color: #1d4ed8;
}

.hero-sub {
    font-size: 18px;
    line-height: 1.8;
    color: #334155;
    margin-bottom: 24px;
    font-weight: 600;
}

/* カード */
.card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 22px;
    padding: 24px 22px;
    box-shadow: 0 10px 24px rgba(15,23,42,0.05);
    margin-bottom: 20px;
}

.card-title {
    font-size: 24px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 12px;
}

.card-text {
    font-size: 16px;
    line-height: 1.85;
    color: #475569;
    font-weight: 600;
}

/* 警告ボックス */
.notice {
    background: linear-gradient(180deg, #fff1f2 0%, #ffe4e6 100%);
    border: 1px solid #fecdd3;
    border-left: 6px solid #ef4444;
    border-radius: 22px;
    padding: 28px 24px;
    margin-bottom: 24px;
}

.notice-title {
    font-size: 28px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 12px;
}

.notice-text {
    font-size: 16px;
    line-height: 1.9;
    color: #374151;
    font-weight: 700;
}

/* 料金ボックス */
.price {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 2px solid #16a34a;
    border-radius: 24px;
    padding: 32px 24px;
    text-align: center;
    margin-bottom: 24px;
}

.price-main {
    font-size: 56px;
    font-weight: 900;
    color: #166534;
    margin: 12px 0 8px;
}

/* フッター */
.footer-box {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    color: #64748b;
    font-size: 14px;
    line-height: 1.9;
    margin-top: 32px;
}

/* ボタンスタイル */
.stButton > button,
div[data-testid="stLinkButton"] a {
    width: 100% !important;
    border-radius: 14px !important;
    height: 3.8rem !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    background: #2563eb !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 10px 24px rgba(37, 99, 235, 0.3) !important;
    transition: all 0.3s ease !important;
    text-decoration: none !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.stButton > button:hover,
div[data-testid="stLinkButton"] a:hover {
    background: #1d4ed8 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 14px 28px rgba(37, 99, 235, 0.35) !important;
}

/* 特別なCTAボタン */
.cta-primary {
    background: #ef4444 !important;
    box-shadow: 0 10px 24px rgba(239, 68, 68, 0.3) !important;
    animation: pulse 2s infinite;
}

.cta-primary:hover {
    background: #dc2626 !important;
    box-shadow: 0 14px 28px rgba(239, 68, 68, 0.4) !important;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.02); }
}

/* スマホ対応 */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.8rem 2rem;
    }
    
    .hero {
        padding: 28px 20px;
        border-radius: 20px;
    }
    
    .hero-title {
        font-size: 32px;
    }
    
    .hero-sub {
        font-size: 16px;
    }
    
    .card {
        padding: 20px 18px;
        border-radius: 18px;
    }
    
    .card-title {
        font-size: 20px;
    }
    
    .card-text {
        font-size: 15px;
    }
    
    .notice {
        padding: 22px 18px;
    }
    
    .notice-title {
        font-size: 22px;
    }
    
    .notice-text {
        font-size: 15px;
    }
    
    .price {
        padding: 26px 18px;
    }
    
    .price-main {
        font-size: 42px;
    }
    
    .stButton > button,
    div[data-testid="stLinkButton"] a {
        height: 3.5rem !important;
        font-size: 1.05rem !important;
    }
}

/* 目立たせるアニメーション */
.highlight {
    background: linear-gradient(90deg, #fef08a, #fde047);
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 900;
}
</style>
""", unsafe_allow_html=True)

# =========================
# ヒーローセクション
# =========================
st.markdown("""
<div class="hero">
    <div class="badge">🏗️ 建設会社専用 / 最短30秒 無料診断</div>
    <div class="hero-title">
        <span class="blue">資金あと何ヶ月もつか</span><br>
        一発で分かる
    </div>
    <div class="hero-sub">
        売上・原価・固定費・現金を入れるだけで、<br>
        あなたの会社の資金ショート危険度と安全ライン不足額を見える化します。
    </div>
</div>
""", unsafe_allow_html=True)

# メインCTAボタン
st.markdown('<div class="cta-primary">', unsafe_allow_html=True)
st.link_button("🚀 今すぐ30秒で無料診断する", APP_URL, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.caption("✅ 登録不要・メールアドレス不要ですぐ使えます")

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# 3つの特徴
# =========================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">⏰ 資金ショート<br>までの期間</div>
        <div class="card-text">あと何ヶ月持つかを、その場で把握できます。</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">💰 安全ライン<br>との差額</div>
        <div class="card-text">あといくら足りないかが明確になります。</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">🎯 改善<br>ポイント</div>
        <div class="card-text">どこを直せばいいか、優先順位が見えます。</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# 警告メッセージ
# =========================
st.markdown("""
<div class="notice">
    <div class="notice-title">🚨 売上があっても、現金が尽きたら終わりです。</div>
    <div class="notice-text">
        利益が出ていても、入金サイト・原価率・固定費のズレで、突然お金が回らなくなることがあります。<br><br>
        会計ソフトや試算表だけでは見えない<span class="highlight">未来の資金繰り</span>を先に確認するためのサービスです。
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# 診断結果のイメージ
# =========================
st.markdown("""
<div class="card">
    <div class="card-title">📊 診断結果のイメージ</div>
    <div class="card-text">
        <b>入力例</b><br>
        売上 900万円 / 原価 620万円 / 固定費 260万円 / 現金 180万円<br><br>
        
        <b>↓ 診断結果</b><br>
        🚨 資金ショートまで：<span class="highlight">3.4ヶ月</span><br>
        ⚠️ 安全ライン不足額：あと<span class="highlight">380万円不足</span><br>
        💡 改善ポイント：原価率 -3%
    </div>
</div>
""", unsafe_allow_html=True)

# 中間CTA
st.link_button("📊 まずは無料で診断してみる", APP_URL, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# お悩み＋向いている会社（統合）
# =========================
col_pain1, col_pain2 = st.columns(2)

with col_pain1:
    st.markdown("""
    <div class="card">
        <div class="card-title">😰 こんなお悩み<br>ありませんか？</div>
        <div class="card-text">
            ✓ 売上はあるのにお金が残らない<br>
            ✓ 原価率が高い現場に後から気づく<br>
            ✓ このままで本当に大丈夫か不安<br>
            ✓ 銀行や税理士に数字を説明しづらい
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_pain2:
    st.markdown("""
    <div class="card">
        <div class="card-title">✅ このサービスが<br>向いている会社</div>
        <div class="card-text">
            ✓ 月ごとの資金繰りを先に把握したい<br>
            ✓ 社長が数字判断を早くしたい<br>
            ✓ 税理士、銀行との会話を強くしたい<br>
            ✓ 年商1〜3億円の建設会社
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# 社会的証明（導入実績＋お客様の声）
# =========================
st.markdown("""
<div class="card">
    <div class="card-title">📈 導入実績</div>
    <div class="card-text">
        ✅ <b>100社以上</b>の建設会社が利用<br>
        ✅ 平均<b>3分</b>で資金状況を把握<br>
        ✅ <b>90%以上</b>が「分かりやすい」と回答
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="card-title">💬 お客様の声</div>
    <div class="card-text">
        <b>「危なかったのに気づけた」</b><br>
        売上あるから大丈夫と思ってたけど、実際あと2ヶ月でショートでした。<br><br>

        <b>「判断がめちゃくちゃ早くなった」</b><br>
        今までは感覚だったけど、数字で判断できるようになった。<br><br>

        <b>「銀行との話が楽になった」</b><br>
        数字見せながら話せるから信用が上がった感じします。
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# FAQ
# =========================
st.markdown("""
<div class="card">
    <div class="card-title">❓ よくある質問</div>
    <div class="card-text">
        <b>Q. 会計ソフトがなくても使えますか？</b><br>
        A. はい。売上・原価・固定費・現金などの数字が分かれば使えます。<br><br>

        <b>Q. 無料診断だけでも使えますか？</b><br>
        A. はい。まずは無料診断だけで、今の資金状況を確認できます。<br><br>

        <b>Q. Pro版では何ができますか？</b><br>
        A. 12ヶ月資金推移、現場利益管理、銀行提出サマリー、利益改善シミュレーターなどが使えます。<br><br>

        <b>Q. サブスクはいつでも解約できますか？</b><br>
        A. はい。解約後は次回請求が発生しません。
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# 最終警告
# =========================
st.markdown("""
<div class="notice">
    <div class="notice-title">⚠️ 「まだ大丈夫」が一番危険です</div>
    <div class="notice-text">
        資金ショートは突然きます。<br>
        気づいた時には手遅れになる前に、一度だけでも確認してください。
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# 料金プラン
# =========================
st.markdown("""
<div class="price">
    <div style="font-size:14px;font-weight:900;color:#166534;">💎 おすすめ</div>
    <div style="font-size:32px;font-weight:900;color:#0f172a;line-height:1.4;margin-top:12px;">
        社長専用 Proダッシュボード
    </div>
    <div style="font-size:17px;line-height:1.8;color:#1f2937;font-weight:700;margin-top:14px;">
        ✅ 12ヶ月資金推移<br>
        ✅ 現場利益管理<br>
        ✅ 銀行提出サマリー<br>
        ✅ 利益改善シミュレーター
    </div>
    <div class="price-main">月 9,800円</div>
    <div style="font-size:15px;color:#475569;font-weight:700;">まずは無料診断から始められます</div>
</div>
""", unsafe_allow_html=True)

# =========================
# 最終CTAボタン
# =========================
st.link_button("💳 PRO版を今すぐ始める（月額9,800円）", STRIPE_URL, use_container_width=True)
st.link_button("📱 LINEで相談する（無料）", LINE_URL, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# =========================
# 法的リンク
# =========================
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("📄 特定商取引法", TOKUSHO_URL, use_container_width=True)
with c2:
    st.link_button("📜 利用規約", TERMS_URL, use_container_width=True)
with c3:
    st.link_button("🔒 プライバシーポリシー", PRIVACY_URL, use_container_width=True)

# =========================
# フッター
# =========================
st.markdown("""
<div class="footer-box">
    🏗️ 建設会社の資金不安を、数字で見える化。<br>
    会計ソフトでは見えない未来のキャッシュを、すぐ確認できます。
</div>
""", unsafe_allow_html=True)
