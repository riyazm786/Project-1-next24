import tkinter as tk
from tkinter import messagebox

# Function to display the form values on button click
def submit():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if name and email and password:
        messagebox.showinfo("Registration", f"Name: {name}\nEmail: {email}\nRegistration Successful!")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Creating the main window
window = tk.Tk()
window.title("Registration Form")
window.geometry("300x200")

# Label and Entry for Name
name_label = tk.Label(window, text="Name")
name_label.pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Label and Entry for Email
email_label = tk.Label(window, text="Email")
email_label.pack(pady=5)
email_entry = tk.Entry(window)
email_entry.pack(pady=5)

# Label and Entry for Password
password_label = tk.Label(window, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(window, show='*')
password_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(pady=10)

# Running the Tkinter event loop
window.mainloop()
