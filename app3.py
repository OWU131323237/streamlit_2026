import streamlit as st

st.header("今日の気分記録アプリ")

if"kibun_history" not in st.session_state:
    st.session_state["kibun_history"] = []


col1,col2,col3,col4   = st.columns(4)

with col1:
    if st.button("うれしい"):
        st.session_state["kibun_history"].append("😊")
with col2:
    if st.button("かなしい"):
        st.session_state["kibun_history"].append("😢")
with col3:
    if st.button("ねむい"):
        st.session_state["kibun_history"].append("💤")
with col4:
    if st.button("おなかすいた"):
        st.session_state["kibun_history"].append("🍕")

for kibun in st.session_state["kibun_history"]:
    st.write(kibun)




# if"count" not in st.session_state:
#     st.session_state["count"] = 1

# if st.button("カウンター"):
#     st.session_state["count"] = st.session_state.get("count", 0) + 1

# st.write(st.session_state["count"])

# st.write("メイン画面")


# col1,col2 = st.columns(2)

# with col1:
#     st.image("purin.png")
# with col2:
#     st.write("プリンが好きです")
#     with st.expander("詳細"):
#         st.write("特にプッチンプリン")

# st.sidebar.write("サイドバー")
# name = st.sidebar.text_input(
#     "お名前"
# )
# student_id = st.sidebar.text_input(
#     "学籍番号"
# )

