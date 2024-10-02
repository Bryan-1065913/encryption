import tkinter as tk
from tkinter import messagebox
import pyperclip
from cryptography.fernet import Fernet, InvalidToken
import base64

def generate_key():
    key = Fernet.generate_key()
    return key

def is_valid_key(key):
    try:
        base64.urlsafe_b64decode(key)
        return len(key) == 44
    except Exception:
        return False

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    try:
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        return decrypted_message
    except InvalidToken:
        raise ValueError("Ongeldige sleutel of corrupte versleutelde boodschap!")

def create_app():
    def encrypt_text():
        message = entry_message.get()
        key = entry_key.get().encode()
        if message and key:
            if is_valid_key(key):
                try:
                    encrypted = encrypt_message(message, key)
                    result_var.set(encrypted.decode())
                except Exception as e:
                    messagebox.showerror("Encryptie Error", f"Fout bij versleuteling: {str(e)}")
            else:
                messagebox.showwarning("Input Error", "De sleutel is ongeldig. Zorg ervoor dat de sleutel correct is.")
        else:
            messagebox.showwarning("Input Error", "Vul zowel tekst als sleutel in.")

    def decrypt_text():
        encrypted_message = entry_message.get().encode()
        key = entry_key.get().encode()
        if encrypted_message and key:
            if is_valid_key(key):
                try:
                    decrypted = decrypt_message(encrypted_message, key)
                    result_var.set(decrypted)
                except ValueError as e:
                    messagebox.showerror("Decryptie Error", str(e))
            else:
                messagebox.showwarning("Input Error", "De sleutel is ongeldig. Zorg ervoor dat de sleutel correct is.")
        else:
            messagebox.showwarning("Input Error", "Vul zowel versleutelde tekst als sleutel in.")

    def copy_encrypted_text():
        encrypted_message = result_var.get()
        if encrypted_message:
            pyperclip.copy(encrypted_message)
            messagebox.showinfo("Gekopieerd", "Versleutelde tekst is gekopieerd naar het klembord.")
        else:
            messagebox.showwarning("Geen tekst", "Geen versleutelde tekst om te kopiëren.")

    def generate_and_copy_key():
        key = generate_key()
        entry_key.delete(0, tk.END)
        entry_key.insert(0, key.decode())
        pyperclip.copy(key.decode())
        messagebox.showinfo("Sleutel Gekopieerd", "Gegenereerde sleutel is gekopieerd naar het klembord.")

    window = tk.Tk()
    window.title("Encryptie App")

    label_message = tk.Label(window, text="Voer de tekst in:")
    label_message.pack()

    entry_message = tk.Entry(window, width=50)
    entry_message.pack()

    label_key = tk.Label(window, text="Voer de sleutel in of genereer een nieuwe:")
    label_key.pack()

    entry_key = tk.Entry(window, width=50)
    entry_key.pack()

    generate_key_button = tk.Button(window, text="Genereer en kopieer sleutel", command=generate_and_copy_key)
    generate_key_button.pack(pady=5)

    encrypt_button = tk.Button(window, text="Versleutel", command=encrypt_text)
    encrypt_button.pack(pady=5)

    decrypt_button = tk.Button(window, text="Ontsleutel", command=decrypt_text)
    decrypt_button.pack(pady=5)

    copy_button = tk.Button(window, text="Kopieer versleutelde tekst", command=copy_encrypted_text)
    copy_button.pack(pady=5)

    result_var = tk.StringVar()
    result_label = tk.Label(window, textvariable=result_var, wraplength=400)
    result_label.pack(pady=10)

    window.mainloop()

create_app()