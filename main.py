import tkinter as tk
from search_entry import SearchEntry
from add_entry import AddEntry

class Main(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Contact Tracing App")
        self.geometry("700x500")
        self.pack_propagate(0)

        AddEntryButton = tk.Button(self, text="Add Entry", command=self.open_add_entry)
        AddEntryButton.place(x=320, y=280)

        SearchEntryButton = tk.Button(self, text="Search Entry", command=self.open_search_entry)
        SearchEntryButton.place(x=313, y=310)
        
        close = tk.Button(self, text="Close", command=self.close_window)
        close.place(x=335, y=450)

    def open_add_entry(self):
        self.destroy()
        entry = AddEntry()
        entry.mainloop()

    def open_search_entry(self):
        self.destroy()
        search = SearchEntry()
        search.mainloop()

    def close_window(self):
        self.destroy()