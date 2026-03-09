import pandas as pd
import streamlit as st

# =====================================
# 基本設定
# =====================================
st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered",
)

LINE_URL = "https://lin.ee/7m28VAs"
DEMO_LIMIT = 6
SALES_BUFFER = 1.3
PRO_ACCESS_CODE = "sugahara9800"   # あとで自由に変更OK

# =====================================
# 見た目
# =====================================
st.markdown("""
<style>
.block-container{
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 900px;
}
h1, h2, h3, p, div, span, label {
    color: #111 !important;
}
.stApp {
    background: #f7f7f7;
}
.result-card{
    border-radius: 18px;
    padding: 22px;
    margin-top: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
.card-danger{
    background:#ffe5e5;
    border-left:12px solid #ff4d4f;
}
.card-warn{
    background:#fff3cd;
    border-left:12px solid #f4b400;
}
.card-safe{
    background:#e6f7e6;
    border-left:12px solid #2e7d32;
}
.card-white{
    background:#ffffff;
    border:3px solid #ececec;
}
.pro-box{
    background:#eef9f0;
    border:4px solid #2e7d32;
    border-radius:20px;
    padding:24px;
    margin-top:22px;
    text-align:center;
    box-shadow:0 4px 14px rgba(0,0,0,0.05);
}
.metric-box{
    background:#f8f9fb;
    border-radius:16px;
    padding:16px;
    border:1px solid #ececec;
    margin-top:10px;
    text-align:center;
}
.small-note{
    color:#666 !important;
    font-size:14px;
    line-height:1.8;
    margin-top:16px;
}
.logo-mini{
    font-size:14px;
    color:#666 !important;
    margin-bottom:8px;
}
.input-box{
    background:#ffffff;
    border:2px solid #ececec;
    border-radius:18px;
    padding:18px;
    margin-top:16px;
    box-shadow:0 4px 12px rgba(0,0,0,0.04);
}
.section-title{
    font-size:20px;
    font-weight:900;
    margin-bottom:10px;
}
div.stLinkButton > a {
    background: #111827 !important;
    color: white !important;
    border: 2px solid #111827 !important;
    border-radius: 14px !important;
    font-weight: 800 !important;
    font-size: 18px !important;
    padding: 14px 18px !important;
    text-align: center !important;
    display: block !important;
}

div.stLinkButton > a:hover {
    background: #000000 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# ヘルパー
# =====================================
def yen(n):
    try:
        return f"{int(round(float(n))):,}円"
    except Exception:
        return "0円"

def months_to_shortage(cash_on_hand, monthly_after_tax_delta):
    if monthly_after_tax_delta >= 0:
        return None
    burn = abs(monthly_after_tax_delta)
    if burn == 0:
        return None
    return cash_on_hand / burn

# =====================================
# セッション
# =====================================
if "calc_count" not in st.session_state:
    st.session_state.calc_count = 0

if "last_calc" not in st.session_state:
    st.session_state.last_calc = False

if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

# =====================================
# ヘッダー
# =====================================
st.markdown('<div class="logo-mini">建設業向け診断ツール</div>', unsafe_allow_html=True)
st.title("建設キャッシュレーダー")
st.write("売上と現場コストを入れるだけ。『いつ資金ショートするか』『安全にするには月いくら必要か』が一発で見える。")

# =====================================
# Proコード
# =====================================
st.markdown('<div class="input-box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🔒 プラン</div>', unsafe_allow_html=True)

pro_code_input = st.text_input("Proコード", type="password", placeholder="Pro版の方だけ入力")

if pro_code_input == PRO_ACCESS_CODE:
    st.session_state.is_pro = True
    st.success("Pro版が有効です")
elif pro_code_input:
    st.session_state.is_pro = False
    st.error("Proコードが違います")

is_pro = st.session_state.is_pro

if is_pro:
    st.caption("✅ Pro版：機能無制限")
else:
    st.caption(f"※ デモは計算ボタン {DEMO_LIMIT} 回まで")
st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# 入力欄
# =====================================
st.markdown('<div class="input-box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 月次入力</div>', unsafe_allow_html=True)

sales = st.number_input("売上（月）", min_value=0, value=8300000, step=100000)
cost = st.number_input("原価（月） ※材料+外注など", min_value=0, value=3700000, step=100000)
fixed_total = st.number_input("固定費（全部） ※人件費/家賃/返済/リース/その他", min_value=0, value=5300000, step=100000)
cash_on_hand = st.number_input("現在の現金残高", min_value=0, value=300000, step=100000)

st.markdown('<div class="section-title" style="margin-top:14px;">⚙️ 設定（ざっくり）</div>', unsafe_allow_html=True)
tax_rate = st.slider("税率（概算）", min_value=0.0, max_value=0.6, value=0.30, step=0.01)
safety_months = st.slider("安全ライン（月）", min_value=1, max_value=12, value=6, step=1)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# Pro機能入力
# =====================================
st.markdown('<div class="input-box">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📋 現場利益（Pro機能）</div>', unsafe_allow_html=True)
site_sales = st.number_input("現場売上", min_value=0, value=1000000, step=10000)
site_cost = st.number_input("現場原価", min_value=0, value=650000, step=10000)

st.markdown('<div class="section-title" style="margin-top:14px;">🧮 利益シミュレーター（Pro機能）</div>', unsafe_allow_html=True)
sim_sales_up = st.number_input("売上をいくら増やす？", min_value=0, value=1000000, step=100000)
sim_cost_down_pct = st.slider("原価を何%下げる？", min_value=0.0, max_value=20.0, value=5.0, step=0.5)
st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# 計算
# =====================================
sales = float(sales)
cost = float(cost)
fixed_total = float(fixed_total)
cash_on_hand = float(cash_on_hand)
tax_rate = float(tax_rate)
safety_months = int(safety_months)

gross_profit = sales - cost
before_tax_profit = gross_profit - fixed_total
after_tax_profit = before_tax_profit * (1.0 - tax_rate) if before_tax_profit > 0 else before_tax_profit
delta_after = after_tax_profit

safe_cash = fixed_total * safety_months
lack_cash = max(0.0, safe_cash - cash_on_hand)

need_after_per_month = abs(delta_after) if delta_after < 0 else 0.0
need_sales_per_month = need_after_per_month / max(0.01, (1.0 - tax_rate))
need_sales_safe = need_sales_per_month * SALES_BUFFER if need_sales_per_month > 0 else 0.0

runway_months = months_to_shortage(cash_on_hand, delta_after)

site_sales = float(site_sales)
site_cost = float(site_cost)
site_profit = site_sales - site_cost
site_rate = (site_profit / site_sales * 100.0) if site_sales > 0 else 0.0

sim_new_sales = sales + sim_sales_up
sim_new_cost = cost * (1.0 - sim_cost_down_pct / 100.0)
sim_new_gross = sim_new_sales - sim_new_cost
sim_new_before_tax = sim_new_gross - fixed_total
sim_new_after_tax = sim_new_before_tax * (1.0 - tax_rate) if sim_new_before_tax > 0 else sim_new_before_tax
sim_diff = sim_new_after_tax - after_tax_profit

demo_locked = (st.session_state.calc_count >= DEMO_LIMIT) and (not is_pro)

# =====================================
# 計算ボタン
# =====================================
calc = st.button("計算する", type="primary", disabled=demo_locked, use_container_width=False)

if is_pro:
    st.caption("✅ Pro版：機能無制限")
else:
    st.caption(f"※ デモは計算ボタンが {DEMO_LIMIT} 回まで")

if calc and (not demo_locked):
    if not is_pro:
        st.session_state.calc_count += 1
    st.session_state.last_calc = True

if demo_locked:
    st.error("⛔ デモは6回までです。続きはProでご利用ください。")

# =====================================
# 結果表示
# =====================================
if calc or st.session_state.get("last_calc", False):
    if not demo_locked:
        months_left = 0
        if runway_months is not None:
            months_left = max(0, int(runway_months))

        # ① 資金ショート結果カード
        if runway_months is None:
            st.markdown(f"""
            <div class="result-card card-safe">
                <div style="font-size:40px; font-weight:900; line-height:1.3;">🟢 いまは安全です</div>
                <div style="font-size:18px; line-height:1.8; margin-top:10px;">
                    税後でも黒字で、資金ショートの心配は小さい状態です。<br>
                    安全ライン（{safety_months}ヶ月分の固定費）: <b>{yen(safe_cash)}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card card-danger">
                <div style="font-size:42px; font-weight:900; line-height:1.3;">⚠ 資金ショートまで<br>あと {months_left} ヶ月</div>
                <div style="font-size:18px; line-height:1.8; margin-top:10px;">
                    このままだと毎月 <b>{yen(abs(delta_after))}</b> ずつ現金が減ります。<br>
                    年間では <b>{yen(abs(delta_after) * 12)}</b> のキャッシュ減少です。
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ② 安全ラインカード
        if lack_cash > 0:
            st.markdown(f"""
            <div class="result-card card-warn">
                <div style="font-size:30px; font-weight:900; line-height:1.4;">安全ラインまで不足<br>{yen(lack_cash)}</div>
                <div style="font-size:18px; line-height:1.8; margin-top:10px;">
                    安全にするには、ざっくり<br>
                    <b>売上 +{yen(need_sales_safe)} / 月</b><br>
                    を目安に見直す必要があります。
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card card-safe">
                <div style="font-size:30px; font-weight:900; line-height:1.4;">安全ラインクリア</div>
                <div style="font-size:18px; line-height:1.8; margin-top:10px;">
                    現在の現金は、{safety_months}ヶ月安全ラインを超えています。
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ③ 今すぐ分かる結論
        urgency = "危険"
        urgency_msg = f"資金余命は約 {months_left} ヶ月。今月中に改善が必要です。"

        if runway_months is None:
            urgency = "安全"
            urgency_msg = "税後でも黒字です。まずは今の水準維持を優先してください。"
        elif months_left >= 12:
            urgency = "注意"
            urgency_msg = f"まだ余裕はありますが、放置すると {months_left} ヶ月後に危険です。"

        st.markdown(f"""
        <div class="result-card card-white">
            <div style="font-size:20px; font-weight:900;">⚡ 今すぐ分かる結論</div>
            <div style="margin-top:10px; font-size:17px; line-height:1.8;">
                <b>{urgency}</b>。{urgency_msg}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ④ 今日やる打ち手
        actions = []

        if lack_cash > 0:
            actions.append(f"まず <b>売上 +{yen(need_sales_safe)} / 月</b> を目安に改善する")
        if delta_after < 0:
            actions.append("入金を早くする（請求締め・入金サイト短縮）")
            actions.append("固定費と返済額を見直す")
            actions.append("原価率の高い現場を洗い出す")

        if not actions:
            actions.append("今の利益率と現金残高を維持する")
            actions.append("原価率が高い現場だけ毎月チェックする")

        actions_html = "".join([f"<li style='margin-bottom:8px;'>{a}</li>" for a in actions[:4]])

        st.markdown(f"""
        <div class="result-card card-white">
            <div style="font-size:20px; font-weight:900;">✅ 今日やる打ち手（最短で効く順）</div>
            <div style="margin-top:10px; font-size:17px; line-height:1.8;">
                <ul style="padding-left:22px; margin:0;">
                    {actions_html}
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # =====================================
        # Pro機能
        # =====================================
        if is_pro:
            # ⑤ 12ヶ月資金推移グラフ
            months = list(range(1, 13))
            cash_list = []
            current_cash = cash_on_hand

            for _ in months:
                current_cash = current_cash + delta_after
                cash_list.append(current_cash)

            df_cash = pd.DataFrame({
                "月": months,
                "現金残高": cash_list
            })

            st.markdown("""
            <div class="result-card card-white">
                <div style="font-size:20px; font-weight:900;">📈 12ヶ月資金推移</div>
                <div style="margin-top:10px; font-size:16px; line-height:1.8;">
                    今の条件のまま進んだ場合、現金が12ヶ月でどう動くかを確認できます。
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.line_chart(df_cash.set_index("月"))

            # ⑥ 銀行提出サマリー
            st.markdown("""
            <div class="result-card card-white">
                <div style="font-size:20px; font-weight:900;">🏦 銀行提出サマリー</div>
                <div style="margin-top:10px; font-size:16px; line-height:1.9;">
                    そのまま銀行や税理士に見せやすい形です。
                </div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f'<div class="metric-box"><b>月商</b><br>{yen(sales)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-box"><b>原価</b><br>{yen(cost)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-box"><b>固定費</b><br>{yen(fixed_total)}</div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="metric-box"><b>税後利益</b><br>{yen(delta_after)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-box"><b>現在現金</b><br>{yen(cash_on_hand)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-box"><b>安全ライン</b><br>{yen(safe_cash)}</div>', unsafe_allow_html=True)

            # ⑦ 現場利益10秒入力
            st.markdown("""
            <div class="result-card card-white">
                <div style="font-size:20px; font-weight:900;">📋 現場利益 10秒チェック</div>
                <div style="margin-top:10px; font-size:16px; line-height:1.9;">
                    この現場が儲かっているかをすぐ確認できます。
                </div>
            </div>
            """, unsafe_allow_html=True)

            s1, s2, s3 = st.columns(3)
            with s1:
                st.markdown(f'<div class="metric-box"><b>現場売上</b><br>{yen(site_sales)}</div>', unsafe_allow_html=True)
            with s2:
                st.markdown(f'<div class="metric-box"><b>現場利益</b><br>{yen(site_profit)}</div>', unsafe_allow_html=True)
            with s3:
                st.markdown(f'<div class="metric-box"><b>利益率</b><br>{site_rate:.1f}%</div>', unsafe_allow_html=True)

            # ⑧ 改善アドバイス
            if delta_after < 0:
                advice = "資金が減少しています。売上アップか固定費削減を最優先で見直してください。"
            elif site_rate < 15:
                advice = "現場利益率が低めです。材料費・外注費・値決めの見直し余地があります。"
            else:
                advice = "利益状態は良好です。この利益率を維持しつつ、現金残高を厚くしていきましょう。"

            st.markdown("""
            <div class="result-card card-white">
                <div style="font-size:20px; font-weight:900;">💡 改善アドバイス</div>
            </div>
            """, unsafe_allow_html=True)
            st.info(advice)

            # ⑨ 利益シミュレーター
            st.markdown("""
            <div class="result-card card-white">
                <div style="font-size:20px; font-weight:900;">🧮 利益シミュレーター</div>
                <div style="margin-top:10px; font-size:16px; line-height:1.9;">
                    売上を増やした場合・原価を下げた場合の利益変化を見られます。
                </div>
            </div>
            """, unsafe_allow_html=True)

            sim1, sim2 = st.columns(2)
            with sim1:
                st.markdown(f'<div class="metric-box"><b>改善後の税後利益</b><br>{yen(sim_new_after_tax)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-box"><b>改善後の売上</b><br>{yen(sim_new_sales)}</div>', unsafe_allow_html=True)
            with sim2:
                st.markdown(f'<div class="metric-box"><b>今との差額</b><br>{yen(sim_diff)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-box"><b>改善後の原価</b><br>{yen(sim_new_cost)}</div>', unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="pro-box">
                <div style="font-size:34px; font-weight:900; line-height:1.4;">
                    続きは Pro版へ
                </div>
                <div style="font-size:18px; line-height:1.9; margin-top:12px;">
                    Pro版では<br>
                    <b>12ヶ月資金推移</b>・<b>現場利益管理</b>・<b>銀行提出サマリー</b><br>
                    ・<b>利益改善シミュレーター</b> まで使えます。
                </div>
                <div style="font-size:44px; font-weight:900; margin-top:16px;">
                    月 9,800円
                </div>
                <div style="font-size:16px; margin-top:8px;">
                    デモは6回まで / Proは無制限
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown(f"""
<a href="{LINE_URL}" target="_blank"
style="
display:block;
text-align:center;
background:#111827;
color:white;
padding:16px;
border-radius:14px;
font-size:20px;
font-weight:800;
text-decoration:none;
margin-top:10px;
">
🚀 LINEでProを申し込む
</a>
""", unsafe_allow_html=True)
# =====================================
# フッター
# =====================================
st.markdown("""
<div class="small-note">
※ スマホでも見やすく設計しています。<br>
※ プロフィール・チラシ・車両QRからそのまま使えます。
</div>
""", unsafe_allow_html=True)
