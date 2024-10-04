from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.geometry("1920x1820")
window.title("National Public School")
window.config(bg="gray")

# Top Heading Label Creation
TopHeadingFrame = Frame(window, bg="#db9730", height=70)
TopHeadingFrame.pack(side=TOP, fill=X)
TopHeadingLabel = Label(TopHeadingFrame, text="Parent's Page ",
                        font=("arial", 24, "bold"), fg="black", bg="#db9730")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
Mid_Frame = Frame(window, bg="#12801d")
Mid_Frame.pack(side=TOP, padx=10, pady=10)

# Variable creation
student_name = StringVar()
parent_name = StringVar()
email = StringVar()
phone = StringVar()
relationship = StringVar()
father_occupation = StringVar()
mother_occupation = StringVar()

# Student name label creation
student_nameLabel = Label(Mid_Frame, text="Student Name",
                          font=("arial", 16, "bold"), fg="black", bg="white")
student_nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
student_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=student_name)
student_nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Parent name Label
Parent_nameLabel = Label(Mid_Frame, text="Parent Name",
                         font=("arial", 16, "bold"), fg="black", bg="white")
Parent_nameLabel.grid(row=0, column=2, padx=10, pady=10, sticky="w")
Parent_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=parent_name)
Parent_nameTextBox.grid(row=0, column=3, padx=10, pady=10, sticky="w")

# email label
email_nameLabel = Label(Mid_Frame, text="Email",
                        font=("arial", 16, "bold"), fg="black", bg="white")
email_nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=email)
email_nameTextBox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Phone
phone_nameLabel = Label(Mid_Frame, text="Phone",
                        font=("arial", 16, "bold"), fg="black", bg="white")
phone_nameLabel.grid(row=2, column=2, padx=10, pady=10, sticky="w")
phone_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=phone)
phone_nameTextBox.grid(row=2, column=3, padx=10, pady=10, sticky="w")

# Relationship
relationship_nameLabel = Label(Mid_Frame, text="Relationship",
                               font=("arial", 16, "bold"), fg="black", bg="white")
relationship_nameLabel.grid(row=4, column=0, padx=10, pady=10, sticky="w")
relationship_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=relationship)
relationship_nameTextBox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Father occupation
father_occupation_nameLabel = Label(Mid_Frame, text="Father Occupation",
                                    font=("arial", 16, "bold"), fg="black", bg="white")
father_occupation_nameLabel.grid(row=4, column=2, padx=10, pady=10, sticky="w")
father_occupation_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=father_occupation)
father_occupation_nameTextBox.grid(row=4, column=3, padx=10, pady=10, sticky="w")

# Mother occupation
mother_occupation_nameLabel = Label(Mid_Frame, text="Mother Occupation",
                                    font=("arial", 16, "bold"), fg="black", bg="white")
mother_occupation_nameLabel.grid(row=6, column=0, padx=10, pady=10, sticky="w")
mother_occupation_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=mother_occupation)
mother_occupation_nameTextBox.grid(row=6, column=1, padx=10, pady=10, sticky="w")

# Permanent address
permanent_address_nameLabel = Label(Mid_Frame, text="Permanent Address",
                                    font=("arial", 16, "bold"), fg="black", bg="white")
permanent_address_nameLabel.grid(row=7, column=0, padx=10, pady=10, sticky="w")
permanent_address_nameTextBox = Text(Mid_Frame, font=("arial", 16), width=30, height=2)
permanent_address_nameTextBox.grid(row=7, column=1, padx=10, pady=10, sticky="w")

# Database setup
conn = sqlite3.connect("School.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS parent_data(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name varchar,
                parent_name varchar,
                email varchar,
                phone varchar,
                relationship varchar,
                father_occupation varchar,
                mother_occupation varchar,
                permanent_address varchar)''')
conn.commit()
conn.close()


# Add function
def add():
    student_name_value = student_name.get()
    parent_name_value = parent_name.get()
    email_value = email.get()
    phone_value = phone.get()
    relationship_value = relationship.get()
    mother_occupation_value = mother_occupation.get()
    father_occupation_value = father_occupation.get()
    permanent_address_value = permanent_address_nameTextBox.get("1.0", END).strip()

    if not (student_name_value and parent_name_value and email_value and phone_value and relationship_value and
            mother_occupation_value and father_occupation_value and permanent_address_value):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO parent_data(student_name, parent_name, email, phone, relationship, father_occupation,
                               mother_occupation, permanent_address) VALUES(?,?,?,?,?,?,?,?)''',
                       (student_name_value, parent_name_value, email_value, phone_value, relationship_value,
                        father_occupation_value, mother_occupation_value, permanent_address_value))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Parents data added successfully")
        clear_all()  # Clear all fields after adding
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Update function
def update():
    student_name_value = student_name.get()
    parent_name_value = parent_name.get()
    email_value = email.get()
    phone_value = phone.get()
    relationship_value = relationship.get()
    mother_occupation_value = mother_occupation.get()
    father_occupation_value = father_occupation.get()
    permanent_address_value = permanent_address_nameTextBox.get("1.0", END).strip()

    if not student_name_value:
        messagebox.showerror("Error", "Student Name is required for updating")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''UPDATE parent_data SET parent_name=?, email=?, phone=?, 
                          relationship=?, mother_occupation=?, father_occupation=?, permanent_address=? WHERE student_name=?''',
                       (parent_name_value, email_value, phone_value, relationship_value,
                        mother_occupation_value, father_occupation_value, permanent_address_value,
                        student_name_value))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Parents data updated successfully")
        clear_all()  # Clear fields after updating
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Delete Function
def delete():
    student_name_value = student_name.get()

    if not student_name_value:
        messagebox.showerror("Error", "Student Name is required for deleting")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM parent_data WHERE student_name=?', (student_name_value,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Parents data deleted successfully")
        clear_all()  # Clear fields after deleting
    except Exception as e:
        messagebox.showerror("Error", str(e))


# View function
def view():
    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM parent_data')
        rows = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())  # Clear any previous data in the tree
        for row in rows:
            tree.insert('', END, values=row)

        clear_all()  # Clear fields after viewing data
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Clear all function
def clear_all():
    # Clearing entry fields
    student_name.set("")
    parent_name.set("")
    email.set("")
    phone.set("")
    relationship.set("")
    father_occupation.set("")
    mother_occupation.set("")
    permanent_address_nameTextBox.delete("1.0", END)  # Clear Text widget for permanent address


def back():
    window.destroy()
    import homepage


# Button Frame Creation
btn_frame = Frame(window, bg="gray")
btn_frame.pack(side=TOP, pady=20)

# Add Button creation
add_btn = Button(btn_frame, text="Add Details", command=add, width=10,
                 font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
add_btn.grid(row=0, column=0, padx=10)

# Update Button
update_btn = Button(btn_frame, text="Update", command=update, width=10,
                    font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
update_btn.grid(row=0, column=1, padx=10)

# Delete Button
delete_btn = Button(btn_frame, text="Delete", command=delete, width=10,
                    font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
delete_btn.grid(row=0, column=2, padx=10)

# View Button
view_btn = Button(btn_frame, text="View Details", command=view, width=10,
                  font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
view_btn.grid(row=0, column=3, padx=10)

# Back Button
back_btn = Button(btn_frame, text="Back", command=back, width=10,
                  font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
back_btn.grid(row=0, column=4, padx=10)

# Treeview (Table)
tree_frame = Frame(window)
tree_frame.pack(fill=BOTH, expand=TRUE)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set,
                    columns=("id", "student_name", "parent_name", "email", "phone", "relationship", "father_occupation",
                             "mother_occupation", "permanent_address"), show='headings')

tree_scroll.config(command=tree.yview)

# Define Columns
tree.heading("id", text="ID")
tree.heading("student_name", text="Student Name")
tree.heading("parent_name", text="Parent Name")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")
tree.heading("relationship", text="Relationship")
tree.heading("father_occupation", text="Father Occupation")
tree.heading("mother_occupation", text="Mother Occupation")
tree.heading("permanent_address", text="Permanent Address")

tree.column("id", anchor=CENTER, width=50)
tree.column("student_name", anchor=W, width=150)
tree.column("parent_name", anchor=W, width=150)
tree.column("email", anchor=W, width=150)
tree.column("phone", anchor=W, width=150)
tree.column("relationship", anchor=W, width=150)
tree.column("father_occupation", anchor=W, width=150)
tree.column("mother_occupation", anchor=W, width=150)
tree.column("permanent_address", anchor=W, width=200)

tree.pack(fill=BOTH, expand=TRUE)

# Run the mainloop
window.mainloop()
