from tkinter import *
win = Tk()
icon=PhotoImage(file='c.png')
win.iconphoto(False,icon)
win.title("Basic calc")
inp=Entry(win,width=40,borderwidth=5)
inp.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
global math
def button_click(number):
	#inp.delete(0,END)
	current=inp.get()
	inp.delete(0,END)
	inp.insert(0,str(current)+str(number))	
    
def button_add():
	first_num = inp.get()
	global math
	math ="addition"
	global f_num
	f_num = float(first_num)
	inp.delete(0,END)
def button_sub():
	first_num = inp.get()
	global math
	math ="subtraction"
	global f_num
	f_num = float(first_num)
	inp.delete(0,END)
def button_mul():
	first_num = inp.get()
	global math
	math ="multiplication"
	global f_num
	f_num = float(first_num)
	inp.delete(0,END)
def button_div():
	first_num = inp.get()
	global math
	math ="division"
	global f_num
	f_num = float(first_num)
	inp.delete(0,END)	
def button_equal():			
	second_num= inp.get()
	inp.delete(0,END)
	if math=="addition" :
		result=f_num + float(second_num)
		inp.insert(0,result)	
	if math=="subtraction" :
		result=f_num - float(second_num)
		inp.insert(0,result)
	if math=="multiplication" :
		result=f_num*float(second_num)
		inp.insert(0,result)
	if math=="division" :
		result= f_num / float(second_num)			
		inp.insert(0,result)	
			
def button_clear():
	inp.delete(0,END)			
def button_py():
	inp.delete(0,END)
	inp.insert(0,"Python powered ")	
	
	
	
# defining buttons	
button_1 = Button(win,bg="#87ceeb",text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(win,bg="#87ceeb",text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(win,bg="#87ceeb",text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(win,bg="#87ceeb",text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(win,bg="#87ceeb",text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(win,bg="#87ceeb",text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(win,bg="#87ceeb",text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(win,bg="#87ceeb",text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(win,bg="#87ceeb",text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0 = Button(win,bg="#87ceeb",text="0",padx=40,pady=20,command=lambda:button_click(0))
button_dot = Button(win,bg="#87ceeb",text=".",padx=41,pady=20,command=lambda:button_click("."))
button_plus = Button(win,bg="white",text=" +",padx=40,pady=20,command=button_add)
button_minus= Button(win,bg="white",text="  -",padx=40,pady=20,command=button_sub)
button_cross = Button(win,bg="white",text="  x",padx=40,pady=20,command=button_mul)
button_divide = Button(win,bg="white",text="  /",padx=40,pady=20,command=button_div)
button_equal = Button(win,bg="#e6e6fa",text="       =          ",padx=60,pady=20,command=button_equal)
button_clear = Button(win,bg="#8EE3D0",text="C",padx=40,pady=20,command=button_clear)
button_py = Button(win,bg="cyan",text="    Python Powered    ",padx=40,pady=20,command=button_py)
#display the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0,columnspan=1)
button_plus.grid(row=1,column=4)
button_minus.grid(row=2,column=4)
button_cross.grid(row=3,column=4)
button_divide.grid(row=4,column=4)
button_equal.grid(row=5,column=0,columnspan=2)
button_dot.grid(row=4,column=1)
button_clear.grid(row=4,column=2)
button_py.grid(row=5,column=2,columnspan=3)
win.mainloop()
