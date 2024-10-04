import sqlite3
from tkinter import *
from tkinter import ttk  # themed tkinter
from tkinter import messagebox

# window creation
window = Tk()
window.title("National Public School")
window.geometry("900x600")
window.config(bg="#161357")

# Heading Frame Creation
TopHeadingFrame = Frame(window, bg="#c1d4e0")
TopHeadingFrame.pack(side=TOP, fill=X)

# Heading Label creation
HeadingLabel = Label(TopHeadingFrame, text="Admission Page", font=("arial", 24, "bold"), fg="black", bg="#c1d4e0")
HeadingLabel.pack(padx=10, pady=10, anchor="center")

# Variable creation
student_name = StringVar()
father_name = StringVar()
mother_name = StringVar()
birth_date = StringVar()
present_address = StringVar()
permanent_address = StringVar()
phone = StringVar()
email = StringVar()

# MidFrame Creation
mid_Frame = Frame(window, bg="#7972cf")
mid_Frame.pack(side=TOP, padx=10, pady=10)

# Student name label and entry
student_nameLabel = Label(mid_Frame, text="Student Name*", font=("arial", 16, "bold"), fg="orange", bg="black")
student_nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
student_nameTextBox = Entry(mid_Frame, textvariable=student_name, font=("arial", 16))
student_nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Student DOB label and entry
birth_dateLabel = Label(mid_Frame, text="Student D.O.B*", font=("arial", 16, "bold"), fg="orange", bg="black")
birth_dateLabel.grid(row=0, column=2, padx=10, pady=10, sticky="w")
birth_dateTextBox = Entry(mid_Frame, font=("arial", 16), textvariable=birth_date)
birth_dateTextBox.grid(row=0, column=3, padx=10, pady=10, sticky="e")

# Father name label and entry
father_nameLabel = Label(mid_Frame, text="Father Name*", font=("arial", 16, "bold"), fg="orange", bg="black")
father_nameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
father_nameTextBox = Entry(mid_Frame, font=("arial", 16), textvariable=father_name)
father_nameTextBox.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Mother name label and entry
mother_nameLabel = Label(mid_Frame, text="Mother Name*", font=("arial", 16, "bold"), fg="orange", bg="black")
mother_nameLabel.grid(row=1, column=2, padx=10, pady=10, sticky="w")
mother_nameTextBox = Entry(mid_Frame, font=("arial", 16), textvariable=mother_name)
mother_nameTextBox.grid(row=1, column=3, padx=10, pady=10, sticky="e")

# Email label and entry
email_nameLabel = Label(mid_Frame, text="Email*", font=("arial", 16, "bold"), fg="orange", bg="black")
email_nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_nameTextBox = Entry(mid_Frame, font=("arial", 16), textvariable=email)
email_nameTextBox.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Phone label and entry
phone_nameLabel = Label(mid_Frame, text="Phone*", font=("arial", 16, "bold"), fg="orange", bg="black")
phone_nameLabel.grid(row=2, column=2, padx=10, pady=10, sticky="w")
phone_nameTextBox = Entry(mid_Frame, font=("arial", 16), textvariable=phone)
phone_nameTextBox.grid(row=2, column=3, padx=10, pady=10, sticky="e")

# Present address label and entry
present_addressLabel = Label(mid_Frame, text="Present Address*", font=("arial", 16, "bold"), fg="orange", bg="black")
present_addressLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")
present_addressTextBox = Text(mid_Frame, font=("arial", 16), width=30, height=3)
present_addressTextBox.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Permanent address label and entry
permanent_addressLabel = Label(mid_Frame, text="Permanent Address*", font=("arial", 16, "bold"), fg="orange", bg="black")
permanent_addressLabel.grid(row=3, column=2, padx=10, pady=10, sticky="w")
permanent_addressTextBox = Text(mid_Frame, font=("arial", 16), width=30, height=3)
permanent_addressTextBox.grid(row=3, column=3, padx=10, pady=10, sticky="e")

# Database Setup
conn = sqlite3.connect("School.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS admission_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT,
                birth_date TEXT,
                father_name TEXT,
                mother_name TEXT,
                email TEXT,
                phone TEXT,
                present_address TEXT,
                permanent_address TEXT)''')
conn.commit()
conn.close()


# Add Function
def add():
    student_name_value = student_name.get()
    birth_date_value = birth_date.get()
    father_name_value = father_name.get()
    mother_name_value = mother_name.get()
    email_value = email.get()
    phone_value = phone.get()
    present_address_value = present_addressTextBox.get("1.0", END).strip()
    permanent_address_value = permanent_addressTextBox.get("1.0", END).strip()

    if not (student_name_value and birth_date_value and father_name_value and mother_name_value and email_value and phone_value and present_address_value and permanent_address_value):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO admission_data(student_name, birth_date, father_name, mother_name, email, phone,
                        present_address, permanent_address) VALUES(?,?,?,?,?,?,?,?)''',
                       (student_name_value, birth_date_value, father_name_value, mother_name_value,
                        email_value, phone_value, present_address_value, permanent_address_value))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Admission data added successfully")
        fetch_data()  # Refresh data
        clear_all()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Update Function
def update():
    try:
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, 'values')
        student_id = values[0]
        student_name_value = student_name.get()
        birth_date_value = birth_date.get()
        father_name_value = father_name.get()
        mother_name_value = mother_name.get()
        email_value = email.get()
        phone_value = phone.get()
        present_address_value = present_addressTextBox.get("1.0", END).strip()
        permanent_address_value = permanent_addressTextBox.get("1.0", END).strip()

        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''UPDATE admission_data SET student_name=?, birth_date=?, father_name=?, mother_name=?, email=?, 
                          phone=?, present_address=?, permanent_address=? WHERE id=?''',
                       (student_name_value, birth_date_value, father_name_value, mother_name_value, email_value,
                        phone_value, present_address_value, permanent_address_value, student_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Admission data updated successfully")
        fetch_data()  # Refresh data
        clear_all()
    except IndexError:
        messagebox.showerror("Error", "Select a record to update")


# Delete Function
def delete():
    try:
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, 'values')
        student_id = values[0]

        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM admission_data WHERE id=?', (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Admission data deleted successfully")
        fetch_data()  # Refresh data
        clear_all()
    except IndexError:
        messagebox.showerror("Error", "Select a record to delete")


# Fetch data function to display in treeview
def fetch_data():
    conn = sqlite3.connect("School.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admission_data')
    rows = cursor.fetchall()
    conn.close()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert('', END, values=row)


def clear_all():
    # Clearing entry fields
    student_name.set("")
    birth_date.set("")
    father_name.set("")
    mother_name.set("")
    email.set("")
    phone.set("")

    # Clearing text fields
    present_address.delete("1.0", END)
    permanent_address.delete("1.0", END)


def back():
    window.destroy()
    import homepage


# Button Frame Creation
btn_frame = Frame(window, bg="#161357")
btn_frame.pack(side=TOP, pady=20)

# Add Button
add_btn = Button(btn_frame, text="Insert", command=add, width=10, font=("arial", 16, "bold"), fg="black", bg="#79b9e8")
add_btn.grid(row=0, column=0, padx=10)

# Update Button
update_btn = Button(btn_frame, text="Update", command=update, width=10, font=("arial", 16, "bold"), fg="black", bg="#79b9e8")
update_btn.grid(row=0, column=1, padx=10)

# Delete Button
delete_btn = Button(btn_frame, text="Delete", command=delete, width=10, font=("arial", 16, "bold"), fg="black", bg="#79b9e8")
delete_btn.grid(row=0, column=2, padx=10)

# Back Button
back_btn = Button(btn_frame, text="Back", command=back, width=10, font=("arial", 16, "bold"), fg="black", bg="#79b9e8")
back_btn.grid(row=0, column=3, padx=10)

# Treeview (Table)
tree_frame = Frame(window)
tree_frame.pack(fill=BOTH, expand=TRUE)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=("id", "student_name", "birth_date", "father_name",
                                                                         "mother_name", "email", "phone", "present_address",
                                                                         "permanent_address"), show='headings')

tree_scroll.config(command=tree.yview)

# Define Columns
tree.heading("id", text="ID")
tree.heading("student_name", text="Student Name")
tree.heading("birth_date", text="D.O.B")
tree.heading("father_name", text="Father Name")
tree.heading("mother_name", text="Mother Name")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")
tree.heading("present_address", text="Present Address")
tree.heading("permanent_address", text="Permanent Address")

tree.column("id", anchor=CENTER, width=50)
tree.column("student_name", anchor=W, width=100)
tree.column("birth_date", anchor=W, width=100)
tree.column("present_address", anchor=W, width=100)
tree.column("permanent_address", anchor=W, width=100)

tree.pack(fill=BOTH, expand=TRUE)

# Fetch initial data
fetch_data()

# Main loop
window.mainloop()
