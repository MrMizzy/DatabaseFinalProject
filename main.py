import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self, text="Welcome to the Hostel Management System", font=("Arial", 16))
        title_label.pack(pady=20)

        # Load button
        load_button = ttk.Button(self, text="Load Hostels", command=self.load_hostels)
        load_button.pack(pady=10)

        # Display area
        self.output_text = tk.Text(self, height=15, width=80)
        self.output_text.pack(padx=10, pady=10)

        # Quit button
        quit_button = ttk.Button(self, text="Quit", command=self.parent.destroy)
        quit_button.pack(pady=10)

    def load_hostels(self):
        # Simulate loading hostels
        hostel_list = [
            {"name": "Ashesi Hostel", "location": "Block A", "rooms": 20},
            {"name": "Unity Hall", "location": "Block B", "rooms": 15},
            {"name": "Peace Lodge", "location": "Block C", "rooms": 10},
        ]
        self.output_text.delete(1.0, tk.END)
        for hostel in hostel_list:
            line = f"{hostel['name']} - {hostel['location']} ({hostel['rooms']} rooms)\n"
            self.output_text.insert(tk.END, line)
