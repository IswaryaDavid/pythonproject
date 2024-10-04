import sqlite3
from tkinter import *
from tkinter import ttk  # Themed tkinter widgets
from tkinter import messagebox

# Initialize the main window
window = Tk()
window.title("Customer Feedback")
window.geometry("900x600")
window.config(bg="white")

# Top Frame creation
TopHeadingFrame = Frame(window, bg="#8f7eed", height=70)
TopHeadingFrame.pack(side=TOP, fill=X)

# Top Heading Label creation
TopHeadingLabel = Label(TopHeadingFrame, text="Customer Feedback",
                        font=("Helvetica", 26, "bold"), fg="black", bg="#8f7eed")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
mid_frame = Frame(window, bg="#8f7eed", bd=5)
mid_frame.pack(side=TOP, padx=15, pady=15)

# Variables creation
customer_name = StringVar()
contact = StringVar()

# Customer Name Label and Entry
customer_nameLabel = Label(mid_frame, text="Customer Name",
                           font=("Helvetica", 16, "bold"), fg="black", bg="#8f7eed")
customer_nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
customer_nameTextBox = Entry(mid_frame, textvariable=customer_name, font=("Helvetica", 16))
customer_nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Contact Label and Entry
contact_nameLabel = Label(mid_frame, text="Contact",
                          font=("Helvetica", 16, "bold"), fg="black", bg="#8f7eed")
contact_nameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
contact_nameTextBox = Entry(mid_frame, textvariable=contact, font=("Helvetica", 16))
contact_nameTextBox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Comment Label and Entry Box
comment_nameLabel = Label(mid_frame, text="Comment",
                          font=("Helvetica", 16, "bold"), fg="black", bg="#8f7eed")
comment_nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
comment_nameTextBox = Text(mid_frame, font=("Helvetica", 16), width=30, height=2)
comment_nameTextBox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Database setup()
conn = sqlite3.connect("hotel.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS feedback (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CUSTOMER_NAME VARCHAR(50) NOT NULL,
            CONTACT VARCHAR(50) NOT NULL,
            COMMENT VARCHAR(100) NOT NULL
            )
            ''')
conn.commit()
conn.close()


# Function to add feedback to the database
def add_feedback():
    customer_name_value = customer_name.get()
    contact_value = contact.get()
    comment_value = comment_nameTextBox.get("1.0", END).strip()

    if not customer_name_value or not contact_value or not comment_value:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO feedback (CUSTOMER_NAME, CONTACT, COMMENT) VALUES (?, ?, ?)''',
                       (customer_name_value, contact_value, comment_value))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Feedback Data added successfully")
        clear_entries()
        view_feedback()  # Refresh the view to show new data
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to view feedback in TreeView
def view_feedback():
    try:

        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        records = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())
        for record in records:
            tree.insert("", "end", values=record)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Updating record in the database
def update_record():
    customer_name_value = customer_name.get()
    contact_value = contact.get()
    comment_value = comment_nameTextBox.get("1.0", END).strip()

    if not customer_name_value:
        messagebox.showerror("Error", "Customer name is required")
        return

    try:
        conn = sqlite3.connect("hotel.db")
        cur = conn.cursor()
        cur.execute('''UPDATE feedback SET contact=?, comment=? WHERE customer_name=?''',
                    (contact_value, comment_value, customer_name_value))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", " Feedback Data updated successfully")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to clear all input fields
def clear_entries():
    customer_name.set("")
    contact.set("")
    comment_nameTextBox.delete("1.0", END)


# delete function
def delete():
    customer_name_value = customer_name.get()

    if not customer_name_value:
        messagebox.showerror("Error", "customer name is  required")
        return

    try:
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM feedback WHERE customer_name=?', (customer_name_value,))

        conn.commit()
        conn.close()
        clear_entries()
        messagebox.showinfo("success", "feedback deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to go back
def back():
    window.destroy()
    import Hotel_homepage  # navigation to the previous page


# Button Frame creation
btn_frame = Frame(window, bg="white")
btn_frame.pack(pady=20)

# Add Feedback Button
add_btn = Button(btn_frame, text="Add Feedback", command=add_feedback,
                 font=("Helvetica", 18, "bold"), fg="white", bg="blue")
add_btn.grid(row=0, column=0, padx=10, pady=10)

# Update Feedback Button
update_btn = Button(btn_frame, text="Update Feedback", command=update_record,
                    font=("Helvetica", 18, "bold"), fg="white", bg="blue")
update_btn.grid(row=0, column=1, padx=10, pady=10)

# delete Feedback Button
delete_btn = Button(btn_frame, text="Delete Feedback", command=delete,
                    font=("Helvetica", 18, "bold"), fg="white", bg="blue")
delete_btn.grid(row=0, column=2, padx=10, pady=10)

# view button creation
view_btn = Button(btn_frame, text="View Feedback", command=view_feedback,
                  font=("Helvetica", 18, "bold"), fg="white", bg="blue")
view_btn.grid(row=0, column=3, padx=10, pady=10)

# Back Button
back_btn = Button(btn_frame, text="Back", command=back,
                  font=("Helvetica", 18, "bold"), fg="white", bg="blue")
back_btn.grid(row=0, column=4, padx=10, pady=10)

# View Frame creation for displaying feedback
view_frame = Frame(window)
view_frame.pack(side=RIGHT, expand=TRUE)

tree_scroll = Scrollbar(view_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# TreeView creation for displaying records
tree = ttk.Treeview(view_frame, yscrollcommand=tree_scroll.set,
                    columns=("id", "customer_name", "contact", "comment"), show="headings")
tree_scroll.config(command=tree.yview)

# Define TreeView columns
tree.heading("id", text="ID")
tree.heading("customer_name", text="Customer Name")
tree.heading("contact", text="Contact")
tree.heading("comment", text="Comment")

tree.column("id", anchor=CENTER, width=100)
tree.column("customer_name", anchor=CENTER, width=200)
tree.column("contact", anchor=CENTER, width=150)
tree.column("comment", anchor=CENTER, width=250)

tree.pack(fill=BOTH, expand=TRUE)

# Run the mainloop
window.mainloop()
