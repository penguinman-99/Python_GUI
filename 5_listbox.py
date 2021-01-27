from tkinter import *

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")
#extended: 다중선택 가능 single:단 하나
listbox=Listbox(root,selectmode="extended",height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    #listbox.delete(END) #END 맨뒤의 항목 삭제 0 첫번째 항목삭제
    #항목의 갯수
    #print("리스트에는",listbox.size(),"개가 있어요")
    #항목 확인
    #print("1번쨰부터 3번째:",listbox.get(0,2))
    #선택된 항목 확인
    print("선택된 항목",listbox.curselection())
btn=Button(root,text="클릭",command=btncmd)
btn.pack()
root.mainloop()

