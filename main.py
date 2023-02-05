from question_list import question_list
import question_model
import question_brain
from ui import Ui
question_bank = []


for i in range(len(question_list)):
    q = question_list[i]["question"]
    a = question_list[i]["correct_answer"]
    x = question_model.Question(q,a)
    question_bank.append(x)

quiz = question_brain.QuizBrain(question_bank)
ui = Ui(quiz)

# while quiz.still_has_questions():
# quiz.next_question()



