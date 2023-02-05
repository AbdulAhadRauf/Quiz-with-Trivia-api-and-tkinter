import html
class Question:
    def __init__(self, question, answer):
        self.question  = html.unescape(question)
        self.answer = html.unescape(answer)