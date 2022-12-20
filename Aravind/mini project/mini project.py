from tkinter import *
import time

def digital():
   d=time.strftime("%H:%M:%S")
   clock.config(text=d)
   clock.after(200,digital)
root=Tk()
root.title("Digital clock-ARAVIND MINI PROJECT")
clock=Label(root,font=("times",100,"bold"),bg="blue")
clock.grid(row=2,column=1)
digital()
root.mainloop ()  