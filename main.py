import calendar
from datetime import date
from datetime import datetime
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
print(" Press 5- Display Events")
print(" Press 6- Delete/Edit Events")


choice = int(input("Enter an option:"))

#Display current month
def cur_month():
    today=date.today()
    mm=today.month
    yy=today.year
    print("\nCurrent month:", mm)
    print("\nCurrent year:\n",yy) 
    print(calendar.month(yy, mm))



#Display month of your choice

def your_month():
    mm=int(input("Enter the month number of your choice:"))
    yy=int(input("Enter the year:"))
    print(calendar.month(yy,mm))

#Display cal for entire year

def year_cal():
    yy=int(input("Enter year:"))
    print(calendar.calendar(yy))

# Add event

def add_event():
    yy=input("Enter year:")
    mm=input("Enter month:")
    dd=input("Enter day:")
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    f=open("events.txt","a")
    
    add_ev=input()

    y=add_ev + ","+ yy + "," + mm + "," + dd

    f.writelines(y + "\n")

    f.close()
  
# Display Event

def display_ev():
    year=input("Enter year:")
    month=input("Enter month:")
    day=input("Enter day:")
    f = open("events.txt", "r")
    for i in f:
        lst=i.split(",")
        lst[3]=lst[3].replace("\n","")
        if (lst[1]== year and lst[2]==month and lst[3]==day):
            print(f.read())
            
# Delete/Edit Event

def del_edit():
    year=input("Enter year:")
    month=input("Enter month:")
    day=input("Enter day:")

    f = open("events.txt", "r")
    for i in f:
        lst=i.split(",")
        lst[3]=lst[3].replace("\n","")
        if (lst[1]== year and lst[2]==month and lst[3]==day):
            print(f.read())
    select=int(input("Select: 1 for deleting an event\n Select:2 for editing an event"))
   # match select:
      # case 1:


#choice

if choice == 1:
    cur_month()
elif choice == 2:
    your_month()
elif choice == 3:
    year_cal()
elif choice == 4:
    add_event()
elif choice == 5:
    display_ev()
#elif choice == 6:

