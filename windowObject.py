import tkinter as tk
from tkinter import ttk
from timeConversion import secondsToTime
from menu import *

class App():
    def __init__(self):

        # root setup
        self.root = tk.Tk()
        self.root.title("Timer!")
        self.root.geometry("500x300")

        self._setupNotebook()


    def _setupNotebook(self):

        # notbook setup
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Timer")
        self.notebook.add(self.tab2, text="Options")

        # extra label stuff just for setup
        ttk.Label(self.tab1, text="Tab 1").pack()
        ttk.Label(self.tab2, text="Tab 2").pack()

    def startLoop(self):
        self.root.mainloop()



    def initTimer(self, seconds):

        self.timeLabel = tk.Label(self.tab1, text=secondsToTime(seconds))
        self.timeLabel.pack()
        self._updateTimer(seconds)




    def _updateTimer(self, seconds):

        
        if seconds != 0:
            self.timeLabel.configure(text=secondsToTime(seconds))
            self.timeLabel.pack()
            self.root.after(1000, self._updateTimer, (seconds - 1))

        else:
            pass
            # Play alarm or something like that
