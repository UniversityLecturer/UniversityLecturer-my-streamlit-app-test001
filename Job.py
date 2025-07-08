{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN9gxJBZ0Rw11ovAygPCvdq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/UniversityLecturer/UniversityLecturer-my-streamlit-app-test001/blob/main/Job.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "# 質問リスト\n",
        "questions = [\n",
        "    \"あなたの強（つよ）みはなんですか？\\n　　What are your strengths?\",\n",
        "    \"あなたの弱点（じゃくてん）はなんですか？\\n　　What are your weaknesses?\",\n",
        "    \"どんな人物（じんぶつ）でありたいですか？\\n　　What kind of person do you want to be?\",\n",
        "    \"大切（たいせつ）にしていることはなんですか？\\n　　What do you value?\",\n",
        "    \"最近（さいきん）の自分（じぶん）の流行（りゅうこう）はなんですか？\\n　　What's trending among you these days?\",\n",
        "    \"弊社（へいしゃ）に入社（にゅうしゃ）したらどんなことがしたいですか？\\n　　What would you like to do if you joined our company?\"\n",
        "]\n",
        "\n",
        "# フィードバック生成関数\n",
        "def generate_feedback(question, answer):\n",
        "    if \"強み\" in question:\n",
        "        return (\n",
        "            \"あなたの「強み」はとても大切です。その強みを使った経験を話すと、もっと良くなります。\\n\"\n",
        "            \"Your strength is very important. If you talk about your experience using that strength, it will be even better.\"\n",
        "        )\n",
        "    elif \"弱点\" in question:\n",
        "        return (\n",
        "            \"自分の「弱点」を話せるのは素晴らしいことです。その弱点を改善するために何をしているか話すと良いです。\\n\"\n",
        "            \"Talking about your weakness is great. It's good to explain how you are working to improve it.\"\n",
        "        )\n",
        "    elif \"大切\" in question or \"価値\" in question:\n",
        "        return (\n",
        "            \"「大切にしていること」があるのは素敵です。なぜそれを大切にしているのか話すと、より伝わります。\\n\"\n",
        "            \"It is great to have something you value. Explaining why helps others understand you more.\"\n",
        "        )\n",
        "    elif \"入社\" in question:\n",
        "        return (\n",
        "            \"「やりたいこと」がはっきりしていて、やる気が伝わります。会社の仕事とつなげて話すと良くなります。\\n\"\n",
        "            \"Your motivation is clear. Connect your ideas to the company’s work to make it better.\"\n",
        "        )\n",
        "    else:\n",
        "        return (\n",
        "            \"あなたの考えは面白いです。もっと詳しく話すと、伝わりやすくなります。\\n\"\n",
        "            \"Your idea is interesting. Giving more details will help others understand you better.\"\n",
        "        )\n",
        "\n",
        "# StreamlitアプリのUI\n",
        "st.title(\"就活準備チャットボット\")\n",
        "st.write(\"以下の質問に答えて、フィードバックをもらいましょう。\")\n",
        "\n",
        "answers = []\n",
        "feedbacks = []\n",
        "\n",
        "# フォーム入力エリア\n",
        "with st.form(\"interview_form\"):\n",
        "    for i, q in enumerate(questions):\n",
        "        answer = st.text_area(f\"Q{i+1}: {q}\", key=f\"q{i}\")\n",
        "        answers.append(answer)\n",
        "\n",
        "    submitted = st.form_submit_button(\"フィードバックを見る\")\n",
        "\n",
        "# 結果の表示\n",
        "if submitted:\n",
        "    st.markdown(\"---\")\n",
        "    st.header(\"あなたの就活プロフィールまとめ\")\n",
        "\n",
        "    for i in range(len(questions)):\n",
        "        st.subheader(f\"Q{i+1}: {questions[i].splitlines()[0]}\")\n",
        "        st.write(f\"【あなたの答え】\\n{answers[i]}\")\n",
        "        feedback = generate_feedback(questions[i], answers[i])\n",
        "        st.text(feedback)\n"
      ],
      "metadata": {
        "id": "T8usdGDQFlzT"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}