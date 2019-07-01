from tkinter import *
from backend_oop import Database

database = Database("books.db")

def delete_text():
    title_text.set("")
    author_text.set("")
    year_text.set("")
    isbn_text.set("")

def get_selected_row(event):
    global selected_row
    try:
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        title_text.set(selected_row[1])
        author_text.set(selected_row[2])
        year_text.set(int(selected_row[3]))
        isbn_text.set(int(selected_row[4]))
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
        delete_text()

def add_command():
    database.add(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, f"{title_text.get()}, {author_text.get()}, {year_text.get()}, {isbn_text.get()}")

def del_command():
    database.delete(selected_row[0])
    list1.delete(0, END)
    view_command()
    delete_text()

def update_command():
    database.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def close_command(window_name):
    database.close()
    window_name.destroy

window = Tk()
window.resizable(width= False, height= False)
window.title('Bookstore')

t1=Label(window, text="Title")
t1.grid(row=0, column=0)

title_text = StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

t2=Label(window, text="Author")
t2.grid(row=0, column=2)

author_text = StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

t3=Label(window, text="Year")
t3.grid(row=1, column=0)

year_text = StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

t4=Label(window, text="ISBN")
t4.grid(row=1, column=2)

isbn_text = StringVar()
e1=Entry(window, textvariable=isbn_text)
e1.grid(row=1, column=3)


list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

view = Button(window, text="View All", width = 12, command=view_command)
view.grid(row=2, column = 3)

search = Button(window, text="Search Entry", width = 12, command=search_command)
search.grid(row=3, column = 3)

add = Button(window, text="Add Entry", width = 12, command=add_command)
add.grid(row=4, column = 3)

update = Button(window, text="Update", width = 12, command=update_command)
update.grid(row=5, column = 3)

delete = Button(window, text="Delete", width = 12, command=del_command)
delete.grid(row=6, column = 3)

close = Button(window, text="Close", width = 12, command=close_command(window))
close.grid(row=7, column = 3)

window.mainloop()
