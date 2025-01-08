from tkinter import *
import pandas
from random import shuffle, choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

words = {}
word = {}

# ---------------------------- Reading the from file ------------------------------- #
try:
    quote = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
    print(len(words), 'Original file')
    shuffle(words)
else:
    words = quote.to_dict(orient="records")
    shuffle(words)


# ---------------------------- Generate Random Word ------------------------------- #
def generate_next_card():
    global word, flip
    window.after_cancel(flip)
    try:
        word = choice(words)
    except TypeError as error_msg:
        print(error_msg)
    else:
        canvas.itemconfig(title, text="French", fill='black')
        canvas.itemconfig(word_text, text=word['French'], fill='black')
        canvas.itemconfig(canvas_img, image=front_card_img)
        flip = window.after(3000, flip_card)


# ---------------------------- Reading the from file ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word_text, text=word['English'], fill='white')


# ---------------------------- Remove Known Word ------------------------------- #
def remove_learned_word():
    try:
        words.remove(word)
    except ValueError as err_msg:
        print(err_msg)
    else:
        df = pandas.DataFrame(words)
        df.to_csv("data/words_to_learn.csv", index=False)
        generate_next_card()


# ---------------------------- Flash Card UI ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip = window.after(3000, flip_card)

front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(410, 263, image=front_card_img)
title = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=generate_next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=remove_learned_word)
right_btn.grid(row=1, column=1)

generate_next_card()

mainloop()
