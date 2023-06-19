def home():
    import customtkinter
    import random
    import inside_home
    from pyswip import Prolog

    prolog = Prolog()
    prolog.consult("Optimizing_Energy.pl")

    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("800x500")

    weather_conditions = ["cloudy", "sunny", "sunny", "sunny", "rainy", "windy", "stormy", "sunny", "foggy"]

    # Randomly select a weather condition
    random_weather = random.choice(weather_conditions)
    prolog.assertz(f"weather({random_weather})")

    time = ["day", "night"]
    random_time = random.choice(time)
    prolog.assertz(f"time({random_time})")

    if random_time == "day":
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")

    grid_status = ["on", "off"]
    random_grid = random.choice(grid_status)
    prolog.assertz(f"grid_status({random_grid})")

    # label for outside home
    label = customtkinter.CTkLabel(root, text="Outside Home", fg_color="transparent", font=('bold', 25), pady=30)
    label.pack()

    frame = customtkinter.CTkFrame(master=root, width=350, height=350)
    frame.pack(padx=(100, 0), pady=10, side="left")
    frame2 = customtkinter.CTkFrame(master=root, width=350, height=350)
    frame2.pack(padx=(0, 100), pady=10, side="right")

    # Day or Night Switch
    time = customtkinter.CTkLabel(frame, text="Time", fg_color="transparent", font=('Arial', 18), )
    time.pack(padx=10, pady=(10, 1))
    weather_text = customtkinter.CTkLabel(frame, text=random_time)
    weather_text.pack(padx=10, pady=(1, 10))

    # Label for the weather condition
    label1 = customtkinter.CTkLabel(frame2, text="Weather Condition: ", fg_color="transparent", font=('Arial', 18), )
    label1.pack(padx=10, pady=(10, 1))
    weather_text = customtkinter.CTkLabel(frame2, text=random_weather)
    weather_text.pack(padx=10, pady=(1, 10))

    # solar panel status
    label2 = customtkinter.CTkLabel(frame, text="Solar Panel Status: ", fg_color="transparent", font=('Arial', 18), )
    label2.pack(padx=10, pady=(10, 1))
    solar_status = list(prolog.query("solar_status(X)"))[0]["X"]
    weather_text = customtkinter.CTkLabel(frame, text=solar_status)
    weather_text.pack(padx=10, pady=(1, 10))

    # Battery Status
    label3 = customtkinter.CTkLabel(frame2, text="Battery Status ", fg_color="transparent", font=('Arial', 18), )
    label3.pack(padx=10, pady=(10, 1))
    battery_status = list(prolog.query("battery_status(X)"))[0]["X"]
    battery_text = customtkinter.CTkLabel(frame2, text=battery_status)
    battery_text.pack(padx=10, pady=(1, 10))

    # Generator Status
    label4 = customtkinter.CTkLabel(frame2, text="Generator Status: ", fg_color="transparent", font=('Arial', 18), )
    label4.pack(padx=10, pady=(10, 1))
    generator_status = list(prolog.query("generator_status(X)"))[0]["X"]
    generator_text = customtkinter.CTkLabel(frame2, text=generator_status)
    generator_text.pack(padx=10, pady=(1, 10))

    # Grid electricity status switch
    grid = customtkinter.CTkLabel(frame, text="Grid Status", fg_color="transparent", font=('Arial', 18), )
    grid.pack(padx=10, pady=(10, 1))
    grid_s = customtkinter.CTkLabel(frame, text=random_grid)
    grid_s.pack(padx=10, pady=(1, 10))

    # What is the source use seen in top
    use_source = list(prolog.query("use_source(X)"))[0]["X"]
    source_text = customtkinter.CTkLabel(root, text="Source of energy is " + use_source, fg_color="transparent",
                                         font=('Arial', 18), )
    source_text.pack(padx=10, pady=10)

    # Button to go inside the home
    button = customtkinter.CTkButton(root, text="Go Inside Home", command=inside_home.inside_home)
    button.pack(padx=10, pady=20)

    root.mainloop()
