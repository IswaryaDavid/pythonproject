from tkinter import *
from PIL import Image, ImageTk  # Import from Pillow
window = Tk()
window.title("National Public School")
window.geometry("900x600")

# Top Frame
TopFrame = Frame(window, bg="black", height=70)
TopFrame.pack(side=TOP, fill=X)

# Top Frame heading
HeadingLabel = Label(TopFrame, text="National Public School system",
                     font=("arial", 24, "bold"), fg="#e07f10", bg="black")
HeadingLabel.pack(side=LEFT, padx=20, anchor="center")

# Right Frame Creation
rightFrame = Frame(window, bg="#144da8", width=250)
rightFrame.pack(side=RIGHT, fill=Y)


def parents_page():
    window.destroy()
    import parents_page


def employee_page():
    window.destroy()
    import employee_page


def teachers_page():
    window.destroy()
    import teachers_page


def attendance():
    window.destroy()
    import attendance


def student_fee():
    window.destroy()
    import student_fee


def admission_page():
    window.destroy()
    import admission_page


def logout():
    window.destroy()
    import Admin_signup


# Add buttons to right Frame
buttons = [
    ("Admission Page", admission_page),
    ("Parent's Page", parents_page),
    ("Employee page", employee_page),
    ("Teacher page", teachers_page),
    ("Attendance", attendance),
    ("Student Fee", student_fee),
    ("Logout", logout)
]

for btn_txt, btn_command in buttons:
    Button(rightFrame, text=btn_txt, font=("arial", 16),
           width=15, height=2, bg="#f07335", command=btn_command).pack(padx=10, pady=10)

# Left Frame creation
LeftFrame = Frame(window)
LeftFrame.pack(side=LEFT, expand=True, fill=BOTH)

# Load image Background to left frame
image_path = "school_bg.png"
img = Image.open(image_path)
img = img.resize((900, 600), Image.Resampling.LANCZOS)  # Resize the image
bg_image = ImageTk.PhotoImage(img)

bgLabel = Label(LeftFrame, image=bg_image)
bgLabel.pack(fill=BOTH, expand=True)

# Run mainloop
window.mainloop()
