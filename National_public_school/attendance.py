from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

# Initialize the main window
window = Tk()
window.geometry("1920x1080")  # Adjusted window size to a more reasonable one
window.title("National Public School")
window.config(bg="#1a5bab")

# Top Heading Label Creation
TopHeadingFrame = Frame(window, bg="black", height=70)
TopHeadingFrame.pack(side=TOP, fill=X)
TopHeadingLabel = Label(TopHeadingFrame, text="Attendance",
                        font=("arial", 24, "bold"), fg="white", bg="black")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
Mid_Frame = Frame(window, bg="#731aab")
Mid_Frame.pack(side=TOP, padx=10, pady=10)

# Variable creation
attendance_id = IntVar()
student_name = StringVar()
status = StringVar()

# Attendance ID label and entry creation
attendance_idLabel = Label(Mid_Frame, text="Attendance ID",
                           font=("arial", 16, "bold"), fg="black", bg="white")
attendance_idLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
attendance_idTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=attendance_id)
attendance_idTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Student Name label and entry creation
student_nameLabel = Label(Mid_Frame, text="Student Name",
                          font=("arial", 16, "bold"), fg="black", bg="white")
student_nameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
student_nameTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=student_name)
student_nameTextBox.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Status label and entry creation
statusLabel = Label(Mid_Frame, text="Status",
                    font=("arial", 16, "bold"), fg="black", bg="white")
statusLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
statusTextBox = Entry(Mid_Frame, font=("arial", 16), textvariable=status)
statusTextBox.grid(row=2, column=1, padx=10, pady=10, sticky="e")


# Database setup
def setup_database():
    conn = sqlite3.connect("School.db")
    cur = conn.cursor()

    # Drop the table if it exists (this will remove existing incorrect schema)
    cur.execute('''DROP TABLE IF EXISTS attendance_data''')

    # Create the table with the correct schema
    cur.execute('''CREATE TABLE IF NOT EXISTS attendance_data (
                    attendance_id INTEGER PRIMARY KEY,
                    student_name TEXT NOT NULL,
                    status TEXT NOT NULL)''')

    conn.commit()
    conn.close()


setup_database()


# Clear fields function
def clear_all():
    attendance_id.set(0)
    student_name.set("")
    status.set("")


# Add data function
def add():
    attendance_id_value = attendance_id.get()
    student_name_value = student_name.get()
    status_value = status.get()

    if not (attendance_id_value and student_name_value and status_value):
        messagebox.showerror("Error", "All Fields are Required")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO attendance_data (attendance_id, student_name, status)
                          VALUES (?, ?, ?)''', (attendance_id_value, student_name_value, status_value))

        conn.commit()
        conn.close()
        clear_all()
        messagebox.showinfo("Success", "Attendance data added successfully")
        view()  # Refresh the view after adding new data
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Update data function
def update():
    attendance_id_value = attendance_id.get()
    student_name_value = student_name.get()
    status_value = status.get()

    if not (attendance_id_value and student_name_value and status_value):
        messagebox.showerror("Error", "All Fields are Required")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()

        cursor.execute('''UPDATE attendance_data SET student_name = ?, status = ?
                          WHERE attendance_id = ?''', (student_name_value, status_value, attendance_id_value))

        conn.commit()
        conn.close()
        clear_all()
        messagebox.showinfo("Success", "Attendance data updated successfully")
        view()  # Refresh the view after updating data
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Delete data function
def delete():
        attendance_id_value = attendance_id.get()

        if not attendance_id_value:
            messagebox.showerror("Error", "Attendance ID is required to delete")
            return

        try:
            conn = sqlite3.connect("School.db")
            cursor = conn.cursor()

            # Check if the record exists
            cursor.execute('''SELECT * FROM attendance_data WHERE attendance_id = ?''', (attendance_id_value,))
            record = cursor.fetchone()

            if record:
                # Proceed with deletion if the record is found
                cursor.execute('''DELETE FROM attendance_data WHERE attendance_id = ?''', (attendance_id_value,))
                conn.commit()
                messagebox.showinfo("Success", f"Attendance record with ID {attendance_id_value} deleted successfully")
                clear_all()
                view()  # Refresh the view after deletion
            else:
                # Show error if the record is not found
                messagebox.showerror("Error", f"No record found with Attendance ID {attendance_id_value}")

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Search data function
def search():
    attendance_id_value = attendance_id.get()

    if not attendance_id_value:
        messagebox.showerror("Error", "Attendance ID is required to search")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM attendance_data WHERE attendance_id = ?''', (attendance_id_value,))
        record = cursor.fetchone()

        if record:
            attendance_id.set(record[0])
            student_name.set(record[1])
            status.set(record[2])
        else:
            messagebox.showinfo("Not Found", "No record found with this Attendance ID")

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# View all data function
def view():
    for item in tree.get_children():
        tree.delete(item)  # Clear current view

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM attendance_data''')
        records = cursor.fetchall()

        for record in records:
            tree.insert('', 'end', values=record)

        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Back function creation
def back():
    window.destroy()
    import homepage


# Button Frame Creation
btn_frame = Frame(window, bg="#1a5bab")
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


# Search Button
search_btn = Button(btn_frame, text="Search", command=search, width=10,
                    font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
search_btn.grid(row=0, column=3, padx=10)

# Back Button
back_btn = Button(btn_frame, text="Back", command=back, width=10,
                  font=("arial", 16, "bold"), fg="black", bg="#ccbd0e")
back_btn.grid(row=0, column=4, padx=10)

# View frame creation
view_frame = Frame(window)
view_frame.pack(side=RIGHT, expand=TRUE)

tree_scroll = Scrollbar(view_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(view_frame, yscrollcommand=tree_scroll.set,
                    columns=("attendance_id", "student_name", "status"), show="headings")
tree_scroll.config(command=tree.yview)

# Define Columns
tree.heading("attendance_id", text=" Attendance ID")
tree.heading("student_name", text="Student Name")
tree.heading("status", text="Status")

tree.column("attendance_id", anchor=CENTER, width=250)
tree.column("student_name", anchor=CENTER, width=250)
tree.column("status", anchor=CENTER, width=250)

tree.pack(fill=BOTH, expand=TRUE)

# Run the mainloop
window.mainloop()

