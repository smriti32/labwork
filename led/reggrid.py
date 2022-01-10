from tkinter import *

root=Tk()
root.title("Registration")
root.configure(bg="powder blue")
root.maxsize(width=400,height=450)
root.minsize(width=400,height=450)


#topic
topic=Label(root, text="Registration form", bg="grey",fg="white" ,font="Times 25 bold",relief=RAISED)
topic.grid(row=1,column=0,columnspan=5,padx=5,pady=5)
#labels for name, address ,email and phone
fname=Label(root, text="First Name", fg="black",bg="light grey",font="Times 14 bold",relief=FLAT)
fname.grid(row= 2, column=0,pady=15,padx=5)
lname=Label(root, text="Last Name", fg="black",bg="light grey",font="Times 14 bold",relief=FLAT)
lname.grid( row= 3,  column=0,pady=15,padx=5)
address=Label(root, text="Address", fg="black",bg="light grey",font="Times 14 bold",relief=FLAT)
address.grid( row= 4,  column=0,padx=5,pady=15)
email=Label(root, text="E-mail", fg="black",bg="light grey",font="Times 14 bold",relief=FLAT)
email.grid(    row= 5,  column=0,pady=15,padx=5)
phoneno=Label(root, text="Phone NO", fg="black",bg="light grey",font="Times 14 bold",relief=FLAT)
phoneno.grid(row= 6, column=0,pady=15,padx=5)

#entries
fnamevalue=StringVar()
lnamevalue=StringVar()
addressvalue=StringVar()
emailvalue=StringVar()
phonevalue=StringVar()

e1=Entry(root,textvariable=fnamevalue,bd=3,relief=RAISED,font="Times 14 bold",bg="light grey").grid(row=2,  column=4)
e2=Entry(root,textvariable=lnamevalue,bd=3,relief=RAISED,font="Times 14 bold",bg="light grey").grid(row=3,  column=4)
e3=Entry(root,textvariable=addressvalue,bd=3,relief=RAISED,font="Times 14 bold",bg="light grey").grid(row=4,column=4)
e4=Entry(root,textvariable=email,bd=3,relief=RAISED,font="Times 14 bold",bg="light grey").grid(row=5,       column=4)
e5=Entry(root, textvariable=phonevalue,bd=3,relief=RAISED,font="Times 14 bold",bg="light grey").grid(row=6, column=4)


submit=Button(root, text="Submit",bg="grey",fg="white",font="Times 14 bold").grid(row=18,column=3,pady=20)

root.mainloop()