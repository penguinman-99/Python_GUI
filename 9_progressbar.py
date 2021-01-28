from tkinter import *
import tkinter.ttk as ttk
import time

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
#progressbar=ttk.Progressbar(root,maximum=100,mode="indeterminate")

# progressbar=ttk.Progressbar(root,maximum=100,mode="determinate")
# progressbar.start(100)
# progressbar.pack()

# def btncmd():
#     progressbar.stop() #중지 
# btn=Button(root,text="Order",command=btncmd)
# btn.pack()
p_var2=DoubleVar()
prog2=ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
prog2.pack()
def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)
        p_var2.set(i)#progresss bar 값 설정
        prog2.update() #ui 업데이트
        print(p_var2.get())


btn=Button(root,text="Order",command=btncmd2)
btn.pack()


root.mainloop()

