import streamlit as st

# セッション初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""
    st.session_state.clicked = None

st.title("ストレスチェックチャットボット")

# カスタムCSSで幅とレイアウト制御
st.markdown("""
<style>
.button-row {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 1em;
}
.button-row form {
    width: 60%;
    text-align: center;
}
button {
    width: 100%;
    padding: 0.5em 1em;
    font-size: 1rem;
    border: none;
    border-radius: 6px;
    background-color: #2c6ed5;
    color: white;
    cursor: pointer;
}
button:hover {
    background-color: #1f4fbf;
}
</style>
""", unsafe_allow_html=True)

def render_custom_buttons(question_key):
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.form(key=f"{question_key}_yes_form").form_submit_button("yes"):
            return "yes"
    with col2:
        if st.form(key=f"{question_key}_no_form").form_submit_button("no"):
            return "no"

    st.markdown('</div>', unsafe_allow_html=True)
    return None

# ステップ1
if st.session_state.step == 1:
    st.subheader("01. 最近、疲れていますか？")
    st.caption("Are you tired recently?")
    st.markdown("あなたの回答を選んでください：")
    choice = render_custom_buttons("stress")

    if choice:
        st.session_state.stress = choice
        if choice == "yes":
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
    st.markdown("あなたの回答を選んでください：")
    choice = render_custom_buttons("sleep")

    if choice:
        st.session_state.sleep = choice
        if choice == "yes":
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

# ステップ3
elif st.session_state.step == 3:
    st.subheader("あなたのストレス診断結果")
    st.text(st.session_state.result)

    if st.button("最初に戻る"):
        st.session_state.clear()
        st.rerun()
