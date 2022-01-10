from tkinter import *
root=Tk()
root.title("Registration")
root.configure(bg="powder blue")
root.maxsize(width=300,height=400)
root.minsize(width=300,height=400)
topic=Label(root, text="Registration form",bg="powder blue",fg="white" ,font="Times 25 bold",relief=RAISED)
topic.pack()

fnamevalue=StringVar()
lnamevalue=StringVar()
addressvalue=StringVar()
emailvalue=StringVar()
phonevalue=StringVar()

fname=Label(root, text="First Name", bg="powder blue",fg="black",font="Times 14 bold").pack()
e1=Entry(root,textvariable=fnamevalue,bd=3).pack()
lname=Label(root, text="Last Name", bg="powder blue",fg="black",font="Times 14 bold").pack()
e2=Entry(root,textvariable=lnamevalue,bd=3).pack()
address=Label(root, text="Address", bg="powder blue",fg="black",font="Times 14 bold").pack()
e3=Entry(root,textvariable=addressvalue,bd=3).pack()
email=Label(root, text="E-mail", bg="powder blue",fg="black",font="Times 14 bold").pack()
e4=Entry(root,textvariable=email,bd=3).pack()
phoneno=Label(root, text="Phone NO", bg="powder blue",fg="black",font="Times 14 bold").pack()
e5=Entry(root, textvariable=phonevalue,bd=3).pack()




phonevalue=StringVar()

submit=Button(root, text="Submit",bg="light grey",fg="black",font="Times 14 bold").pack(side=BOTTOM)

root.mainloop()