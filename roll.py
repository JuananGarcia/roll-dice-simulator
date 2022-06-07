#import libraries
#random use to randomize numbers from 1 to 6 
#tkinter use to create a simple GUI in python
import random
from tkinter import *

#Create a window/instance 
window=Tk()

#Size window
window.geometry("500x500")

window.title("Roll two dices")

#GUI
    #Dices represent
    #Button for roll dices
l1=Label(window,font=("Helvetica", 260))

#function of the dice in the tkinder instance
def roll_dices():
    #Dice represent by ACII characters
    first_dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']  
    
    #This is how works and shiw the dices in window
    l1.config(text=f'{random.choice(first_dice)}{random.choice(first_dice)}')
    l1.pack()

#Button for activate the function roll_dices()
b1=Button(window,text="ROLL", foreground='red',command=roll_dices)
b1.place(x=300,y=0)
b1.pack()

window.mainloop()

'''first_dice = random.randint(1,20)
second_dice = random.randint(1,20)

print("Dice 1: " + repr(first_dice))
print("Dice 2: " + repr(second_dice))'''