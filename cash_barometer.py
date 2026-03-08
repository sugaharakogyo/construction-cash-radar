import streamlit as st
import pandas as pd
import altair as alt
import json
from pathlib import Path
import datetime
t.markdown("""
<style>
.result-danger{
    background:#ffe5e5 !important;
    color:#111 !important;
    border-left:12px solid #ff4d4f !important;
    border-radius:18px !important;
    padding:20px !important;
    margin-top:18px !important;
}
.result-danger .kpi-big,
.result-danger .kpi-mid,
.result-danger .card-body,
.result-danger div,
.result-danger span,
.result-danger b{
    color:#111 !important;
}

.result-warn{
    background:#fff3cd !important;
    color:#111 !important;
    border-left:12px solid #f4b400 !important;
    border-radius:18px !important;
    padding:20px !important;
    margin-top:18px !important;
}
.result-warn .kpi-big,
.result-warn .kpi-mid,
.result-warn .card-body,
.result-warn div,
.result-warn span,
.result-warn b{
    color:#111 !important;
}

.result-safe{
    background:#e6f7e6 !important;
    color:#111 !important;
    border-left:12px solid #2e7d32 !important;
    border-radius:18px !important;
    padding:20px !important;
    margin-top:18px !important;
}
.result-safe .kpi-big,
.result-safe .kpi-mid,
.result-safe .card-body,
.result-safe div,
.result-safe span,
.result-safe b{
    color:#111 !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 設定・保存
# ===============================
SAVE_PATH = Path("cash_barometer_state.json")


def load_state() -> dict:
    if SAVE_PATH.exists():
        try:
            return json.loads(SAVE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state():
    data = {
        "sales": st.session_state.get("sales", 0),
        "cost": st.session_state.get("cost", 0),
        "fixed_total": st.session_state.get("fixed_total", 0),
        "cash_on_hand": st.session_state.get("cash_on_hand", 0),
        "plan": st.session_state.get("plan", "デモ（無料）"),
        "tax_rate": st.session_state.get("tax_rate", 0.30),
        "safety_months": st.session_state.get("safety_months", 6),
        "scenario_pct": st.session_state.get("scenario_pct", 0),
        "calc_count": st.session_state.get("calc_count", 0),
        "pro_unlocked": st.session_state.get("pro_unlocked", False),
        "projects": st.session_state.get("projects", []),
    }
    SAVE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def yen(n: float) -> str:
    try:
        return f"{int(round(float(n))):,}円"
    except Exception:
        return "0円"


def safe_div(a: float, b: float, default: float = 0.0) -> float:
    try:
        if float(b) == 0:
            return default
        return float(a) / float(b)
    except Exception:
        return default


# ===============================
# ページ設定
# ===============================
st.set_page_config(page_title="建設キャッシュレーダー", layout="wide")

# ===============================
# スマホ用レイアウト調整（上のほうでOK）
# ===============================
st.markdown(
    """
<style>
@media (max-width: 768px) {
  h1 { font-size: 26px !important; }
  h2 { font-size: 22px !important; }
  h3 { font-size: 20px !important; }

  .block-container {
    padding-top: 1rem;
    padding-left: 0.9rem;
    padding-right: 0.9rem;
  }

  div[data-testid="stMetricValue"] { font-size: 22px !important; }
  div[data-testid="stMetricLabel"] { font-size: 13px !important; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ===============================
# 初期値
# ===============================
defaults = {
    "sales": 9_500_000,
    "cost": 6_100_000,
    "fixed_total": 4_000_000,  # 固定費ぜんぶ（人件費/家賃/リース/返済/その他）
    "cash_on_hand": 6_800_000,
    "plan": "デモ（無料）",
    "tax_rate": 0.30,
    "safety_months": 6,
    "scenario_pct": -10,
    "calc_count": 0,
    "pro_unlocked": False,
    "projects": [],
}

saved = load_state()
for k, v in defaults.items():
    st.session_state.setdefault(k, saved.get(k, v))

# ===============================
# デモ / Pro
# ===============================
DEMO_LIMIT = 6

with st.sidebar:
    st.header("📌 入力（ざっくりでOK）")

    st.markdown("## 🔐 プラン")
    plan= "デモ（無料）"
    if "is_pro" not in st.session_state:
        st.session_state.is_pro = False

    if plan == "デモ（無料）":
        st.session_state.is_pro = False
        st.caption("※ デモは一部制限あり（計算ボタン6回まで）")
    else:
        if st.session_state.pro_unlocked:
            st.session_state.is_pro = True
            st.success("Pro 解放中")
        else:
            pro_key = st.text_input("Proキー", type="password")
            if pro_key == "9800":
                st.session_state.pro_unlocked = True
                st.session_state.is_pro = True
                save_state()
                st.success("Pro 解放！")
            elif pro_key:
                st.session_state.is_pro = False
                st.error("キーが違うよ")

    is_pro = st.session_state.is_pro
    demo_locked = (not is_pro) and (st.session_state.calc_count >= DEMO_LIMIT)

    st.subheader("📊 月次入力")
    st.number_input(
        "売上（月）",
        min_value=0,
        step=100000,
        key="sales",
        disabled=(not is_pro),  # デモは固定
        on_change=save_state,
    )
    st.number_input(
        "原価（月）※材料+外注など",
        min_value=0,
        step=100000,
        key="cost",
        disabled=(not is_pro),  # デモは固定
        on_change=save_state,
    )
    st.number_input(
        "固定費（全部）※人件費/家賃/返済/リース/その他",
        min_value=0,
        step=100000,
        key="fixed_total",
        on_change=save_state,
    )
    st.number_input(
        "現在の現金残高",
        min_value=0,
        step=100000,
        key="cash_on_hand",
        on_change=save_state,
    )

    st.divider()
    st.subheader("⚙️ 設定（ざっくり）")
    st.slider("税率（概算）", 0.0, 0.5, float(st.session_state.tax_rate), 0.01, key="tax_rate", on_change=save_state)
    st.slider("安全ライン（月）", 3, 12, int(st.session_state.safety_months), 1, key="safety_months", on_change=save_state)

    st.divider()
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("💾 保存"):
            save_state()
            st.success("保存しました！")
    with col_s2:
        if st.button("🧹 保存を初期化"):
            if SAVE_PATH.exists():
                SAVE_PATH.unlink()
            st.session_state.clear()
            st.rerun()

# ===============================
# タイトル
# ===============================
left, right = st.columns([1, 7])
with left:
    if Path("logo.png").exists():
        st.image("logo.png", width=120)
with right:
    st.markdown(
        """# 建設キャッシュレーダー
売上と現場コストを入れるだけ。 **「いつ資金ショートするか」「安全にするには月いくら必要か」** が一発で見える。"""
    )

# ===============================
# 計算（共通）
# ===============================
sales = float(st.session_state.sales)
cost = float(st.session_state.cost)
fixed_total = float(st.session_state.fixed_total)
cash_on_hand = float(st.session_state.cash_on_hand)
tax_rate = float(st.session_state.tax_rate)
safety_months = int(st.session_state.safety_months)

gross = sales - cost
burn = fixed_total
delta_pre = gross - burn
tax_est = delta_pre * tax_rate if delta_pre > 0 else 0
delta_after = delta_pre - tax_est  # 税後の月次増減

# 資金余命（税後がマイナスのときだけ）
runway_months = None
if delta_after < 0:
    runway_months = cash_on_hand / abs(delta_after) if abs(delta_after) > 0 else 0

# 資金ショート日（ざっくり 30日=1ヶ月換算）
today = datetime.date.today()
short_date = None
if runway_months is not None:
    months_left = max(0, int(runway_months))
    short_date = today + datetime.timedelta(days=months_left * 30)

# 安全ライン（手元目標）
target_cash = burn * safety_months
need_cash = max(0.0, target_cash - cash_on_hand)

# 月あたり必要な税後利益
need_after_per_month = None
if safety_months > 0 and need_cash > 0:
    need_after_per_month = need_cash / safety_months

# 売上アップ目安（原価率を現状維持の前提で逆算）
cost_rate_now = (cost / sales) if sales > 0 else 0.65
gross_margin_rate = max(0.01, 1.0 - cost_rate_now)

need_sales_per_month = None
if need_after_per_month is not None:
    denom = gross_margin_rate * max(0.01, (1.0 - tax_rate))
    need_sales_per_month = need_after_per_month / denom if denom > 0 else None

SALES_BUFFER = 1.3
need_sales_safe = None
if need_sales_per_month is not None:
    need_sales_safe = need_sales_per_month * SALES_BUFFER

# 固定費を下げるなら（税後の必要利益を税前に戻すイメージ）
need_cost_cut = None
if need_after_per_month is not None:
    need_cost_cut = need_after_per_month / max(0.01, (1.0 - tax_rate))
    need_cost_cut *= SALES_BUFFER

# ===============================
# 計算ボタン（デモ回数管理）
# ===============================
is_pro = st.session_state.is_pro
demo_locked = (not is_pro) and (st.session_state.calc_count >= DEMO_LIMIT)
can_calculate = is_pro or (st.session_state.calc_count < DEMO_LIMIT)

col_btn1, col_btn2 = st.columns([1, 3])
with col_btn1:
    calc = st.button("計算する", type="primary", disabled=not can_calculate)
with col_btn2:
    st.caption("※ デモは計算ボタンが6回まで。Proは無制限。")

if calc and (not is_pro):
    st.session_state.calc_count += 1
    save_state()
    st.rerun()

if demo_locked:
    st.error("⛔ デモは6回までです。続きはProでご利用ください。")

# ===============================
# 🚨 超重要：資金ショート巨大表示
# ===============================
if runway_months is None:
    st.markdown("## 🟢 資金ショート：なし（黒字）")
else:
    months_left = max(0, int(runway_months))
    sd = datetime.date.today() + datetime.timedelta(days=months_left * 30)
    st.markdown(
        f"""
<div style="background:#fff0f0;border-left:12px solid #ff3b30;padding:18px;border-radius:14px;margin:10px 0;">
  <div style="font-size:18px;font-weight:800;">⚠ このままだと</div>
  <div style="font-size:44px;font-weight:900;line-height:1.05;margin:6px 0;">
    {sd.year}年{sd.month}月<br>資金ショート
  </div>
  <div style="font-size:16px;margin-top:6px;">（目安：あと <b>{months_left}ヶ月</b>）</div>
</div>
""",
        unsafe_allow_html=True,
    )

# ===============================
# ✔ 安全にするには（売上）
# ===============================
if need_sales_safe is not None and need_sales_safe > 0:
    st.markdown(
        f"""
<div style="background:#fff8e6;border-left:10px solid #f59e0b;padding:16px;border-radius:12px;margin-bottom:20px;">
  <div style="font-size:18px;font-weight:700;">✔ 安全にするには</div>
  <div style="font-size:34px;font-weight:900;margin-top:6px;">売上 +{yen(need_sales_safe)} / 月</div>
  <div style="font-size:14px;margin-top:6px;color:#666;">※ 原価率が今と同じ前提（余裕係数×{SALES_BUFFER}込み）</div>
</div>
""",
        unsafe_allow_html=True,
    )

# ===============================
# ⚡ 今すぐ分かる結論（売れる版）
# ===============================
st.markdown("## ⚡ 今すぐ分かる結論（売れる版）")

if runway_months is None:
    st.success("🟢 いまは安全。税後でも黒字で、資金ショートの心配は小さい。")
else:
    if runway_months >= 6:
        st.success(f"🟢 いまは安全寄り。資金余命は約 {runway_months:.1f} ヶ月。")
    elif runway_months >= 3:
        st.warning(f"🟡 注意。資金余命は約 {runway_months:.1f} ヶ月。早めに手を打とう。")
    else:
        st.error(f"🔴 危険。資金余命は約 {runway_months:.1f} ヶ月。今月中に改善が必要。")

if need_sales_safe is not None and need_sales_safe > 0:
    st.markdown("### ✅ 今日やる打ち手（最短で効く順）")
    st.write(f"・まず **売上 +{yen(need_sales_safe)} / 月** を目標に置く（余裕係数×{SALES_BUFFER}込み）")
    st.write("・入金を早くする（請求締め/前金/出来高）")
    st.write("・支払いを遅くする（外注/材料のサイト交渉）")
    st.write("・固定費の一時停止（サブスク/リース/交際費など）")

st.divider()

# ===============================
# 🚨 社長トップ診断（NEW）
# ===============================
st.markdown("## 🚨 キャッシュ診断（社長が最初に見る）")

b1, b2, b3, b4 = st.columns(4)
with b1:
    b1.metric("今月の増減（税後）", yen(delta_after))
with b2:
    b2.metric("安全ライン（手元目標）", yen(target_cash))
with b3:
    b3.metric("安全ラインまで不足", yen(need_cash))
with b4:
    b4.metric("毎月必要利益（税後）", yen(need_after_per_month) if need_after_per_month is not None else "0円")

# ===============================
# 🛟 安全ライン（建設会社の目安）
# ===============================
st.markdown("## 🛟 安全ライン")

safe_cash = burn * 6
lack_cash = max(0, safe_cash - cash_on_hand)

s1, s2, s3 = st.columns(3)

s1.metric(
    "安全ライン（6ヶ月）",
    yen(safe_cash)
)

s2.metric(
    "現在の現金",
    yen(cash_on_hand)
)

if lack_cash > 0:
    s3.metric(
        "不足額",
        yen(lack_cash)
    )
    st.warning("⚠ 安全ラインに届いていません")
else:
    s3.metric(
        "余裕資金",
        yen(cash_on_hand - safe_cash)
    )
    st.success("🟢 安全ラインクリア")

# ===============================
# ✔ 安全にするには（売上 / 利益）
# ===============================
st.markdown("## ✔ 安全にするには")

need_profit_text = "0円"
if need_after_per_month is not None:
    need_profit_text = yen(need_after_per_month)

need_sales_text = "0円"
if need_sales_safe is not None:
    need_sales_text = yen(need_sales_safe)

a1, a2 = st.columns(2)

with a1:
    st.metric(
        "売上を増やすなら（月）",
        f"+{need_sales_text}"
    )

with a2:
    st.metric(
        "利益を増やすなら（月）",
        f"+{need_profit_text}"
    )


# ===============================
# 🔮 もしもシミュレーション（社長が触るやつ）
# ===============================
st.markdown("## 🔮 もしもシミュレーション（社長が触るやつ）")
st.caption("売上・原価率・固定費を少し動かしたら、資金ショートと安全ラインがどう変わるかを一瞬で確認。")

scol1, scol2, scol3 = st.columns(3)
with scol1:
    sales_up = st.number_input("売上をいくら増やす？（月）", min_value=0, step=100000, value=0, key="sim_sales_up")
with scol2:
    cost_rate_diff = st.slider("原価率を何%下げる？（改善）", 0.0, 10.0, 0.0, 0.1, key="sim_cost_rate_down")
with scol3:
    fixed_cut = st.number_input("固定費をいくら下げる？（月）", min_value=0, step=50000, value=0, key="sim_fixed_cut")

sales2 = sales + float(sales_up)
cost_rate2 = max(0.0, cost_rate_now - (float(cost_rate_diff) / 100.0))
cost2 = sales2 * cost_rate2
burn2 = max(0.0, burn - float(fixed_cut))

gross2 = sales2 - cost2
delta2 = gross2 - burn2
tax2 = delta2 * tax_rate if delta2 > 0 else 0
after2 = delta2 - tax2

runway2 = None
if after2 < 0:
    runway2 = (cash_on_hand / abs(after2)) if abs(after2) > 0 else 0

short_text2 = "ショートなし（黒字）"
if runway2 is not None:
    months_left2 = max(0, int(runway2))
    sd2 = datetime.date.today() + datetime.timedelta(days=months_left2 * 30)
    short_text2 = f"{sd2.year}年{sd2.month}月"

m1, m2, m3, m4 = st.columns(4)
m1.metric("売上（想定）", yen(sales2))
m2.metric("税後の増減（想定）", yen(after2))
m3.metric("資金ショート（想定）", short_text2)
m4.metric("原価率（想定）", f"{cost_rate2*100:.1f}%")

st.caption("💡 使い方：まず全部0で現状確認 → 次にどれか1つだけ動かす。")
st.divider()

# ===============================
# 🧱 現場利益（10秒入力UI + 原価率：売れる）
# ===============================
st.markdown("## 🧱 現場利益（10秒で入力）")
st.caption("『現場名・請負・原価合計（ざっくり）』でもOK。『原価率%』で入れてもOK（自動計算）。")

if "projects" not in st.session_state or not isinstance(st.session_state.projects, list) or len(st.session_state.projects) == 0:
    st.session_state.projects = [
        {"現場名": "現場A", "請負金額": 3_000_000, "原価合計": 2_300_000, "原価率(%)": 0.0, "メモ": ""},
        {"現場名": "現場B", "請負金額": 2_500_000, "原価合計": 1_850_000, "原価率(%)": 0.0, "メモ": ""},
    ]

dfp = pd.DataFrame(st.session_state.projects)

for col in ["現場名", "請負金額", "原価合計", "原価率(%)", "メモ"]:
    if col not in dfp.columns:
        if col in ["現場名", "メモ"]:
            dfp[col] = ""
        else:
            dfp[col] = 0

st.caption("👇 行追加してOK（社長はここだけで終わり）")
edited = st.data_editor(
    dfp[["現場名", "請負金額", "原価合計", "原価率(%)", "メモ"]],
    use_container_width=True,
    num_rows="dynamic",
    key="projects_editor_fast_rate",
)

for col in ["請負金額", "原価合計", "原価率(%)"]:
    edited[col] = pd.to_numeric(edited[col], errors="coerce").fillna(0)

edited["原価率(%)"] = edited["原価率(%)"].clip(lower=0, upper=100)

# 自動計算（壊れにくい）
for i in edited.index:
    contract = float(edited.at[i, "請負金額"])
    cost_sum = float(edited.at[i, "原価合計"])
    rate = float(edited.at[i, "原価率(%)"])

    if contract <= 0:
        continue

    if cost_sum == 0 and rate > 0:
        edited.at[i, "原価合計"] = round(contract * rate / 100.0)
    elif rate == 0 and cost_sum > 0:
        edited.at[i, "原価率(%)"] = round((cost_sum / contract) * 100.0, 1)

edited["現場利益"] = edited["請負金額"] - edited["原価合計"]
edited["利益率"] = edited.apply(lambda r: safe_div(r["現場利益"], r["請負金額"], 0.0), axis=1)

# 保存
st.session_state.projects = edited.drop(columns=["現場利益", "利益率"], errors="ignore").to_dict("records")
save_state()

# KPI（社長が最初に見る）
valid = edited[edited["請負金額"] > 0].copy()
site_count = int(len(valid))
total_site_profit = float(valid["現場利益"].sum()) if site_count > 0 else 0.0
avg_site_profit = (total_site_profit / site_count) if site_count > 0 else 0.0
avg_site_margin = float(valid["利益率"].mean()) if site_count > 0 else 0.0

k1, k2, k3, k4 = st.columns(4)
k1.metric("現場数（請負入力あり）", f"{site_count}件")
k2.metric("今月の現場合計利益", yen(total_site_profit))
k3.metric("✅ 1現場 平均利益", yen(avg_site_profit))
k4.metric("参考：平均利益率", f"{avg_site_margin*100:.1f}%")

st.divider()

# TOP5（利益）
st.markdown("### 🏆 儲かってる現場 TOP5")
top_profit = valid.sort_values("現場利益", ascending=False).head(5)
if len(top_profit) == 0:
    st.info("現場を追加して『請負金額』を入れるとTOPが出ます。")
else:
    cols = st.columns(min(5, len(top_profit)))
    for i, (_, r) in enumerate(top_profit.iterrows()):
        cols[i].metric(r["現場名"] if r["現場名"] else "（未入力）", yen(float(r["現場利益"])))

# TOP5（利益率）
st.markdown("### 📈 利益率が高い現場 TOP5（上手い現場）")
top_rate = valid.sort_values("利益率", ascending=False).head(5)
if len(top_rate) == 0:
    st.info("現場を追加して『請負金額』を入れるとTOPが出ます。")
else:
    cols2 = st.columns(min(5, len(top_rate)))
    for i, (_, r) in enumerate(top_rate.iterrows()):
        cols2[i].metric(
            r["現場名"] if r["現場名"] else "（未入力）",
            f"{float(r['利益率'])*100:.1f}%",
            delta=yen(float(r["現場利益"])),
        )

# 赤字当たりTOP3（ざっくり）
st.markdown("### 🛠 赤字の原因（当たり）TOP3（ざっくり）")
loss_df = valid.sort_values("現場利益").head(3).copy()
if len(loss_df) == 0:
    st.info("請負金額を入れると分析が出ます。")
else:
    for _, r in loss_df.iterrows():
        name = r["現場名"] if r["現場名"] else "（未入力）"
        profit = float(r["現場利益"])
        margin = float(r["利益率"]) * 100
        if profit < 0:
            st.error(f"🔥 {name}：赤字 {yen(abs(profit))}（利益率 {margin:.1f}%）")
            st.write("当たり：①請負が安い ②原価が盛れてる ③外注/材料が想定より高い（まず原価率を疑う）")
        else:
            st.warning(f"⚠ {name}：利益 {yen(profit)}（利益率 {margin:.1f}%）")

with st.expander("📌 現場一覧（表で確認）"):
    show = edited[["現場名", "請負金額", "原価合計", "原価率(%)", "現場利益", "利益率", "メモ"]].copy()
    show["利益率"] = (show["利益率"] * 100).round(1).astype(str) + "%"
    show = show.sort_values("現場利益", ascending=False)
    st.dataframe(show, use_container_width=True)

st.divider()

# ===============================
# 📈 12ヶ月 現金推移（予測）+ CSV
# ===============================
st.markdown("## 📈 12ヶ月 現金推移（予測）")

months = list(range(0, 13))
cash_series_pre = [cash_on_hand + (delta_pre * m) for m in months]
cash_series_after = [cash_on_hand + (delta_after * m) for m in months]

df = pd.DataFrame({"月": months, "税前キャッシュ": cash_series_pre, "税後キャッシュ": cash_series_after})

danger_month = None
for m, v in zip(months, cash_series_after):
    if v < 0:
        danger_month = m
        break

c1, c2, c3 = st.columns(3)
c1.metric("税後 月次増減", yen(delta_after))
c2.metric("税後 最終月（12ヶ月目）", yen(cash_series_after[-1]))
if danger_month is None:
    c3.success("危険月：なし（税後が0円を下回らない）")
else:
    c3.error(f"危険月：{danger_month} ヶ月目")

base = alt.Chart(df).encode(x=alt.X("月:Q", title="月"))
line_pre = base.mark_line().encode(y=alt.Y("税前キャッシュ:Q", title="現金残高"), tooltip=["月", "税前キャッシュ"])
line_after = base.mark_line().encode(y="税後キャッシュ:Q", tooltip=["月", "税後キャッシュ"])
chart = (line_pre + line_after).properties(height=260)
st.altair_chart(chart, use_container_width=True)

with st.expander("📋 12ヶ月の明細（表/CSV）"):
    st.dataframe(df, use_container_width=True)
    st.download_button(
        "CSVをダウンロード",
        data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name="cash_forecast_12m.csv",
        mime="text/csv",
        key="download_csv_12m_main",
    )

st.divider()

# ===============================
# 🏦 銀行提出用 1枚サマリー（TXT）
# ===============================
st.markdown("## 🏦 銀行提出用（1枚サマリー）")
st.caption("※ このままコピペでメール/稟議に貼れます。")

short_text = "ショートなし（黒字）"
if runway_months is not None:
    months_left = max(0, int(runway_months))
    sd = datetime.date.today() + datetime.timedelta(days=months_left * 30)
    short_text = f"{sd.year}年{sd.month}月"

need_sales_text = "0円/月"
if need_sales_safe is not None and need_sales_safe > 0:
    need_sales_text = yen(need_sales_safe) + "/月"

summary_text = f"""
【建設キャッシュレーダー：銀行提出サマリー】

■今月（概算）
・売上：{yen(sales)}
・原価（材料+外注など）：{yen(cost)}
・固定費+返済（毎月出ていく）：{yen(burn)}
・税率（概算）：{int(tax_rate*100)}%

■キャッシュ状況（税後ベース）
・今月の増減（税後）：{yen(delta_after)}
・資金ショート予測：{short_text}

■安全ライン（手元目標）
・安全ライン（手元目標）：{yen(target_cash)}
・安全ラインまで不足：{yen(need_cash)}

■安全にするための目安
・売上を上げるなら：+{need_sales_text}

（備考）本数値は“月次のざっくり予測”です。実績の入金/支払サイト差は別途反映可能。
""".strip()

st.text_area("👇 そのまま銀行に送れる文面", summary_text, height=240)
st.download_button(
    "📄 サマリーをTXTで保存（銀行に送れる）",
    data=summary_text.encode("utf-8-sig"),
    file_name="bank_summary.txt",
    mime="text/plain",
)

# ===============================
# デモ案内
# ===============================
if not is_pro:
    remain = DEMO_LIMIT - int(st.session_state.calc_count)
    if remain > 0:
        st.warning(f"⏳ デモ残り {remain} 回（計算ボタン）")
    else:
        st.error("🚫 デモ上限に達しました。Proで無制限に利用できます。")

    st.markdown("## 💰 Pro（月9,800円）でできること")
    p1, p2 = st.columns([2, 1])
    with p1:
        st.markdown(
            """- 売上/原価も自由に変更（デモは固定）
- 計算回数の制限なし
- 12ヶ月推移・銀行提出CSV/TXTを業務で使い倒せる
- 現場の10秒入力＆ランキングで利益の見える化"""
        )
    with p2:
        st.link_button(
"🚀 Proを申し込む",
"https://lin.ee/7m28VAs",
use_container_width=True
)

