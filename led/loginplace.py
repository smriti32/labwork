from tkinter import *
root=Tk()
root.title("Registration")
root.configure(bg="powder blue")
root.maxsize(width=380,height=450)
root.minsize(width=380,height=450)

#heading
topic=Label(root, text="Login Form", bg="orange",fg="white" ,font="Times 25 bold",relief=RAISED)
topic.place(x=15,y=15)
#labels
user_name=Label(root, text="Username", fg="black",bg="orange",font="Times 14 bold",relief=FLAT)
user_name.place(x=15,y=140)
password=Label(root, text="Password", fg="black",bg="orange",font="Times 14 bold",relief=FLAT)
password.place(x=15 ,y=190)
remember=Label(root, text="Not a member?", fg="black",bg="orange",font="Times 14 bold",relief=FLAT)
remember.place(x=15 ,y=290)
#buttons
for_password=Button(root, text="Forget password?", bg="orange",fg="black",font="Times 14 bold",relief=FLAT)
for_password. place(x= 15,y=240)
signup=Button(root, text="Sign Up", bg="orange",fg="black",font="Times 12 italic",relief=RAISED)
signup.place(x=170 ,y=290)

#Entry
user_value=StringVar()
password_value=StringVar()
e1=Entry(root,textvariable=user_value,bd=3,relief=RAISED,font="Times 14 bold").place(x=140 ,y=140)
e2=Entry(root,textvariable=password_value,bd=3,relief=RAISED,font="Times 14 bold").place(x=140 ,y=190)


#login button
login=Button(root, text="Login",bg="orange",fg="white",font="Times 14 bold").place(x=25 ,y=350)

root.mainloop()