from tkinter import *

root=Tk()

e= Entry(root,width=50,borderwidth=5)
e.pack()
# e.insert(0,"Enter")
def myclick():
    my=Label(root,text="Hi "+e.get())
    my.pack()
myLabel= Label(root,text="Hello world")
myButton=Button(root,text="click",command=myclick,fg="blue",bg="cyan")

myLabel.pack()
myButton.pack()

root.mainloop()