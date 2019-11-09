import Screen
# Setting x and y:
x = 15
y = 50
place = 10
Board = Screen.ScreenMaker(x, y)
BoardValues = Screen.ScreenValuer(Board)
Checker = list(BoardValues)
BoardValues[place] = 'O'
def Movement(StartingPostion): # wasd
    postion = StartingPostion
    while True:
        Choice = input()
        if Choice == 'd':
            BoardValues[postion] = '.'
            BoardValues[postion + 1] = 'O'
            postion = postion + 1
        if Choice == 'a':
            BoardValues[postion] = '.'
            BoardValues[postion - 1] = 'O'
            postion = postion - 1
        Screen.ScreenRefresher(BoardValues,y,Checker)
Movement(place)