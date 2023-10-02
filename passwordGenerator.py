import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            result_label.config(text="Password length must be a positive integer.")
            return
        password = generate_password(password_length)
        result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Please enter a valid integer for password length.")

root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter password length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_click)
result_label = tk.Label(root, text="")


length_label.pack()
length_entry.pack()
generate_button.pack()
result_label.pack()

root.mainloop()
