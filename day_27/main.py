from tkinter import *


def button_clicked():
    new_text = input_box.get()
    label["text"] = new_text.title()


window = Tk()
window.title("Widgets")
window.minsize(width=500, height=500)

# Adding padding to entire window
window.config(padx=100, pady=50)

label = Label(text="Hello", font=("Fira code", 25, "bold"))
label.grid(column=0, row=0)

label["text"] = "Come on"
label.config(text="Terminus")
# Adding padding to individual element
label.config(padx=20, pady=0)

new_button = Button(text="Test Btn")
new_button.grid(column=2, row=0)

button = Button(text="submit", command=button_clicked)
button.grid(column=1, row=1)

input_box = Entry(width=20)
input_box.insert(END, string="Some text to begin with.")
input_box.grid(column=3, row=3)

window.mainloop()
