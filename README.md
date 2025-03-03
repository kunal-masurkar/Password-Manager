# 🔐 Password Manager

A simple **Password Manager** with a GUI using Tkinter. It encrypts passwords using **AES encryption (Fernet)** and stores them securely in a JSON file.

---

## 📌 Features
- **Secure Storage** – Encrypts passwords before saving.
- **Retrieve Passwords** – Decrypts stored passwords when needed.
- **User-Friendly UI** – Built with Tkinter for easy interaction.
- **AES Encryption** – Uses **Fernet (cryptography module)** for security.
- **Persistent Storage** – Saves data in a JSON file.

---

## 📌 Installation

### **1️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **2️⃣ Run the Application**
```sh
python password_manager.py
```

---

## 📌 How It Works
1️⃣ **Save Password** – Enter website, username, and password → Encrypts & stores securely.  
2️⃣ **Retrieve Password** – Enter website → Decrypts & displays the stored password.  
3️⃣ **Encryption Key** – A unique encryption key is generated and stored in `key.key`.  

> **⚠️ DO NOT share `key.key`, as it is required to decrypt stored passwords!**

---

## 📌 Files Structure
```
📂 PasswordManager
 ├── password_manager.py  # Main application file
 ├── passwords.json       # Encrypted password storage
 ├── key.key              # Encryption key
 ├── requirements.txt     # Dependencies
 ├── README.md            # Documentation
```

---

## 📌 Dependencies
- `cryptography`
- `tkinter`
- `json`
- `os`

---

## 📌 License
MIT Licence

## 📌 Author
👨‍💻 Developed by **Kunal Masurkar**  
🌐 [GitHub](https://github.com/kunal-masurkar) | 🔗 [LinkedIn](https://linkedin.com/in/kunal-masurkar-8494a123a)
