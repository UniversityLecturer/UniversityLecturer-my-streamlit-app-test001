import streamlit as st

# 質問リスト（日本語＋英語）
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

# セッションの初期化
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.feedbacks = []

st.title("就活準備チャット（アイコンなし）")

step = st.session_state.step

# 回答が完了していないとき
if step < len(questions):
    jp_q, en_q = questions[step]

    st.markdown(f"**Q{step+1}:** {jp_q}  \n*{en_q}*")

    with st.form(key="answer_form"):
        user_input = st.text_input("あなたの答えを入力してください")
        submitted = st.form_submit_button("送信する")

    if submitted and user_input.strip():
        st.session_state.answers.append(user_input)
        fb_jp, fb_en = generate_feedback(jp_q, user_input)
        st.session_state.feedbacks.append((fb_jp, fb_en))
        st.session_state.step += 1
        st.success("回答が記録されました。次の質問に進んでください。")
    elif submitted:
        st.warning("回答を入力してください。")

# すべての質問が終了したらまとめを表示
else:
    st.header("あなたの就活プロフィールまとめ")

    for i in range(len(questions)):
        jp_q, en_q = questions[i]
        st.markdown(f"**Q{i+1}:** {jp_q}  \n*{en_q}*")
        st.markdown(
            f"""
            <div style="background-color:#f0f2f6; padding:10px; border-radius:10px; margin-bottom:5px;">
            <strong>あなたの回答:</strong><br>{st.session_state.answers[i]}
            </div>
            <div style="background-color:#e2f4ea; padding:10px; border-radius:10px; margin-bottom:20px;">
            <strong>フィードバック:</strong><br>{st.session_state.feedbacks[i][0]}<br><i>{st.session_state.feedbacks[i][1]}</i>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("最初からやり直す"):
        st.session_state.clear()
        st.experimental_rerun()
