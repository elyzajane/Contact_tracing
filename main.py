import tkinter as tk
from search_entry import SearchEntry
from add_entry import AddEntry

class Main(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Contact Tracing App")
        self.geometry("700x500")
        self.pack_propagate(0)