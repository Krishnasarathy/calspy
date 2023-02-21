import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")


frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="Login",text_font=("Roboto",24))


