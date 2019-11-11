# Testpile...

'''
from threading import Thread
on = ''
def func1():
    global on
    on = str(input())

def func2():
    global on
    while on != 'stop':
        print('yes')

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()

#
def ScreenPlayer(ScreenValues, Screen_y):
    # Press f to turn off
    on = ''

    def switch():
        nonlocal on
        while True:
            on = str(input())

    def player():
        nonlocal on
        while on != 'f':
            for counter_print in range(0, len(ScreenValues), Screen_y):
                print(str(ScreenValues[counter_print:(counter_print + Screen_y)]).replace(
                    '[', '').replace(',', '').replace(']', '').replace("'", ''))
                time.sleep(0.5)
            os.system('cls')
    if __name__ == '__main__':
        Thread(target=switch).start()
        Thread(target=player).start()
'''
from Screen import ScreenMaker, ScreenPrinter, ScreenRefresher, ScreenValuer

x = 15
y = 50
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
    ScreenValues[counter] = '+'
for counter in range((y*x)-y, (y*x)):  # Bottom Border
    ScreenValues[counter] = '+'
for counter in range(0, (y*x)-y+1, y):  # Left Border
    ScreenValues[counter] = '+'
for counter in range(y-1, (y*x), y):  # Right Border
    ScreenValues[counter] = '+'
ScreenRefresher(ScreenValues, y, Checker, 0)
