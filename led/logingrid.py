from tkinter import *

root=Tk()
root.title("Registration")
root.configure(bg="powder blue")
root.maxsize(width=380,height=450)
root.minsize(width=380,height=450)


#heading
topic=Label(root, text="Login Form", bg="orange",fg="white" ,font="Times 25 bold",relief=RAISED)
topic.grid(row=1,columnspan=2,pady=15)
#labels
user_name=Label(root, text="Username", fg="black",bg="orange",font="Times 14 bold",relief=FLAT)
user_name.grid(row= 2, column=1,pady=15,padx=15)
password=Label(root, text="Password", fg="black",bg="orange",font="Times 14 bold",relief=FLAT)
password.grid( row=4,  column=1,pady=15,padx=15)
remember=Label(root, text="Not a member?", fg="black",bg="orange",font="Times 14 bold",relief=FLAT)
remember.grid( row= 8,  column=1,pady=15,padx=15)
#buttons
for_password=Button(root, text="Forget password?", bg="orange",fg="black",font="Times 14 bold",relief=FLAT)
for_password.grid( row= 6,  column=1,pady=15,padx=15)
signup=Button(root, text="Sign Up", bg="orange",fg="black",font="Times 12 italic",relief=RAISED)
signup.grid( row= 8, column=2,padx=15)

#Entry
user_value=StringVar()
password_value=StringVar()
e1=Entry(root,textvariable=user_value,bd=3,relief=RAISED,font="Times 14 bold").grid(row=3,  column=1,padx=40)
e2=Entry(root,textvariable=password_value,bd=3,relief=RAISED,font="Times 14 bold").grid(row=5,  column=1,padx=40)


#login button
login=Button(root, text="Login",bg="powder blue",fg="white",font="Times 14 bold").grid(row=7,column=1,pady=20)

root.mainloop()