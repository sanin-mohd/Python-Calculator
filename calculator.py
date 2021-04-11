from tkinter import *                               #for frame works
win=Tk()                                            #initiating window
win.title("Calculator..")                           #heading
win.resizable(0,0)                                  #to fix size of window
win.geometry("240x312")                             #geometry

input_text=StringVar()                              #to get value from input_field

                                                    #creating a frame for input_field
input_frame=Frame(win,width=312,height=50,bd=0, highlightbackground="pink", highlightcolor="pink",highlightthickness=10)
input_frame.pack(side=TOP)                                  #connceting to window

                                                    #creating a entry_feld
input_field=Entry(input_frame,width=312,font=('arial', 18, 'bold'), textvariable=input_text,bg="#eee",justify=RIGHT)
input_field.pack()                                  #connecting to window




expression=""                                       #variable to store entering values
input_text.set("")                                  #variable in entry_field

def btn_click(item):                                #function to display entered btns
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def btn_clear():                                    #function to clear input_field
    global expression
    expression=""
    input_text.set(expression)

def btn_equal():                                    #function to evaluate expression
    global expression
    result=str(eval(expression))
    input_text.set(result)

                                                    # creating frame for btns
btns_frame = Frame(win, width=312, height=272.5, bg="pink",bd=5)
btns_frame.pack()                                   # connecting to window

                                                    #creating buttons in grid system

#first row
clear_btn=Button(btns_frame,text="C",width=20,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_clear()).grid(row=0,column=0,columnspan=3)

divide_btn=Button(btns_frame,text="/",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("/")).grid(row=0,column=3,padx=1,pady=1)

#second row

_7_btn=Button(btns_frame,text="7",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("7")).grid(row=1,column=0,padx=1,pady=1)
_8_btn=Button(btns_frame,text="8",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("8")).grid(row=1,column=1,padx=1,pady=1)
_9_btn=Button(btns_frame,text="9",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("9")).grid(row=1,column=2,padx=1,pady=1)
_mult_btn=Button(btns_frame,text="*",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("*")).grid(row=1,column=3,padx=1,pady=1)

#third row

_4_btn=Button(btns_frame,text="4",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("4")).grid(row=2,column=0,padx=1,pady=1)
_5_btn=Button(btns_frame,text="5",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("5")).grid(row=2,column=1,padx=1,pady=1)
_6_btn=Button(btns_frame,text="6",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("6")).grid(row=2,column=2,padx=1,pady=1)
_add_btn=Button(btns_frame,text="+",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("+")).grid(row=2,column=3,padx=1,pady=1)

#forth row

_1_btn=Button(btns_frame,text="1",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("1")).grid(row=3,column=0,padx=1,pady=1)
_2_btn=Button(btns_frame,text="2",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("2")).grid(row=3,column=1,padx=1,pady=1)
_3_btn=Button(btns_frame,text="3",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("3")).grid(row=3,column=2,padx=1,pady=1)
_sub_btn=Button(btns_frame,text="-",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("-")).grid(row=3,column=3,padx=1,pady=1)

#fifth row
_zero_btn=Button(btns_frame,text="0",width=12,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click("0")).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
_equal_btn=Button(btns_frame,text="=",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_equal()).grid(row=4,column=2,padx=1,pady=1)
_dot_btn=Button(btns_frame,text=".",width=5,height=2,fg="black",font=('arial', 10, 'bold'),bd=4,cursor="hand2",command=lambda :btn_click(".")).grid(row=4,column=3,padx=1,pady=1)



win.mainloop()                                      #running window



