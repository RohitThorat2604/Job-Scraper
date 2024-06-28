import tkinter as tk
class HomeScreenDisplay:
    def __init__(self, master):

        self.WINDOW_HEIGHT = 1200
        self.WINDOW_WIDTH = 680

        self.TITLE_STYLE = ("Arial", 12)

        self.master = master
        self.center_window(self.master, self.WINDOW_HEIGHT, self.WINDOW_WIDTH)
        self.master.resizable(False, False)
        

        self.master.title("Home Sceen - Online Job Aggregator")

        self.home_frame = tk.Frame(self.master, height=self.WINDOW_HEIGHT, width=self.WINDOW_WIDTH)
        self.home_frame.grid(padx=30, pady=30)

        self.profile_frame = self.render_profile_frame()
        # Ensure the frame expands to fill the window
        self.profile_frame.grid()

        
        self.master.mainloop()
    
    def render_profile_frame(self):


        skills = ["java", "mysql", "c++"]

        # Create a frame to hold the profile information
        profile_frame = tk.Frame(self.home_frame, 
                    width=250,
                    height=600, 
                    # highlightbackground="black", 
                    # highlightthickness=2,
                    padx=4,
                    pady=0,

                )
        profile_frame.grid(row=0, column=0, sticky="nsew")  # Place the frame in the left side of the window

        # Configure grid columns to expand with window resizing
        profile_frame.grid_columnconfigure(0, weight=1)
        # profile_frame.grid_rowconfigure(12, weight=1)

        # Section 1: Name
        name_label = tk.Label(profile_frame, text="Siddharth Pawar", font=("Arial", 12, "bold"),  highlightbackground="black", highlightthickness=2,)
        name_label.grid(row=0, column=0, pady=10, sticky="ew")


        # Section 2: Username, Email, City, Experience
        user_creds_frame = tk.Frame(profile_frame, 
                    highlightbackground="black", 
                    highlightthickness=2
                )
        user_creds_frame.grid(row=1, column=0, pady=30, columnspan=1, sticky="ew")

        Username_label = tk.Label(user_creds_frame, text="siddharth01", font=self.TITLE_STYLE)
        Username_label.grid(padx=20, pady=10)

        email_label = tk.Label(user_creds_frame, text="sidd@gmail.com", font=self.TITLE_STYLE)
        email_label.grid(padx=20, pady=10)

        city_label = tk.Label(user_creds_frame, text="Pune", font=self.TITLE_STYLE)
        city_label.grid(padx=20, pady=10)

        experience_label = tk.Label(user_creds_frame, text="3 Years", font=self.TITLE_STYLE)
        experience_label.grid(padx=20, pady=10)



        # Section 3: Skills
        skills_frame = tk.Frame(profile_frame,
                    highlightbackground="black", 
                    highlightthickness=2,
                    width = profile_frame.winfo_width()
                )
        skills_frame.grid(row=3, column=0, columnspan=1, sticky="ew")

        skills_label = tk.Label(skills_frame, text="Skills:", font=self.TITLE_STYLE)
        skills_label.grid()

        for skill in skills:
            skills_label = tk.Label(skills_frame, text=skill, font=self.TITLE_STYLE)
            skills_label.grid()


        # Section 4: Edit Profile button
        edit_profile_button = tk.Button(profile_frame, text="Edit Profile", bg='#4CAF50', fg='#fff', font=self.TITLE_STYLE)
        edit_profile_button.grid(row=4, column=0, columnspan=1, padx=20, pady=80)

        

        return profile_frame
        

    def center_window(self, window, width, height):
        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set geometry
        window.geometry(f'{width}x{height}+{x}+{y}')
