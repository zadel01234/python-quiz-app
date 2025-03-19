from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("The Quizzler")
        self.root.geometry("340x500+100+100")
        self.root.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text= f"Score: {0}",fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row=0, column =1, pady= 10)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR, font = ("Arial", 20, "italic"), width=280)
        self.canvas.grid(row = 1, column = 0, columnspan = 2)

        wrong = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong, highlightthickness=0, command=self.right_answer)
        self.wrong.grid(row = 2, column = 0, pady=15)

        right = PhotoImage(file="images/true.png")
        self.right = Button(image=right, highlightthickness=0, command=self.wrong_answer)
        self.right.grid(row = 2, column = 1, pady=15)

        self.get_next_question()
        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you've reached the end")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')

        self.root.after(1000,self.get_next_question)