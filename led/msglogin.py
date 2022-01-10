from tkinter import *
import tkinter .messagebox as tmsg

def message():
    username=str(user.get())
    tmsg.showinfo("username",username)


#window
mainWindow = Tk()  
mainWindow.maxsize(width=360,height=360) 
mainWindow.minsize(width=360,height=360) 
mainWindow.title('Tkinter Login Form ')
mainWindow.configure(bg="light blue")

l=LabelFrame(mainWindow,text="LOGIN FORM",bd=5,bg="light green",fg="black",relief=RAISED,width=340,height=340,font="Times 20 bold")
l.place(x=10,y=10)
#user label and user entry box
userLabel = Label(l,text="User",font='Times 11 italic',bg='light green').place(x=15,y=70)  
user = StringVar()
userEntry = Entry(l, textvariable=user).place(x=150,y=70)

remember=Label(l, text="Not a member?", fg="black",bg="light green",font="Times 11 bold",relief=FLAT)
remember.place(x=15 ,y=250)

#password label and password entry box
passwordLabel = Label(l,text="Password",font='Times 11 italic',bg='light green').place(x=15,y=100)  
password = StringVar()
passwordEntry = Entry(l, textvariable=password, show='*').place(x=150,y=100)  


for_password=Button(l, text="Forget password?", bg="light green",fg="black",font="Times 11 normal",relief=FLAT)
for_password. place(x= 15,y=150)
signup=Button(l, text="Sign Up", bg="light green",fg="black",font="Times 11 italic",relief=RAISED)
signup.place(x=160 ,y=250)



#login button
loginButton = Button(l, text="Login",bd=5,relief=RAISED, command=message).place(x=150,y=200)  

mainWindow.mainloop()