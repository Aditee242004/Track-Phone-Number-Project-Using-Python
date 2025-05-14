import tkinter as tk
from tkinter import ttk, messagebox
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_info():
    number = phone_entry.get()
    try:
        phoneNumber = phonenumbers.parse(number)
        
        timeZone = timezone.time_zones_for_number(phoneNumber)
        geolocation = geocoder.description_for_number(phoneNumber, "en")
        service = carrier.name_for_number(phoneNumber, "en")

        result = (
            f"📍 Timezone: {', '.join(timeZone)}\n"
            f"🌍 Location: {geolocation}\n"
            f"📡 Service Provider: {service}"
        )
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", "Please enter a valid phone number with country code.")

# Main Window
root = tk.Tk()
root.title("📞 Phone Number Tracker")
root.geometry("450x350")
root.configure(bg="#f0f4f8")

# Style Setup
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Segoe UI", 11, "bold"),
                foreground="white",
                background="#2cb1bc",
                padding=10)
style.map("TButton",
          background=[("active", "#239ba3")])

style.configure("TEntry",
                font=("Segoe UI", 11),
                padding=5)

style.configure("TLabel",
                background="#f0f4f8",
                font=("Segoe UI", 11))

# Layout
title = ttk.Label(root, text="📱 Enter Phone Number", font=("Segoe UI", 14, "bold"))
title.pack(pady=(20, 10))

phone_entry = ttk.Entry(root, width=30)
phone_entry.pack(pady=5)

get_button = ttk.Button(root, text="🔍 Get Info", command=get_info)
get_button.pack(pady=15)

result_label = ttk.Label(root, text="", justify="left", wraplength=380, font=("Segoe UI", 11))
result_label.pack(pady=(10, 20))

root.mainloop()

