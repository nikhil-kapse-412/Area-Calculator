#calculator

from tkinter import*
from tkinter.messagebox import*
import re 
from math import *

def f1():
    root.withdraw()
    ca.deiconify()

def back1():
    ca.withdraw()
    root.deiconify()

def f3():
    root.withdraw()
    tr.deiconify()

def back2():
    tr.withdraw()
    root.deiconify()

def f5():
    root.withdraw()
    sq.deiconify()

def back3():
    sq.withdraw()
    root.deiconify()

def f7():
    root.withdraw()
    rec.deiconify()

def back4():
    rec.withdraw()
    root.deiconify()

def f8():

    try:
        length = rec_ent_l.get()
        breadth = rec_ent_b.get()
        if  not (length):
            showerror("Issue", "length should not be empty")
            return
        if  not (breadth):
            showerror("Issue", "breadth should not be empty")
            return
        elif length.isalpha():
            showerror("issue", "length should not be text")
            return
        elif breadth.isalpha():
            showerror("issue", "breath should not be text")
            return
        elif float(length) < 0:
            showerror("Issue", "length cannot be negative")
            return
        elif float(breadth) < 0:
            showerror("Issue", "breadth cannot be negative")
            return
        else:
           length = float(length)
           breadth = float(breadth)
           area = length * breadth
           rec_lab_a.config(text=f"Area of Rectangle: {area:.2f} ")

    except ValueError as e:
        showerror("Issue", "Do not enter Special Character")

def f6():
    try:
        square = sq_ent_side.get()
       # regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if  not square:
            showerror("Issue", "side should not be empty")
            return
        elif square.isalpha():
            showerror("issue", "side should not be text")
            return
        elif float(square) < 0:
            showerror("Issue", "side cannot be negative")
            return
        else:
           
            square = float(square)
            area = square * square
            sq_lab_a.config(text=f"Area of Square: {area:.2f} ")
    except ValueError as e:
        showerror("Issue", "Do not enter special character")

def f2():
    try:
        radius = ca_ent_r.get()
        if  not radius:
            showerror("Issue", "Radius should not be empty")
            return
        elif radius.isalpha():
            showerror("issue", "Radius should not be text")
            return
        elif float(radius) < 0:
            showerror("Issue", "Radius cannot be negative")
            return
        else:
           radius = float(radius)
           area = radius * radius * 3.14
           ca_lab_a.config(text=f"Area of Cirle: {area:.2f} ")

    except ValueError as e:
        showerror("Issue", "Do not enter Special Character")
      
def f4():
    try:
        base = tr_ent_b.get()
        height = tr_ent_h.get()
        if  not (base):
            showerror("Issue", "base should not be empty")
            return
        if  not (height):
            showerror("Issue", " height should not be empty")
            return
        elif base.isalpha():
            showerror("issue", "base should not be text")
            return
        elif height.isalpha():
            showerror("issue", "height should not be text")
            return
        elif float(base) < 0:
            showerror("Issue", "base cannot be negative")
            return
        elif float(height) < 0:
            showerror("Issue", "height cannot be negative")
            return
        else:
           base = float(base)
           height = float(height)
           area = base * height * 0.5
           tr_lab_a.config(text=f"Area of Triangle: {area:.2f} ")
    except ValueError as e:
        showerror("Issue", "Do not enter Special Character")

root = Tk()
root.title("Calculator")
root.geometry("600x600+50+50")
f = ("Arial", 30, "bold")

lab_header = Label(root, text="Area Calculator", font=f)
lab_header.pack(pady=5)

root_btn_circle = Button(root, text="Area of Circle", font=f, command = f1)
root_btn_triangle = Button(root, text="Area of Triangle", font=f, command=f3)
root_btn_square = Button(root, text="Area of Sqaure", font=f, command=f5)
root_btn_rectangle = Button(root, text="Area of Rectangle", font=f, command=f7)
root_btn_circle.pack(pady=5)
root_btn_triangle.pack(pady=5)
root_btn_square.pack(pady=5)
root_btn_rectangle.pack(pady=5)

ca = Tk()
ca.title("Area of Circle")
ca.geometry("600x600+40+40")

def cr3():
        ca_ent_r.delete(0, END)
        ca_ent_cr3.delete(0,END)
        ca_lab_a.config(text="Area of Circle")

ca_lab_r = Label(ca, text="Enter radius of circle", font=f)
ca_ent_r = Entry(ca, font=f)
ca_lab_a = Label(ca, text="Area of circle ", font=f)
ca_btn_calc = Button(ca, text="Calculate Area of Circle", font=f, command=f2)
ca_btn_cr3 = Button(ca, text="Clear", font=f, command=cr3)
ca_ent_cr3 = Entry(ca, font=f)
ca_btn_back = Button(ca, text="back", font=f, command=back1)
ca_lab_r.pack(pady=5)
ca_ent_r.pack(pady=5)
ca_lab_a.pack(pady=5)
ca_btn_calc.pack(pady=5)
ca_btn_cr3.pack(pady=5)
ca_btn_back.pack(pady=5)
ca.withdraw()

tr = Tk()
tr.title("Area of Triangle")
tr.geometry("600x600+40+40")

def cr2():
    tr_ent_b.delete(0, END)
    tr_ent_h.delete(0, END)
    tr_ent_cr2.delete(0, END)  # Clear the rec_ent_clear entry field
    tr_lab_a.config(text="Area of rectangle")

tr_lab_b = Label(tr, text="Enter base of triangle", font=f)
tr_ent_b = Entry(tr, font=f)
tr_lab_h = Label(tr, text="Enter the height of triangle", font=f)
tr_ent_h = Entry(tr, font=f)
tr_lab_a = Label(tr, text="Area of Triangle ", font=f)
tr_btn_calc = Button(tr, text="Calculate area of triangle", font=f, command=f4)
tr_btn_cr2 = Button(tr, text="Clear", font=f, command=cr2)
tr_ent_cr2 = Entry(tr, font=f)
tr_btn_back = Button(tr, text="back", font=f, command=back2)
tr_lab_b.pack(pady=5)
tr_ent_b.pack(pady=5)
tr_lab_h.pack(pady=5)
tr_ent_h.pack(pady=5)
tr_lab_a.pack(pady=5)
tr_btn_calc.pack(pady=5)
tr_btn_cr2.pack(pady=5)
tr_btn_back.pack(pady=5)
tr.withdraw()

sq = Tk()
sq.title("Area of Sqaure")
sq.geometry("600x600+40+40")
font=f

def cr1():
    sq_ent_side.delete(0, END)
    sq_ent_clear.delete(0,END)
    sq_lab_a.config(text="Area of Square")

sq_lab_side = Label(sq, text="Enter side of square", font=f)
sq_ent_side = Entry(sq, font=f)
sq_lab_a = Label(sq, text="Area of Square", font=f)
sq_btn_calc = Button(sq, text="Calculate Area of Square", font=f, command=f6)
sq_btn_clear = Button(sq, text="Clear all", font=f, command=cr1)
sq_ent_clear = Entry(sq, font=f)
sq_btn_back = Button(sq, text="back", font=f, command=back3)
sq_lab_side.pack(pady=5)
sq_ent_side.pack(pady=5)
sq_lab_a.pack(pady=5)
sq_btn_calc.pack(pady=5)
sq_btn_clear.pack(pady=5)
sq_btn_back.pack(pady=5)
sq.withdraw()

rec = Tk()
rec.title("Area of Rectangle")
rec.geometry("600x600+40+40")

def cr():
    rec_ent_l.delete(0, END)
    rec_ent_b.delete(0, END)
    rec_ent_clear.delete(0, END)  # Clear the rec_ent_clear entry field
    rec_lab_a.config(text="Area of rectangle")

rec_lab_l = Label(rec, text="Enter length of rectangle", font=f)
rec_ent_l = Entry(rec, font=f)
rec_lab_b = Label(rec, text="Enter the breadth of rectangle", font=f)
rec_ent_b = Entry(rec, font=f)
rec_lab_a = Label(rec, text="Area of Rectangle", font=f)
rec_btn_calc = Button(rec,text="Calculate area of rectangle", font=f, command=f8 )
rec_btn_clear = Button(rec, text="Clear All", font=f, command=cr)
rec_ent_clear = Entry(rec, text="", font=f)
rec_btn_back = Button(rec, text="back", font=f, command=back4)
rec_lab_l.pack(pady=5)
rec_ent_l.pack(pady=5)
rec_lab_b.pack(pady=5)
rec_ent_b.pack(pady=5)
rec_lab_a.pack(pady=5)
rec_btn_calc.pack(pady=5)
rec_btn_clear.pack(pady=5)
rec_btn_back.pack(pady=5)
rec.withdraw()

def f9():
    if askokcancel("Quit", "Do u want to exit"):
        ca.destroy()
        tr.destroy()
        sq.destroy()
        rec.destroy()

ca.protocol("WM_DELETE_WINDOW", f9)
tr.protocol("WM_DELETE_WINDOW", f9)
sq.protocol("WM_DELETE_WINDOW", f9)
rec.protocol("WM_DELETE_WINDOW", f9)

root.mainloop()