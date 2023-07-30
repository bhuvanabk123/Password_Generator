from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#
#Password Generator
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for char in range(nr_letters)]

    symbol_list = [random.choice(symbols) for symbol in range(nr_symbols) ]

    number_list = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = letter_list+symbol_list+number_list

    random.shuffle(password_list)

    password = "".join(password_list)


    password_input.insert(0, password)
    pyperclip.copy(password)



## Save the password:

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title= "OOPS!", message = "Please dont leave any field empty.")
        yes_no = False
    else:
        yes_no = messagebox.askokcancel(title='Website', message = f"These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it okay to save?")

    if yes_no:
        data = open('data.txt', 'a')
        data.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)


# ############## UI INTERFACE
window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50)

canvas = Canvas(height = 200,width = 200)
key_image = PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = key_image)
canvas.grid(column = 1, row = 0)

website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text = "Email/Username:")
email_label.grid(column=0, row = 2)


password_label =  Label(text = "Password:")
password_label.grid(column=0, row = 3)


website_input = Entry(width=40)
website_input.grid(column = 1, row = 1, columnspan=2)
website_input.focus()

email_input = Entry(width=40)
email_input.grid(column=1, row =2, columnspan=2)
email_input.insert(0, "bhvanabk@gmail.com")

password_input = Entry(width = 22)
password_input.grid( row = 3, column=1 )


generate_pass_button = Button(text = 'Generate Password', command = password_generator)
generate_pass_button.grid( row =3, column=2)

add_button = Button(text = "Add", width = 34, command=save)
add_button.grid(row = 4,column=1, columnspan=2)


window.mainloop()

