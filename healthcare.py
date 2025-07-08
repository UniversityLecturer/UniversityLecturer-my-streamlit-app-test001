import streamlit as st

# セッション初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""
    st.session_state.submitted = False  # 再実行用のトリガー

st.title("ストレスチェックチャットボット")
st.caption("Stress Check Chatbot")

# ステップ1：質問1
if st.session_state.step == 1:
    st.subheader("01. 最近、疲れていますか？")
    st.caption("Are you tired recently?")

    col_left, _ = st.columns([1, 5])
    with col_left:
        # horizontal=True を追加
        stress = st.radio("あなたの回答を選んでください", ["yes", "no"], key="q1", horizontal=True)

        if st.button("次へ", key="to_step2"):
            st.session_state.stress = stress
            if stress == "yes":
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

    col_left, _ = st.columns([1, 5])
    with col_left:
        # horizontal=True を追加
        sleep = st.radio("あなたの回答を選んでください", ["yes", "no"], key="q2", horizontal=True)

        if st.button("診断する", key="to_result"):
            st.session_state.sleep = sleep
            if sleep == "yes":
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

# ステップ3：診断結果表示
elif st.session_state.step == 3:
    st.subheader("あなたのストレス診断結果")
    st.text(st.session_state.result)

    col_left, _ = st.columns([1, 5])
    with col_left:
        if st.button("最初に戻る", key="reset"):
            st.session_state.step = 1
            st.session_state.stress = ""
            st.session_state.sleep = ""
            st.session_state.result = ""
            st.rerun()
