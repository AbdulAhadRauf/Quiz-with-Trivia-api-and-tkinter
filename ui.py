from tkinter import*
from question_brain import QuizBrain
THEME_COLOR = "#375362"
class Ui:
    def __init__(self, question_brain: QuizBrain):
        self.question_brain = question_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg = THEME_COLOR, padx=20, pady=20)
        self.scoretitle = Label(text="Score: 0", bg= THEME_COLOR, fg = "white")
        self.scoretitle.grid(row= 0, column = 1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.tick= PhotoImage(file = "green-tick-checkmark-icon-vector.png")
        self.cross= PhotoImage(file = "cross-mark-icon-vector-44545882.png")
        self.canvastext = self.canvas.create_text(150,125, text="", width= 250, fill= THEME_COLOR, font= ("ariel", 15, "italic"))
        self.canvas.grid(row =1 , column= 0, columnspan= 2)
        self.right = Button(image= self.tick, bg="black" ,width= 100, command = self.righthai)
        self.right.grid(row=2, column=0, pady=10)
        self.wrong = Button(image= self.cross, bg = "black" ,width= 100, command = self.wronghai)
        self.wrong.grid(row=2, column=1)
        self.display_next_question()
        self.window.mainloop()

    def righthai(self):
        self.show_output(self.question_brain.check_answer(guess="True"))

    def wronghai(self):
        self.show_output(self.question_brain.check_answer(guess="False"))

    def show_output(self, status):
        if status:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.display_next_question)



    def display_next_question(self):
        self.canvas.config(bg="white")
        if self.question_brain.still_has_questions():
            self.scoretitle.config(text=f"Score: {self.question_brain.score}") 
            qtext = self.question_brain.next_question()
            self.canvas.itemconfig(self.canvastext, text =qtext)
        else:
            self.canvas.itemconfig(self.canvastext, text= f"             {self.question_brain.score}/10\nThat's the end of it. For all and more see you tomorrow")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")