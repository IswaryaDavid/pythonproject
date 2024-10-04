import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# Create the main window
window = tk.Tk()
window.geometry("1920x1820")
window.title("National Public School")
window.config(bg="#24574a")

# Top Heading Label Creation
TopHeadingFrame = Frame(window, bg="black", height=70)
TopHeadingFrame.pack(side=TOP, fill=X)
TopHeadingLabel = Label(TopHeadingFrame, text="Teacher's Page ",
                        font=("arial", 24, "bold"), fg="#db9730", bg="black")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
Mid_Frame = Frame(window, bg="#532457")
Mid_Frame.pack(side=TOP, padx=10, pady=10, fill=X)

# Variable creation
name = StringVar()
father_name = StringVar()
email = StringVar()
subject_combo = StringVar()
birth_date = StringVar()
cell_no = StringVar()
join_date = StringVar()
qualification = StringVar()

# Name Label and Entry
Label(Mid_Frame, text="Name:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=name)
nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Father Name Label and Entry
Label(Mid_Frame, text="Father Name:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=0, column=2, padx=10, pady=10, sticky="w")
father_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=father_name)
father_nameTextBox.grid(row=0, column=3, padx=10, pady=10, sticky="e")

# Birth Date Label and Entry
Label(Mid_Frame, text="D.O.B:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
birth_dateTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=birth_date)
birth_dateTextBox.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Email Label and Entry
Label(Mid_Frame, text="Email:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=1, column=2, padx=10, pady=10, sticky="w")
emailTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=email)
emailTextBox.grid(row=1, column=3, padx=10, pady=10, sticky="e")

# Phone Label and Entry
Label(Mid_Frame, text="Cell No:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
cell_noTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=cell_no)
cell_noTextBox.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Subject Combo Box
Label(Mid_Frame, text="Subject:", font=("Arial", 16, "bold"), fg="black", bg="white").grid(row=2, column=2, padx=10, pady=10, sticky="w")
subject_combo = ttk.Combobox(Mid_Frame, font=("Arial", 16), width=18, values=["Tamil", "English", "Maths", "Physics", "Social"])
subject_combo.grid(row=2, column=3, padx=10, pady=10, sticky="e")

# Join Date Label and Entry
Label(Mid_Frame, text="Join Date:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
join_dateTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=join_date)
join_dateTextBox.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Qualification Label and Entry
Label(Mid_Frame, text="Qualification:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=3, column=2, padx=10, pady=10, sticky="w")
qualificationTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=qualification)
qualificationTextBox.grid(row=3, column=3, padx=10, pady=10, sticky="e")

# Description Label and Textbox
Label(Mid_Frame, text="Description:", font=("arial", 16, "bold"), fg="black", bg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
descriptionTextBox = Text(Mid_Frame, font=("arial", 16), width=30, height=2)
descriptionTextBox.grid(row=4, column=1, padx=10, pady=10, sticky="e")

# Button frame creation
btn_frame = Frame(window, bg="#24574a")
btn_frame.pack(side=TOP, pady=10)

# Database setup
conn = sqlite3.connect("School.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS teacher_data(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    father_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    cell_no TEXT NOT NULL,
                    qualification TEXT NOT NULL,
                    description TEXT NOT NULL,
                    join_date TEXT NOT NULL,
                    birth_date TEXT NOT NULL)''')
conn.commit()
conn.close()


# CRUD Functions

# Function to clear fields
def clear_fields():
    name.set("")
    father_name.set("")
    email.set("")
    subject_combo.set("")
    birth_date.set("")
    cell_no.set("")
    join_date.set("")
    qualification.set("")
    descriptionTextBox.delete('1.0', END)


# Function to add a new record
def send():
    if name.get() == "" or father_name.get() == "" or email.get() == "" or subject_combo.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO teacher_data(name, father_name, email, subject, cell_no, qualification, description, join_date, birth_date)
                          VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (name.get(), father_name.get(), email.get(), subject_combo.get(), cell_no.get(), qualification.get(),
                        descriptionTextBox.get('1.0', END), join_date.get(), birth_date.get()))
        conn.commit()
        conn.close()
        clear_fields()
        messagebox.showinfo("Success", "Record added successfully")


# Function to update a record
def update():
    selected_item = tree.focus()
    if selected_item == "":
        messagebox.showerror("Error", "Please select a record to update")
    else:
        values = tree.item(selected_item, "values")
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''UPDATE teacher_data SET name=?, father_name=?, email=?, subject=?, cell_no=?, qualification=?, description=?, join_date=?, birth_date=?
                          WHERE id=?''',
                       (name.get(), father_name.get(), email.get(), subject_combo.get(), cell_no.get(), qualification.get(),
                        descriptionTextBox.get('1.0', END), join_date.get(), birth_date.get(), values[0]))
        conn.commit()
        conn.close()
        clear_fields()
        messagebox.showinfo("Success", "Record updated successfully")


# Function to delete a record
def delete():
    selected_item = tree.focus()
    if selected_item == "":
        messagebox.showerror("Error", "Please select a record to delete")
    else:
        values = tree.item(selected_item, "values")
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM teacher_data WHERE id=?", (values[0],))
        conn.commit()
        conn.close()
        clear_fields()
        messagebox.showinfo("Success", "Record deleted successfully")


# Function to show all records
def show_detail():
    conn = sqlite3.connect("School.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_data")
    records = cursor.fetchall()
    tree.delete(*tree.get_children())
    for record in records:
        tree.insert('', 'end', values=record)
    conn.close()


# Function to search for a record by name
def search():
    search_term = name.get()
    conn = sqlite3.connect("School.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_data WHERE name LIKE ?", ('%' + search_term + '%',))
    records = cursor.fetchall()
    tree.delete(*tree.get_children())
    for record in records:
        tree.insert('', 'end', values=record)
    conn.close()


def back():
    window.destroy()
    import homepage


# Button creation
Button(btn_frame, text="Send", command=send, font=("arial", 16, "bold"),
       fg="white", bg="#3748b3").grid(row=0, column=0, padx=10, pady=10)
Button(btn_frame, text="Update", command=update, font=("arial", 16, "bold"),
       fg="white", bg="#3748b3").grid(row=0, column=1, padx=10, pady=10)
Button(btn_frame, text="Delete", command=delete, font=("arial", 16, "bold"),
       fg="white", bg="#3748b3").grid(row=0, column=2, padx=10, pady=10)
Button(btn_frame, text="Show", command=show_detail, font=("arial", 16, "bold"),
       fg="white", bg="#3748b3").grid(row=0, column=3, padx=10, pady=10)
Button(btn_frame, text="Search", command=search, font=("arial", 16, "bold"),
       fg="white", bg="#3748b3").grid(row=0, column=4, padx=10, pady=10)
Button(btn_frame, text="Back", command=back, font=("arial", 16, "bold"),
       fg="white", bg="#3748b3").grid(row=0, column=5, padx=10, pady=10)

# Treeview (Display records)
view_frame = Frame(window)
view_frame.pack(fill=X, expand=TRUE)

tree_scroll = Scrollbar(view_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(view_frame, yscrollcommand=tree_scroll.set, columns=("ID", "Name", "Father Name", "Email", "Subject", "D.O.B", "Cell No", "Join Date", "Qualification", "Description"), show="headings")
tree_scroll.config(command=tree.yview)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Father Name", text="Father Name")
tree.heading("Email", text="Email")
tree.heading("Subject", text="Subject")
tree.heading("D.O.B", text="D.O.B")
tree.heading("Cell No", text="Cell No")
tree.heading("Join Date", text="Join Date")
tree.heading("Qualification", text="Qualification")
tree.heading("Description", text="Description")

tree.column("ID", anchor=CENTER, width=50)
tree.column("Name", anchor=W, width=150)
tree.column("Father Name", anchor=W, width=150)
tree.column("Email", anchor=W, width=150)
tree.column("Subject", anchor=W, width=150)
tree.column("D.O.B", anchor=W, width=150)
tree.column("Cell No", anchor=W, width=150)
tree.column("Join Date", anchor=W, width=150)
tree.column("Qualification", anchor=W, width=150)
tree.column("Description", anchor=W, width=200)

tree.pack(fill=BOTH, expand=TRUE)

# Load all records on start
show_detail()

window.mainloop()
