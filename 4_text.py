from tkinter import *

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
txt=Text(root,width=30,height=5)
txt.pack()

#글자를 미리 넣어두기
txt.insert(END,"글자 넣어조")
#Text: 줄바꿈 가능 Entry:줄바꿈 불가능
e=Entry(root,width=30)
e.pack()
e.insert(0,"한줄만...")
def btncmd():
    #내용 출력
    print(txt.get("1.0", END))#1: 첫번째 라인, 0:0번쨰 컬럼
    print(e.get())
    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)
bt1=Button(root,text="삐빅",command=btncmd)
bt1.pack()
root.mainloop()

