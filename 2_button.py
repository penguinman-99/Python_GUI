from tkinter import *

root=Tk()
root.title("Made by KKH")

bt1=Button(root,text="버튼1")
bt1.pack()
#pad:글자와 상자 여백 width, height:글자에 상관없이 상자 크기
bt2=Button(root,padx=5,pady=10,text="버튼2ddddd")
bt2.pack()

bt3=Button(root,padx=10,pady=5,text="버튼3")
bt3.pack()

bt4=Button(root,width=10,height=3,text="버튼4")
bt4.pack()
#fg: 글자 색, bg: 배경색
bt5=Button(root,fg="red",bg="yellow",text="버튼5")
bt5.pack()
photo=PhotoImage(file="C:/Users/Administrator/Desktop/PythonWorkSpace/Python_GUI/Python_GUI/img.png")
bt6=Button(root,image=photo)
bt6.pack()
def btncmd():
    print("정지가 안돼잖아")
bt7=Button(root,text="장비를 정지합니다.",command=btncmd)
bt7.pack()
root.mainloop()

