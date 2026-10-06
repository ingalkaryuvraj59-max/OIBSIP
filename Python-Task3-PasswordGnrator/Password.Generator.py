import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Password Generator APP..")
root.geometry("650x750")
root.config(bg="#040333")
root.resizable(False, False)

# ---------------- FUNCTIONS ---------------- #

def check_strength(password):
    strength = "Poor"
    
    if len(password) >= 8:
        strength = "Medium"
        
    if (
         len(password) >= 12
        and any(c.isdigit() for c in password)
        and any(c in string.punctuation for c in password)
    ):
        strength = "Strong"

    strength_label.config(text=f"Strength: {strength}")


def generate_password():
    length = slider.get()

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showwarning("Warning", "Select at least one option")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

    check_strength(password)


def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Copied", "Password copied successfully!")


def toggle_password():
    if password_entry.cget('show') == "":
        password_entry.config(show="*")
        eye_btn.config(text="👁 Show")
    else:
        password_entry.config(show="")
        eye_btn.config(text="🙈 Hide")


# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="🔐 Password Generator App..",
    font=("Poppins", 25, "bold"),
    bg="#0b245e",
    fg="#9feb08"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Create Strong & Secure Passwords",
    font=("Poppins", 11),
    bg="#0f172a",
    fg="white"
)
subtitle.pack()

# ---------------- FRAME ---------------- #

frame = tk.Frame(root, bg="#48679b")
frame.pack(pady=27, padx=27, fill="both", expand=True)

# ---------------- SLIDER ---------------- #

slider_label = tk.Label(
    frame,
    text="Select Password Length",
    font=("Poppins", 15, "bold"),
    bg="#293951",
    fg="white"
)
slider_label.pack(pady=(25, 12))

slider = tk.Scale(
    frame,
    from_=6,
    to=25,
    orient="horizontal",
    bg="#1e293b",
    fg="white",
    troughcolor="#0E7318",
    activebackground="#0FEF2D",
    highlightthickness=0,
    font=("Poppins", 11),
    length=300
)
slider.set(12)
slider.pack()

# ---------------- CHECKBOXES ---------------- #

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

style = {
    "bg": "#1e293b",
    "fg": "white",
    "activebackground": "#1e293b",
    "activeforeground": "white",
    "selectcolor": "#334155",
    "font": ("Poppins", 11)
}

tk.Checkbutton(
    frame,
    text="Include Letters",
    variable=letters_var,
    **style
).pack(anchor="w", padx=30, pady=5)

tk.Checkbutton(
    frame,
    text="Include Numbers",
    variable=numbers_var,
    **style
).pack(anchor="w", padx=30, pady=5)

tk.Checkbutton(
    frame,
    text="Include Symbols",
    variable=symbols_var,
    **style
).pack(anchor="w", padx=30, pady=5)

# ---------------- GENERATE BUTTON ---------------- #

generate_btn = tk.Button(
    frame,
    text="⚡ Generate Password",
    command=generate_password,
    font=("Poppins", 12, "bold"),
    bg="#bf51b0",
    fg="black",
    relief="flat",
    padx=15,
    pady=10,
    cursor="hand2"
)
generate_btn.pack(pady=25)

# ---------------- PASSWORD OUTPUT ---------------- #

password_entry = tk.Entry(
    frame,
    font=("Consolas", 14),
    width=30,
    justify="center",
    bg="#62A2B8",
    fg="#43d779",
    relief="flat"
)
password_entry.pack(pady=10, ipady=10)

# ---------------- SHOW/HIDE BUTTON ---------------- #

eye_btn = tk.Button(
    frame,
    text="🙈 Hide",
    command=toggle_password,
    bg="#263D5D",
    fg="white",
    relief="flat",
    font=("Poppins", 10, "bold"),
    padx=10,
    pady=5,
    cursor="hand2"
)
eye_btn.pack()

# ---------------- STRENGTH LABEL ---------------- #

strength_label = tk.Label(
    frame,
    text="Strength: ",
    font=("Poppins", 12, "bold"),
    bg="#1e293b",
    fg="#c6a936"
)
strength_label.pack(pady=15)

# ---------------- COPY BUTTON ---------------- #

copy_btn = tk.Button(
    frame,
    text="📋 Copy Password",
    command=copy_password,
    font=("Poppins", 11, "bold"),
    bg="#15db15",
    fg="white",
    relief="flat",
    padx=12,
    pady=10,
    cursor="hand2"
)
copy_btn.pack(pady=10)

root.mainloop()

#Program write by 
#Yuvraj Ingalkar
