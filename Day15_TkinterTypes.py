
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Welcome to Registration")
window.geometry("1300x900")
window.config(bg="black")
window.resizable(False, False)

# Title
Label(window, text="Welcome To Registration Page", font=("Script MT Bold", 24, "bold"),
      bg="black", fg="white").pack(pady=(30, 30))

# Helper
def make_row(text):
    frame = Frame(window, bg="black")
    frame.pack(pady=12)
    Label(frame, text=text, font=("Arial", 13), bg="black", fg="white", width=12, anchor="w").pack(side=LEFT, padx=10)
    e = Entry(frame, font=("Arial", 13), bg="black", fg="white", insertbackground="white", relief="solid", bd=1, highlightthickness=1, highlightbackground="white", width=28)
    e.pack(side=LEFT, ipady=6)
    return e

name_entry = make_row("Full Name")
email_entry = make_row("Email")
phone_entry = make_row("Phone")
pass_entry = make_row("Password")
pass_entry.config(show="*")

# Gender - Radiobutton Black Theme
g_frame = Frame(window, bg="black")
g_frame.pack(pady=12)
Label(g_frame, text="Gender", font=("Arial", 13), bg="black", fg="white", width=12, anchor="w").pack(side=LEFT, padx=10)
gender_var = StringVar(value="Male")
Radiobutton(g_frame, text="Male", variable=gender_var, value="Male", bg="black", fg="white", selectcolor="black", activebackground="black", activeforeground="white", font=("Arial", 11)).pack(side=LEFT)
Radiobutton(g_frame, text="Female", variable=gender_var, value="Female", bg="black", fg="white", selectcolor="black", activebackground="black", activeforeground="white", font=("Arial", 11)).pack(side=LEFT, padx=10)

# City - Combobox
c_frame = Frame(window, bg="black")
c_frame.pack(pady=12)
Label(c_frame, text="City", font=("Arial", 13), bg="black", fg="white", width=12, anchor="w").pack(side=LEFT, padx=10)
city_combo = Combobox(c_frame, values=["Coimbatore", "Chennai", "Salem", "Madurai", "Trichy"], font=("Arial", 12), width=26, state="readonly")
city_combo.pack(side=LEFT)
city_combo.set("Select City")

# Skills - Checkbutton
s_frame = Frame(window, bg="black")
s_frame.pack(pady=12)
Label(s_frame, text="Skills", font=("Arial", 13), bg="black", fg="white", width=12, anchor="w").pack(side=LEFT, padx=10)
Checkbutton(s_frame, text="Python", bg="black", fg="white", selectcolor="black", activebackground="black", activeforeground="white", font=("Arial", 11)).pack(side=LEFT)
Checkbutton(s_frame, text="Java", bg="black", fg="white", selectcolor="black", activebackground="black", activeforeground="white", font=("Arial", 11)).pack(side=LEFT, padx=5)
Checkbutton(s_frame, text="Web", bg="black", fg="white", selectcolor="black", activebackground="black", activeforeground="white", font=("Arial", 11)).pack(side=LEFT)

result_label = Label(window, text="", font=("Arial", 12, "bold"), bg="black", fg="white")
result_label.pack(pady=15)

# Submit Button 
def register():
    if name_entry.get() == "" or email_entry.get() == "":
        result_label.config(text="Please Fill Name & Email!", fg="red")
    else:
        result_label.config(text=f"Welcome {name_entry.get()}! Registered Successfully", fg="#00ff00")

Button(window, text="Submit Register", font=("Arial", 14), bg="black", fg="white", relief="solid", bd=1, highlightthickness=1, width=30, cursor="hand2", command=register).pack(ipady=8, pady=10)

window.mainloop()

#---------------------------------------------------------------------------------------------

from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("All Widgets")
window.geometry("400x700")

# 1. Label
Label(window, text="1. Label - Name:").pack()

# 2. Entry
Entry(window).pack()

# 3. Combobox
Label(window, text="3. Combobox - City:").pack()
Combobox(window, values=["Coimbatore", "Chennai", "Salem"]).pack()

# 4. Button
Button(window, text="4. Button - Submit").pack(pady=5)

# 5. Radiobutton
Label(window, text="5. Radiobutton - Gender:").pack()
Radiobutton(window, text="Male", value=1).pack()
Radiobutton(window, text="Female", value=2).pack()

# 6. Checkbutton
Label(window, text="6. Checkbutton:").pack()
Checkbutton(window, text="I Agree").pack()

# 7. Listbox
Label(window, text="7. Listbox:").pack()
listbox = Listbox(window, height=3)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack()

# 8. Text - Periya Paragraph
Label(window, text="8. Text Box:").pack()
Text(window, height=3, width=30).pack()

# 9. Spinbox
Label(window, text="9. Spinbox - Age:").pack()
Spinbox(window, from_=1, to=100).pack()

# 10. Scale
Label(window, text="10. Scale - Volume:").pack()
Scale(window, from_=0, to=100, orient=HORIZONTAL).pack()

window.mainloop()

#---------------------------------------------------------------------------------------

#image

from PIL import ImageTk
from PIL import *
m1 = Image.open(r"m1.jpg")
mr1 = ImageTk.PhotoImage(m1.resize((201,251)))
photo =Label(a, image=mr1)
photo.place(x=100,y=100)
