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
        ttk.Label(self.tab2, text="Options and Stuff... To come later").pack()

    def startLoop(self):
        self.root.mainloop()



    def initTimer(self, seconds):

        self.timeLabel = tk.Label(self.tab1, text=secondsToTime(seconds))
        self.timeLabel.pack(fill="both", expand=True)
        self._updateTimer(seconds)

        self.timeLabel.bind("<Configure>", self._resizeText)


    def _resizeText(self, event):

        new_font_size = max(10, int(event.height / 2))
        self.timeLabel.config(font=("Helvetica", new_font_size))



    def _updateTimer(self, seconds):

        
        if seconds != 0:
            self.timeLabel.configure(text=secondsToTime(seconds))
            self.timeLabel.pack(fill="both", expand=True)
            self.root.after(1000, self._updateTimer, (seconds - 1))

        else:
            pass
            # Play alarm or something like that
