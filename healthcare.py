import streamlit as st

# セッション初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""

st.title("health check")
st.caption("人事アプリ")

# ステップ1：質問1
if st.session_state.step == 1:
    st.subheader("01. 最近、疲れていますか？")
    st.caption("Are you tired recently?")
    st.markdown("あなたの回答を選んでください：")

    answer = st.radio(
        label="",
        options=["yes", "no"],
        horizontal=True,
        key="q1"
    )

    if st.button("次へ", key="to_step2"):
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

# ステップ2：質問2
elif st.session_state.step == 2:
    st.subheader("02. 睡眠時間は足りていますか？")
    st.caption("Do you get enough sleep?")
    st.markdown("あなたの回答を選んでください：")

    answer = st.radio(
        label="",
        options=["yes", "no"],
        horizontal=True,
        key="q2"
    )

    if st.button("診断する", key="to_result"):
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

# ステップ3：結果表示
elif st.session_state.step == 3:
    st.subheader("あなたのヘルスケア診断結果")
    st.text(st.session_state.result)

    if st.button("最初に戻る"):
        st.session_state.clear()
        st.rerun()
