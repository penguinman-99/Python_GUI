from tkinter import *
    
root=Tk()
root.title("This is example.")
root.geometry("640x480")
root.resizable(False,False)
txt=Text(root,width=30,height=5)
txt.pack()
txt.insert(END,"후후")

ent=Entry(root,width=10)
ent.pack()
ent.insert(END,"히히히")

getvar=IntVar()
var1=Checkbutton(root,text="3일간 안보기",variable=getvar)
var1.select()
var1.pack()


def func():
    print(getvar.get())
bt1=Button(root,text="후이잉",command=func)
bt1.pack()




root.mainloop()