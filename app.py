import streamlit as st

# 質問リスト
questions = [
    "あなたの強（つよ）みはなんですか？\n　　What are your strengths?",
    "あなたの弱点（じゃくてん）はなんですか？\n　　What are your weaknesses?",
    "どんな人物（じんぶつ）でありたいですか？\n　　What kind of person do you want to be?",
    "大切（たいせつ）にしていることはなんですか？\n　　What do you value?",
    "最近（さいきん）の自分（じぶん）の流行（りゅうこう）はなんですか？\n　　What's trending among you these days?",
    "弊社（へいしゃ）に入社（にゅうしゃ）したらどんなことがしたいですか？\n　　What would you like to do if you joined our company?"
]

# フィードバック生成関数
def generate_feedback(question, answer):
    if "強み" in question:
        return "あなたの「強み」はとても大切です。その強みを使った経験を話すと、もっと良くなります。\nYour strength is very important. If you talk about your experience using that strength, it will be even better."
    elif "弱点" in question:
        return "自分の「弱点」を話せるのは素晴らしいことです。その弱点を改善するために何をしているか話すと良いです。\nTalking about your weakness is great. It's good to explain how you are working to improve it."
    elif "大切" in question or "価値" in question:
        return "「大切にしていること」があるのは素敵です。なぜそれを大切にしているのか話すと、より伝わります。\nIt is great to have something you value. Explaining why helps others understand you more."
    elif "入社" in question:
        return "「やりたいこと」がはっきりしていて、やる気が伝わります。会社の仕事とつなげて話すと良くなります。\nYour motivation is clear. Connect your ideas to the company’s work to make it better."
    else:
        return "あなたの考えは面白いです。もっと詳しく話すと、伝わりやすくなります。\nYour idea is interesting. Giving more details will help others understand you better."

# StreamlitアプリのUI
st.title("就活準備チャットボット")
st.write("以下の質問に答えて、フィードバックをもらいましょう。")

answers = []

with st.form("interview_form"):
    for i, q in enumerate(questions):
        answer = st.text_area(f"Q{i+1}: {q}", key=f"q{i}")
        answers.append(answer)

    submitted = st.form_submit_button("フィードバックを見る")

if submitted:
    st.markdown("---")
    st.header("あなたの就活プロフィールまとめ")

    for i in range(len(questions)):
        st.subheader(f"Q{i+1}: {questions[i].splitlines()[0]}")
        st.write(f"【あなたの答え】\n{answers[i]}")
        st.text(generate_feedback(questions[i], answers[i]))
