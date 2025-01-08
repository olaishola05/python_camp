from tkinter import *


def convert_miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609344)
    km_conversion.config(text=f"{km}")


window = Tk()
window.minsize(width=500, height=300)
window.title("Mile to KM Converter")
window.config(padx=100, pady=100)

font_props = ("Fira code", 20, "bold")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=font_props)
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=font_props)
equal_label.grid(column=0, row=1)

km_conversion = Label(text="0", font=font_props)
km_conversion.grid(column=1, row=1)

km_label = Label(text="Km", font=font_props)
km_label.grid(column=2, row=1)
km_label.config(padx=10)

button = Button(text="Calculate", font=font_props, command=convert_miles_to_km)
button.grid(column=1, row=2)



window.mainloop()