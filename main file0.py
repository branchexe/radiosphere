from tkinter import *
import random
import tkinter.messagebox
#create window
root = Tk()
txt_call
#change bg color
root.configure(bg="white")

#change title
root.title("To-Do List")

#change window size
root.geometry("425x250")

#   ---Create empty List
tasks = []

#For testing use default List
tasks = ["call mom", "feed dog", "Code some more"]

#   ---create functions---

def update_listbox():
    #clear the current List
    clear_listbox()
    #populate the Listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    #gET THE TASK TO Add
    task = txt_input.get()
    #confirm task is not empty
    if task !="":
        #append new task to list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Did not enter", "Please enter text")
    txt_input.delete(0,"end")
def del_all():
    confirmed = tkinter.messagebox.askyesno("Delete All!", "Are you sure you want to delete all?")
    if confirmed == True:
        #since we are changing a list it needs to be global
        global tasks
        #clear tasks List
        tasks = []
        #update the Listbox
        update_listbox()

def del_one():
    #Get the text of the currently selected item
    task = lb_tasks.get("active")
    #confirm its in the list
    if task in tasks:
        tasks.remove(task)
    #update Listbox
    update_listbox()

def sort_asc():
    #sort the list
    tasks.sort()
    #update the Listbox
    update_listbox()

def sort_desc():
    #sort the list
    tasks.sort()
    #reverse the List
    tasks.reverse()
    #update the Listbox
    update_listbox()

def choose_random():
    #Choose random task
    task = random.choice(tasks)
    #update display Label
    lbl_display["text"]=task

def show_number_of_tasks():
    #get the number of tasks
    number_of_tasks = len(tasks)
    #create and format the Message
    msg = "Number of tasks: %s" %number_of_tasks
    #Display the Message
    lbl_display["text"]=msg

def new_contact():
    new = Toplevel(root)
    new.configure(bg="white")
    new.title("New Contact")
    lbl_call = Label(new, text="Callsign:").grid(column=0, row=0, sticky=E)
    lbl_loc = Label(new,text="Location:").grid(column=0, row=1, sticky=E)
    lbl_name = Label(new,text="Name:").grid(column=0,row=2, sticky=E)

    txt_call = Entry(new, width=50).grid(column=1,row=0)
    txt_loc = Entry(new, width=50).grid(column=1,row=1)
    txt_name = Entry(new, width=50).grid(column=1, row=2)

    btn_submit = Button(new, text="Submit", command=add_contact, width=50).grid(column=0, columnspan=2, row=3)

    new.mainloop()
def add_contact():
    pass

lbl_title = Label(root, text="To-Do List", bg="white")
lbl_title.grid(row=0, column=0)

lbl_display = Label(root, text="", bg="white")
lbl_display.grid(row=0, column=1)

txt_input = Entry(root, width=50)
txt_input.grid(row=0, column=0)

btn_add_task = Button(root, text="Add Task", fg="black", bg="white", command=add_task)
btn_add_task.grid(row=1, column=1)

btn_del_all = Button(root, text="Delete All", fg="black", bg="white", command=del_all)
btn_del_all.grid(row=2, column=1)

btn_del_one = Button(root, text="Delete", fg="black", bg="white", command=del_one)
btn_del_one.grid(row=3, column=1)

btn_sort_asc = Button(root, text="Sort Ascending", fg="black", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4, column=1)

btn_sort_desc = Button(root, text="Sort Decending", fg="black", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5, column=1)

btn_choose_random = Button(root, text="Choose random", fg="black", bg="white", command=choose_random)
btn_choose_random.grid(row=6, column=1)

btn_number_of_tasks = Button(root, text="Number Of Tasks", fg="black", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7, column=1)

btn_exit = Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_exit.grid(row=8, column=1)

btn_new = Button(root, text="New", fg="black", bg="white", command=new_contact)
btn_new.grid(row=8, column=1)


lb_tasks = Listbox(root, width=50)
lb_tasks.grid(row=2, column=0, rowspan=8)

#main event mainloop
root.mainloop()
