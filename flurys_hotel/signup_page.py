from tkinter import *
import sqlite3
from tkinter import messagebox

# Initialize the main window
window = Tk()
window.title("Flurys Hotel - Signup")
window.geometry("1920x1820")
window.config(bg="#0f18d1")  # background colour

# Top Heading Frame
TopHeadingFrame = Frame(window, bg="#d1a40f")
TopHeadingFrame.pack(side=TOP, fill=X)

# Top Heading Label
TopHeadingLabel = Label(TopHeadingFrame, text="Welcome To  Flurys Hotel",
                        font=("Helvetica", 30, "bold"), fg="black", bg="#d1a40f")
TopHeadingLabel.pack(padx=10, pady=10, anchor="center")

# MidFrame Background Frame
mid_frame = Frame(window, bg='#4ebaaf')
mid_frame.pack(side=TOP, padx=10, pady=10)

# Signup Label
signupLabel = Label(mid_frame, text="Signup", font=("Helvetica", 26, "bold"),
                    fg="black", bg="#4ebaaf")
signupLabel.grid(row=1, column=1, padx=10, pady=10, sticky="n")

# Variable creation
username_var = StringVar()
email_var = StringVar()
password_var = StringVar()
confirm_password_var = StringVar()

# Username Label
usernameLabel = Label(mid_frame, text="Username",
                      font=("Helvetica", 16, "bold"), fg="black", bg="#4ebaaf")
usernameLabel.grid(row=2, column=0, padx=10, pady=10)
usernameTextBox = Entry(mid_frame, font=("arial", 18), textvariable=username_var)
usernameTextBox.grid(row=2, column=1, padx=10, pady=10)

# Email Label
emailLabel = Label(mid_frame, text="Email",
                   font=("Helvetica", 16, "bold"), fg="black", bg="#4ebaaf")
emailLabel.grid(row=3, column=0, padx=10, pady=10)
emailTextBox = Entry(mid_frame, font=("arial", 18), textvariable=email_var)
emailTextBox.grid(row=3, column=1, padx=10, pady=10)

# Password Label
passwordLabel = Label(mid_frame, text="Password",
                      font=("Helvetica", 16, "bold"), fg="black", bg="#4ebaaf")
passwordLabel.grid(row=4, column=0, padx=10, pady=10)
passwordTextBox = Entry(mid_frame, font=("arial", 18), textvariable=password_var, show="*")
passwordTextBox.grid(row=4, column=1, padx=10, pady=10)

# Confirm Password Label
confirmPasswordLabel = Label(mid_frame, text="Confirm Password",
                             font=("Helvetica", 16, "bold"), fg="black", bg="#4ebaaf")
confirmPasswordLabel.grid(row=5, column=0, padx=10, pady=10)
confirm_passwordTextBox = Entry(mid_frame, font=("arial", 18), textvariable=confirm_password_var, show="*")
confirm_passwordTextBox.grid(row=5, column=1, padx=10, pady=10)


# Function to toggle show/hide password
def toggle_password():
    if show_password_var.get():  # If checkbox is checked
        passwordTextBox.config(show="")
        confirm_passwordTextBox.config(show="")
    else:  # If unchecked, hide password
        passwordTextBox.config(show="*")
        confirm_passwordTextBox.config(show="*")


# Checkbox to show/hide password
show_password_var = StringVar()  # Variable to store checkbox state
show_password_checkbox = Checkbutton(mid_frame, text="Show Password", variable=show_password_var,
                                     onvalue=1, offvalue=0, bg='#4ebaaf', fg="black",
                                     command=toggle_password)
show_password_checkbox.grid(row=6, column=1, padx=10, pady=10, sticky="W")


# Database Creation and Table creation with error handling
def create_database():
    try:
        # Connect to SQLite
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS regdata(
               USERNAME TEXT NOT NULL,
               EMAIL TEXT NOT NULL,
               PASSWORD TEXT NOT NULL,
               CONFIRM_PASSWORD TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()  # close the connection
    except sqlite3.Error as error:
        messagebox.showerror("Database Error", f"Error while connecting to database: {error}")


# Call the function to create the database and table
create_database()


# Submit function creation
def submit():
    if username_var.get() == "" or email_var.get() == "" or password_var.get() == "" or confirm_password_var.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif password_var.get() != confirm_password_var.get():
        messagebox.showerror("Error", "Passwords do not match")
    else:
        try:
            conn = sqlite3.connect("hotel.db")  # Connect to the database
            cursor = conn.cursor()

            cursor.execute('''INSERT INTO regdata(USERNAME, EMAIL, PASSWORD, CONFIRM_PASSWORD) 
                              VALUES(?,?,?,?)''',
                           (username_var.get(), email_var.get(), password_var.get(), confirm_password_var.get()))
            conn.commit()
            conn.close()  # Close the connection after inserting the data

            messagebox.showinfo("Success", "New Account Created Successfully")
            clear_all()
        except sqlite3.Error as error:
            messagebox.showerror("Database Error", f"Error while inserting data: {error}")


def clear_all():
    usernameTextBox.delete(0, END)
    emailTextBox.delete(0, END)
    passwordTextBox.delete(0, END)
    confirm_passwordTextBox.delete(0, END)


# Submit Button
submit_btn = Button(mid_frame, text="Submit", command=submit,
                    font=("arial", 16), fg="black", bg="green")
submit_btn.grid(row=7, column=1, padx=10, pady=10)

# Already a user label and Back button in the same row and column
AlreadyUserLabel = Label(mid_frame, text='I have an account?',
                         font=('arial', 10), fg='black', bg='#4ebaaf')
AlreadyUserLabel.grid(row=8, column=1, padx=10, pady=10, sticky="W")


# Back function creation
def back():
    window.destroy()
    import login_page


# Back Label
backUserLabel = Button(mid_frame, text='Back',
                       font=('Helvetica', 10), fg='black', bg='#4ebaaf',
                       command=back)
backUserLabel.grid(row=8, column=1, padx=140, pady=10, sticky="W")

# Run the mainloop
window.mainloop()