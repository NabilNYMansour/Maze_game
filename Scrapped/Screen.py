import os
import time


def ScreenMaker(Screen_x, Screen_y, EmptyPixetValue):
    '''
    Creates a screen given Screen_x{int} and Screen_y{int} coordinates and places EmptyPixetValue{single char. str} as the screen empty value.
    The output is a dictionary of that contains coordinates as keys and pixets as values.
    Notes:
    - The grid starts at (1,1) and ends at (Screen_x, Screen_y).
    - A pixet is a pixel for a terminal.
    '''
    ScreenAxis = []
    Screen = {}
    for x in range(Screen_x):
        for y in range(Screen_y):
            ScreenAxis.append((x, y))
    for counter in range(len(ScreenAxis)):
        Screen[ScreenAxis[counter]] = EmptyPixetValue
    return Screen


def ScreenValuer(Screen):
    '''
    Takes the values from Screen{dict} and returns their values as a list. (So output is a list).
    '''
    ScreenValues = list(Screen.values())
    return ScreenValues


def ScreenPrinter(ScreenValues, Screen_y):
    '''
    Prints the Screen in then console given the ScreenValues{list} and Screen_y{int}. Works with accordance with ScreenMaker and ScreenValuer
    '''
    for counter_print in range(0, len(ScreenValues), Screen_y):
        print(str(ScreenValues[counter_print:(counter_print + Screen_y)]).replace(
            '[', '').replace(',', '').replace(']', '').replace("'", ''))


def ScreenRefresher(ScreenValues, Screen_y, ScreenChecker, TimeDelay):
    '''
    Reprints the screen if ScreenValues{list} is different from ScreenChecker{list} as ScreenChecker should be declared
    in the begining of the code as = list(ScreenValues), the Screen_y{int} is needed for reprinting.
    TimeDelay{float} allows for a bit of delay in reprinting. If no delay is desired, place TimeDelay = 0 as the last argument.
    '''
    # When placing the ScreenChecker, remember that it musts be equal to list(ScreenValues).
    if ScreenChecker != ScreenValues:
        if os.name == 'nt':  # If windows.
            os.system('cls')
        else:  # If linux or others (assuming they are linux based).
            os.system('clear')
        time.sleep(TimeDelay)  # Time delay for refresh rate purposes.
        ScreenPrinter(ScreenValues, Screen_y)


'''
In order to use these commands, you first declare x and y then run
(1) ScreenMaker --> (2) ScreenValuer --> (3) declare checker = list(ScreenValues) --> Then do the code for the Screen Change and implement
ScreenRefresher at the end of each code that changes something in the screen.
'''


# The following is a test/example:

'''
x = 15
y = 30
Screen = ScreenMaker(x, y)
ScreenValues = ScreenValuer(Screen)
Checker = list(ScreenValues)
def SampleChange_Screen():
    ScreenValues[5] = 'X' # This is the change that will occur on the Screen (u place the functions that change the screen here) 
    ScreenRefresher(ScreenValues, y, Checker) # U intigrate this at the end of the function
SampleChange_Screen()
'''

# The following is a comprehensive visualization for the Corners and Borders equations:
'''
x = 15
y = 30
Screen = ScreenMaker(x, y)
ScreenValues = ScreenValuer(Screen)
Checker = list(ScreenValues)
#__________________________________________________________________________
# The Corners:

ScreenValues[0] = 'X'
ScreenValues[y - 1] = 'X'
ScreenValues[(y*x) - y] = 'X'
ScreenValues[(y*x) - 1] = 'X'
#__________________________________________________________________________
#__________________________________________________________________________
# The Borders:

for counter in range(1, y):  # Top Border
    ScreenValues[counter] = 'T'
for counter in range((y*x)-y, (y*x)):  # Bottom Border
    ScreenValues[counter] = 'B'
for counter in range(0, (y*x)-y+1, y):  # Left Border
    ScreenValues[counter] = 'L'
for counter in range(y-1, (y*x), y):  # Right Border
    ScreenValues[counter] = 'R'
ScreenRefresher(ScreenValues, y, Checker, 0)
'''
