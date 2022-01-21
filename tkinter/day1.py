# from tkinter import*
# win=Tk()
# win.mainloop()

# CHANGE TITLE
# from tkinter import*
# win=Tk()
# win.title("login")
# win.mainloop()

# cHANGE ICON 
# from tkinter import *
# win=Tk()
# win.title("Register")
# win.iconbitmap('tkinter/sa.ico')
# win.mainloop()
# from tkinter import*
# win=Tk()
# win.title("system")
# win.iconbitmap('icon.ico')
# win.maxsize(width=300,height=200)
# win.maxsize(width=300,height=200)
# win.mainloop


# from tkinter import*
# win=Tk()
# win.title("system")
# win.iconbitmap('tkinter/sa.ico')
# win.geometry('600x300')
# win.mainloop()

# from tkinter import*
# root=Tk()
# # creating a button widget
# redbutton=Button(root,text="LEFT",fg="green")
# # shoving into the stream
# redbutton.pack(side=LEFT)
# greenbutton=Button(root,text="RIGHT",fg="black")
# greenbutton.pack(side=RIGHT)
# bluebutton=Button(root,text="TOP",fg="blue")
# bluebutton.pack(side=TOP)
# blackbutton=Button(root,text="BOTTOM",fg="red")
# blackbutton.pack(side=BOTTOM)
# root.mainloop()

# from tkinter import*
# root=Tk()
# name=Label(root,text="Name").grid(row=0,column=0)
# e1=Entry(root).grid(row=0,column=1)
# password=Label(root,text="Password").grid(row=1,column=0)
# e1=Entry(root).grid(row=1,column=1)
# submit=Button(root,text="Submit").grid(row=4,column=1)
# root.mainloop()


# from tkinter import*
# top=Tk()
# top.geometry("400x250")
# name=Label(top,text="Name").place(x=30,y=50)
# adress=Label(top,text="Adress").place(x=30,y=130)
# contact=Label(top,text="Contact").palce(x=30,y=130)
# e1=Entry(top).place(x=80,y=50)
# e1=Entry(top).place(x=80,y=90)
# e1=Entry(top).place(x=95,y=130)
# top.mainloop()

# from tkinter import*
# root=Tk()
# # to rename the title of the window
# root.title("GUI")
# mylabel=Label(root,text="Tkinter")
# # pqck is used to show the object in the window
# mylabel.pack()
# root.mainloop()


# from tkinter import*
# root=Tk()
# # to rename the title of the window
# root.title("GUI")
# mylabel=Button(root,text="Tkinter",)
# # pqck is used to show the object in the window
# mylabel.pack()
# root.mainloop()

# from tkinter import*
# window=Tk()
# window.maxsize(width=300,height=300)
# window.minsize(width=300,height=300)
# def func():
#     print("button is cliched")
# btn=Button(window,text="login",command=func) 
# btn.pack(side="top")
# window.mainloop()

# from tkinter import*
# window=Tk()
# def myClick():
#     myLabel=Button(window,text="Look! I  clicked button",fg="red",bg="green",font="50")
#     myLabel.pack()
# my_button=Button(window,text="click me",padx=10,pady=10,command=myClick,fg="red",bg="blue")
# my_button.pack()
# window.mainloop()

# from tkinter import *
# root=Tk()
# name=Label(root,text="User").grid(row=0,column=0)
# e1=Entry(root).grid(row=0, column=1)
# password=Label(root,text="Password").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# email=Label(root,text="Email").grid(row=2,column=0)
# e3=Entry(root).grid(row=2,column=1)
# Age=Label(root,text="Age").grid(row=3,column=0)
# e4=Entry(root).grid(row=3,column=1)
# Contact_no=Label(root,text="Contact no.").grid(row=4,column=0)
# e5=Entry(root).grid(row=4,column=1)
# submit=Button(root, text="Login").grid(row=5, column=1)
# root.mainloop()

# TURTLE
# import turtle
# # Creating a graphics window  on which we can draw
# turtle._Screen()
# turtle.mainloop()

# import turtle 
# # help(turtle.shape)
# t=turtle.Turtle()
# t.shape("turtle")
# turtle.done()

# import turtle 
# t=turtle.Turtle()
# t.shape("turtle")
# t.color("red")
# t.forward(100)
# turtle.done()

# import turtle 
# t=turtle.Turtle()
# t.shape("turtle")
# t.color("red","green")
# turtle.done()

# import turtle 
# sc=turtle.Screen()
# sc.bgcolor("green")
# sc.title("Turtle")
# t=turtle.Turtle()
# t.shape("turtle")
# t.color("green","red")
# t.forward(100)
# turtle.done()

# import turtle
# # creating turtle screen
# t=turtle.Turtle()
# turtle.bgcolor("red")
# turtle.mainloop()

# # changing the screensize
# import turtle
# t=turtle.Turtle()
# turtle.screensize()
# turtle.screensize(1500,1000)
# turtle.mainloop()

# changing the pen size
# import turtle
# t=turtle.Turtle()
# t.pensize(4)
# t.forward(50)
# turtle.mainloop()

# # changing the pen speed 
# import turtle
# # creating turtle
# t=turtle.Turtle()
# t.speed(4)
# t.forward(100)
# t.speed(8)
# t.forward(100)
# turtle.mainloop()


# import turtle
# # creating turtle
# t=turtle.Turtle()
# # to stop the screeen display
# t.forward(100)
# turtle.mainloop()


# import turtle
# t=turtle.Turtle()
# sc=turtle.Screen()
# t=turtle.Turtle()
# t.right(75)
# t.forward(100)
# t.mainloop()


# # # Drawing a shape
# import turtle
# # creating turtle screen
# t=turtle.Turtle()
# # move turtle with coordinates
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# # to stop the screen
# turtle.mainloop()


# drawing shapes using loops
# import turtle
# t=turtle.Turtle()
# for i in range(7):
#     t.forward(50)
#     t.left(51.42)
# turtle.done()  


# import turtle
# t=turtle.Turtle()
# t.begin_fill()
# t.fillcolor("green")
# for i in range(7):
#     t.forward(50)
#     t.left(51.42)
# t.end_fill()    
# turtle.done()

# import turtle
# t=turtle.Turtle()
# t.circle(70)
# turtle.mainloop()

# hide turtle(important)
# import turtle
# t=turtle.Turtle()
# for i in range(7):
#     t.forward(50)
#     t.left(51.42)
# t.hide_turtle()
# turtle.done() 

# dot
# import turtle
# t=turtle.Turtle()
# t.dot(70)
# turtle.mainloop()

# to draw shape from difernt position
# import turtle
# t=turtle.Turtle()
# t.up()
# t.goto(0,-100)
# t.down()
# t.circle(70)
# t.speed(1)
# turtle.mainloop()


# turtle.seth()function in python
# import turtle
# # set direction at 0
# # angle using seth function
# turtle.seth(0)
# # motion
# turtle.forward(80)
# turtle.write("East")
# # back to home 
# turtle.home()
# # set direction at 90
# # angle using sethading
# turtle.setheading(90)
# # motion
# turtle.forward(80)
# turtle.write("north")
# # back to home 
# turtle.home()
# # set direction at 90
# # angle using sethading
# turtle.setheading(180)
# # motion
# turtle.forward(80)
# turtle.write("West")
# # back to home 
# turtle.home()
# # set direction at 90
# # angle using sethading
# turtle.setheading(270)
# # motion
# turtle.forward(80)
# turtle.write("south")
# # hide the turtle
# turtle.ht()
# turtle.done()


# import turtle
# t=turtle.Turtle()
# turtle.bgcolor("black")
# turtle.pensize(2)
# turtle.speed(6)
# while(True):
#     for i in range(6):
#         for colors in["red","green","blue","yellow","white","black"]:
#           turtle.color(colors)
#           turtle.circle(100)
#           turtle.left(10)



from tkinter import *
from tkinter import messagebox
root =Tk()

def popup():
    response=messagebox.askyesno("This is my Popup","hello world")
    Label(root,text=response).pack()

    if response == 1:
        Label(root,text="Clicked Yes").pack()
    else:
        Label(root,text="Clicked No").pack()

btn =Button(root,text="Popup",command=popup).pack()
root.mainloop()            