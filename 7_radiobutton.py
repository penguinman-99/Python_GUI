from tkinter import *

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")

Label(root,text="메뉴 골라요").pack()
burger_var=IntVar() #여기에 정수형으로 값 저장
bt_burger1=Radiobutton(root,text="햄버거",value=1,variable=burger_var)
bt_burger1.select()
bt_burger2=Radiobutton(root,text="치즈버거",value=2,variable=burger_var)
bt_burger3=Radiobutton(root,text="싸이버거",value=3,variable=burger_var)
bt_burger1.pack()
bt_burger2.pack()
bt_burger3.pack()
drink_var=StringVar()
bt_drink1=Radiobutton(root,text="콜라",value="콜라",variable=drink_var)

bt_drink2=Radiobutton(root,text="사이다",value="사이다",variable=drink_var)
bt_drink3=Radiobutton(root,text="환타",value="환타",variable=drink_var)
bt_drink1.select()
bt_drink1.pack()
bt_drink2.pack()
bt_drink3.pack()
def btncmd():
    print(burger_var.get())
    print(drink_var.get())
btn=Button(root,text="Order",command=btncmd)
btn.pack()
root.mainloop()

