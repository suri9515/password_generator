import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Invalid Selection", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# === GUI Setup ===
root = tk.Tk()
root.title("🔒 Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# === Variables ===
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

# === Widgets ===
ttk.Label(root, text="Password Length:").pack(pady=(10, 0))
length_slider = ttk.Scale(root, from_=4, to=32, variable=length_var, orient="horizontal")
length_slider.pack(pady=5)

ttk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=20)
ttk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=20)
ttk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

ttk.Label(root, text="Generated Password:").pack()
result_entry = ttk.Entry(root, font=("Segoe UI", 12), justify='center')
result_entry.pack(pady=5, ipadx=30)

# === Run App ===
root.mainloop()
