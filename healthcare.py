import streamlit as st

# セッション初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""

st.title("ストレスチェックチャットボット")
st.caption("Stress Check Chatbot")

# 共通レイアウト：中央寄せ用の関数
def center_block(label_text, options, key, button_label, action_key):
    # 空白で左右の余白を確保
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(f"<div style='text-align: center; font-weight: bold;'>{label_text}</div>", unsafe_allow_html=True)
        answer = st.radio(
            label="",
            options=options,
            horizontal=True,
            key=key,
            index=0
        )
        # ボタン中央表示
        if st.button(button_label, key=action_key):
            return answer, True
        return answer, False

# ステップ1
if st.session_state.step == 1:
    st.subheader("01. 最近、疲れていますか？")
    st.caption("Are you tired recently?")
    answer, submitted = center_block(
        label_text="あなたの回答を選んでください",
        options=["yes", "no"],
        key="q1",
        button_label="次へ",
        action_key="to_step2"
    )
    if submitted:
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

# ステップ2
elif st.session_state.step == 2:
    st.subheader("02. 睡眠時間は足りていますか？")
    st.caption("Do you get enough sleep?")
    answer, submitted = center_block(
        label_text="あなたの回答を選んでください",
        options=["yes", "no"],
        key="q2",
        button_label="診断する",
        action_key="to_result"
    )
    if submitted:
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

# ステップ3：診断結果表示
elif st.session_state.step == 3:
    st.subheader("あなたのストレス診断結果")
    st.text(st.session_state.result)

    left, center, right = st.columns([1, 2, 1])
    with center:
        if st.button("最初に戻る", key="reset"):
            st.session_state.step = 1
            st.session_state.stress = ""
            st.session_state.sleep = ""
            st.session_state.result = ""
            st.rerun()
