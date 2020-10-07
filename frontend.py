from tkinter import *
import backend

def get_selected_data(event):
    global selected
    index=list1.curselection()[0]
    selected=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected[1])
    e2.delete(0,END)
    e2.insert(END,selected[2])
    e3.delete(0,END)
    e3.insert(END,selected[3])
    e4.delete(0,END)
    e4.insert(END,selected[4])

def update_data():
    backend.update(selected[0],name_entry.get(),email_entry.get(),address_entry.get(),number_entry.get())
    list1.delete(0,END)
    list1.insert(END,"updated succesfully!!!!!")    

def delete_data():
    backend.delete(selected[0])
    list1.delete(0,END)
    list1.insert(END,"deleted succesfully!!!!!")

def view_data():
    list1.delete(0,END)
    for i in backend.view():
        list1.insert(END,i)

def search_data():
    list1.delete(0,END)
    for i in backend.search(name_entry.get(),email_entry.get(),address_entry.get(),number_entry.get()):
        list1.insert(END,i)

def add_data():
    list1.delete(0,END)
    backend.insert(name_entry.get(),email_entry.get(),address_entry.get(),number_entry.get())
    list1.insert(END,"Added succesfully!!!!!")


window=Tk()

window.wm_title("Address book")

l1=Label(window,text='Name')
l1.grid(row=0,column=0)

l2=Label(window,text='E-mail')
l2.grid(row=0,column=3)

l3=Label(window,text='Address')
l3.grid(row=1,column=0)

l4=Label(window,text='Phone')
l4.grid(row=1,column=3)

name_entry=StringVar()
e1=Entry(window,textvariable=name_entry)
e1.grid(row=0,column=1)

email_entry=StringVar()
e2=Entry(window,textvariable=email_entry)
e2.grid(row=0,column=4)

address_entry=StringVar()
e3=Entry(window,textvariable=address_entry)
e3.grid(row=1,column=1)

number_entry=StringVar()
e4=Entry(window,textvariable=number_entry)
e4.grid(row=1,column=4)

list1=Listbox(window,height=6,width=30)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_data)

b1=Button(window,text='view all',width=12,command=view_data)
b1.grid(row=3,column=4)

b2=Button(window,text='search',width=12,command=search_data)
b2.grid(row=4,column=4)

b3=Button(window,text='add',width=12,command=add_data)
b3.grid(row=5,column=4)

b4=Button(window,text='update',width=12,command=update_data)
b4.grid(row=6,column=4)

b5=Button(window,text='delete',width=12,command=delete_data)
b5.grid(row=7,column=4)

b6=Button(window,text='close',width=12,command=window.destroy)
b6.grid(row=8,column=4)

window.mainloop()
