from tkinter import *
import tkinter.messagebox as msgbox

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")

Label(root,text="메뉴 선택해주세요").pack(side="top")
Button(root,text="주문하기").pack(side="bottom")
#relief:테두리모양 bd:외곽선 
frame_burger=Frame(root,relief="solid",bd=1)
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger,text="햄버거").pack()

Button(frame_burger,text="치즈버거").pack()
Button(frame_burger,text="오징어버거").pack()

frame_drink=LabelFrame(root,text="음료")
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()

root.mainloop()

