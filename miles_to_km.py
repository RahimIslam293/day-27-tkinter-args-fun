from tkinter import *

def calculate():
    miles = int(miles_entry.get())
    km = str(round(miles * 1.6, 1))
    converted_label.config(text=km)


window = Tk()
window.config(width=300, height=300)
window.title("Mile to Km Converter")

miles_entry = Entry()
miles_entry.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text="Convert", command=calculate)
button.grid(column=1,row=2)

window.mainloop()