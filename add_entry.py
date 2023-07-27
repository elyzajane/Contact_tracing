import tkinter as tk
from tkinter import messagebox

class ContactTracingApp(tk.Tk):
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

        contact_list_text = "Lagay ka terms and conditionss"
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
        self.interaction_email_entry = self.create_entry(self.contact_form_frame, "Who has been in your house with you since your contact tracing date?:", 9, 0)
        
        self.corona_var = tk.StringVar()

    def create_entry(self, parent, label_text, row, column):
        label = tk.Label(parent, text=label_text, bg="#f0f0f0", fg="#333333", font=("Helvetica", 12), anchor="w")
        label.grid(row=row, column=column, sticky="w")
        entry = tk.Entry(parent, bg="white", fg="#333333", font=("Helvetica", 12))
        entry.grid(row=row, column=column+1, pady=5, sticky="w")
        return entry