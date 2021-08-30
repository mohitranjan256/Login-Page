from tkinter import *
boot = Tk()
from PIL import ImageTk, Image


boot.title("LOGIN Page")
boot.geometry("800x500")

#image open=========================
my_pic = Image.open("C:/Users/Mohit Ranjan/Desktop/Mohit/RAYS/NIT logo black.png")

#resize===================

resized = my_pic.resize((100,100), Image.ANTIALIAS)
icon =ImageTk.PhotoImage(resized)


l0 = Label(boot, text ="WELCOME TO TEAM RAYS " ,font = ("Arial Bold",20),bg=("Yellow"),fg=("Green"))

my_pic1 = Image.open("C:/Users/Mohit Ranjan/Desktop/Mohit/RAYS/TEAM RAYS logo 2-1.png")
#resize==========================

resized = my_pic1.resize((150,150), Image.ANTIALIAS)
icon1 =ImageTk.PhotoImage(resized)

#===========================================
def click():
    txt_1.set("")
    txt_2.set("")
    


txt_1=StringVar()
txt_2=StringVar()

#=========================

l3 = Label(boot, image=icon)
l3.grid(column = 0 ,row =0)
l0.grid(column = 2,row =0)
l4 = Label(boot, image=icon1)
l4.grid(column = 4,row =0)




l1 = Label(boot, text ="Enter The Username" ,font = ("Arial Bold",10))
E1 = Entry(boot, textvariable=txt_1)
l2 = Label(boot, text ="Enter your Password" ,font = ("Arial Bold",10))
E2 = Entry(boot, textvariable=txt_2)

l1.grid(column = 1 ,row = 8)
E1.grid(column = 2, row = 8)
l2.grid(column = 1 ,row =9)
E2.grid(column = 2, row = 9)


Button(boot, text = "Submmit" , font = ("BOLD"),command=lambda:click()).grid(column=2,row=12)

boot.mainloop()
