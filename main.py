


import customtkinter
import home

from pyswip import Prolog

prolog = Prolog()
prolog.consult("Optimizing_Energy.pl")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x500")
root.title("Optimizing Energy Uses In Smart Homes")

# label for outside home
label = customtkinter.CTkLabel(root, text="Optimizing Energy Uses In Smart Homes", fg_color="transparent", font=('bold', 25))
label.pack(padx=10, pady=(150,40))

# Button to go inside the home
button = customtkinter.CTkButton(root, text="Lets Start", width=200,height=40, font=('bold', 18), command=home.home)
button.pack(padx=10, pady=20)


root.mainloop()