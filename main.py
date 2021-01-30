#  TEMPERATURE CALCULATOR
#  By Albert Murphy
#  Feel Free To Use
#  https://github.com/ex1tt


import tkinter as tk
from time import strftime

OPTIONS = ['Celsius', 'Fahrenheit']

root = tk.Tk()
root.resizable(0, 0)


C = tk.Canvas(root, bg='white', height=400, width=600)  # creating the canvas everything will be on
C.pack()


def time():
    string = strftime('%H:%M:%S %p')  # making a simple clock function
    clock_label.config(text=string)   # which was imported earlier
    clock_label.after(1000, time)


clock_label = tk.Label(root, font=('calibri', 20, 'bold'),  # making the clock look nice
                       bg='white',
                       fg='black')


clock_label.place(x=300, y=30, anchor="center")  # placing the clock
time()


Temp_1 = tk.StringVar(root)  # For Either Celsius Or Fahrenheit
Temp_1.set(OPTIONS[0])

Temp_2 = tk.StringVar(root)  # For Either Celsius Or Fahrenheit
Temp_2.set(OPTIONS[0])

Title = tk.Label(root, text="Temperature Calculator", font=('calibri', 20, ), borderwidth=2, width=20, anchor='center')
Title.place(x=150, y=75)


#  Creating celsius and fahrenheit section


Temperature_Entry = tk.Entry(root, width=3, font=('calibri', 20, 'bold'), bg='#FBEFEF')
Temperature_Entry.place(x=50, y=151)

Temperature_Box_1 = tk.OptionMenu(root, Temp_1, *OPTIONS)
Temperature_Box_1.configure(font=('calibri', 15, 'bold'), width=8)
Temperature_Box_1.place(x=115, y=150)

Temperature_Text = tk.Label(root, text="To", font=('calibri', 20, ), borderwidth=2, width=3)
Temperature_Text.place(x=260, y=150)

Temperature_Box_2 = tk.OptionMenu(root, Temp_2, *OPTIONS)
Temperature_Box_2.configure(font=('calibri', 15, 'bold'), width=8)
Temperature_Box_2.place(x=330, y=150)


#  Calculating Celsius To Fahrenheit
#  creating the function for the button


def calc_temperature():
    T_Entry_Input = Temperature_Entry.get()
    T_Box_Input_1 = Temp_1.get()
    T_Box_Input_2 = Temp_2.get()

    if str(T_Box_Input_1) == "Celsius" and str(T_Box_Input_2) == "Fahrenheit":
        Temp_Label = int(T_Entry_Input) * 9 / 5 + 32
        Temp_Label = str(Temp_Label) + " °F"
    elif str(T_Box_Input_1) == "Celsius" and str(T_Box_Input_2) == "Celsius":
        Temp_Label = int(T_Entry_Input)
        Temp_Label = str(Temp_Label) + " °C"
    elif str(T_Box_Input_1) == "Fahrenheit" and str(T_Box_Input_2) == "Celsius":
        Temp_Label = int(T_Entry_Input) - 32
        Temp_Label = Temp_Label * 5 / 9   # For some reason it would keep giving 14.1111111
        Temp_Label = round(Temp_Label, 2)
        Temp_Label = str(Temp_Label) + " °C"
    elif str(T_Box_Input_1) == "Fahrenheit" and str(T_Box_Input_2) == "Fahrenheit":
        Temp_Label = int(T_Entry_Input)
        Temp_Label = str(Temp_Label) + " °F"

    #  Creating Label

    Temperature_Label = tk.Label(root, width=10, font=('calibri', 17, 'bold'), text=Temp_Label, anchor='center')

    Temperature_Label.place(x=225, y=275)


#  Creating The Button

Temperature_Button = tk.Button(root, width=8, font=('calibri', 13, 'bold'), text="Calculate", command=calc_temperature)
Temperature_Button.place(x=475, y=150)

root.mainloop()
