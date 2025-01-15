import tkinter as tk
from menu import *

root = tk.Tk()

root.geometry("500x300")

menu = tk.Menu(root)
configureMenu(menu)
root.config(menu=menu)



root.mainloop()