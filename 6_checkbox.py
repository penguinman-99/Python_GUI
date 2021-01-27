from tkinter import *

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
checkvar=IntVar()#체크바에 int형으로 값저장 
checkbox=Checkbutton(root,text="3일간 보지 않기",variable=checkvar)
checkbox.select()#자동선택처리
#checkbox.deselect() 자동 비선택처리
checkbox.pack()
checkvar2=IntVar()
checkbox2=Checkbutton(root,text="일주일동안 안보기",variable=checkvar2)
checkbox2.pack()
def btncmd():
    print(checkvar.get())#0:체크해제, 1:체크됨
    print(checkvar2.get())
btn=Button(root,text="클릭",command=btncmd)
btn.pack()
root.mainloop()

