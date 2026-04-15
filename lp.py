import streamlit as st

st.set_page_config(
    page_title="建設キャッシュレーダー",
    page_icon="🏗️",
    layout="centered"
)

APP_URL = "https://construction-cash-check.streamlit.app"
LINE_URL = "https://lin.ee/7m28VAs"

st.title("建設キャッシュレーダー")

st.markdown("## 資金あと何ヶ月もつか一発で分かる")

st.write("""
売上・原価・固定費・現金を入れるだけで  
資金ショートまでの期間と改善ポイントを見える化
""")

st.link_button("無料診断する", APP_URL, use_container_width=True)
st.link_button("LINEで相談する", LINE_URL, use_container_width=True)

st.markdown("---")

st.subheader("こんな悩みありませんか？")

st.write("""
・売上あるのにお金が残らない  
・このままで大丈夫か不安  
・原価率が高い現場に後から気づく  
""")

st.markdown("---")

st.subheader("このアプリで分かること")

st.write("""
・資金ショートまでの期間  
・安全ラインとの差額  
・改善ポイント  
""")

st.markdown("---")

st.success("まずは無料診断からどうぞ")
