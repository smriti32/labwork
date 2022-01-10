from tkinter import *


root=Tk()
root.title("Registration")
root.configure(bg="powder blue")
root.maxsize(width=300,height=450)
root.minsize(width=300,height=450)



topic=Label(root, text="Registration form",bg="powder blue",fg="blue" ,font="Times 25 bold",relief=RAISED)
topic.place(x=10,y=20)
fname=Label(root, text="First Name", bg="grey",fg="black",font="Times 14 bold").place(x=15 ,y=120)
lname=Label(root, text="Last Name", bg="grey",fg="black",font="Times 14 bold").place(x=15 ,y=170)
address=Label(root, text="Address", bg="grey",fg="black",font="Times 14 bold").place(x=15 ,y=220)
email=Label(root, text="E-mail", bg="grey",fg="black",font="Times 14 bold").place(x=15 ,y=275)
phoneno=Label(root, text="Phone NO", bg="grey",fg="black",font="Times 14 bold").place(x=15 ,y=325)

fnamevalue=StringVar()
lnamevalue=StringVar()
addressvalue=StringVar()
emailvalue=StringVar()
phonevalue=StringVar()

e1=Entry(root,textvariable=fnamevalue,bd=3).place(x=130, y=120)
e2=Entry(root,textvariable=lnamevalue,bd=3).place(x=130 ,y=170)
e3=Entry(root,textvariable=addressvalue,bd=3).place(x=130 ,y=220 )
e4=Entry(root,textvariable=email,bd=3).place(x=130 ,y=275 )
e5=Entry(root, textvariable=phonevalue,bd=3).place(x=130 ,y=325 )

phonevalue=StringVar()

submit=Button(root, text="Submit",bg="grey",fg="black",bd=10,relief=SUNKEN).place(x=115,y=400)

root.mainloop()