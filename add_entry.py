import tkinter as tk
from tkinter import messagebox
import csv

class AddEntry(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Covid-19 Contact Tracing Form")
        self.geometry("1000x800")

        self.configure(bg="#f0f0f0")

        title_frame = tk.Frame(self, bg="#4CAF50")
        title_frame.pack(fill="x")
        self.title_label = tk.Label(title_frame, text="Covid-19 Contact Tracing Form", font=("Helvetica", 20, "bold"), fg="white", bg="#4CAF50")
        self.title_label.pack(pady=10)

        self.message_frame = tk.Frame(self, bg="#f0f0f0")
        main_message_text = "Trace any possible contact a person may have had with anyone who could be a carrier of the COVID-19 virus. The Contact Tracing survey will help track down people who are in danger of being exposed to the virus. This can lead to timely detection and treatment, as well as preventing it from spreading further. Use the Contact Tracing form within your organization, community, clients, and more to detect possible exposure to the virus."

        paragraph1_label = tk.Label(self.message_frame, text=main_message_text, font=("Helvetica", 12), justify="left", wraplength=550, bg="#f0f0f0", fg="#333333", anchor="w")
        paragraph1_label.pack(pady=5)

        terms_title_label = tk.Label(self.message_frame, text="Terms and Conditions:", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#4CAF50", anchor="w")
        terms_title_label.pack(pady=5)

        contact_list_text = "I hereby authorize this Contact Tracing Form, to collect and process the data indicated herein for the purpose of contact tracing effecting control of the COVID-19 transmission. I understand that my personal information is protected by RA 10173 or the Data Privacy Act of 2012, following the National Archives of the Philippines protocol."
        paragraph2_label = tk.Label(self.message_frame, text=contact_list_text, font=("Helvetica", 12), justify="left", wraplength=550, bg="#f0f0f0", fg="#333333", anchor="w")
        paragraph2_label.pack(pady=5)

        self.agree_var = tk.BooleanVar()
        self.agree_var.set(False)
        self.agree_checkbutton = tk.Checkbutton(self.message_frame, text="I agree to terms and conditions", variable=self.agree_var, font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
        self.agree_checkbutton.pack(pady=5)

        self.message_frame.pack(pady=10)

        self.proceed_button = tk.Button(self, text="Proceed", command=self.show_contact_form, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=20, pady=10)
        self.proceed_button.pack(pady=20)

        self.contact_form_frame = tk.Frame(self, bg="#f0f0f0")

        self.name_entry = self.create_entry(self.contact_form_frame, "Name:", 0, 0)
        self.age_entry = self.create_entry(self.contact_form_frame, "Age:", 1, 0)

        self.sex_var = tk.StringVar()
        self.sex_var.set("Female") 
        self.create_label(self.contact_form_frame, "Sex:", 2, 0)

        female_checkbutton = tk.Radiobutton(self.contact_form_frame, text="Female", variable=self.sex_var, value="Female", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12))
        female_checkbutton.grid(row=2, column=1, sticky="w")

        male_checkbutton = tk.Radiobutton(self.contact_form_frame, text="Male", variable=self.sex_var, value="Male", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12))
        male_checkbutton.grid(row=2, column=2, sticky="w")

        self.email_entry = self.create_entry(self.contact_form_frame, "Email Address:", 3, 0)
        self.phone_entry = self.create_entry(self.contact_form_frame, "Phone Number:", 4, 0)
        self.address_entry = self.create_entry(self.contact_form_frame, "Address:", 5, 0)
        self.emergency_name_entry = self.create_entry(self.contact_form_frame, "Emergency Contact Name:", 6, 0)
        self.emergency_phone_entry = self.create_entry(self.contact_form_frame, "Emergency Contact Phone:", 7, 0)
        self.emergency_email_entry = self.create_entry(self.contact_form_frame, "Emergency Contact Email:", 8, 0)
        self.interaction_entry = self.create_entry(self.contact_form_frame, "Who has been in your house with you since your contact tracing date?(Create a list):", 9, 0)
        self.places_entry = self.create_entry(self.contact_form_frame, "Specify the places you've visited for the past 14 days?:", 10, 0)     
        
        self.corona_var = tk.StringVar()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=20, pady=10)
        self.submit_button.pack(pady=10)

        self.show_main_window()

    def create_label(self, parent, label_text, row, column):
        label = tk.Label(parent, text=label_text, bg="#f0f0f0", fg="#333333", font=("Helvetica", 12), anchor="w")
        label.grid(row=row, column=column, sticky="w")

    def show_main_window(self):

        self.message_frame.pack()
        self.proceed_button.pack()

        self.contact_form_frame.pack_forget()
        self.submit_button.pack_forget()


    def show_contact_form(self):
        # Show the contact form frame and the Submit button
        if self.agree_var.get():
            self.message_frame.pack_forget()
            self.proceed_button.pack_forget()
            self.contact_form_frame.pack()
            self.submit_button.pack()

        else:
            messagebox.showwarning("Agreement Required", "Please agree to the terms and conditions before proceeding.")

    def create_entry(self, parent, label_text, row, column):
        label = tk.Label(parent, text=label_text, bg="#f0f0f0", fg="#333333", font=("Helvetica", 12), anchor="w")
        label.grid(row=row, column=column, sticky="w")
        entry = tk.Entry(parent, bg="white", fg="#333333", font=("Helvetica", 12))
        entry.grid(row=row, column=column+1, pady=5, sticky="w")  # Align the entry to the left (west)
        return entry

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        sex = self.sex_var.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        emergency_name = self.emergency_name_entry.get()
        emergency_phone = self.emergency_phone_entry.get()
        emergency_email = self.emergency_email_entry.get()
        housemates = self.interaction_entry.get()
        places = self.places_entry.get()


        if not name or not age or not sex or not email or not phone or not address or not emergency_name or not emergency_phone or not emergency_email or not housemates:
            messagebox.showwarning("Incomplete Form", "Please fill in all the required fields.")
            return
        try:
            age = int(age)
        except ValueError:
            messagebox.showwarning("Invalid Age", "Please enter a valid age.")
            return

        if age < 0 or age > 120:
            messagebox.showwarning("Invalid Age", "Please enter a valid age between 0 and 120.")
            return

        else:
            messagebox.showinfo("Confirmation", "Your information has been saved.")
            
        data = [name, age,sex, email, phone, address, emergency_name, emergency_phone, emergency_email, housemates, places ]
        file = open("Informations.csv", mode="a", newline="")
        response = csv.writer(file)
        response.writerow(data)
        file.close()

if __name__ == "__main__":
    app = AddEntry()
    app.mainloop()