from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

FONT_NAME = 'Fira Code'
FONT_SIZE = 12
FONT_WGTH = 'bold'


def reset_values():
    website_entry.delete(0, 'end')
    password_input.delete(0, 'end')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_username_input.get()
    password = password_input.get()

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"\nsite: {website} | email/username: {email} | Passwd: {password}")
                reset_values()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, FONT_WGTH))
web_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE, FONT_WGTH))
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, 'devnetman@gmail.com')

password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE, FONT_WGTH))
password_label.grid(column=0, row=3)
password_input = Entry(width=19)
password_input.grid(row=3, column=1)

generate_passwd_btn = Button(text="Generate Password", width=12, font='bold', command=generate_password)
generate_passwd_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=33, command=save_info)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
