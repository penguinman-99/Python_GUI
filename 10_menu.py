from tkinter import *

root=Tk()
root.title("Made by KKH")
root.geometry("640x480")

menu=Menu(root)

root.config(menu=menu)
def create_new_file():
    print("새파일 만듭니다.")
#File menu
menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="New file",command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()
menu_file.add_command(label="Open file")
menu_file.add_separator()
menu_file.add_command(label="save all",state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="FILE",menu=menu_file)
#edit menu(빈값)

menu.add_cascade(label="edit")
#language 메뉴 추가(radio로 택 1)
menu_lang=Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="python")

menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="java")
menu.add_cascade(label="lanauge",menu=menu_lang)

#View menu
menu_view=Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="show minimap")
menu.add_cascade(label="view",menu=menu_view)


root.mainloop()

