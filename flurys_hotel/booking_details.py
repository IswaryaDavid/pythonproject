from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
window = Tk()
window.title("FLURYS HOTEL")
window.geometry("900x600")

# Background image setting
bg_image = PhotoImage(file="booking_bg.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1,)

TopHeadingFrame = Frame(window, bg="#13056b", height=80)
TopHeadingFrame.pack(side=TOP, fill=X)
TopHeadingLabel = Label(TopHeadingFrame, text="Booking Page",
                        font=("Helvetica", 30, "bold"), fg="white", bg="#1d0870")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
mid_frame = Frame(window, bd=4, bg="#a2d6db")
mid_frame.pack(side=TOP, padx=10, pady=10)

# variable creation
name = StringVar()
email = StringVar()
room_type_combo = StringVar()
guest = IntVar()
arrival_date = StringVar()
departure_date = StringVar()

# name creation label
nameLabel = Label(mid_frame, text="Name",
                  font=("Helvetica", 12, "bold"), fg="white", bg="black")
nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
nameTextBox = Entry(mid_frame, textvariable=name, font=("Helvetica", 14))
nameTextBox.grid(row=0, column=1, padx=10, pady=10, sticky="w")


# Email label and entry box creation
email_label = Label(mid_frame, text="Email",
                    font=("Helvetica", 12, "bold"), fg="white", bg="black")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
email_TextBox = Entry(mid_frame, textvariable=email, font=("Helvetica", 14))
email_TextBox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# room type and entry box creation
room_label = Label(mid_frame, text="Room Type",
                   font=("Helvetica", 12, "bold"), fg="white", bg="black")
room_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
room_TextBox = ttk. Combobox(mid_frame, font=("Helvetica", 14), width=18, values=["Ac", "No A/c", "Single", "Double", "Suite"])
room_TextBox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Arrival Date
arrival_date_label = Label(mid_frame, text="Arrival Date",
                           font=("Helvetica", 12, "bold"), fg="white", bg="black")
arrival_date_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
arrival_dateTextBox = Entry(mid_frame, font=("Helvetica", 14))
arrival_dateTextBox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# departure_Date
departure_date_label = Label(mid_frame, text="Departure Date",
                             font=("Helvetica", 12, "bold"), fg="white", bg="black")
departure_date_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
departure_dateTextBox = Entry(mid_frame, font=("Helvetica", 14))
departure_dateTextBox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Button Frame
button_frame = Frame(window, bg="gray")
button_frame.pack(side=TOP, pady=10)


import sqlite3
from tkinter import messagebox, Tk, StringVar

# Assuming these variables are defined elsewhere in your form
name = StringVar()
email = StringVar()
room_type = StringVar()
guest = StringVar()
arrival_date = StringVar()
departure_date = StringVar()


def save():
    # Fetch the values from the entry fields
    name_value = name.get()
    email_value = email.get()
    room_type_value = room_type.get()
    guest_value = guest.get()
    arrival_date_value = arrival_date.get()
    departure_date_value = departure_date.get()

    # Check if required fields are filled
    if not name_value or not email_value or not room_type_value or not guest_value:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        # Connect to the database
        conn = sqlite3.connect("hotel.db")
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS booking_detail (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CUSTOMER_NAME TEXT,
                EMAIL TEXT,
                ROOM_TYPE TEXT,
                GUESTS INTEGER,
                ARRIVAL_DATE TEXT,
                DEPARTURE_DATE TEXT
            )
        ''')

        # Insert the booking details into the table
        cursor.execute('''
            INSERT INTO booking_detail (CUSTOMER_NAME, EMAIL, ROOM_TYPE, GUESTS, ARRIVAL_DATE, DEPARTURE_DATE)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name_value, email_value, room_type_value, guest_value, arrival_date_value, departure_date_value))

        # Commit changes and close connection
        conn.commit()
        conn.close()

        # Display success message
        messagebox.showinfo("Success", "Booking details saved successfully")
    except Exception as e:
        # Display error message if something goes wrong
        messagebox.showerror("Error", str(e))


# submit button
save_btn = Button(button_frame, text="Save", command=save,
                  font=("Helvetica", 14, "bold"), fg="black", bg="#14cc1e")
save_btn.grid(row=0, column=0, padx=10, pady=10)

window.mainloop()