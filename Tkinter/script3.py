from tkinter import *

window = Tk()

def convert():
    grams = float(e1value.get())*1000
    pounds = float(e1value.get())*2.20462
    ounces = float(e1value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1value=StringVar()
e1 = Entry(window, textvariable=e1value)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 2)

window.mainloop()
