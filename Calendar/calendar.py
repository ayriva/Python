"""
Calendar
* View the calendar
* Add an event to the calendar
* Update an existing event
* Delete an existing event
"""

from time import sleep, strftime

name = 'Alex'
calendar = {}

def welcome():
  print('Hello, ' + name + '!')
  print('calendar is starting...')
  sleep(1)
  print('Today is: ' + strftime('%A %B %d, %Y'))
  print('Time: ' + strftime('%H:%M:%S'))
  print('What would you like to do?')

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input('A to Add, U to Update, V to View, D to Delete, X to Exit: ')
    user_choice = user_choice.upper()

    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print('Calendar empty')
      else:
        print(calendar)

    elif user_choice == 'U':
      date = input('What date? ')
      update = input('Enter the update: ')
      calendar[date] = update
      print('The date has been updated')
      print(calendar)

    elif user_choice == 'A':
      event = input('Enter event: ')
      date = input('Enter date (MM/DD/YYY): ')
      if (len(date) > 10 or int(date[6:]) < int(strftime('%Y'))):
        print('Invalid year: cant input prev years')
        try_again = input('Try Again? Y for Yes, N for No: ')
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print('Event has been added')
        print(calendar)

    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print('Calendar empty')
      else:
        event = input('What event? ')
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print('Event has been deleted')
          else:
            print('Event not found')

    elif user_choice == 'X':
      start = False

    else:
      print('Invalid command')
      start = False

start_calendar()
