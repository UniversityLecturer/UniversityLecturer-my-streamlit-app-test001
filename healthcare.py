import streamlit as st

# 初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""

st.title("ストレスチェックチャットボット")

# 共通：横並びyes/no選択関数
def render_yes_no_buttons(key_prefix):
    col1, col2 = st.columns([1, 1])
    selected = None
    with col1:
        if st.button("yes", key=f"{key_prefix}_yes"):
            selected = "yes"
    with col2:
        if st.button("no", key=f"{key_prefix}_no"):
            selected = "no"
    return selected

# Step 1
if st.session_state.step == 1:
    st.subheader("01. 最近、疲れていますか？")
    st.caption("Are you tired recently?")
    st.markdown("あなたの回答を選んでください：")

    answer = render_yes_no_buttons("stress")

    if answer:
        st.session_state.stress = answer
        if answer == "yes":
            st.session_state.step = 2
        else:
            st.session_state.result = (
                "■ 良(よ)かったです！引(ひ)き続(つづ)き健康(けんこう)に過(す)ごしましょう。\n"
                "Good to hear! Stay healthy."
            )
            st.session_state.step = 3
        st.rerun()

# Step 2
elif st.session_state.step == 2:
    st.subheader("02. 睡眠時間は足りていますか？")
    st.caption("Do you get enough sleep?")
    st.markdown("あなたの回答を選んでください：")

    answer = render_yes_no_buttons("sleep")

    if answer:
        st.session_state.sleep = answer
        if answer == "yes":
            st.session_state.result = (
                "■ 軽(かる)い疲(つか)れですね。少(すこ)しリフレッシュしましょう！\n"
                "You have mild fatigue. Let's refresh a bit!"
            )
        else:
            st.session_state.result = (
                "■ 注意(ちゅうい)！ストレスが高(たか)めです。休息(きゅうそく)を取(と)ってください。\n"
                "Caution! High stress level. Please take some rest."
            )
        st.session_state.step = 3
        st.rerun()

# Step 3
elif st.session_state.step == 3:
    st.subheader("あなたのストレス診断結果")
    st.text(st.session_state.result)

    if st.button("最初に戻る"):
        st.session_state.clear()
        st.rerun()
