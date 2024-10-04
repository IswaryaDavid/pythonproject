import sqlite3
from tkinter import *
from tkinter import messagebox as msg

# window creation
window = Tk()
window.title("National Public School")
window.geometry("1920x1820")
window.config(bg="#0b4045")

# Top Heading Frame
TopHeadingFrame = Frame(window, bg="black")
TopHeadingFrame.pack(side=TOP, fill=X)

# Top Heading Label
TopHeadingLabel = Label(TopHeadingFrame, text="ADMIN LOGIN",
                        font=("arial", 30, "bold"), fg="black", bg="white")
TopHeadingLabel.pack(padx=10, pady=10, anchor="center")

# MidFrame Background Frame
mid_frame = Frame(window, bg='white')
mid_frame.pack(side=TOP, padx=20, pady=20)

# Variable creation
username_var = StringVar()
password_var = StringVar()

# Username Label
usernameLabel = Label(mid_frame, text="Username:", font=("arial", 16), fg="white", bg="black")
usernameLabel.grid(row=0, column=0, padx=10, pady=10)
usernameTextBox = Entry(mid_frame, font=("arial", 18), textvariable=username_var)
usernameTextBox.grid(row=0, column=1, padx=10, pady=10)

# Password Label
passwordLabel = Label(mid_frame, text="Password:", font=("arial", 16), fg="white", bg="black")
passwordLabel.grid(row=1, column=0, padx=10, pady=10)
passwordTextBox = Entry(mid_frame, font=("arial", 18), textvariable=password_var, show="*")
passwordTextBox.grid(row=1, column=1, padx=10, pady=10)


def toggle_password():
    if show_password_var.get():
        passwordTextBox.config(show="")
    else:
        passwordTextBox.config(show="*")


# Checkbox to show/hide password
show_password_var = IntVar()
show_password_checkbox = Checkbutton(mid_frame, text="Show Password", variable=show_password_var,
                                     onvalue=1, offvalue=0, bg='white', fg="black",
                                     command=toggle_password)
show_password_checkbox.grid(row=2, column=1, padx=10, pady=10, sticky="W")


def login():
    try:
        conn = sqlite3.connect("School.db")
        cursor = conn.cursor()

        # Corrected SQL query
        find_user = 'SELECT * FROM regdata WHERE UserName = ? AND Password = ?'
        cursor.execute(find_user, (username_var.get(), password_var.get()))
        result = cursor.fetchall()

        if result:
            msg.showinfo("Success", 'Logged in Successfully.')
            homepage()
        else:
            msg.showerror("Failed", "Wrong Login details, please try again.")

        conn.close()

    except sqlite3.Error as e:
        msg.showerror("Database Error", f"An error occurred: {e}")
    except Exception as e:
        msg.showerror("Error", f"An unexpected error occurred: {e}")


def homepage():
    window.destroy()
    import homepage


# clear function
def clear_all():
    usernameTextBox.delete(0, END)
    passwordTextBox.delete(0, END)


# Buttons for login and clear
loginButton = Button(mid_frame, text="Login", font=("arial", 16), fg="black", bg="green", command=login)
loginButton.grid(row=3, column=1, padx=10, pady=10)

# Already a user label and Back button in the same row and column
AlreadyUserLabel = Label(mid_frame, text='I have dont an account?',
                         font=('arial', 10), fg='#726f73', bg='white')
AlreadyUserLabel.grid(row=4, column=1, padx=10, pady=10, sticky="W")


def back():
    window.destroy()
    import Admin_signup


# Back Label
backUserLabel = Button(mid_frame, text='Back', command=back,
                       font=('arial', 10), fg='#726f73', bg='white')
backUserLabel.grid(row=4, column=1, padx=170, pady=10, sticky="W")

# Run mainloop
window.mainloop()