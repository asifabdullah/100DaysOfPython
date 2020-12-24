from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NAME_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

data = pandas.read_csv("data/french_words.csv")
print(data)
print(type(data))

# --------------------------------UI SETUP------------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
language_name = canvas.create_text(400, 150, text="French", font=LANGUAGE_NAME_FONT)
word = canvas.create_text(400, 263, text="French", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)


window.mainloop()

