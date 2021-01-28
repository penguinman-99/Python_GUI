from tkinter import *
import tkinter.messagebox as msgbox

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
#기차 예매 시스템
def info():
    msgbox.showinfo("알림","정상적으로 예매되었습니다.")
def warn():
    msgbox.showwarning("경고","이미 예매된 좌석입니다.")
def error():
    msgbox.showerror("오류","결제 오류 발생.")
def okcancel():
    msgbox.askokcancel("확인/취소","유아석입니다. 예매하시겠습니까?")
def retrycancel():
    msgbox.askretrycancel("재시도/취소","다시하겠습니까?")
def yesno():
    msgbox.askyesno("yes/no","역방향석입니다. 그래도 하시겠습니까?")
def yesnocancel():
    response=msgbox.askyesnocancel(title=None,message="저장하시겠습니까?")
    #네: 저장후 종료
    #아니오: 저장안하고 종료
    print("응답:",response)

Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="오류").pack()

Button(root,command=okcancel,text="확인취소").pack()

Button(root,command=retrycancel,text="재시도취소").pack()
Button(root,command=yesno,text="예 아니오").pack()
Button(root,command=yesnocancel,text="예 아니오 취소").pack()

root.mainloop()

