# from langchain import ChatOpenAI
from langchain.chat_models import ChatOpenAI


class LLM:
    def __init__(self):
        self.model = ChatOpenAI()

    def evaluate_answer(self, question, answer):
        prompt = f"Question: {question}\nAnswer: {answer}\nScore the answer out of 10 and provide feedback."
        response = self.model.chat(prompt)
        score = int(response.get("score", 0))
        feedback = response.get("feedback", "No feedback provided.")
        return score, feedback
