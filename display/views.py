import tkinter as tk

import PIL
import PIL.Image
import PIL.ImageTk

class HomeScreenDisplay:
    def __init__(self, master):

        self.WINDOW_HEIGHT = 1200
        self.WINDOW_WIDTH = 680

        self.TITLE_STYLE = ("Arial", 12)

        self.master = master
        self.center_window(self.master, self.WINDOW_HEIGHT, self.WINDOW_WIDTH)
        self.master.resizable(False, False)
        

        self.master.title("Home Sceen - Online Job Aggregator")

        self.home_frame = tk.Frame(self.master, height=self.WINDOW_HEIGHT, width=self.WINDOW_WIDTH, highlightbackground="black", highlightthickness=1)
        self.home_frame.grid(padx=30, pady=30)

        # PROFILE SECTION
        self.profile_frame = self.render_profile_frame()
        # Ensure the frame expands to fill the window
        self.profile_frame.grid(row = 0, column=0, padx=25)

        #TITLE
        self.title = tk.Label(self.home_frame, 
                        text = "Online Job Aggregator", 
                        highlightbackground = "black", 
                        highlightthickness = 1,
                        font = ("Arial", 20),
                        width = 50,
                        padx = 20,
                        pady=20,
                        height=1,
                        anchor="w"
                    )
        self.title.grid(row=0, column=1, sticky="n")

        #JOB SEARCH RESULT SECTION
        self.search_result_frame = self.render_search_result_frame()
        self.search_result_frame.grid(row=0, column=1, sticky="ew")

        self.master.mainloop()
    
    def render_profile_frame(self):


        skills = ["java", "mysql", "c++"]

        # Create a frame to hold the profile information
        profile_frame = tk.Frame(self.home_frame, 
                    width=250,
                    height=600, 
                    highlightbackground="black", 
                    highlightthickness=2,
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

    def render_search_result_frame(self):

        self.lower_limit = 0
        self.upper_limit = 3
        
        def render_3_jobs(job_search_result, LOWER_LIMIT, UPPER_LIMIT):
            
            self.lower_limit = LOWER_LIMIT
            self.upper_limit = UPPER_LIMIT

            existing_job_frame = job_container.winfo_children()
            for job_frame in existing_job_frame:
                job_frame.destroy()

            """
            lower limit should always be greater the ZERO OR(else) it should equal to passed lower_limit.
            The following line of code ensures that
            """
            LOWER_LIMIT = 0 if LOWER_LIMIT < 0 else LOWER_LIMIT

            """
            upper limit should always be less the LENGHT OF job_search_result OR(else) it should be equal to passed upper_limit.
            The following line of code ensures that
            """
            UPPER_LIMIT = len(job_search_result) if UPPER_LIMIT > len(job_search_result) else UPPER_LIMIT

            
            for job in job_search_result[LOWER_LIMIT: UPPER_LIMIT ]:
                job_frame = self.create_job_frame(job_container, job["job_title"], job["company_name"], job["job_location"], job["experience_level"], job["employement_type"], job["date_posted"], job["apply_link"])
                job_frame.grid()

        job_search_result = [
            {
                "job_title": "Java Developer 1",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 2",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 3",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 4",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 5",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 6",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 7",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 8",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            },
            {
                "job_title": "Java Developer 9",
                "company_name": "Capgemini",
                "job_location": "Pune",
                "experience_level": "1 year",
                "employement_type": "Full Time",
                "date_posted": "21-Jan-2024",
                "apply_link": "linked.com"
            }
        ]

        search_result_frame = tk.Frame(
            self.home_frame,
            width = 100,
            # highlightbackground="red",
            # highlightthickness=1,
            height=180,
            padx=40
        )

        

        search_result_count_label = tk.Label(
            search_result_frame,
            text="56 Jobs found matching your skills",
            # pady=20,
            # padx=40,
            # highlightbackground="green",
            # highlightthickness=1,
            anchor="w"
        )
        search_result_count_label.grid(columnspan=1, sticky="ew")

        job_container = tk.Frame(
            search_result_frame,
            # highlightbackground="green",
            # highlightthickness=1,
            pady=20
        )
        job_container.grid(sticky="ew")

        
        render_3_jobs(job_search_result, self.lower_limit, self.upper_limit)


        prev_button = tk.Button(
            search_result_frame,
            text="Previous",
            font=self.TITLE_STYLE,
            bg='#4CAF50', fg='#fff',
            command= lambda : render_3_jobs(job_search_result, self.lower_limit - 3, self.upper_limit - 3)
        )
        prev_button.grid(row=3, sticky="w")

        next_button = tk.Button(
            search_result_frame,
            text="Next",
            font=self.TITLE_STYLE,
            bg='#4CAF50', fg='#fff',
            command= lambda : render_3_jobs(job_search_result, self.lower_limit + 3, self.upper_limit + 3)
        )
        next_button.grid(row=3, sticky="e")
        
        
        


        return search_result_frame

    def create_job_frame(self, job_container, job_title, company_name, job_location, experience_level, employement_type, date_posted, apply_link):
        job_frame = tk.Frame(
            job_container,
            highlightbackground="black",
            highlightthickness=1,
        )


        job_title_label = tk.Label(
            job_frame,
            text= job_title,
            font=self.TITLE_STYLE,
            width=30,
            pady=5,
            anchor="w"
        )
        job_title_label.grid(columnspan=2)

        company_name_label = tk.Label(
            job_frame,
            text= company_name,
            font=self.TITLE_STYLE,
            padx=70,
            pady=5
        )
        company_name_label.grid()

        location_label = tk.Label(
            job_frame,
            text= job_location,
            font=self.TITLE_STYLE,
            padx=70,
            pady=5
        )
        location_label.grid()
        
        experience_level_label = tk.Label(
            job_frame,
            text= experience_level,
            font=self.TITLE_STYLE,
            padx=80,
            pady=5
        )
        experience_level_label.grid(row=1, column=1)

        employement_type_label = tk.Label(
            job_frame,
            text= employement_type,
            font=self.TITLE_STYLE,
            padx=80,
            pady=5
        )
        employement_type_label.grid(row=2, column=1)

        date_posted_label = tk.Label(
            job_frame,
            text= date_posted,
            font=self.TITLE_STYLE,
            pady=5
        )
        date_posted_label.grid(row=0, column=3)

        apply_link_label = tk.Button(
            job_frame,
            text="Apply Link",
            font=self.TITLE_STYLE,
            bg="#3632a8",
            fg="#fff",
        )
        apply_link_label.grid(row=1, column=3)

        return job_frame


    def center_window(self, window, width, height):
        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set geometry
        window.geometry(f'{width}x{height}+{x}+{y}')


