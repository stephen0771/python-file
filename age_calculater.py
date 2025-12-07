
#def pattern(n):
   # p=n+3
   # for i in range(0,n):
       # for j in range(0,p):
           # print(end="")
            #p=p-4
            #for j in range(0,i+1):
             #   if i==2:
              #    print("🎉❤️‍🔥🥂🖇️",end="")
               # elif i==3:
                #    print("❤️‍🔥💝🎂🍿happybirthday buddy",end="")
            #print("\r")
#pattern(2)#

import time
import random
from datetime import datetime
from tkinter import Tk, ttk , messagebox


class mmotivationalapp(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Daily motivation"
        self.geometry("300*300")
        self.resizable(False, False)
        self.moods = ["Happy","Tired","anxious", "unmotivated"]
        ttk.label(self, text="select mood:").pack(pady=(15,5))
        self.mood_var = ("happy")
        self.mood_dropdown = ttk.Combobox
















    
