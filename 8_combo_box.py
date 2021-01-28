from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
values=[i for i in range(1,32)]

combobox=ttk.Combobox(root,height=5,values=values)
combobox.pack()
combobox.set("카드결제일") #최초 목록 제목

combobox2=ttk.Combobox(root,height=10,values=values,state="readonly")
combobox.current(0)
combobox2.pack()
combobox2.set("임의로 작성 불가능") #최초 목록 제목

def btncmd():
    print(combobox.get())
btn=Button(root,text="Order",command=btncmd)
btn.pack()
root.mainloop()

