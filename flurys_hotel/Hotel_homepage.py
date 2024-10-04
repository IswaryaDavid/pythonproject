from tkinter import *
window = Tk()
window.title("Flurys Hotel HomePage")
window.geometry("900x600")

# Background image creation
back_image = PhotoImage(file="background.png")
bgLabel = Label(window, image=back_image)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Heading Label frame
TopHeadingFrame = Frame(window, bg="black", height=80)
TopHeadingFrame.pack(side=TOP, fill=X)
TopHeadingLabel = Label(TopHeadingFrame, text="Flurys Hotel DashBoard",
                        font=("Helvetica", 24, "bold"), fg="white", bg="black")
TopHeadingLabel.pack(side=TOP, padx=10, anchor="center")

# MidFrame creation
mid_frame = Frame(window, bg="#7eed9f", bd=3)
mid_frame.pack(side=TOP, padx=30, pady=30)


#  Navigate customer page
def customer_page():
    window.destroy()
    import customer_page


# customer button
customer_btn = Button(mid_frame, text="Customer Page", command=customer_page,
                      font=("Helvetica", 18, "bold"), fg="black", bg="#7eed9f")
customer_btn.grid(row=0, column=0, padx=10, pady=10)


def customer_feedback():
    window.destroy()
    import customer_feedback


# navigate to customer feedback
feedback_btn = Button(mid_frame, text=" Customer Feedback", command=customer_feedback,
                      font=("Helvetica", 18, "bold"), fg="black", bg="#7eed9f")
feedback_btn.grid(row=1, column=0, padx=10, pady=10)


# booking page
def booking_details():
    window.destroy()
    import booking_details


# navigate to booking details
booking_btn = Button(mid_frame, text="Booking Details", command=booking_details,
                     font=("Helvetica", 18, "bold"), fg="black", bg="#7eed9f")
booking_btn.grid(row=2, column=0, padx=10, pady=10)

# Run the mainloop
window.mainloop()