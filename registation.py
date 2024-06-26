import tkinter as tk
from tkinter import messagebox
import re

from db import db

from display import views

class JobPortal:
    def __init__(self, master):
        self.master = master
        self.master.title("Job Portal - Register")

        views.HomeScreenDisplay(self.master)
        return

        # self.master.geometry("600x450")
        self.center_window(self.master, 600, 450)

        self.register_window = self.render_register_window()
        self.register_window.pack()

        

        self.login_window = self.render_login_window()
        self.login_frame.pack()

        

    def create_register_widgets(self):

        tk.Label(self.register_frame, text="Username:", bg='#f0f0f0', fg='#333').grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self.register_frame, width=30, bg='#fff', fg='#333')
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.register_frame, text="Password:", bg='#f0f0f0', fg='#333').grid(row=1, column=0, sticky="w")
        self.register_password_entry = tk.Entry(self.register_frame, width=30, bg='#fff', fg='#333', show="*")
        self.register_password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.register_frame, text="Name:", bg='#f0f0f0', fg='#333').grid(row=2, column=0, sticky="w")
        self.name_entry = tk.Entry(self.register_frame, width=30, bg='#fff', fg='#333')
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.register_frame, text="Email:", bg='#f0f0f0', fg='#333').grid(row=3, column=0, sticky="w")
        self.email_entry = tk.Entry(self.register_frame, width=30, bg='#fff', fg='#333')
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.register_frame, text="City:", bg='#f0f0f0', fg='#333').grid(row=4, column=0, sticky="w")
        self.city_entry = tk.Entry(self.register_frame, width=30, bg='#fff', fg='#333')
        self.city_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.register_frame, text="Skills:", bg='#f0f0f0', fg='#333').grid(row=5, column=0, sticky="w")
        self.skills_frame = tk.Frame(self.register_frame, bg='#f0f0f0')
        self.skills_frame.grid(row=5, column=1, padx=10, pady=5)

        self.skills_vars = []
        self.skills_checkboxes = []

        self.skills_list = ["Java", "Python", "JavaScript", "C++", "Sql", "HTML", "CSS"]
        for i, skill in enumerate(self.skills_list):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.skills_frame, text=skill, variable=var)
            checkbox.pack(side=tk.LEFT)
            self.skills_vars.append(var)
            self.skills_checkboxes.append(checkbox)

        tk.Label(self.register_frame, text="Experience:", bg='#f0f0f0', fg='#333').grid(row=6, column=0, sticky="w")
        self.experience_entry = tk.Entry(self.register_frame, width=30, bg='#fff', fg='#333')
        self.experience_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self.register_frame, text="Register", command=self.register, bg='#4CAF50', fg='#fff').grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.register_frame, text="Login", command=self.login, bg='#2196F3', fg='#fff').grid(row=8, column=0, columnspan=2, pady=10)

    def create_login_widgets(self):
        tk.Label(self.login_frame, text="Username:", bg='#f0f0f0', fg='#333').grid(row=0, column=0, sticky="w")
        self.login_username_entry = tk.Entry(self.login_frame, width=30, bg='#fff', fg='#333')
        self.login_username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.login_frame, text="Password:", bg='#f0f0f0', fg='#333').grid(row=1, column=0, sticky="w")
        self.login_password_entry = tk.Entry(self.login_frame, width=30, bg='#fff', fg='#333', show="*")
        self.login_password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login_validate, bg='#4CAF50', fg='#fff').grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="Back to Register", command=self.back_to_register, bg='#2196F3', fg='#fff').grid(row=3, column=0, columnspan=2, pady=10)

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def register(self):
        username = self.username_entry.get().strip()
        password = self.register_password_entry.get().strip()
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        city = self.city_entry.get().strip()
        experience = self.experience_entry.get().strip()

        # self.skills_vars = [1, 0, 1]
        # self.skills_list = [java, c++, python]
        skills = [self.skills_list[i] for i, var in enumerate(self.skills_vars) if var.get() == 1]

        if not username or not name or not email or not city or not skills or not experience:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        # check if username already exists or not
        # check if email is unique
        
        skills = f"{skills}"


        
        try:
            db.register_user(username,password, name, email, city, experience, skills)
            messagebox.showinfo("Success", "User registered successfully!")
        except Exception:
            messagebox.showinfo("Error", "User was not registered")

        


    def login(self):
        self.register_window.destroy()
        
        self.login_window = self.render_login_window()
        self.login_window.pack()
        

    def back_to_register(self):
        self.login_window.destroy()
        
        self.register_window = self.render_register_window()
        self.register_window.pack()

    def render_register_window(self):
        register_window = tk.Frame(self.master, padx=20, pady=20, bg='#f0f0f0')
        self.register_frame = tk.Frame(register_window, padx=20, pady=20, bg='#f0f0f0')

        self.create_register_widgets()

        self.register_frame.pack()
        return register_window
    
    def render_login_window(self):
        login_window = tk.Frame(self.master, padx=20, pady=20, bg='#f0f0f0')
        # self.login_window.title("Job Portal - Login")
        # self.login_window.withdraw()

        self.login_frame = tk.Frame(login_window, padx=50, pady=50, bg='#f0f0f0')

        self.create_login_widgets()

        self.login_frame.pack()
        return login_window

    def login_validate(self):
        username = self.login_username_entry.get().strip()
        password = self.login_password_entry.get().strip()

        if not username or not password:
            
            messagebox.showerror("Error", "All fields must be filled out.")
            return
         
       
        try:
            if (db.validate_login(username, password)):
                messagebox.showinfo("Success", "User logged in successfully!")

                """
                #########################
                    RENDERING HOME SCREEN HERE 
                #########################
                """
                # views.HomeScreenDisplay(self.master)


            else:
                messagebox.showinfo("Error","Login failed")
        except Exception as e:
            messagebox.showinfo("Error","Login failed")
        
        
    
    def center_window(self, window, width, height):
        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set geometry
        window.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
job_portal = JobPortal(root)
root.mainloop()