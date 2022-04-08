from tkinter import *
import math
def Calculate(event):
    LabelBoxResult = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if LabelBoxResult >= 30:
        print("อ้วนมาก")
    elif LabelBoxResult >= 25.0:
        print("อ้วน")
    elif LabelBoxResult >= 23.0:
        print("น้ำหนักเกิน")
    elif LabelBoxResult >= 18.6:
        print("น้ำหนักปกติ ")
    elif LabelBoxResult <= 18.5:
        print("ผอมเกินไป")

main = Tk()
labelHeight = Label(main,text = "Height (cm.)")
labelHeight.grid(row = 0,column = 0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row = 0,column = 1)
labelWeight = Label(main,text = "Weight (Kg.)")
labelWeight.grid(row = 1,column = 0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row = 1,column = 1)
Calculatebutton = Button(main,text = "Total BMI")
Calculatebutton.bind("<Button-1>",Calculate)
Calculatebutton.grid(row = 2,column = 0)
LabelBoxResult = Label(main,text = "BMI")
LabelBoxResult.grid(row = 2,column = 1)
main.mainloop()