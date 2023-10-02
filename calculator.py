from tkinter import *

def button_click(num):
    global val
    val=val+str(num)
    data.set(val)
    
def button_clear():
    global val
    val=""
    data.set("")
    
def button_Equals():
    global val
    result=str(eval(val))
    data.set(result)
    


#for creating GUI


root=Tk()
root.title("calculator")
root.geometry("361x430+500+200")
root.configure(bg="#7f8274")
root.resizable(0,0)
val=""
data=StringVar()
display=Entry(root,text=data,bd=29,justify="right",bg="powder blue",font=("arial",20))
display.grid(row=0,columnspan=4)

##BUTTONS
##ROW1 BUTTONS
b_c=Button(root,text="C",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=button_clear)
b_c.grid(row=1,column=0)

b_s=Button(root,text="%",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click("%"))
b_s.grid(row=1,column=1)

b_d=Button(root,text="/",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click("/"))
b_d.grid(row=1,column=2)

b_m=Button(root,text="*",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click('*'))
b_m.grid(row=1,column=3)


##ROW2 BUTTONS

b_7=Button(root,text="7",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(7))
b_7.grid(row=2,column=0)

b_8=Button(root,text="8",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(8))
b_8.grid(row=2,column=1)

b_9=Button(root,text="9",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(9))
b_9.grid(row=2,column=2)


b_s=Button(root,text="-",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click('-'))
b_s.grid(row=2,column=3)


##ROW3 BUTTONS

b_4=Button(root,text="4",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(4))
b_4.grid(row=3,column=0)

b_5=Button(root,text="5",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(5))
b_5.grid(row=3,column=1)

b_6=Button(root,text="6",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(6))
b_6.grid(row=3,column=2)


b_a=Button(root,text="+",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click('+'))
b_a.grid(row=3,column=3)


##ROW4 BUTTONS

b_1=Button(root,text="1",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(1))
b_1.grid(row=4,column=0)

b_2=Button(root,text="2",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(2))
b_2.grid(row=4,column=1)

b_3=Button(root,text="3",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(3))
b_3.grid(row=4,column=2)

b_do=Button(root,text=".",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click("."))
b_do.grid(row=4,column=3)



##ROW5 BUTTONS

b_bracket1=Button(root,text="(",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click("("))
b_bracket1.grid(row=5,column=0)

b_bracket2=Button(root,text=")",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(")"))
b_bracket2.grid(row=5,column=1)

b_z=Button(root,text="0",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=lambda: button_click(0))
b_z.grid(row=5,column=2)

b_e=Button(root,text="=",font=("calibri",12,"bold"),bd=8,height=2,width=6,command=button_Equals)
b_e.grid(row=5,column=3)
root.mainloop()