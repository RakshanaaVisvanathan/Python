from tkinter import Tk,Entry,Button,StringVar
import math


#FUNCTIONS


def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op




#VARIABLES


log, ln = math.log10, math.log
e = math.exp
E = '10*'




#TKINTER WINDOW
tk = Tk()
tk.configure(bg="BLACK", bd=10)
tk.resizable(False,False)
tk.title("Scientific Calculator")

calc_operator = ""




#TEXT AREA FOR USER INPUT
text_input = StringVar()
text_display = Entry(tk, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='HONEYDEW1', justify='right').grid(columnspan=5, padx = 10, pady = 15)
button_params = {'bd':5, 'fg':'BLACK', 'bg':'#7FFFD4', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'AQUAMARINE4', 'font':('sans-serif', 20, 'bold')}





#BUTTONS


#1st row
second_power = Button(tk, button_params, text='x\u00B2',
             command=lambda:button_click('**2')).grid(row=1, column=0, sticky="nsew")
third_power = Button(tk, button_params, text='x\u00B3',
             command=lambda:button_click('**3')).grid(row=1, column=1, sticky="nsew")
nth_power = Button(tk, button_params, text='x^n',
             command=lambda:button_click('**')).grid(row=1, column=2, sticky="nsew")
square_root = Button(tk, button_params, text='\u00B2\u221A',
                     command=square_root).grid(row=1, column=3, sticky="nsew")
third_root = Button(tk, button_params, text='\u00B3\u221A',
                    command=third_root).grid(row=1, column=4, sticky="nsew")


#2nd row
left_par = Button(tk, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=2, column=0, sticky="nsew")
right_par = Button(tk, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=2, column=1, sticky="nsew")   
log_base10 = Button(tk, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                   command=lambda:button_click('log(')).grid(row=2, column=2, sticky="nsew")
percentage = Button(tk, button_params, text='%',
               command=percent).grid(row=2, column=3, sticky="nsew")
ex = Button(tk, button_params, text='e^x',
               command=lambda:button_click('e(')).grid(row=2, column=4, sticky="nsew")

#3rd row
button_7 = Button(tk, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=3, column=0, sticky="nsew")
button_8 = Button(tk, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=3, column=1, sticky="nsew")
button_9 = Button(tk, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=3, column=2, sticky="nsew")
delete_one = Button(tk, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='LIGHTSALMON1').grid(row=3, column=3, sticky="nsew")
delete_all = Button(tk, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='LIGHTSALMON1').grid(row=3, column=4, sticky="nsew")

#4th row
button_4 = Button(tk, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=4, column=0, sticky="nsew")
button_5 = Button(tk, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=4, column=1, sticky="nsew")
button_6 = Button(tk, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=4, column=2, sticky="nsew")
mul = Button(tk, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=4, column=3, sticky="nsew")
div = Button(tk, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=4, column=4, sticky="nsew")

#5th row
button_1 = Button(tk, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=5, column=0, sticky="nsew")
button_2 = Button(tk, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=5, column=1, sticky="nsew")
button_3 = Button(tk, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=5, column=2, sticky="nsew")
add = Button(tk, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=5, column=3, sticky="nsew")
sub = Button(tk, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=5, column=4, sticky="nsew")

#6th row
button_0 = Button(tk, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=9,  columnspan=2, column=0, sticky="nsew")
point = Button(tk, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=2, sticky="nsew")
equal = Button(tk, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")




tk.mainloop()
