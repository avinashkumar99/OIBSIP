# BMI app 
import customtkinter
from tkinter import *
from tkinter import messagebox

# To calculate BMI
def bmiCalculator():
    try: 
        height = float(ht_entry.get())
        weight = float(wt_entry.get())
        if var2.get() == 'ft':
            height *= 30.48
        if var1.get() == 'lbs':
            weight *= 0.453592
        result = weight / ((height/100)**2)
        info = checkBMI(result)
        category_label.configure(text = f'BMI is : {format(result,'.2f')} \nCategory is : {info}')
    except ValueError:
        messagebox.showerror('Error', 'Enter a valid number!')
    except ZeroDivisionError :
        messagebox.showerror('Error','Height cannot be zero!')

# Checking the BMI
def checkBMI(result):
    if result < 18.5:
        text = 'Under Weight'
        return text
    
    elif result >= 18.5 and result< 25 :
        text = 'Healthy'
        return text 
    
    else :
        text = 'Obesity'
        return text

bmi_app = customtkinter.CTk()
bmi_app.title('BMI_APP')
bmi_app.geometry('450x500')
bmi_app.config(bg = '#023047')

font1 = ('Monaco', 40, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 25, 'bold')

title = customtkinter.CTkLabel(bmi_app, font=font1, text='BMI Calculator', text_color='#fdf0d5',bg_color='#023047')
title.place(x=60,y=20)

wt = customtkinter.CTkLabel(bmi_app, font=font2, text='Weight', text_color='#f7ede2',bg_color='#023047')
wt.place(x=40,y=90)

ht = customtkinter.CTkLabel(bmi_app, font=font2, text='Height', text_color='#f7ede2',bg_color='#023047')
ht.place(x=40,y=185)

ht_entry = customtkinter.CTkEntry(bmi_app, font=font2, text_color='#000',fg_color='#fff',border_color='#000')
ht_entry.place(x=40,y=220)

wt_entry = customtkinter.CTkEntry(bmi_app, font=font2, text_color='#000',fg_color='#fff',border_color='#000')
wt_entry.place(x=40,y=125)

wt_opts = ['kg','lbs']
ht_opts = ['cm','ft']

var1 = StringVar()
var2 = StringVar()

wt_opts = customtkinter.CTkComboBox(bmi_app, font=font2, text_color='#000',fg_color='#fff', dropdown_hover_color='#06911f', values=wt_opts,variable=var1,width=80)
wt_opts.place(x=200,y=125)
wt_opts.set('kg')

ht_opts = customtkinter.CTkComboBox(bmi_app, font=font2, text_color='#000',fg_color='#fff', dropdown_hover_color='#06911f', values=ht_opts,variable=var2,width=80)
ht_opts.place(x=200,y=220)
ht_opts.set('cm')

calculate_btn = customtkinter.CTkButton(bmi_app,command=bmiCalculator, font=font2, text_color='#fff', text='Calculate', fg_color='#00b4d8', hover_color='#0096c7', bg_color='#023047',cursor="hand2",corner_radius=20,width=200)
calculate_btn.place(x=125,y=400)

category_label = customtkinter.CTkLabel(bmi_app,text='', font=font3, text_color='#fff',bg_color='#023047')
category_label.place(x=90,y=290)


bmi_app.mainloop()


