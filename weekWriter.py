#! python3

import pyautogui
import time
guiPress = pyautogui.press
guiWrite = pyautogui.write
year = '2021'


months = {'1': 'January',
          '2': 'February',
          '3': 'March',
          '4': 'April',
          '5': 'May',
          '6': 'June',
          '7': 'July',
          '8': 'August',
          '9': 'September',
          '10': 'October',
          '11': 'November',
          '12': 'December'
          }

weekdays = {'1': 'Monday',
            '2': 'Tuesday',
            '3': 'Wednesday',
            '4': 'Thursday',
            '5': 'Friday',
            '6': 'Saturday',
            '7': 'Sunday'
            }

def spacer(amount):
    guiPress('enter', presses=amount)

def morning_routine():
    guiWrite('- [ ] **6:00am** Wake up, gym, prepair for classes')
    spacer(3)
	
def after_5pm():
    guiWrite('- [ ] **Study and Freetime after 5pm**')
    spacer(2)


def monday_wednesday_classes():
    morning_routine()

    guiWrite('- [ ] **CMPSCI203 9:05am - 9:55am** Lecture in Wartik Lab 101, '
    'Complete the quiz that is due at 7pm tonight')

    spacer(2)
    guiWrite('- [ ] **Classwork 9:55am - 11:15am**')
    spacer(2)
    
    guiWrite('- [ ] **RPTM320 11:15am - 12:05pm** Lecture in ' 
    'Reber Building 135')

    spacer(2)
    guiWrite('- [ ] **Classwork 12:05pm - 2:30pm**')
    spacer(2)
    
    guiWrite('- [ ] **RPTM325 2:30pm - 3:45pm** Lecture in Forest '
    'Resources Building 104')
    
    spacer(2)
    guiWrite('- [ ] **Classwork 3:45pm - 5pm**')
    spacer(3)
    
    after_5pm()


def tuesday_thursday_classes(weekday_num):
    morning_routine()
    if weekday_num == 4:
        guiWrite('- [ ] **CMPSCI203 9:05am - 10:20am** Recitation on Zoom')
        spacer(2)
    elif weekday_num == 2:
        guiWrite('- [ ] **Classwork 9:00am - 10:35am**')
        spacer(2)

    guiWrite('- [ ] **RPTM277 10:35am - 11:50am** Lecture in Borland Building 112')
    spacer(2)


    guiWrite('- [ ] **Classwork 11:50am - 5pm**')
    spacer(3)
   
    after_5pm()


def friday_classes():
    morning_routine()

    guiWrite('- [ ] **CMPSCI203 9:05am - 9:55am** Recorded Lecture')
    
    spacer(2)
    guiWrite('- [ ] **Classwork 9:55am - 11:15am**')
    spacer(2)

    guiWrite('- [ ] **RPTM320 11:15am - 12:05pm** Lecture in Reber Building 135')
    
    spacer(2)
    guiWrite('- [ ] **Classwork 12:05pm - 1:25pm**')
    spacer(2)

    guiWrite('- [ ] **RPTM394 1:25pm - 3:20pm** Lecture in Rackley Building 104')

    spacer(2)
    guiWrite('- [ ] **Classwork 3:20pm - 5pm**')
    spacer(3)

    after_5pm()


def saturday():
    guiWrite('- [ ] Temp')

def sunday():
    guiWrite('- [ ] Temp')

    



def weekday_writer(): #writes out the daily schedule for the entire week
    weekday_counter = 1
    print('These are the month options:')
    
    for i in months:
        print(i + ': ' + months[str(i)]) #Prints out list of months

    current_month = input('what is the current month: ')
    monday_start_date = input('Date of monday in the upcoming week: ')
    #The line above requests the date of upcoming monday
    
    print('Waiting for 3 seconds before writing')
    time.sleep(3)


    
    while weekday_counter <= 7:
        guiWrite('### ' + months[current_month] + ' ' + str(monday_start_date)
                + ', ' + year + ' ' + weekdays[str(weekday_counter)])
        #above line prints out the month, day, year, and the day of the week as a heading

        spacer(1)
        guiPress('-', presses=3)
        spacer(1)

        #The statements below will print the consecutive days of the week
        if weekday_counter == 1 or weekday_counter == 3:
            monday_wednesday_classes()
        elif weekday_counter == 2 or weekday_counter == 4:
            tuesday_thursday_classes(weekday_counter)
        elif weekday_counter == 5:
            friday_classes()
        elif weekday_counter == 6:
            saturday()
        else:
            sunday()

        spacer(3) #adds space for next day
        weekday_counter = weekday_counter + 1 #setup for the next weekday 
        monday_start_date = int(monday_start_date) + 1  #calender date


if __name__ == "__main__":
    weekday_writer()
