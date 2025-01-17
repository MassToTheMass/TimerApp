import tkinter as tk
from menu import *
import datetime
from time_funcs import getTime

root = tk.Tk()

root.geometry("500x300")

menu = tk.Menu(root)
configureMenu(menu)
root.config(menu=menu)


root.after(1000, print(getTime))
root.mainloop()