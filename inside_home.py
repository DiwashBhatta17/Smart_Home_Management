def inside_home():
    import customtkinter
    import random
    from pyswip import Prolog

    prolog = Prolog()
    prolog.consult("Optimizing_Energy.pl")

    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("800x500")


    occupancy_list = ["yes", "no"]
    people_list = ["yes", "no"]
    people = random.choice(people_list)
    prolog.assertz(f"people({people})")

    occupancy = random.choice(occupancy_list)

    monitor_list = ["use", "not_use"]
    monitor = random.choice(monitor_list)

    prolog.assertz(f"occupancy({occupancy})")

    prolog.assertz(f"monitor({monitor})")
    print(" Occupancy: ", occupancy)
    print("Monitor :", monitor)
    print(" Occupancy2: ", people)
    # label for Inside the  home
    label = customtkinter.CTkLabel(root, text="Inside The Home", fg_color="transparent", font=('bold', 25), pady=30)
    label.pack()

    # Defines the frame in tkinder
    frame = customtkinter.CTkFrame(master=root, width=350, height=350)
    frame.pack(padx=(70, 0), pady=10, side="left")
    frame2 = customtkinter.CTkFrame(master=root, width=350, height=350)
    frame2.pack(padx=(0, 70), pady=10, side="right")

    # Inside temperature label and rules goes here
    time = customtkinter.CTkLabel(frame, text=" Temperature Inside ", fg_color="transparent", font=('Arial', 18), )
    time.pack(padx=10, pady=(10, 1))
    temperature_inside = list(prolog.query("temperature(X)"))[0]["X"]
    temperatureI = customtkinter.CTkLabel(frame, text=temperature_inside)
    temperatureI.pack(padx=10, pady=(1, 10))

    # Label for the Temperature outside
    label1 = customtkinter.CTkLabel(frame2, text=" Temperature Outside ", fg_color="transparent", font=('Arial', 18), )
    label1.pack(padx=10, pady=(10, 1))
    temperature_outside = list(prolog.query("raise_temp(X)"))[0]["X"]
    temperatureO = customtkinter.CTkLabel(frame2, text=temperature_outside)
    temperatureO.pack(padx=10, pady=(1, 10))

    # solar panel status
    label2 = customtkinter.CTkLabel(frame, text="Lightings", fg_color="transparent", font=('Arial', 18), )
    label2.pack(padx=10, pady=(10, 1))
    light_status = list(prolog.query("lights(X)"))[0]["X"]
    lighting = customtkinter.CTkLabel(frame, text=light_status)
    lighting.pack(padx=10, pady=(1, 10))

    label3 = customtkinter.CTkLabel(frame2, text="Monitoring Appliance", fg_color="transparent", font=('Arial', 18), )
    label3.pack(padx=10, pady=(10, 1))
    monitor_status = customtkinter.CTkLabel(frame2, text=monitor)
    monitor_status.pack(padx=10, pady=(1, 10))

    label4 = customtkinter.CTkLabel(frame2, text="Appliance Status", fg_color="transparent", font=('Arial', 18), )
    label4.pack(padx=10, pady=(10, 1))
    generator_status = list(prolog.query("appliance(X)"))[0]["X"]
    generator_text = customtkinter.CTkLabel(frame2, text=generator_status)
    generator_text.pack(padx=10, pady=(1, 10))

    # Grid electricity status switch
    grid = customtkinter.CTkLabel(frame, text="Entertainment Status", fg_color="transparent", font=('Arial', 18), )
    grid.pack(padx=10, pady=(10, 1))
    entertainment_status = list(prolog.query("entertainment_system(X)"))[0]["X"]
    entertainment = customtkinter.CTkLabel(frame, text=entertainment_status)
    entertainment.pack(padx=10, pady=(1, 10))
    print("Ent: ", entertainment)

    source_text = customtkinter.CTkLabel(root, text="Room Occupancy : " + occupancy, fg_color="transparent",
                                         font=('Arial', 17), )
    source_text.pack(padx=10, pady=(10, 1))

    source_text = customtkinter.CTkLabel(root, text="Entertainment Occupancy : " + people, fg_color="transparent",
                                         font=('Arial', 17), )
    source_text.pack(padx=10, pady=(1, 10))

    root.mainloop()
