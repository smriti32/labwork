from tkinter import *
root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.configure(bg='grey')
def Clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
    result.delete(0,'end')

def Add():
   num=int(e1.get())
   num2=int(e2.get())

   sum=num+num2
   result.insert(10,sum)

def Sub():
       num3=int(e1.get())
       num4=int(e2.get())

       sub=num3-num4
       result.insert(10,sub)

def Mul():
       num5=int(e1.get())
       num6=int(e2.get())

       mul=num5*num6
       result.insert(10,mul)

def Div():
       num7=int(e1.get())
       num8=int(e2.get())
       divide=num7/num8

       result.insert(10,divide)


la=LabelFrame(root,width=380,height=380, text='ARITHMETIC CALCULATOR',bd=15,relief=RAISED,bg=" purple",font="Times 14 bold")
la.place(x=10,y=10)

label1=Label(la, text="FIRST NO",font="Times 16 bold",bg=' purple',fg=' purple')
label1.place(x=30,y=60)
label2=Label(la, text="SECOND NO",font="Times 16 bold",bg=' purple',fg=' purple')
label2.place(x=30,y=120)
r_label=Label(la, text="RESULT",font="Times 16 bold",bg=' purple',fg=' purple')
r_label.place(x=50,y=250)

fvalue=StringVar()
svalue=StringVar()
dvalue=StringVar()

e1=Entry(la, textvariable=fvalue,font='Times,20,italic',width=10)
e1.place(x=200,y=60)
e2=Entry(la, textvariable=svalue,font='Times,20,italic',width=10)
e2.place(x=200,y=120)

result=Entry(la, textvariable=dvalue,font='Times,20,italic',width=10)
result.place(x=200,y=250)

add_button= Button(la, text="ADD",bd=10,relief=RAISED, command=Add,fg=" purple",font="Times 11 normal")
add_button.place(y=170,x=20)  
su_button= Button(la, text="SUB",bd=10,relief=RAISED, command=Sub,fg=" purple",font="Times 11 normal")
su_button.place(y=170,x=100)  
multi_button= Button(la, text="MULTI",bd=10,relief=RAISED,command=Mul,fg=" purple",font="Times 11 normal")
multi_button.place(y=170,x=180)  
divi_button= Button(la, text="DIV",bd=10,relief=RAISED, command=Div,fg=" purple",font="Times 11 normal")
divi_button.place(y=170,x=260)  

clear_button= Button(la, text="CLEAR",bd=10,relief=RAISED, command=Clear,fg=" purple",font="Times 11 normal").place(y=300,x=100)  

root.mainloop()