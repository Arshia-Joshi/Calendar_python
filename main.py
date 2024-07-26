import calendar
from datetime import date
import colorama
from colorama import Fore,Back,Style

#Contents
print("--------------------------------------------------")
print("               CALENDAR                              ")
print("---------------------------------------------------")
print(" Press 1- Display Current-Month Calendar")
print(" Press 2- Select Calendar for Month of your choice")
print(" Press 3- Select Calendar for Year of your choice")
print(" Press 4- Add Events")

choice = int(input("Enter an option:"))

#Display current month
def cur_month():
    today=date.today()
    mm=today.month
    yy=today.year
    print("\nCurrent month:", mm)
    print("\nCurrent year:\n",yy) 
    print(calendar.month(yy, mm))

    #present day text col
    class ANSI():
        def style_text(code):
        return "\33[{code}m".format(code=code)


#Display month of your choice

def your_month():
    mm=int(input("Enter the month number of your choice:"))
    yy=int(input("Enter the year:"))
    print(calendar.month(yy,mm))

#Display cal for entire year

def year_cal():
    yy=int(input("Enter year:"))
    print(calendar.calendar(yy))



#choice

if choice == 1:
    cur_month()
elif choice == 2:
    your_month()
elif choice == 3:
    year_cal()
