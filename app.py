import streamlit as st

# 質問リスト（日本語＋英語）
questions = [
    ("あなたの強（つよ）みはなんですか？", "What are your strengths?"),
    ("あなたの弱点（じゃくてん）はなんですか？", "What are your weaknesses?"),
    ("どんな人物（じんぶつ）でありたいですか？", "What kind of person do you want to be?"),
    ("大切（たいせつ）にしていることはなんですか？", "What do you value?"),
    ("最近（さいきん）の自分（じぶん）の流行（りゅうこう）はなんですか？", "What's trending among you these days?"),
    ("弊社（へいしゃ）に入社（にゅうしゃ）したらどんなことがしたいですか？", "What would you like to do if you joined our company?")
]

# フィードバックを生成する関数
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

st.title("就活準備チャットボット（日本語＋英語）")

step = st.session_state.step

# 質問を1つずつ表示
if step < len(questions):
    jp_q, en_q = questions[step]
    with st.chat_message("assistant"):
        st.markdown(f"Q{step+1}: {jp_q}\n*{en_q}*")

    user_input = st.chat_input("あなたの答えを入力してください / Type your answer here")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        fb_jp, fb_en = generate_feedback(jp_q, user_input)
        st.session_state.answers.append(user_input)
        st.session_state.feedbacks.append((fb_jp, fb_en))
        st.session_state.step += 1

        with st.chat_message("assistant"):
            st.markdown("フィードバック / Feedback:")
            st.success(f"{fb_jp}\n\n*{fb_en}*")

        st.experimental_rerun()

# 全質問に答えた後のまとめ
else:
    st.markdown("---")
    st.header("あなたの就活プロフィールまとめ")

    for i in range(len(questions)):
        jp_q, _ = questions[i]
        st.subheader(f"Q{i+1}: {jp_q}")
        st.write(f"あなたの回答: {st.session_state.answers[i]}")
        fb_jp, fb_en = st.session_state.feedbacks[i]
        st.markdown("フィードバック:")
        st.write(fb_jp)
        st.markdown(f"*{fb_en}*")

    if st.button("最初からやり直す"):
        st.session_state.clear()
        st.experimental_rerun()
