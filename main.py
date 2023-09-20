from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0 or len(email_data) == 0:
        messagebox.showwarning(title="Error", message="Fields should not be empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)


# ---------------------------- SEARCH ENTRIES ------------------------------- #


def search_website():
    website_data = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website_data in data:
            search_mail = data[website_data]['email']
            search_password = data[website_data]['password']
            messagebox.showinfo(title=f"{website_data}",
                                message=f"Email: {search_mail}\nPassword: {search_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_data} found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
website_label.config(pady=5)

email_label = Label(text="Username/Email:")
email_label.grid(column=0, row=3)
email_label.config(pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=4)
password_label.config(pady=5)

# Entries

website_input = Entry(width=50)
website_input.grid(column=1, row=2, sticky="EW")
website_input.focus()

email_input = Entry(width=50)
email_input.grid(column=1, row=3, sticky="EW")
email_input.insert(0, "siddhuadari633@gmail.com")

password_input = Entry(width=40)
password_input.grid(column=1, row=4, sticky="EW")

# Buttons

search_button = Button(text="Search", command=search_website)
search_button.grid(column=2, row=2, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=4)

add_button = Button(width=40, text="Add", command=add_data)
add_button.grid(column=1, row=5)

# Canvas

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1,row=1)

window.mainloop()
