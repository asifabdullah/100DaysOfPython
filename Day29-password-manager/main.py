from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----------------------------Search Password--------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                              f"{email} "f"\nPassword: {password} \nIs "
                                                              f"it ok to save?")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as file:
                    # Reading the old data
                    data = json.load(file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open(file="data.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# email/username label
website_label = Label(text="Email/Username:")
website_label.grid(column=0, row=2)

# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# website input
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# email/username input
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "asif.ndc@gmail.com")

# password input
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Search Button
button_search = Button(text="Search", command=find_password, width=13)
button_search.grid(column=2, row=1)
# password Generate Button
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)

# Add Button
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
