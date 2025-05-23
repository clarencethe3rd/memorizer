from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import*
gui = Tk()

gui.geometry("800x500")

gui.title("Memorizer")

def save():
    f=asksaveasfile(defaultextension=".txt")
    for i in listbox.get(0,END):
        print(i.strip(),file=f)
        
def open_file():
    f=askopenfile(title = "Open file")
    content = f.readlines()
    listbox.delete(0,END)
    for i in content:
        listbox.insert(END,i)
def add():
    e = entry.get()
    listbox.insert(END,e)
    entry.delete(0,END)

def delete1():
    index = listbox.curselection()
    listbox.delete(index)

save_button = Button(text="SAVE",command=save)
save_button.pack(pady=(20,0))

entry = Entry()
entry.pack()

add_button = Button(text="ADD",command=add)
add_button.pack()

open_button = Button(text="OPEN",command=open_file)
open_button.place(x=0,y=150)


    

frame = Frame(gui)
frame.place(x=95,y=125)
scrollbar=Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)

listbox = Listbox(frame,width=66,height=20,yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT)
scrollbar.config(command=listbox.yview)

delete_button = Button(text="DELETE",command=delete1)
delete_button.place(x=705,y=150)

for i in range(100):
    listbox.insert(END,i)


gui.mainloop()
