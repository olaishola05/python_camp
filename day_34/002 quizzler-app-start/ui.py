from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.score_label.config(fg="white")
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Question',
            font=("Arial", 20, "italic"),
            fill="black"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(
            image=check_img,
            highlightthickness=0,
            command=self.answer_true
        )
        self.check_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=false_img,
            highlightthickness=0,
            command=self.answer_false
        )
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz")
            self.false_btn.config(state="disabled")
            self.check_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
