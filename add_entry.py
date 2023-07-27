import tkinter as tk
from tkinter import messagebox

class ContactTracingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Covid-19 Contact Tracing Form")
        self.geometry("1000x800")

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