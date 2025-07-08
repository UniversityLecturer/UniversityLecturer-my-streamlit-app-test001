import streamlit as st

# セッション初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.stress = ""
    st.session_state.sleep = ""
    st.session_state.result = ""

st.title("ストレスチェックチャットボット")
st.caption("Stress Check Chatbot")

# カスタムボタンCSS：列内60%幅にして中央寄せ
st.markdown("""
<style>
.custom-button-wrapper {
    width: 60%;
    margin: auto;
}
.custom-button-wrapper > div {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# 共通：yes/no 横並び選択ボタン（60%幅）
def render_yes_no_buttons(key_prefix):
    col1, col2 = st.columns([1, 1])
    selected = None

    with col1:
        with st.container():
            st.markdown('<div class="custom-button-wrapper">', unsafe_allow_html=True)
            if st.button("yes", key=f"{key_prefix}_yes"):
                selected = "yes"
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="custom-button-wrapper">', unsafe_allow_html=True)
            if st.button("no", key=f"{key_prefix}_no"):
                selected = "no"
            st.markdown('</div>', unsafe_allow_html=True)

    return selected

# Step 1：質問① 疲れているか
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

# Step 2：質問② 睡眠足りてるか
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

# Step 3：診断結果
elif st.session_state.step == 3:
    st.subheader("あなたのストレス診断結果")
    st.text(st.session_state.result)

    if st.button("最初に戻る"):
        st.session_state.clear()
        st.rerun()
