import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from datetime import datetime

# Main window setup
window = tk.Tk()
window.geometry("1920x1080")
window.title(" Student Fee Report")
window.config(bg="gray")

# Global list to act as a temporary database
fee_records = []

# Heading
heading = tk.Label(window, text=" STUDENT FEE REPORT", font=("Arial", 24, "bold"),
                   bg="gray", fg="black")
heading.pack(pady=10)

# Frame for the left section (form)
form_frame = Frame(window, bg="#f4ce9e")
form_frame.pack(side=TOP, padx=10)

# Frame for the right section (fee receipt)
receipt_frame = Frame(window, bg="#f4ce9e")
receipt_frame.pack(side=LEFT, padx=10, pady=10, anchor="center")


# Function to clear fields
def reset_fields():
    receipt_no.set("")
    student_name.set("")
    admission_no.set("")
    total_amount.set(0)
    paid_amount.set(0)
    balance.set(0)
    medium_combo.set("")  # Changed back to Medium
    standard_combo.set("")
    date_entry.delete(0, END)
    date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
    receipt_text.delete(1.0, END)


# Function to save the data
def save_record():
    record = {
        "receipt_no": receipt_no.get(),
        "student_name": student_name.get(),
        "admission_no": admission_no.get(),
        "date": date_entry.get(),
        "medium": medium_combo.get(),
        "standard": standard_combo.get(),
        "total_amount": total_amount.get(),
        "paid_amount": paid_amount.get(),
        "balance": total_amount.get() - paid_amount.get(),
    }

    if any(val == "" or val == 0 for val in record.values()):
        messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
        return

    fee_records.append(record)
    messagebox.showinfo("Success", "Record saved successfully.")
    reset_fields()


# Function to display all records
# Function to display all records
def display_records():
    receipt_text.delete(1.0, END)  # Clear previous display
    for record in fee_records:
        receipt_text.insert(END, f"Receipt No: {record['receipt_no']}\n")
        receipt_text.insert(END, f"Student Name: {record['student_name']}\n")
        receipt_text.insert(END, f"Admission No: {record['admission_no']}\n")
        receipt_text.insert(END, f"Date: {record['date']}\n")
        receipt_text.insert(END, f"Medium: {record['medium']}\n")  # Changed back to Medium
        receipt_text.insert(END, f"Standard: {record['standard']}\n")  # Changed back to Standard
        receipt_text.insert(END, f"Total Amount: {record['total_amount']}\n")
        receipt_text.insert(END, f"Paid Amount: {record['paid_amount']}\n")
        receipt_text.insert(END, f"Balance: {record['balance']}\n")
        receipt_text.insert(END, "-" * 30 + "\n")


# Function to search for a record by receipt number
def search_record():
    searched_receipt = receipt_no.get()
    for record in fee_records:
        if record["receipt_no"] == searched_receipt:
            receipt_text.delete(1.0, END)
            receipt_text.insert(END, f"Receipt No: {record['receipt_no']}\n")
            receipt_text.insert(END, f"Student Name: {record['student_name']}\n")
            receipt_text.insert(END, f"Admission No: {record['admission_no']}\n")
            receipt_text.insert(END, f"Date: {record['date']}\n")
            receipt_text.insert(END, f"Medium: {record['medium']}\n")  # Changed back to Medium
            receipt_text.insert(END, f"Standard: {record['standard']}\n")  # Changed back to Standard
            receipt_text.insert(END, f"Total Amount: {record['total_amount']}\n")
            receipt_text.insert(END, f"Paid Amount: {record['paid_amount']}\n")
            receipt_text.insert(END, f"Balance: {record['balance']}\n")
            return
    messagebox.showwarning("Not Found", f"No record found for receipt no: {searched_receipt}")


# Function to update a record
def update_record():
    searched_receipt = receipt_no.get()
    for record in fee_records:
        if record["receipt_no"] == searched_receipt:
            record["student_name"] = student_name.get()
            record["admission_no"] = admission_no.get()
            record["date"] = date_entry.get()
            record["medium"] = medium_combo.get()  # Changed back to Medium
            record["standard"] = standard_combo.get()  # Changed back to Standard
            record["total_amount"] = total_amount.get()
            record["paid_amount"] = paid_amount.get()
            record["balance"] = total_amount.get() - paid_amount.get()
            messagebox.showinfo("Success", "Record updated successfully.")
            return
    messagebox.showwarning("Not Found", f"No record found for receipt no: {searched_receipt}")


# Function to delete a record
def delete_record():
    searched_receipt = receipt_no.get()
    for record in fee_records:
        if record["receipt_no"] == searched_receipt:
            fee_records.remove(record)
            messagebox.showinfo("Success", "Record deleted successfully.")
            reset_fields()
            return
    messagebox.showwarning("Not Found", f"No record found for receipt no: {searched_receipt}")


# Function to generate a receipt
def generate_receipt():
    receipt_text.delete(1.0, END)
    receipt_text.insert(END, f"Receipt No: {receipt_no.get()}\n")
    receipt_text.insert(END, f"Student Name: {student_name.get()}\n")
    receipt_text.insert(END, f"Admission No: {admission_no.get()}\n")
    receipt_text.insert(END, f"Date: {date_entry.get()}\n")
    receipt_text.insert(END, f"Medium: {medium_combo.get()}\n")  # Changed back to Medium
    receipt_text.insert(END, f"Standard: {standard_combo.get()}\n")  # Changed back to Standard
    receipt_text.insert(END, f"Total Amount: {total_amount.get()}\n")
    receipt_text.insert(END, f"Paid Amount: {paid_amount.get()}\n")
    receipt_text.insert(END, f"Balance: {total_amount.get() - paid_amount.get()}\n")


# Function to exit the application
def exit_app():
    window.destroy()
    import homepage


# Form labels and entries
receipt_no = StringVar()
student_name = StringVar()
admission_no = StringVar()
medium_combo = StringVar()
standard_combo = StringVar()
total_amount = DoubleVar(value=0.0)
paid_amount = DoubleVar(value=0.0)
balance = DoubleVar(value=0.0)

# Receipt Number
tk.Label(form_frame, text="Receipt No.:", font=("Arial", 12), bg="#f4ce9e").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(form_frame, textvariable=receipt_no, font=("Arial", 12), width=20).grid(row=0, column=1, pady=5)

# Student Name
tk.Label(form_frame, text="Student Name:", font=("Arial", 12), bg="#f4ce9e").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(form_frame, textvariable=student_name, font=("Arial", 12), width=20).grid(row=1, column=1, pady=5)

# Admission Number
tk.Label(form_frame, text="Admission No.:", font=("Arial", 12), bg="#f4ce9e").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(form_frame, textvariable=admission_no, font=("Arial", 12), width=20).grid(row=2, column=1, pady=5)

# Date
tk.Label(form_frame, text="Date:", font=("Arial", 12), bg="#f4ce9e").grid(row=3, column=0, sticky="w", pady=5)
date_entry = tk.Entry(form_frame, font=("Arial", 12), width=20)
date_entry.grid(row=3, column=1, pady=5)
date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

# Branch
tk.Label(form_frame, text="Medium:", font=("Arial", 12),
         bg="#f4ce9e").grid(row=4, column=0, sticky="w", pady=5)
branch_combo = ttk.Combobox(form_frame, font=("Arial", 12), width=18,
                            values=["Tamil", "English", " CBSE"])
branch_combo.grid(row=4, column=1, pady=5)

# Semester
tk.Label(form_frame, text="Standard:", font=("Arial", 12), bg="#f4ce9e").grid(row=5, column=0, sticky="w", pady=5)
semester_combo = ttk.Combobox(form_frame, font=("Arial", 12), width=18, values=["1", "2", "3", "4", "5", "6", "7", "8","9", "10"])
semester_combo.grid(row=5, column=1, pady=5)

# Total Amount
tk.Label(form_frame, text="Total Amount:", font=("Arial", 12), bg="#f4ce9e").grid(row=0, column=2, sticky="w", pady=5)
tk.Entry(form_frame, textvariable=total_amount, font=("Arial", 12), width=20).grid(row=0, column=3, pady=5)

# Paid Amount
tk.Label(form_frame, text="Paid Amount:", font=("Arial", 12), bg="#f4ce9e").grid(row=1, column=2, sticky="w", pady=5)
tk.Entry(form_frame, textvariable=paid_amount, font=("Arial", 12), width=20).grid(row=1, column=3, pady=5)

# Balance
tk.Label(form_frame, text="Balance:", font=("Arial", 12), bg="#f4ce9e").grid(row=2, column=2, sticky="w", pady=5)
tk.Entry(form_frame, textvariable=balance, font=("Arial", 12), width=20).grid(row=2, column=3, pady=5)

# Fee Receipt Text Area
receipt_label = tk.Label(receipt_frame, text="Fee Receipt",
                         font=("Arial", 12, "bold"), bg="#f4ce9e")
receipt_label.pack(anchor="nw")

receipt_text = Text(receipt_frame, font=("Arial", 12), width=60, height=15)
receipt_text.pack()

# Button Frame
button_frame = Frame(window, bg="gray")
button_frame.pack(side=TOP, pady=10)

# Buttons
tk.Button(button_frame, text="SAVE", font=("Arial", 12, "bold"), width=12,
          command=save_record).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="DISPLAY", font=("Arial", 12, "bold"), width=12,
          command=display_records).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="RESET", font=("Arial", 12, "bold"), width=12,
          command=reset_fields).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="UPDATE", font=("Arial", 12, "bold"), width=12,
          command=update_record).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="SEARCH", font=("Arial", 12, "bold"), width=12,
          command=search_record).grid(row=1, column=0, padx=5)
tk.Button(button_frame, text="DELETE", font=("Arial", 12, "bold"), width=12,
          command=delete_record).grid(row=1, column=1, padx=5)
tk.Button(button_frame, text="RECEIPT", font=("Arial", 12, "bold"), width=12,
          command=generate_receipt).grid(row=1, column=2, padx=5)
tk.Button(button_frame, text="EXIT", font=("Arial", 12, "bold"), width=12,
          command=exit_app).grid(row=1, column=3, padx=5)

# Run the application
window.mainloop()
