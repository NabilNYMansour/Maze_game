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

'''
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