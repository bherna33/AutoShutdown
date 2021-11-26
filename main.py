# This program is to shutdown the computer at a certain time.

import os  # inport Operating System Libary
import time  # inport Time Libary
import datetime  # inport DateTime Libary
from datetime import datetime
from datetime import timedelta
from tkinter import *  # inport tkinter Libary for windows GUI
import tkinter as tk


# make a class
class ShutdownApp(tk.Tk):

    def __init__(self):  # defines all varibles

        # Creating the window GUI
        tk.Tk.__init__(self)
        self.title("---WARNING!---")  # title of the window
        self.label = tk.Label(self, text="", width=100)
        self.iconbitmap(r'rsz_1rsz_city_seal_Xbl_icon.ico')  # icon for window (must be an ico file)
        self.geometry("300x200")  # size of window
        self.myButton = tk.Button(self, text="Shutdown Now", command=self.ButtonAction, width=15)  # Button on window
        self.myButton.pack()
        self.label.pack()
        self.myButton.place(x=90, y=165)  # button placement
        self.protocol("WM_DELETE_WINDOW", False)  # disable "x" button
        self.resizable(width=False, height=False)  # disable resize of window

        # adding the photo
        self.photo = PhotoImage(file="rsz_1rsz_city-seal.png")  # added a picture
        self.photolabel = Label(self, image=self.photo)
        self.photolabel.place(x=100, y=60)  # Where the picture is placed on the window

        # Funtions
        self.getTime()  # gets time initialize

        self.countdown(self.getTime())  # countdown funtion initialize and takes seconds as argument.
        self.remaining = 0
        self.ButtonAction()  # button action initialize

    # This function will take the current time and subtract another time and returns seconds.
    def getTime(self):
        # 86400 is 24 hours
        # cannot work if over that many seconds so keep it to the same day.
        time_delta = datetime.combine(datetime.now().date() + timedelta(), datetime.strptime("19:00:00","%H:%M:%S").time()) - datetime.now()  # subtracts the current time from the time you want to shutdown in 24-hour format.
        return time_delta.seconds  # returns the seconds left till time

    # countdown function takes seconds as an input and returns the time left in 24-hour format
    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:  # if remaining seconds == 0 it shutdowns
            self.label.configure(text="Shutdown...", font=32)
            os.system("shutdown -t 5 -r -f")  # shutdown operation with additional 5 secs
        else:
            self.label.configure(
                text="DISCLAMER: YOU CAN NOT CLOSE THIS WINDOW.\n" + "\nTime left till Shutdown: %s" % time.strftime(
                    "%H:%M:%S", time.gmtime(self.remaining)))  # formats time in a string and takes seconds as inputs.
            self.remaining = self.remaining - 1  # subracts remaing seconds
            self.after(1000, self.countdown)  # tells how fast to update in milliseconds

    def ButtonAction(self):
        os.system("shutdown -t 0 -r -f")  # shutdown command for button.


if __name__ == "__main__":  # main function
    app = ShutdownApp()  # runs program
    app.mainloop()  # runs tkinter window
