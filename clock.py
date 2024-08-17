#makes a digital clock

#imports tkinter
from tkinter import *
from tkinter.ttk import *

#imports string for time
from time import strftime

root = Tk()
root.title("Clock.py")
root.geometry("600x150")
root.configure(background='black')
#function to get the time and update the string
def time():
    string = strftime('%H : %M %S')
    label.config(text=string)
    label.after(200, time)

#aesthetics
label = Label(root,font=("Ubuntu", 100, "bold"), background = "black", foreground = "orange")
label.pack(anchor='center')
time()

mainloop()