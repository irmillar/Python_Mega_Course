from tkinter import *

"""
This class is used to create a new instance of a Project GUI for users to
access. Methods within this class will allows users to add and manage
resources for their project and track total project spend.
"""

window = Tk()
window.title("Resource Planner")

# Create a label for the 'First Name' option
l1 = Label(window, text="First Name")
l1.grid(row=0, column=0)

# Create an entry field for the 'Name' option
fname_text = StringVar()
e1 = Entry(window, textvariable=fname_text)
e1.grid(row=0, column=1)

# Create a label for the 'Role' option
l2 = Label(window, text="Role")
l2.grid(row=0, column=2)

# Create an entry field for the 'Role' option
role_text = StringVar()
e2 = Entry(window, textvariable=role_text)
e2.grid(row=0, column=3)

# Create a label for the 'Start Date' option
l3 = Label(window, text="Start Date")
l3.grid(row=1, column=0)

# Create an entry field for the 'Start Date' option
sdate_text = StringVar()
e3 = Entry(window, textvariable=sdate_text)
e3.grid(row=1, column=1)

# Create a label for the 'End Date' option
l4 = Label(window, text="End Date")
l4.grid(row=1, column=2)

# Create an entry field for the 'Start Date' option
edate_text = StringVar()
e4 = Entry(window, textvariable=edate_text)
e4.grid(row=1, column=3)

# Create a label for the 'Daily Salary' option
l5 = Label(window, text="Daily Salary")
l5.grid(row=2, column=0)

# Create an entry field for the 'Daily Salary' option
dsalary_text = StringVar()
e5 = Entry(window, textvariable=dsalary_text)
e5.grid(row=2, column=1)


# Create a Listbox to list all of the data in
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 3, column = 0, rowspan = 6, columnspan = 2)

# Add a scrollbar for the listbox
scrollbar = Scrollbar(window)
scrollbar.grid(row = 3, column = 2, rowspan = 6)

# Attach the scrollbar to the listbox
list1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list1.yview)

# Add bind the listbox to a command which occurs when an item occurs
#list1.bind('<<ListboxSelect>>', get_selected_row)

# Add a view all button
view = Button(window, text="View", width=12, command=print("View"))
view.grid(row = 3, column = 3)

# Add a search Button
search = Button(window, text="Search", width=12, command=print("Search"))
search.grid(row=4, column=3)

# Add an Add Button
add = Button(window, text="Add", width=12, command=print("Add"))
add.grid(row=5, column=3)

window.mainloop()
