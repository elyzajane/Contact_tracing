import tkinter as tk
import csv
from tkinter import simpledialog

class SearchEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Search Entry")
        self.geometry("800x500")

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


        with open("Informations.csv", mode="r") as file:
            reader = csv.reader(file)
            found_entries = []
            for row in reader:
                if row[0] == name_to_search:
                    found_entries.append(row)

        if found_entries:
            found = tk.Label(self, text="Here's what we have found", font=("Helvetica", 11, "bold"))
            found.place(x=250, y=80)
            self.name_entry = tk.Label(self, text=f"Name: {found_entries[0][0]}", font=("Helvetica", 11))
            self.name_entry.place(x=30, y=130)
            self.age_entry = tk.Label(self, text=f"Age: {found_entries[0][1]}", font=("Helvetica", 11))
            self.age_entry.place(x=250, y=130)
            self.sex_var = tk.StringVar(value=f"Sex: {found_entries[0][2]}")
            self.sex_entry = tk.Label(self, textvariable=self.sex_var, font=("Helvetica", 11))
            self.sex_entry.place(x=300, y=130)
            self.email_entry = tk.Label(self, text=f"Email Address:: {found_entries[0][3]}", font=("Helvetica", 11))
            self.email_entry.place(x=250, y=130)
            self.phone_entry = tk.Label(self, text=f"Phone Number: {found_entries[0][4]}", font=("Helvetica", 11))
            self.phone_entry.place(x=30, y=160)
            self.address_entry = tk.Label(self, text=f"Address: {found_entries[0][5]}", font=("Helvetica", 11))
            self.address_entry.place(x=30, y=220)
            self.emergency_name_entry = tk.Label(self, text=f"Emergency Contact Name: {found_entries[0][6]}", font=("Helvetica", 11))
            self.emergency_name_entry.place(x=30, y=250)
            self.emergency_phone_entry = tk.Label(self, text=f"Emergency Contact Phone: {found_entries[0][7]}", font=("Helvetica", 11))
            self.emergency_phone_entry.place(x=290, y=280)
            self.emergency_email_entry = tk.Label(self, text=f"Emergency Contact Email: {found_entries[0][8]}", font=("Helvetica", 11))
            self.emergency_email_entry.place(x=290, y=220)
            self.interaction_entry= tk.Label(self, text=f"Who has been in your house with you since your contact tracing date?(Create a list): {found_entries[0][9]}", font=("Helvetica", 11))
            self.interaction_entry.place(x=30, y=250)
            self.places_entry= tk.Label(self, text=f"Specify the places you've visited for the past 14 days?: {found_entries[0][10]}", font=("Helvetica", 11))
            self.places_entry.place(x=30, y=280)
        else:
            result_label = tk.Label(self, text="No entries found", font=("Helvetica", 11, "bold"))
            result_label.place(x=290, y=80)     

if __name__ == "__main__":
    search = SearchEntry()
    search.mainloop()