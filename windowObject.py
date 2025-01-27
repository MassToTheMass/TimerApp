import tkinter as tk
from tkinter import ttk
from timeConversion import secondsToTime

class App():
    def __init__(self):
        # root setup
        self.root = tk.Tk()
        self.root.title("Timer!")
        self.root.geometry("500x300")

        self.is_running = False
        self.remaining_time = 0
        self.timer_id = None

        with open("settings/settings.txt") as current_log:
            lines = current_log.readlines()
            for index, line in enumerate(lines):
                if index == 0:  # set binding for start/pause
                    self.binding = line.strip()

        self._setupNotebook()

        # Initial listener for binding
        self.root.bind(f"<{self.binding}>", self._toggleTimer)

    def _setupNotebook(self):
        # notebook setup
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Timer")
        self.notebook.add(self.tab2, text="Options")

        # extra label stuff just for setup
        ttk.Label(self.tab2, text="Options and Stuff... To come later").grid(row=0, column=1, pady=10)
        ttk.Label(self.tab2, text="Binding: Start/Pause").grid(column=0, row=1)
        self.binding_button = ttk.Button(self.tab2, text=self.binding, command=self._changeBinding)
        self.binding_button.grid(row=1, column=1)

    def startLoop(self):
        self.root.mainloop()

    def initTimer(self, seconds):
        self.remaining_time = seconds
        self.timeLabel = tk.Label(self.tab1, text=secondsToTime(self.remaining_time))
        self.timeLabel.pack(fill="both", expand=True)
        self._resizeText({"height": 100})  # Set initial font size
        self.timeLabel.bind("<Configure>", self._resizeText)

    def _resizeText(self, event):
        new_font_size = max(10, int(event["height"]))
        self.timeLabel.config(font=("Helvetica", new_font_size))

    def _updateTimer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timeLabel.configure(text=secondsToTime(self.remaining_time))
            self.timer_id = self.root.after(1000, self._updateTimer)
        else:
            self.is_running = False
            self.timer_id = None
            # Play alarm or perform some action when time runs out

    def _toggleTimer(self, event=None):
        if self.is_running:
            # Pause the timer
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None
            self.is_running = False
        else:
            # Start the timer
            self.is_running = True
            self._updateTimer()

    def _changeBinding(self):
        # Change the button text and wait for user keypress
        self.binding_button.config(text="Press a key...")
        self.root.bind("<Key>", self._onKeyPress)

    def _onKeyPress(self, event):
        # Save the pressed key as the new binding
        self.binding = event.keysym
        self.binding_button.config(text=self.binding)

        # Save the new binding to settings file
        with open("settings/settings.txt", "r") as file:
            lines = file.readlines()
        lines[0] = self.binding + "\n"  # Update the binding on the first line
        with open("settings/settings.txt", "w") as file:
            file.writelines(lines)

        # Unbind the key event after capturing the input
        self.root.unbind("<Key>")

        # Rebind the new key to toggle timer functionality
        self.root.bind(f"<{self.binding}>", self._toggleTimer)
