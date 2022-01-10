from tkinter import *
root=Tk()

def button_click(number):
    global operator
    operator=operator+str(number)
    entry_value.set(operator)
    
def button_Clear():
    global operator
    operator=""
    entry_value.set("")


def button_Equal():
    global operator
    result=str(eval(operator))
    entry_value.set(result)

#definng title of project
root.title("simple calculator")
root.geometry('410x350')
root.configure(bg="forestgreen")
root.resizable(0,0)


topic=Label(root, text=' CALCULATOR',font='Times 20 bold',bg="forestgreen").grid(row=0,columnspan=5)

operator=""
entry_value=StringVar()
e=Entry(root, textvariable=entry_value,bd=15,width=65,justify="right")
e.grid(row=1,columnspan=4)

#Defining button
button_1=Button(root, text="1",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(1))
button_2=Button(root, text="2",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(2))
button_3=Button(root, text="3",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(3))
button_4=Button(root, text="4",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(4))
button_5=Button(root, text="5",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(5))
button_6=Button(root, text="6",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(6))
button_7=Button(root, text="7",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(7))
button_8=Button(root, text="8",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(8))
button_9=Button(root, text="9",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(9))
button_0=Button(root, text="0",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click(0))


button_sub=Button(root, text="-",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click('-'))
button_add=Button(root, text="+",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click('+'))
button_div=Button(root, text="/",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda : button_click('/'))
buttonequal=Button(root, text="=",bd=12,bg='lime',fg='black',width=9,height=2, command=button_Equal)
buttonclear=Button(root, text="clear",bd=12, bg='lime',fg='black',width=9,height=2, command=button_Clear)
button_mul=Button(root, text="",bd=12, bg='lime',fg='black',width=9,height=2, command=lambda: button_click(''))
#putting button on the screen

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_div.grid(row=4, column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_sub.grid(row=3, column=3)


button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_add.grid(row=2, column=3)


button_0.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
buttonclear.grid(row=5, column=2)
buttonequal.grid(row=5, column=3)

root.mainloop()