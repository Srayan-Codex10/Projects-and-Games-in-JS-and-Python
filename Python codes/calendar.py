"""
Program to Create 
A Command-Line Calender 
Developed by: Srayan Ray
"""
from time import sleep , strftime
USR_NAME = 'Srayan'

calendar = {}

def welcome():
  print("Welcome "+USR_NAME+".")
  
#welcome()
sleep(1)
print("Today is: "+strftime("%A %B %d,%Y"))
print("Time is: "+strftime("%H:%M:%S"))
sleep(1)
print("What would you like to do ?")
def start_calendar():
  welcome()
  start = True
  while (start):
    print("A-Add\n"+"U-Update\n"+"V-View\n"+"D-Delete\n"+"X-Exit\n")
    user_choice = str(raw_input("Enter Your Choice: "))
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print("Calender Empty!")
      else:
        print(calendar)
    elif user_choice == 'U':
      date = str(raw_input("What Date ?: "))
      update = str(raw_input("Enter the update: "))
      calendar[date] = update
      print(calendar)
    elif user_choice == 'A':
      event = str(raw_input("Enter Event: "))
      date = str(raw_input("Enter date(MM/DD/YYYY): "))
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print("Invalid Date!")
        try_again = str(raw_input("Try Again? Y-Yes, N-No: "))
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        sleep(1)
        print("Event Added")
        print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print("Calendar Empty!")
      else:
        event = str(raw_input("What Event ?: "))
        for keys in calendar.keys():
          if calendar[date] == event :
            del(calendar[date])
            sleep(1)
            print("Event Deleted!")
            print(calendar)
          else:
            print("Incorrect Event!")
    elif user_choice == 'X':
      start = False
	  sleep(1)
      print("Exiting Calendar...")
    else:
      print("Invalid Choice!!")
      start = False
	  sleep(1)
      print("Exiting Calendar...")
