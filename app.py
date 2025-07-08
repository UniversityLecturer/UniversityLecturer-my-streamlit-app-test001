import streamlit as st

# 質問リスト（日＋英）
questions = [
    ("あなたの強みはなんですか？", "What are your strengths?"),
    ("あなたの弱点はなんですか？", "What are your weaknesses?"),
    ("どんな人物でありたいですか？", "What kind of person do you want to be?"),
    ("大切にしていることはなんですか？", "What do you value?"),
    ("最近の自分の流行はなんですか？", "What's trending among you these days?"),
    ("入社したら何がしたいですか？", "What would you like to do if you joined our company?")
]

# フィードバック関数
def generate_feedback(question, answer):
    if "強み" in question:
        return (
            "あなたの「強み」はとても大切です。その強みを使った経験を話すと、もっと良くなります。",
            "Your strength is very important. If you talk about your experience using that strength, it will be even better."
        )
    elif "弱点" in question:
        return (
            "自分の「弱点」を話せるのは素晴らしいことです。その弱点を改善するために何をしているか話すと良いです。",
            "Talking about your weakness is great. It's good to explain how you are working to improve it."
        )
    elif "大切" in question or "価値" in question:
        return (
            "「大切にしていること」があるのは素敵です。なぜそれを大切にしているのか話すと、より伝わります。",
            "It is great to have something you value. Explaining why helps others understand you more."
        )
    elif "入社" in question:
        return (
            "「やりたいこと」がはっきりしていて、やる気が伝わります。会社の仕事とつなげて話すと良くなります。",
            "Your motivation is clear. Connect your ideas to the company’s work to make it better."
        )
    else:
        return (
            "あなたの考えは面白いです。もっと詳しく話すと、伝わりやすくなります。",
            "Your idea is interesting. Giving more details will help others understand you better."
        )

# セッション状態の初期化
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.feedbacks = []

st.title("Job hunting practice｜就活練習")

step = st.session_state.step

# ✅ フォーム全体の囲いをCSSで非表示
st.markdown("""
<style>
/* st.form に自動で付与される囲い（div[data-testid="stForm"]）を非表示に */
div[data-testid="stForm"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# 質問の表示と入力フォーム
if step < len(questions):
    jp_q, en_q = questions[step]

    st.write(f"Q{step+1}: {jp_q}")
    st.caption(en_q)

    with st.form(key="answer_form", clear_on_submit=True):
        user_input = st.text_input("あなたの答えを入力してください", key=f"input_{step}")
        col1, col2 = st.columns([6, 1])
        with col2:
            submitted = st.form_submit_button("次へ")

    if submitted and user_input.strip():
        st.session_state.answers.append(user_input)
        fb_jp, fb_en = generate_feedback(jp_q, user_input)
        st.session_state.feedbacks.append((fb_jp, fb_en))
        st.session_state.step += 1
        st.rerun()
    elif submitted:
        st.warning("入力してください。")

# 回答がすべて完了したらまとめを表示
else:
    st.header("あなたの就活プロフィールまとめ")

    for i in range(len(questions)):
        jp_q, en_q = questions[i]
        st.subheader(f"Q{i+1}: {jp_q}")
        st.caption(en_q)
        st.markdown(f"**あなたの回答:** {st.session_state.answers[i]}")
        fb_jp, fb_en = st.session_state.feedbacks[i]
        st.markdown(f"**フィードバック:**\n{fb_jp}\n\n*{fb_en}*")

    if st.button("最初からやり直す"):
        st.session_state.clear()
        st.rerun()
