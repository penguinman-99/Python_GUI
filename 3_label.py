from tkinter import *

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
label1=Label(root,text="도우너 어서오고.")
label1.pack()

photo=PhotoImage(file="C:/Users/Administrator/Desktop/PythonWorkSpace/Python_GUI/Python_GUI/img.png")
label2=Label(root,image=photo)
label2.pack()
def change():
    label1.config(text="아침부터 왜이리 죽상이야")
    global photo2
    photo2=PhotoImage(file="C:/Users/Administrator/Desktop/PythonWorkSpace/Python_GUI/Python_GUI/img2.png")
    label2.config(image=photo2)
bt1=Button(root,text="클릭",command=change)
bt1.pack()


root.mainloop()

