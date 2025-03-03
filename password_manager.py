import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet

# Generate or load encryption key
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

encryptor = load_key()

# Save password to file
def save_password():
    website = simpledialog.askstring("Website", "Enter website:")
    username = simpledialog.askstring("Username", "Enter username:")
    password = simpledialog.askstring("Password", "Enter password:")

    if not website or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    encrypted_password = encryptor.encrypt(password.encode()).decode()
    data = {website: {"username": username, "password": encrypted_password}}

    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    existing_data.update(data)
    with open("passwords.json", "w") as file:
        json.dump(existing_data, file, indent=4)

    messagebox.showinfo("Success", "Password saved successfully!")

# Retrieve password from file
def retrieve_password():
    website = simpledialog.askstring("Retrieve", "Enter website:")
    if not os.path.exists("passwords.json"):
        messagebox.showwarning("Error", "No passwords saved yet!")
        return
    
    with open("passwords.json", "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}
    
    if website in data:
        username = data[website]["username"]
        decrypted_password = encryptor.decrypt(data[website]["password"].encode()).decode()
        messagebox.showinfo("Retrieved Info", f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}")
    else:
        messagebox.showwarning("Error", "No details found for this website!")

# GUI Setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Save Password", command=save_password, width=20).pack(pady=5)
tk.Button(frame, text="Retrieve Password", command=retrieve_password, width=20).pack(pady=5)
tk.Button(frame, text="Exit", command=root.quit, width=20).pack(pady=5)

root.mainloop()
