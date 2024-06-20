
import tkinter as tk
from tkinter import messagebox
import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def register():
   
    name = name_entry.get()
    email = email_entry.get()
    city = city_entry.get()
    skills= skills_entry.get()
    expirence=skills_entry.get()

 
    if not name or not email or not city or not skills or not expirence:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    # Validate that the email is in a valid format
    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    # If everything is valid, register the user and show a success message
    messagebox.showinfo("Success", "User registered successfully!")

    # Redirect the user to the login page
    login_window.deiconify()
    window.withdraw()


def login():
 
    login_window.deiconify()
    window.withdraw()

def back_to_register():
   
    window.deiconify()
    login_window.withdraw()

def login_validate():

    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields must be filled out.")
        return


 
    messagebox.showinfo("Success", "User logged in successfully!")

window = tk.Tk()
window.title("Job Portal - Register")


name_label = tk.Label(window, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

email_label = tk.Label(window, text="Email")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1)

city_label = tk.Label(window, text="city")
city_label.grid(row=2, column=0)
city_entry = tk.Entry(window)
city_entry.grid(row=2, column=1)

skills_label = tk.Label(window, text="skills")
skills_label.grid(row=3, column=0)
skills_entry = tk.Entry(window)
skills_entry.grid(row=3, column=1)

expirence_label = tk.Label(window, text="expirence")
expirence_label.grid(row=4, column=0)
expirence_entry = tk.Entry(window)
expirence_entry.grid(row=4, column=1)

# Create the registration button
register_button = tk.Button(window, text="Register", command=register)
register_button.grid(row=5, column=0)

# Create the login button
login_button = tk.Button(window, text="Already registered? Login", command=login)
login_button.grid(row=5, column=1)

# Create the login window
login_window = tk.Toplevel()
login_window.title("Job Portal - Login")
login_window.withdraw()


login_username_label = tk.Label(login_window, text="username")
login_username_label.grid(row=0, column=0)
login_username_entry = tk.Entry(login_window)
login_username_entry.grid(row=0, column=1)

login_password_label = tk.Label(login_window, text="Password")
login_password_label.grid(row=1, column=0)
login_password_entry = tk.Entry(login_window, show="*")
login_password_entry.grid(row=1, column=1)

# Create the login button for the login window
login_login_button = tk.Button(login_window, text="Login", command=login_validate)
login_login_button.grid(row=2, column=0)


register_button = tk.Button(login_window, text="Register", command=back_to_register)
register_button.grid(row=2, column=1)


window.mainloop()