import tkinter

window = tkinter.Tk()
window.title("My GUI App")
window.minsize(width=500, height=400)

label = tkinter.Label(text="Name", font=("Fira code", 34))
label.pack(side="left")






window.mainloop()