import streamlit as st

# 初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""

st.title("ストレスチェックチャットボット")
st.caption("Stress Check Chatbot")

# 質問01：疲れていますか？
if st.session_state.step == 1:
    st.subheader("01. 最近、疲れていますか？")
    st.caption("Are you tired recently?")
    answer = st.radio("あなたの回答を選んでください", ["yes", "no"], key="q1")

    if st.button("次へ"):
        st.session_state.stress = answer
        if answer == "yes":
            st.session_state.step = 2
        elif answer == "no":
            st.session_state.result = "■ 良(よ)かったです！引(ひ)き続(つづ)き健康(けんこう)に過(す)ごしましょう。\nGood to hear! Stay healthy."
            st.session_state.step = 3

# 質問02：睡眠は足りていますか？
elif st.session_state.step == 2:
    st.subheader("02. 睡眠時間は足りていますか？")
    st.caption("Do you get enough sleep?")
    answer = st.radio("あなたの回答を選んでください", ["yes", "no"], key="q2")

    if st.button("診断する"):
        st.session_state.sleep = answer
        if answer == "yes":
            st.session_state.result = "■ 軽(かる)い疲(つか)れですね。少(すこ)しリフレッシュしましょう！\nYou have mild fatigue. Let's refresh a bit!"
        else:
            st.session_state.result = "■ 注意(ちゅうい)！ストレスが高(たか)めです。休息(きゅうそく)を取(と)ってください。\nCaution! High stress level. Please take some rest."
        st.session_state.step = 3

# 結果表示
elif st.session_state.step == 3:
    st.subheader("あなたのストレス診断結果")
    st.text(st.session_state.result)

    if st.button("もう一度診断する"):
        st.session_state.step = 1
        st.session_state.stress = ""
        st.session_state.sleep = ""
        st.session_state.result = ""
