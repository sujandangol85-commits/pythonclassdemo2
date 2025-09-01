import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Student Records Management System")
root.geometry("400x400")

def add_record():
    roll = roll_entry.get()
    name = name_entry.get()
    grade = grade_entry.get()

    if not roll or not name or not grade:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    with open("records.txt", "a") as file:
        file.write(f"{roll},{name},{grade}\n")
    messagebox.showinfo("Success", "Record added successfully.")
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Grade").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

tk.Button(root, text="Add Record", command=add_record).pack(pady=10)

def show_records():
    if not os.path.exists("records.txt"):
        messagebox.showinfo("Info", "No records found.")
        return

    with open("records.txt", "r") as file:
        data = file.read()
    messagebox.showinfo("Records", data)
    
tk.Button(root, text="Show Records", command=show_records).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()
