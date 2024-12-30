# from twilio import client
import random
from tkinter import *
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.title("OTP Verifier")
        self.geometry("600x550")
        self.resizable(False, False)

    def Labels(self):
        self.c = Canvas(bg = "white", width=400, height=200)
        self.c.place(x=100, y=60)

        self.Login_Title = Label(text="Otp Verifier",font="bold, 20",bg="white")
        self.Login_Title.place(x=210, y=90)

    def Entry_Fields(self):
        self.User_Name = Text(borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190, y=160)


if __name__ == "__main__":
    window = otp_verifier()
    window.mainloop()