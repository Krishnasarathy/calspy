from tkinter import *
root=Tk()
root.title("Calculator")
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    # e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_cl():
    e.delete(0,END)

def button_add():
    first_number= e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))

bt_1=Button(root,text=1,padx=40,pady=20,command=lambda:button_click(1))
bt_2=Button(root,text=2,padx=40,pady=20,command=lambda:button_click(2))
bt_3=Button(root,text=3,padx=40,pady=20,command=lambda:button_click(3))
bt_4=Button(root,text=4,padx=40,pady=20,command=lambda:button_click(4))
bt_5=Button(root,text=5,padx=40,pady=20,command=lambda:button_click(5))
bt_6=Button(root,text=6,padx=40,pady=20,command=lambda:button_click(6))
bt_7=Button(root,text=7,padx=40,pady=20,command=lambda:button_click(7))
bt_8=Button(root,text=8,padx=40,pady=20,command=lambda:button_click(8))
bt_9=Button(root,text=9,padx=40,pady=20,command=lambda:button_click(9))
bt_0=Button(root,text=0,padx=40,pady=20,command=lambda:button_click(0))
button_ad=Button(root,text="+",padx=39,pady=20,command=button_add)
button_el=Button(root,text="=",padx=100,pady=20,command=button_equal)
button_clear=Button(root,text="C",padx=100,pady=20,command=button_cl)

bt_1.grid(row=3,column=0)
bt_2.grid(row=3,column=1)
bt_3.grid(row=3,column=2)
bt_4.grid(row=2,column=0)
bt_5.grid(row=2,column=1)
bt_6.grid(row=2,column=2)
bt_7.grid(row=1,column=0)
bt_8.grid(row=1,column=1)
bt_9.grid(row=1,column=2)

bt_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=3)
button_ad.grid(row=5,column=0)
button_el.grid(row=5,column=1,columnspan=3)

root.mainloop()