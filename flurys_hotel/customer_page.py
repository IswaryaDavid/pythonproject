from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
window = Tk()
window.title("FLURYS HOTEL")
window.geometry("900x600")
window.config(bg="lightblue")

TopHeadingFrame = Frame(window, bg="#1d0870", height=70)
TopHeadingFrame.pack(side=TOP, fill=X)
TopHeadingLabel = Label(TopHeadingFrame, text="Flurys Hotel Customer Page",
                        font=("Helvetica", 30, "bold"), fg="white", bg="#1d0870")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
mid_frame = Frame(window, bd=4, bg="#ad1365", relief=RIDGE)
mid_frame.place(x=10, y=80, width=450, height=400)

# variable creation
first_name = StringVar()
last_name = StringVar()
mobile_no = StringVar()
age = IntVar()
gender = StringVar()
email = StringVar()
address = StringVar()
pincode = StringVar()

# first name creation label
first_nameLabel = Label(mid_frame, text="First Name",
                        font=("Helvetica", 12, "bold"), fg="white", bg="black")
first_nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
first_nameTextBox = Entry(mid_frame, textvariable=first_name, font=("Helvetica", 14))
first_nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Last Name Label creation
last_nameLabel = Label(mid_frame, text="Last Name",
                       font=("Helvetica", 12, "bold"), fg="white", bg="black")
last_nameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
last_nameTextBox = Entry(mid_frame, textvariable=last_name, font=("Helvetica", 14,))
last_nameTextBox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Mobile number label with entry box
mobile_noLabel = Label(mid_frame, text="Mobile No",
                       font=("Helvetica", 12, "bold"), fg="white", bg="black")
mobile_noLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
mobile_noTextBox = Entry(mid_frame, textvariable=mobile_no, font=("Helvetica", 14))
mobile_noTextBox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# age label and enry box
age_Label = Label(mid_frame, text="Age",
                  font=("Helvetica", 12, "bold"), fg="white", bg="black")
age_Label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
age_TextBox = Entry(mid_frame, textvariable=age, font=("Helvetica", 14))
age_TextBox.grid(row=3, column=1, padx=10, pady=10, sticky="w")
# Email label and entry box creation
email_label = Label(mid_frame, text="Email",
                    font=("Helvetica", 12, "bold"), fg="white", bg="black")
email_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
email_TextBox = Entry(mid_frame, textvariable=email, font=("Helvetica", 14))
email_TextBox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Gender Label and Entry box creation
gender_Label = Label(mid_frame, text="Gender",
                     font=("Helvetica", 12, "bold"), fg="white", bg="black")
gender_Label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
# Female Radio Button
femaleRadio = Radiobutton(mid_frame, text="Female", variable=gender, value="Female",
                          font=('Helvetica', 10), fg='white', bg='#ad1365')
femaleRadio.grid(row=5, column=1, padx=10, pady=10, sticky='w')
# Male Radio Button
maleRadio = Radiobutton(mid_frame, text="Male", variable=gender, value="Male",
                        font=('Helvetica', 10), fg="white", bg="#ad1365")
maleRadio.grid(row=5, column=2, padx=3, pady=4, sticky="w")
# Address Label and entry box creation
address_Label = Label(mid_frame, text="Address",
                      font=("Helvetica", 12, "bold"), fg="white", bg="black")
address_Label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
address_TextBox = Entry(mid_frame, textvariable=address, font=("Helvetica", 14))
address_TextBox.grid(row=6, column=1, padx=10, pady=10, sticky="w")

# pincode label creation
pincode_label = Label(mid_frame, text="Pincode",
                      font=("Helvetica", 12, "bold"), fg="white", bg="black")
pincode_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
pincodeTextBox = Entry(mid_frame, textvariable=pincode, font=("Helvetica", 14))
pincodeTextBox.grid(row=7, column=1, padx=10, pady=10, sticky="w")

# Database setup()
conn = sqlite3.connect("hotel.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS contact_details
(
              ID INTEGER  PRIMARY KEY AUTOINCREMENT,
              FIRST_NAME VARCHAR(50) NOT NULL,
              LAST_NAME VARCHAR(50) NOT NULL,
              MOBILE_NO VARCHAR(50) NOT NULL,
              AGE INT NOT NULL,
              EMAIL VARCHAR(100) NOT NULL,
              GENDER VARCHAR(50) NOT NULL,
              ADDRESS VARCHAR(100) NOT NULL,
              PINCODE VARCHAR(50) NOT NULL
              )
              ''')
conn.commit()
conn.close()


# Add record function creation
def add_record():
    first_name_value = first_name.get()
    last_name_value = last_name.get()
    mobile_no_value = mobile_no.get()
    age_value = age.get()
    email_value = email.get()
    gender_value = gender.get()
    address_value = address.get()
    pincode_value = pincode.get()

    if not (first_name_value and last_name_value and mobile_no_value and age_value and email_value
            and gender_value and address_value and pincode_value):
        messagebox.showerror("Error", "All fields are Required")
        return

    try:
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO contact_details(first_name, last_name, mobile_no, age,
                                email, gender, address, pincode ) VALUES(?,?,?,?,?,?,?,?)''',
                       (first_name_value, last_name_value, mobile_no_value, age_value, email_value, gender_value,
                        address_value, pincode_value))

        conn.commit()
        conn.close()
        clear_all()
        messagebox.showinfo("Success", "contact data added successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Button Frame creation
button_frame = Frame(window, bg="lightblue")
button_frame.place(x=20, y=500, width=480, height=60)

# Add button
add_btn = Button(button_frame, text="Add Record", command=add_record,
                 font=("Helvetica", 14, "bold"), fg="black", bg="#14cc1e")
add_btn.grid(row=0, column=0, padx=10, pady=10)


# update function
def update():
    first_name_value = first_name.get()
    last_name_value = last_name.get()
    mobile_no_value = mobile_no.get()
    age_value = age.get()
    email_value = email.get()
    gender_value = gender.get()
    address_value = address.get()
    pincode_value = pincode.get()

    if not first_name_value:
        messagebox.showerror("Error", "First Name is Required")
        return

    try:
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute('''UPDATE contact_details SET last_name=?, mobile_no=?, age=?,
                       email=?, gender=?, address=?, pincode=? WHERE first_name=?''',
                       (last_name_value, mobile_no_value, age_value, email_value, gender_value, address_value, pincode_value, first_name_value))
        conn.commit()
        conn.close()
        clear_all()
        messagebox.showinfo("Success", "Contact Data updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


update_btn = Button(button_frame, text="Update", command=update,
                    font=("Helvetica", 14, "bold"), fg="black", bg="#14cc1e")
update_btn.grid(row=0, column=1, padx=10, pady=10)


# delete function
def delete():
    first_name_value = first_name.get()

    if not first_name_value:
        messagebox.showerror("Error", "first name is Required")
        return

    try:
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contact_details WHERE first_name=?', (first_name_value,))

        conn.commit()
        conn.close()
        clear_all()
        messagebox.showinfo("Success", "contact data deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# delete button creation
del_btn = Button(button_frame, text="Delete", command=delete,
                 font=("Helvetica", 14, "bold"), fg="black", bg="#14cc1e")
del_btn.grid(row=0, column=2, padx=10, pady=10)


# view function
def view():
    try:
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contact_details')
        rows = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", END, values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# view button
view_btn = Button(button_frame, text="view", command=view,
                  font=("Helvetica", 14, "bold"), fg="black", bg="#14cc1e")
view_btn.grid(row=0, column=3, padx=10, pady=10)


# Quit button creation
def quit_e():
    window.destroy()
    import Hotel_homepage


#  quit button
quit_btn = Button(button_frame, text="quit", command=quit_e,
                  font=("Helvetica", 12, "bold"), fg="black", bg="#14cc1e")
quit_btn.grid(row=0, column=4, padx=10, pady=10)


# clear all
def clear_all():
    # Enter the clear fields
    first_name.set("")
    last_name.set("")
    mobile_no.set("")
    age.set("")
    gender.set("")
    email.set("")
    address.set("")
    pincode.set("")


# view Frame creation
view_frame = Frame(window, bd=5, relief=RIDGE)
view_frame.place(x=520, y=120, width=750, height=320)

yscroll = Scrollbar(view_frame, orient=VERTICAL)

tree = ttk.Treeview(view_frame, yscrollcommand=yscroll.set,
                    columns=("id", "first_name", "last_name", "mobile_no", "age",
                             "email", "gender", "address", "pincode"), show="headings")
yscroll.pack(side=RIGHT, fill=Y)
yscroll.config(command=tree.yview)

# tree view creation
tree.heading("id", text="ID")
tree.heading("first_name", text="First_Name")
tree.heading("last_name", text="Last_Name")
tree.heading("mobile_no", text="Mobie_No")
tree.heading("age", text="Age")
tree.heading("email", text="Email")
tree.heading("gender", text="Gender")
tree.heading("address", text="Address")
tree.heading("pincode", text="Pincode")

tree.column("id", anchor=CENTER, width=50)
tree.column("first_name", anchor=W, width=60)
tree.column("last_name", anchor=W, width=60)
tree.column("mobile_no", anchor=W, width=60)
tree.column("age", anchor=W, width=50)
tree.column("email", anchor=W, width=60)
tree.column("gender", anchor=W, width=50)
tree.column("address", anchor=W, width=50)
tree.column("pincode", anchor=W, width=50)

tree.pack(fill=BOTH, expand=True)

window.mainloop()