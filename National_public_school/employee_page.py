from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Themed tkinter
import tkinter as tk
import sqlite3

# Create the main window
window = tk.Tk()
window.title('National Public School')
window.geometry('1200x800')

# create the background image
back_image = PhotoImage(file='school_emp.png')
bgLabel = Label(window, image=back_image)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Top heading frame
TopHeadingFrame = Frame(window, bg="#7859bd")
TopHeadingFrame.pack(side=TOP, fill=X, anchor="center")
HeadingLabel = Label(TopHeadingFrame, text='National Public School Employee Details Page',
                     font=('Helvetica', 24, "bold"), fg='white', bg='#7859bd')
HeadingLabel.grid(row=0, column=0, padx=10, pady=10)

# MidFrame creation
MidFrame = Frame(window, width=700, bd=1, bg='#362221')
MidFrame.pack(side=TOP, padx=10, pady=10)

# Name
name = StringVar()
nameLabel = Label(MidFrame, text='Name',
                  font=('Helvetica', 16), fg='orange', bg='black')
nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky='w')
nameTextBox = Entry(MidFrame, textvariable=name,
                    font=('Helvetica', 16))
nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Contact
contact = StringVar()
contactLabel = Label(MidFrame, text='Contact',
                     font=("Helvetica", 16), fg='orange', bg='black')
contactLabel.grid(row=0, column=2, padx=10, pady=10, sticky='w')
contactTextBox = Entry(MidFrame, textvariable=contact,
                       font=('Helvetica', 16))
contactTextBox.grid(row=0, column=3, padx=10, pady=10, sticky='w')

# Email
email = StringVar()
emailLabel = Label(MidFrame, text='Email',
                   font=('Helvetica', 16), fg='orange', bg='black')
emailLabel.grid(row=1, column=0, padx=10, pady=10, sticky='w')
emailLabelTextBox = Entry(MidFrame, textvariable=email,
                          font=('Helvetica', 16))
emailLabelTextBox.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# City
city = StringVar()
cityLabel = Label(MidFrame, text='City',
                  font=('Helvetica', 16), fg='orange', bg='black')
cityLabel.grid(row=1, column=2, padx=10, pady=10, sticky='w')
cityLabelTextBox = Entry(MidFrame, textvariable=city,
                         font=('Helvetica', 16))
cityLabelTextBox.grid(row=1, column=3, padx=10, pady=10, sticky='w')

# Gender
gender = StringVar()
genderLabel = Label(MidFrame, text="Gender",
                    font=("Helvetica", 16), fg='orange', bg='black')
genderLabel.grid(row=2, column=0, padx=10, pady=10, sticky='w')

maleRadio = Radiobutton(MidFrame, text="Male", variable=gender, value="Male",
                        font=('Helvetica', 10), fg='white', bg='#482752')
maleRadio.grid(row=2, column=1, padx=10, pady=10, sticky='w')

femaleRadio = Radiobutton(MidFrame, text="Female", variable=gender, value="Female",
                          font=('Helvetica', 10), fg='white', bg='#482752')
femaleRadio.grid(row=2, column=2, padx=10, pady=10, sticky='e')

# Date of joining
date = StringVar()
dateLabel = Label(MidFrame, text="Date of Joining",
                  font=("Helvetica", 16), fg='orange', bg='black')
dateLabel.grid(row=3, column=0, padx=10, pady=10, sticky='w')
dateLabelTextBox = Entry(MidFrame, textvariable=date,
                         font=("Helvetica", 16))
dateLabelTextBox.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Salary
Salary = DoubleVar()  # Corrected variable
SalaryLabel = Label(MidFrame, text="Salary",
                    font=("Helvetica", 16), fg='orange', bg='black')
SalaryLabel.grid(row=3, column=2, padx=10, pady=10, sticky='w')
SalaryLabelTextBox = Entry(MidFrame, textvariable=Salary,
                           font=("Helvetica", 16))
SalaryLabelTextBox.grid(row=3, column=3, padx=10, pady=10, sticky='w')

# Address
Address_label = tk.Label(MidFrame, text="Address:", font=("Helvetica", 16), fg='orange', bg='black')
Address_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
Address_text = tk.Text(MidFrame, width=60, height=5)
Address_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)


# Database setup
def setup_db():
    conn = sqlite3.connect("School.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data
    (        
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME VARCHAR NOT NULL,
              EMAIL VARCHAR  NOT NULL,
              CONTACT VARCHAR  NOT NULL,
              CITY VARCHAR NOT NULL,
              GENDER VARCHAR  NOT NULL,
              SALARY INTEGER NOT NULL,
              ADDRESS VARCHAR  NOT NULL,
              DATE_OF_JOINING VARCHAR NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Add employee details in the database
def save():
    name_value = name.get()
    email_value = email.get()
    contact_value = contact.get()
    city_value = city.get()
    gender_value = gender.get()
    salary_value = Salary.get()
    address_value = Address_text.get("1.0", tk.END).strip()
    date_value = date.get()

    if (not name_value or not email_value or not contact_value or not city_value or not gender_value or not salary_value
            or not address_value or not date_value):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO employee_data(name, email, contact, city, 
                      gender, salary, address, date_of_joining) 
                      VALUES (?,?,?,?,?,?,?,?)''',
                       (name_value, email_value, contact_value, city_value,
                        gender_value, salary_value, address_value, date_value))
        conn.commit()
        conn.close()
        clear_fields()
        messagebox.showinfo("Success", "Employee data added successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Update employee details
def update_employee():
    name_value = name.get()
    contact_value = contact.get()
    email_value = email.get()
    city_value = city.get()
    gender_value = gender.get()
    salary_value = Salary.get()
    date_value = date.get()
    address_value = Address_text.get("1.0", tk.END).strip()

    # ID should be provided to update the record
    # Assuming ID_value is selected from somewhere
    if not name_value:
        messagebox.showerror("Error", "Name is required to update data")
        return

    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()

        cursor.execute('''UPDATE employee_data SET NAME=?, CONTACT=?, EMAIL=?, CITY=?, GENDER=?, 
                        SALARY=?, DATE_OF_JOINING=?, ADDRESS=? WHERE NAME=?''',
                       (name_value, contact_value, email_value, city_value, gender_value,
                        salary_value, date_value, address_value, name_value))

        conn.commit()
        conn.close()
        messagebox.showinfo('Success', "Employee data updated successfully")
        clear_fields()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Clear input fields
def clear_fields():
    nameTextBox.delete(0, tk.END)
    emailLabelTextBox.delete(0, tk.END)
    contactTextBox.delete(0, tk.END)
    cityLabelTextBox.delete(0, tk.END)
    SalaryLabelTextBox.delete(0, tk.END)
    gender.set("")
    dateLabelTextBox.delete(0, tk.END)
    Address_text.delete("1.0", tk.END)


# Back to the homepage
def back():
    window.destroy()
    import homepage


# View function to display data in a new window
def view():
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_data")
    data = cursor.fetchall()

    # Create a new window to display view data
    view_window = Toplevel(window)
    view_window.title("View labor data")
    view_window.geometry("700x500")

    # Treeview for displaying data in the new window
    view_tv = ttk.Treeview(view_window, columns=('ID', 'NAME', 'EMAIL', 'CONTACT', 'CITY', 'GENDER',
                                                 'SALARY', 'ADDRESS', 'DATE_OF_JOINING'), height=20)
    view_tv.heading('#1', text='ID')
    view_tv.heading('#2', text='NAME')
    view_tv.heading('#3', text='EMAIL')
    view_tv.heading('#4', text='CONTACT')
    view_tv.heading('#5', text='CITY')
    view_tv.heading('#6', text='GENDER')
    view_tv.heading('#7', text='SALARY')
    view_tv.heading('#8', text='ADDRESS')
    view_tv.heading('#9', text='DATE OF JOINING')
    view_tv.column('#0', width=0, stretch=NO)
    view_tv.column('#1', width=50)
    view_tv.column('#2', width=100)
    view_tv.column('#3', width=150)
    view_tv.column('#4', width=100)
    view_tv.column('#5', width=100)
    view_tv.column('#6', width=100)
    view_tv.column('#7', width=100)
    view_tv.column('#8', width=150)
    view_tv.column('#9', width=150)
    view_tv.pack(fill=BOTH, expand=True)

    # Inserting data into the new Treeview
    for i in data:
        view_tv.insert('', 'end', values=i)

    cursor.close()
    conn.commit()
    conn.close()


# Call the database setup function
setup_db()

# Button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Save button
save_button = tk.Button(button_frame, text="Save", command=save,
                        font=("Helvetica", 14), bg="green", fg="black")
save_button.grid(row=0, column=0, padx=10, pady=5)

# view button
view_button = tk.Button(button_frame, text="view", command=view,
                        font=("Helvetica", 14), bg="blue", fg="white")
view_button.grid(row=0, column=1, padx=10, pady=5)


# Update button
update_button = tk.Button(button_frame, text="Update", command=update_employee,
                          font=("Helvetica", 14), bg="white", fg="black")
update_button.grid(row=0, column=2, padx=10, pady=5)


# Delete function
def delete():
        name_value = name.get()
        if name_value == 0:  # Check if no ID is entered
            messagebox.showerror("Error", "Employee Name is required")
            return

        try:
            conn = sqlite3.connect('TimePause.db')
            cursor = conn.cursor()

            # Check if the record exists
            cursor.execute("SELECT * FROM employee_data WHERE NAME=?", (name_value,))
            record = cursor.fetchone()

            if record:
                cursor.execute("DELETE FROM employee_data WHERE NAME=?", (name_value,))
                conn.commit()
                messagebox.showinfo("Success", "employee data deleted successfully")
                clear_fields()
                view()
            else:
                messagebox.showerror("Error", "Employee  Name not found")

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Delete Function
del_button = tk.Button(button_frame, text="Delete", command=delete,
                       font=("Helvetica", 14), bg="brown", fg="black")
del_button.grid(row=0, column=3,  padx=10, pady=10)

# Back button
back_button = tk.Button(button_frame, text="Back", command=back,
                        font=("Helvetica", 14), bg="#458c6a", fg="black")
back_button.grid(row=0, column=4,  padx=10, pady=10)

window.mainloop()