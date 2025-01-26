import tkinter as tk
from tkinter import ttk
from timeConversion import secondsToTime
from menu import *

def setupTimer(seconds):

    timeLabel = tk.Label(tab1, text=secondsToTime(seconds))

def updateTimer(seconds):



    root.after(1000, updateTimer(seconds - 1))

root = tk.Tk()
root.title("Timer!")
root.geometry("500x300")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Timer")
notebook.add(tab2, text="Options")

ttk.Label(tab1, text="Tab 1").pack()
ttk.Label(tab2, text="Tab 2").pack()

root.mainloop()