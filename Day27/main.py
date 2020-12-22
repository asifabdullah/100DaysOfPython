from tkinter import *


def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am  a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


# New Button
button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

# Entry
input = Entry()
input.grid(column=3, row=3)

window.mainloop()
