import tkinter as tk
import csv
from tkinter import simpledialog

class SearchEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Search Entry")
        self.geometry("900x800")

        search = tk.Label(self, text="Enter the Name:")
        search.place(x=30, y=30)

        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.place(x=130, y=30)

        search_button = tk.Button(self, text="Search", command=self.search_info)
        search_button.place(x=325, y=27)

        close = tk.Button(self, text="Close", command=self.destroy)
        close.place(x=360, y=450)

    def search_info(self):
        name_to_search = self.search_entry.get()