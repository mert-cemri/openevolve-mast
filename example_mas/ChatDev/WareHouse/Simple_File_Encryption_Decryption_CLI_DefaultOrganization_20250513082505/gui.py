'''
Provides a graphical user interface for the file encryption and decryption application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_encryptor import FileEncryptor
def create_main_window():
    encryptor = FileEncryptor()
    def on_encrypt():
        input_file = filedialog.askopenfilename(title="Select file to encrypt")
        output_file = filedialog.asksaveasfilename(title="Save encrypted file as")
        password = password_entry.get()
        if input_file and output_file and password:
            try:
                validate_password(password)
                encryptor.encrypt_file(input_file, output_file, password)
                messagebox.showinfo("Success", "File encrypted successfully!")
            except ValueError as e:
                messagebox.showerror("Error", f"Password error: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Encryption failed: {e}")
    def on_decrypt():
        input_file = filedialog.askopenfilename(title="Select file to decrypt")
        output_file = filedialog.asksaveasfilename(title="Save decrypted file as")
        password = password_entry.get()
        if input_file and output_file and password:
            try:
                validate_password(password)
                encryptor.decrypt_file(input_file, output_file, password)
                messagebox.showinfo("Success", "File decrypted successfully!")
            except ValueError as e:
                messagebox.showerror("Error", f"Password error: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {e}")
    root = tk.Tk()
    root.title("File Encryptor")
    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=5)
    tk.Button(root, text="Encrypt File", command=on_encrypt).pack(pady=5)
    tk.Button(root, text="Decrypt File", command=on_decrypt).pack(pady=5)
    root.mainloop()
def validate_password(password):
    # Enforce strong password requirements
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        raise ValueError("Password must contain at least one special character.")
    return True