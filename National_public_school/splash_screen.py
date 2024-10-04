import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image


# Create a splash screen window
def splash_screen():
    splash = tk.Tk()
    splash.title("National Public School")
    splash.geometry("1200x800")
    splash.configure(bg='lightblue')

    # Load the background image
    try:
        bg_image = Image.open("child.png")
        resized_bg_image = bg_image.resize((1200, 800), Image.LANCZOS)
        bg_image_tk = ImageTk.PhotoImage(resized_bg_image)

        # Create a Label to hold the background image
        bg_label = Label(splash, image=bg_image_tk)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_image_tk  # Keep a reference to avoid garbage collection

    except Exception as e:
        # In case the image is not found, display a fallback text
        Label(splash, text="Welcome", font=("Helvetica", 24, "bold"),
              bg='#63420f', fg="white").pack(pady=200)

    # Add a Welcome Label
    welcome_label = Label(splash, text="Welcome",
                          font=("Helvetica", 24, "bold"), bg="black", fg="white")
    welcome_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Make the splash window stay on screen for 3 seconds and then open the Register/Login page
    splash.after(3000, lambda: Admin_signup(splash))

    splash.mainloop()


# Function to open Register page after splash screen
def Admin_signup(splash):
    splash.destroy()  # Close the splash screen
    import Admin_signup  # Ensure 'Register' module exists and works properly


# Run the splash screen
splash_screen()
