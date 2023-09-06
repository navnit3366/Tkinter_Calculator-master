from tkinter import Tk, StringVar, Entry, SUNKEN, Button, RAISED
from colors import (background, display, display_font, button_active,
                    button_top_active, button_equal, text, clear,
                    clear_active, button, button_top, symbol,
                    symbol_font, symbol_active, equal)
from functions import string_fill, get_value, operator_list, dot_list, numbers_list
from ast import literal_eval
# creating main object
root = Tk()
# For validation
screen_value = StringVar()
screen_value.set(string_fill)
got_result = False
got_point = False
got_operator = False

# Function to do calculation
def calculate():
    global got_result
    string = get_value(screen.get()).replace('÷', '/')  # Changed the ÷ symbol before devide
    try:
        result = literal_eval(string)
        got_result = True
    except ZeroDivisionError:
        result = string
    except Exception as e:
        print(e)
        result = string
    screen_value.set(result)


# Function to enter number by button
def number_btn(num):
    global got_operator, got_point, got_result
    string = get_value(screen.get())
    if got_result:  # When we calculate result it clear the value and set new input value
        string = num
        got_result = False
    else:
        string = string + num
    screen_value.set(string)
    got_operator = True


# Function to enter number by button
def point_btn():
    global got_operator, got_point, got_result
    got_result = False
    string = get_value(screen.get())
    if got_point:
        btn_value = '.'
        string = string + btn_value
        got_operator = False
        got_point = False
    screen_value.set(string)


# Function to enter symbol by button
def operator_btn(operator):
    global got_operator, got_point, got_result
    got_result = False
    string = get_value(screen.get())
    if got_operator:
        string = string + operator
        got_point = True
        got_operator = False
    else:
        if string == '0' or string == '':
            string = '0'
        else:
            string = string[:-1] + operator
            got_point = True
            got_operator = False
    screen_value.set(string)


# Function to clear window by button
def clear_btn():
    global got_point
    screen_value.set("0")
    got_point = True


def m_plus():
    string = get_value(screen.get())
    try:
        if string[0] == "-":
            string = string[1:]
        else:
            string = "-" + string
    except IndexError:
        pass
    screen_value.set(string)


# Function to get keypress
def key(event):
    global got_operator, got_point, got_result
    # Get the keypress
    my_input = event.keycode
    string = get_value(screen.get())  # get the existing value of screen
    kp = repr(event.char)
    if my_input == 9:
        # Exit when escape key is pressed
        # root.destroy() # It creates an error
        exit()
    elif my_input == 49:  # Toggle positive and negative
        try:
            if string[0] == "-":  # Value is negative
                string = string[1:]
            else:  # Value is positive
                string = "-" + string
        except IndexError:
            pass  # To do nothing
    elif my_input == 119 or my_input == 22:
        # Delete last later when del key or backspace key is pressed
        new = string[:-1]
        if len(string) == 1 or len(string) == 0:
            string = "0"
            got_operator = False
        else:
            string = new
            if string[-1] in operator_list:  # Multi oprator Bug Was here
                got_operator = False
            else:
                got_operator = True
            if string[-1] in dot_list:
                got_point = False
            else:
                got_point = True

    elif my_input == 36:
        # Calculate the result when enter key is pressed
        try:
            result = literal_eval(string)
            got_result = True
        except ZeroDivisionError:
            result = string
        except Exception as e:
            print(e)
            result = string
        string = str(result)
    if kp[1] in numbers_list:  # Check pressed key is in number list
        num = kp[1]
        got_operator = True
        string = string + num
    elif kp[1] in operator_list:  # Check pressed key is in oprator list
        value_btn = kp[1]
        if got_operator:  # Validation to get oprator
            got_operator = False
            got_point = True
            string = string + value_btn
        else:  # If oprator already typed it replace previous one
            if string == '0' or string == '':
                string = '0'
            else:
                if string[-1] in operator_list and string[-2] in operator_list:
                    string = string[:-3] + string[-1]
                got_point = True
                got_operator = False
    elif kp[1] in dot_list:  # Check pressed key is in oprator list
        if got_point:  # Validation to get number
            num = kp[1]
            got_operator = False
            got_point = False
            string = string + num
    if len(string) == 1 and string == "0":  # Whene the value is 0 you can,t input oprator
        got_operator = False
    screen_value.set(string)
    # To handle the bug
    string = get_value(screen.get())
    if string == "":
        screen_value.set("0")


# Window behaviour
root.resizable(height=0, width=0)
root.title("Rudransh's Calculator")
root.configure(background=background)

# input output screen
screen = Entry(root,
               font=("cursive", 33, "bold"),
               background=display,
               state='disabled',
               cursor='arrow',
               disabledbackground=display,
               disabledforeground=text,
               fg=display_font,
               relief=SUNKEN,
               border=0,
               highlightcolor=background,
               textvariable=screen_value,
               justify="right"
               )

button1 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="MC",
                 background=button_top,
                 fg=text,
                 activebackground=button_top_active,
                 activeforeground=text,
                 padx=38,
                 pady=10
                 )

button2 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="M+",
                 background=button_top,
                 fg=text,
                 activebackground=button_top_active,
                 activeforeground=text,
                 padx=38,
                 pady=10,
                 command=m_plus
                 )

button3 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="÷",
                 background=symbol,
                 fg=symbol_font,
                 activebackground=symbol_active,
                 activeforeground=symbol_font,
                 padx=50,
                 pady=10,
                 command=lambda: operator_btn("÷")
                 )

button4 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="×",
                 background=symbol,
                 fg=symbol_font,
                 activebackground=symbol_active,
                 activeforeground=symbol_font,
                 padx=50,
                 pady=10,
                 command=lambda: operator_btn("*")
                 )

button5 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="7",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("7")
                 )

button6 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="8",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("8")
                 )

button7 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="9",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("9")
                 )

button8 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="-",
                 background=symbol,
                 fg=symbol_font,
                 activebackground=symbol_active,
                 activeforeground=symbol_font,
                 padx=50,
                 pady=10,
                 command=lambda: operator_btn("-")
                 )

button9 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="4",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("4")
                 )

button10 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="5",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("5")
                  )

button11 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="6",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("6")
                  )

button12 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="+",
                  background=symbol,
                  fg=symbol_font,
                  activebackground=symbol_active,
                  activeforeground=symbol_font,
                  padx=50,
                  pady=10,
                  command=lambda: operator_btn("+")
                  )

button13 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="1",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("1")
                  )

button14 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="2",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("2")
                  )

button15 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="3",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("3")
                  )

button16 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="=",
                  background=equal,
                  fg=text,
                  activebackground=button_equal,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=calculate
                  )

button17 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="0",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=119,
                  pady=10,
                  command=lambda: number_btn("0")
                  )

button18 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text=".",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=52,
                  pady=10,
                  command=point_btn
                  )

button19 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="CLEAR",
                  background=clear,
                  fg=background,
                  activebackground=clear_active,
                  activeforeground=background,
                  padx=16,
                  pady=10,
                  command=clear_btn
                  )

# Styling
screen.config(highlightbackground=background, highlightthickness=5)
button1.config(highlightbackground=background, highlightthickness=5)
button2.config(highlightbackground=background, highlightthickness=5)
button3.config(highlightbackground=background, highlightthickness=5)
button4.config(highlightbackground=background, highlightthickness=5)
button5.config(highlightbackground=background, highlightthickness=5)
button6.config(highlightbackground=background, highlightthickness=5)
button7.config(highlightbackground=background, highlightthickness=5)
button8.config(highlightbackground=background, highlightthickness=5)
button9.config(highlightbackground=background, highlightthickness=5)
button10.config(highlightbackground=background, highlightthickness=5)
button11.config(highlightbackground=background, highlightthickness=5)
button12.config(highlightbackground=background, highlightthickness=5)
button13.config(highlightbackground=background, highlightthickness=5)
button14.config(highlightbackground=background, highlightthickness=5)
button15.config(highlightbackground=background, highlightthickness=5)
button16.config(highlightbackground=background, highlightthickness=5)
button17.config(highlightbackground=background, highlightthickness=5)
button18.config(highlightbackground=background, highlightthickness=5)
button19.config(highlightbackground=background, highlightthickness=5)

# First Row
screen.grid(columnspan=4)

# Second row
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=3, row=1)

# Third Row
button5.grid(column=0, row=2)
button6.grid(column=1, row=2)
button7.grid(column=2, row=2)
button8.grid(column=3, row=2)

# Fourth Row
button9.grid(column=0, row=3)
button10.grid(column=1, row=3)
button11.grid(column=2, row=3)
button12.grid(column=3, row=3)

# Fifth Row
button13.grid(column=0, row=4)
button14.grid(column=1, row=4)
button15.grid(column=2, row=4)
button16.grid(column=3, row=4)

# Sixth Row
button17.grid(columnspan=2, column=0, row=5)
button18.grid(column=2, row=5)
button19.grid(column=3, row=5)

# Bind Keypress
root.bind("<Key>", key)
# Starting main gui window
root.mainloop()
