from tkinter import *
import random
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
#import json
#create window
root = Tk()

#change bg color
root.configure(bg="#244761")

#change title
root.title("Radio Sphere")

#change window size
root.geometry("440x315")

#   ---Create empty List
tasks = []

#For testing use default List
tasks = []
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
    task1 = call_input.get()
    task2 = name_input.get()
    task3 = loc_input.get()
    task = "Callsign: " + task1 + " | Name: " + task2 + " | Location: " + task3
    #confirm task is not empty
    if task1 !="" and task2 != "" and task3 != "":
        #append new task to list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Did not enter", "Please enter text in all fields")
    call_input.delete(0,"end")
    name_input.delete(0,"end")
    loc_input.delete(0,"end")
def del_all():
    confirmed = tkinter.messagebox.askyesno("Delete All!", "Are you sure you want to delete all?")
    if confirmed == True:
        #since we are changing a list it needs to be global
        global tasks
        #clear tasks List
        tasks = []
        lbl_tooltip["text"]="Deleted All"
        #update the Listbox
        update_listbox()

def del_all_event(event):
    confirmed = tkinter.messagebox.askyesno("Delete All!", "Are you sure you want to delete all?")
    if confirmed == True:
        #since we are changing a list it needs to be global
        global tasks
        #clear tasks List
        tasks = []
        lbl_tooltip["text"]="Deleted All"
        #update the Listbox
        update_listbox()

def del_one():
    #Get the text of the currently selected item
    task = lb_tasks.get("active")
    #confirm its in the list
    if task in tasks:
        tasks.remove(task)
    lbl_tooltip["text"]="Deleted"
    #update Listbox
    update_listbox()


def del_one_event(event):
    #Get the text of the currently selected item
    task = lb_tasks.get("active")
    #confirm its in the list
    if task in tasks:
        tasks.remove(task)
    lbl_tooltip["text"]="Deleted"
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
    if not tasks:
        tkinter.messagebox.showinfo("none", "Nothing in list")
    else:
        task = random.choice(tasks)
        #update display Label
        tkinter.messagebox.showinfo("Random Call", str(task))

def show_number_of_tasks():
    #get the number of tasks
    number_of_tasks = len(tasks)
    #create and format the Message
    msg = "Number of Entries: %s" %number_of_tasks
    #Display the Message
    if number_of_tasks == 0:
        tkinter.messagebox.showinfo('None','No Entries, Make some')
    else:
        lbl_tooltip["text"]=msg

def save_file_as():
    res = filedialog.askopenfilename(filetypes = (("Text Files", "*.txt"), ("all files", "*.*")))
    if res is None:
        return
    else:
        print(res)

        lbl_tooltip["text"]="Saved"
        with open(res, "w") as filehandle:
            for item in tasks:
                filehandle.write('%s\n' % item)

def save_file_as_event(event):
    res = filedialog.askopenfilename(filetypes = (("Text Files", "*.txt"), ("all files", "*.*")))
    if res is None:
        return
    else:
        print(res)

        lbl_tooltip["text"]="Saved"

        with open(res, "w") as filehandle:
            for item in tasks:
                filehandle.write('%s\n' % item)


comm4 = """
def save_file(re):
    if re is None:
         re = save_file_as()
    else:
        print(re)
        with open(re, "w") as filehandle:
            for item in tasks:
                filehandle.write('%s\n' % item)
"""
def open_file_as():
    open_con = tkinter.messagebox.askyesno("Open File", "Are you sure you want to Open the file, \n this will delete all unsaved work")
    if open_con:
        res = filedialog.askopenfilename(filetypes = (("Text Files", "*.txt"), ("all files", "*.*")))
        if res is None:
            return
        else:
            print(res)
            print("open")
            tasks.clear()
            clear_listbox()
            lbl_tooltip["text"]="Opened"
            with open(res, "r") as filehandle:
                for line in filehandle:
                    #remove linebreak which is last character of string
                        currentTask = line[:-1]
                        tasks.append(currentTask)
            update_listbox()

def open_file_as_event(event):
    open_con = tkinter.messagebox.askyesno("Open File", "Are you sure you want to Open the file, \n this will delete all unsaved work")
    if open_con:
        res = filedialog.askopenfilename(filetypes = (("Text Files", "*.txt"), ("all files", "*.*")))
        if res is None:
            return
        else:
            print(res)
            print("open")
            tasks.clear()
            clear_listbox()
            lbl_tooltip["text"]="Opened"
            with open(res, "r") as filehandle:
                for line in filehandle:
                    #remove linebreak which is last character of string
                        currentTask = line[:-1]
                        tasks.append(currentTask)
            update_listbox()






def add_call():
    #gET THE TASK TO Add
    new_call = call_input.get()

    task = "Callsign: " + new_call
    #confirm task is not empty
    if new_call != "":
        #append new task to list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Did not enter", "Please enter text in Callsign field")
    call_input.delete(0,"end")







def add_name():
    #gET THE TASK TO Add
    new_name = name_input.get()

    task = "Name: " + new_name
    #confirm task is not empty
    if new_name != "":
        #append new task to list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Did not enter", "Please enter text in Name field")
    name_input.delete(0,"end")


def res_print(a):
    print(a)







def add_loc():
    #gET THE TASK TO Add
    new_loc = loc_input.get()

    task = "Location: " + new_loc
    #confirm task is not empty
    if new_loc != "":
        #append new task to list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Did not enter", "Please enter text in Location field")
    loc_input.delete(0,"end")


def place_search():
    if search_entry is not None:
        if search_entry.get() in tasks:
            print("found")
    else:
        return








comm3 = """
def open_file():
    open_con = tkinter.messagebox.askyesno("Open File", "Are you sure you want to Open the file, \n this will delete all unsaved work")
    if open_con:
        try:
            res
        except NameError:
            tkinter.messagebox.showinfo('Error', "No file to open to, use open as")
            open_file_as()
        else:
            print(res)
            print("open")
            tasks.clear()
            clear_listbox()
            with open(res, "r") as filehandle:
                for line in filehandle:
                    #remove linebreak which is last character of string
                        currentTask = line[:-1]
                        tasks.append(currentTask)
            update_listbox()
"""
#   ---Drop Down Menu---
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
#fileMenu.add_command(label="Save", command=save_file)
#fileMenu.add_command(label="Open", command=open_file)
#fileMenu.add_separator()
fileMenu.add_command(label="Save As", command=save_file_as, accelerator="Ctrl+S")
fileMenu.add_command(label="Open As", command=open_file_as, accelerator="Ctrl+O")
fileMenu.add_command(label="Quit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Delete", command=del_one, accelerator="Ctrl+D")
editMenu.add_command(label="Delete All", command=del_all, accelerator="Ctrl+E")

optMenu = Menu(menu)
menu.add_cascade(label="Options", menu=optMenu)
optMenu.add_command(label="Sort Ascending", command=sort_asc)
optMenu.add_command(label="Sort Descending", command=sort_desc)
optMenu.add_command(label="Choose Random", command=choose_random)
optMenu.add_command(label="Number of Entries", command=show_number_of_tasks)

#   ---Status Bar---

#   ---main elements---

lbl_title = Label(root, text="Radio Sphere", bg="#244761", fg="white")
lbl_title.grid(row=0, column=0,columnspan=2)

lbl_tooltip = Label(root, text="", bg="#244761", fg="white")
lbl_tooltip.grid(row=0,column=3, columnspan=2)


lbl_display = Label(root, text="", bg="#244761", fg="white")
lbl_display.grid(row=0, column=2)


call_label = Label(root, text="Callsign:", bg='#244761', fg="white").grid(column=1, row=2, sticky=E)
call_input = Entry(root, width=25, bg="#244761", fg="white")
call_input.grid(row=2, column=2)

name_label = Label(root, text="Name:", bg="#244761", fg="white").grid(column=1, row=3, sticky=E)
name_input = Entry(root, width=25,bg="#244761", fg="white")
name_input.grid(row=3,column=2)

loc_label = Label(root, text="Location:", bg="#244761", fg="white").grid(column=1, row=4, sticky=E)
loc_input = Entry(root, width=25, bg="#244761", fg="white")
loc_input.grid(row=4, column=2)

search_label = Label(root, text="Search:", bg="#244761", fg="white").grid(column=1, row=1, sticky=E)
search_entry = Entry(root, width=56, bg="#244761", fg="white").grid(column=2,row=1, columnspan=6, sticky=W)
btn_search = Button(root, text="Go", fg="#49e67b", bg="#244761", command=place_search).grid(column=0,row=1, pady=2)

btn_add_task = Button(root, text="Add Contact", fg="white", bg="#244761", command=add_task, height=4, width=25)
btn_add_task.grid(row=2, column=3, sticky=W, rowspan=3, padx=4)

btn_add_call = Button(root, text="Add", fg="#49e67b", bg="#244761", command=add_call)
btn_add_call.grid(row=2, column=0, sticky=W, padx=3, pady=1)

btn_add_name = Button(root, text="Add", fg="#49e67b", bg="#244761", command=add_name)
btn_add_name.grid(row=3, column=0, sticky=W, padx=3, pady=1)

btn_add_loc = Button(root, text="Add", fg="#49e67b", bg="#244761", command=add_loc)
btn_add_loc.grid(row=4, column=0, sticky=W, padx=3, pady=1)

comment = """
btn_del_all = Button(root, text="Delete All", fg="black", bg="white", command=del_all)
btn_del_all.grid(row=2, column=2)

btn_del_one = Button(root, text="Delete", fg="black", bg="white", command=del_one)
btn_del_one.grid(row=3, column=2)

btn_sort_asc = Button(root, text="Sort Ascending", fg="black", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4, column=2)

btn_sort_desc = Button(root, text="Sort Decending", fg="black", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5, column=2)

btn_choose_random = Button(root, text="Choose random", fg="black", bg="white", command=choose_random)
btn_choose_random.grid(row=6, column=2)

btn_number_of_tasks = Button(root, text="Number Of Tasks", fg="black", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7, column=2)

btn_exit = Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_exit.grid(row=8, column=2)
btn_save = Button(root, text="Save", fg="black", bg="white", command=save_file)
btn_save.grid(row=9, column=2)

btn_open = Button(root, text="Open", fg="black", bg="white", command=open_file)
btn_open.grid(row=10, column=2)
"""
lb_tasks = Listbox(root, width=71, bg="#244761", fg="white")
lb_tasks.grid(row=5, column=0, rowspan=10, columnspan=6, pady=2, padx=1)

lbl_creator = Label(root, text="Created by Nathan Branch 2019 :)", bg="#244761", fg="white").grid(row=15, column=0, columnspan=6, pady=2)
#   ---Keyboard Shortcuts
root.bind("<Control-s>", save_file_as_event)
root.bind("<Control-S>", save_file_as_event)
root.bind("<Control-o>", open_file_as_event)
root.bind("<Control-O>", open_file_as_event)
root.bind("<Control-D>", del_one_event)
root.bind("<Control-d>", del_one_event)
root.bind("<Control-E>", del_all_event)
root.bind("<Control-e>", del_all_event)

#main event mainloop
root.mainloop()
