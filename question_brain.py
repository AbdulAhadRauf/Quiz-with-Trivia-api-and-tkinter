import html
class QuizBrain:
    def __init__(self, question_bank):
        self.score = 0
        self.currentqanda = None
        self.question_number = 0
        self.question_list = question_bank

    def still_has_questions(self):
        return self.question_number< len(self.question_list)

    def next_question(self):
        self.currentqanda = self.question_list[self.question_number]
        self.question_number += 1
        currq = html.unescape(self.currentqanda.question)
        return f" Q.{self.question_number}) {currq} (T/F)"
        # guess = input(f" Q.{self.question_number}) {currq} (T/F)")
        self.check_answer(guess, currentqanda.question, currentqanda.answer)


    def check_answer(self, guess):
        corrans = self.currentqanda.answer
        que = self.currentqanda.question
        if guess == corrans:
            self.score +=1
            return True
        else:
            return False
