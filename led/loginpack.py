from tkinter import *

root=Tk()
root.title("Registration")
root.configure(bg="powder blue")
root.maxsize(width=390,height=550)
root.minsize(width=390,height=550)


#heading
topic=Label(root, text="Login Form", bg="light blue",fg="white" ,font="Times 25 bold",relief=RAISED)
topic.pack(pady=15)
#labels
user_name=Label(root, text="Username", fg="black",bg="light blue",font="Times 14 bold",relief=FLAT)
user_name.pack(pady=15)
user_value=StringVar()
e1=Entry(root,textvariable=user_value,bd=3,relief=RAISED,font="Times 14 bold",bg="light blue").pack(pady=10)


password=Label(root, text="Password", fg="black",bg="light blue",font="Times 14 bold",relief=FLAT)
password.pack(pady=15)
password_value=StringVar()
e2=Entry(root,textvariable=password_value,bd=3,relief=RAISED,font="Times 14 bold",bg="light blue").pack(pady=10)

for_password=Button(root, text="Forget password?", bg="light blue",fg="black",font="Times 14 bold",relief=FLAT)
for_password. pack(pady=15)

remember=Label(root, text="Not a member?", fg="black",bg="light blue",font="Times 14 bold",relief=FLAT)
remember.pack(pady=15)

signup=Button(root, text="Sign Up", bg="light blue",fg="black",font="Times 12 italic",relief=RAISED)
signup.pack(pady=15)


#login button
login=Button(root, text="Login",bg="light blue",fg="white",font="Times 14 bold").pack(side=BOTTOM)

root.mainloop()