from tkinter import *
from PIL import ImageTk,Image
import os

root=Tk()
root.title("notepad")
root.maxsize(1200,1200)
root.minsize(650,650)

open_img=ImageTk.PhotoImage(Image.open("open.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))

filename=Label(root,text="File Name")
filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename=Entry(root)
input_filename.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

open_btn=Button(root,image=open_img,text="Open_file")
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

save_btn=Button(root,image=save_img,text="Save image")
save_btn.place(relx=0.15,rely=0.03,anchor=CENTER)

def exitfunc():
    root.destroy()
    
exit_btn=Button(root,image=exit_img,text="EXIT",command=exitfunc)
exit_btn.place(relx=0.9,rely=0.03,anchor=CENTER)


root.mainloop()
