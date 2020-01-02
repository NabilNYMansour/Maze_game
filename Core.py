import os
import random
import time
if os.name == 'nt':
    import msvcrt
    windows = True
else:
    import getch
    windows = False

#------------------------|The functions|------------------------#


def Grid_Maker(x, y, Empty_Point_Value):
    '''
    Creates a grid given x{int} and y{int} coordinates and places Empty_Point_Value{single char. str} as the empty values in the grid.
    The output is a dictionary of a grid made up with Empty_Point_Value strings as values and x,y coordinates as keys.
    '''
    Grid = {}
    for i in range(x):
        for j in range(y):
            Grid[(i, j)] = Empty_Point_Value
    return Grid


def Grid_Printer(Grid):
    '''
    Prints a given Grid{dict} after clearing the terminal.
    Will also print a boarder with '◻'.
    '''
    if os.name == 'nt':  # If windows.
        os.system('cls')
    else:  # If linux or others (assuming they are linux based).
        os.system('clear')
    y_max = list(Grid.keys())[-1][-1] + 1
    # the y axis is needed to know where to stop printing each line and to skip y times to start the next line.
    print('◻ '*(y_max+2))
    for i in range(0, len(list(Grid.values())), y_max):
        print('◻ ' + str(list(Grid.values())[i:(i + y_max)]).replace('[', '').replace(
            ',', '').replace(']', '').replace("'", '') + ' ◻')
    print('◻ '*(y_max+2))


def Win_Screen(Grid, counter):
    '''Prints a "YOU WIN!" in the middle of the Grid and shows number of moves.'''
    x_mid = (list(Grid.keys())[-1][0] + 1)//2
    y_mid = (list(Grid.keys())[-1][-1] + 1)//2
    # YOU WIN!
    Grid[(x_mid - 1, y_mid - 4)] = ' '
    Grid[(x_mid - 1, y_mid - 3)] = 'Y'
    Grid[(x_mid - 1, y_mid - 2)] = 'O'
    Grid[(x_mid - 1, y_mid - 1)] = 'U'
    Grid[(x_mid - 1, y_mid)] = ' '
    Grid[(x_mid - 1, y_mid + 1)] = 'W'
    Grid[(x_mid - 1, y_mid + 2)] = 'I'
    Grid[(x_mid - 1, y_mid + 3)] = 'N'
    Grid[(x_mid - 1, y_mid + 4)] = '!'
    Grid[(x_mid - 1, y_mid + 5)] = ' '
    # Moves:
    Grid[(x_mid, y_mid - 3)] = ' '
    Grid[(x_mid, y_mid - 2)] = 'M'
    Grid[(x_mid, y_mid - 1)] = 'o'
    Grid[(x_mid, y_mid)] = 'v'
    Grid[(x_mid, y_mid + 1)] = 'e'
    Grid[(x_mid, y_mid + 2)] = 's'
    Grid[(x_mid, y_mid + 3)] = ':'
    Grid[(x_mid, y_mid + 4)] = ' '
    # counter that centers the length to the middle such that 01234 becomes -2-1012.
    length = len(str(counter))
    j = length - 1
    if length % 2 == 0:
        Grid[(x_mid + 1, y_mid - length//2)] = ' '
    else:
        Grid[(x_mid + 1, y_mid - (length//2 + 1))] = ' '
    for i in range(length//2, - length//2, - 1):
        Grid[(x_mid + 1, y_mid + i)] = str(counter)[j]
        j -= 1
    Grid[(x_mid + 1, y_mid + 1 + length//2)] = ' '


def Movement(Grid, Position_x, Position_y, trail):
    '''
    Places a head as string 'O' in Grid{dict} and allows for the movement of the head using wsad.
    Utilizes Grid_Printer
    Requires the current position of snake head x and y coordinates.
    # The trail can be changed using trail{single char. str}.
    # Or, the trail can be a counter of moves.
    Will not allow movement if a wall exists and will assume that the wall is ◻.
    '''

    counter = 0
    while True:
        try:
            if windows:
                Choice = msvcrt.getch()
            else:
                Choice = getch.getch()
            if str(Choice) == "b'd'" or str(Choice) == 'd':
                if Grid[(Position_x, Position_y + 1)] == '◻':
                    pass
                elif Grid[(Position_x, Position_y + 1)] == 'E':  # Win screen.
                    Win_Screen(Grid, counter)
                    Grid_Printer(Grid)
                    return
                else:
                    Grid[(Position_x, Position_y)] = trail
                    Grid[(Position_x, Position_y + 1)] = 'O'
                    Position_y += 1
                    counter += 1
            if str(Choice) == "b'a'" or str(Choice) == 'a':
                if Grid[(Position_x, Position_y - 1)] == '◻':
                    pass
                elif Grid[(Position_x, Position_y - 1)] == 'E':
                    Win_Screen(Grid, counter)
                    Grid_Printer(Grid)
                    return
                else:
                    Grid[(Position_x, Position_y)] = trail
                    Grid[(Position_x, Position_y - 1)] = 'O'
                    Position_y -= 1
                    counter += 1
            if str(Choice) == "b's'" or str(Choice) == 's':
                if Grid[(Position_x + 1, Position_y)] == '◻':
                    pass
                elif Grid[(Position_x + 1, Position_y)] == 'E':
                    Win_Screen(Grid, counter)
                    Grid_Printer(Grid)
                    return
                else:
                    Grid[(Position_x, Position_y)] = trail
                    Grid[(Position_x + 1, Position_y)] = 'O'
                    Position_x += 1
                    counter += 1
            if str(Choice) == "b'w'" or str(Choice) == 'w':
                if Grid[(Position_x - 1, Position_y)] == '◻':
                    pass
                elif Grid[(Position_x - 1, Position_y)] == 'E':
                    Win_Screen(Grid, counter)
                    Grid_Printer(Grid)
                    return
                else:
                    Grid[(Position_x, Position_y)] = trail
                    Grid[(Position_x - 1, Position_y)] = 'O'
                    Position_x -= 1
                    counter += 1
            Grid_Printer(Grid)
        except KeyError:
            pass


def Wall_Maker(Grid):
    '''
    Applies walls to Grid{dict} to be demolished later.
    '''
    x_max = list(Grid.keys())[-1][0] + 1
    y_max = list(Grid.keys())[-1][1] + 1
    for i in range(x_max):
        for j in range(1, y_max, 2):
            Grid[(i, j)] = '◻'
    for i in range(1, x_max, 2):
        for j in range(y_max):
            Grid[(i, j)] = '◻'


def Start_End_Setter(Grid):
    '''
    Places strings S and E to indicate the start and end of a maze in places randomly at the first and last columns.
    Will output x position of starting value.
    '''
    x_max = list(Grid.keys())[-1][0]
    y_max = list(Grid.keys())[-1][1]
    Starting_x_value = random.randrange(0, x_max)
    Ending_x_value = random.randrange(0, x_max)
    Grid[(Starting_x_value, 0)] = 'S'
    Grid[(Ending_x_value, y_max)] = 'E'
    return Starting_x_value


def Maze_Maker(Grid, Build_up_bool):
    '''
    Creates a Maze given a Grid{dict}
    Will assume the Grid consists of 'X' empty values,'.' as trails in Grid_Maker{func} and Movement{func} and '◻' as walls.
    Will show the build up of the maze if Build_up_bool{Bool} is True.
    '''
    Position = (0, 0)  # The start S.
    x_max = list(Grid.keys())[-1][0] + 1
    y_max = list(Grid.keys())[-1][-1] + 1

    def Break(x, y):
        '''Destroys a wall given x,y coordinates'''
        Grid[(x, y)] = '.'

    def To_See(x, y, pixet):
        '''Will output True if coordinates x,y show a pixet, False otherwise'''
        try:
            if Grid[(x, y)] == pixet:
                return True
            else:
                return False
        except:
            return False

    def Check_X(x, y):
        '''
        Checks if a position on the has X's on the left, right, up or down. Will return True for each side with order wsad.
        So the output is (W{Bool}, S{Bool}, A{Bool}, D{Bool}).
        '''
        W, S, A, D = False, False, False, False
        # +-2 is placed due to the walls.
        if To_See(x-2, y, 'X'):  # up
            W = True
        if To_See(x+2, y, 'X'):  # down
            S = True
        if To_See(x, y-2, 'X'):  # left
            A = True
        if To_See(x, y+2, 'X'):  # right
            D = True
        return (W, S, A, D)

    def Check_X_dot(x, y):
        '''Checks if there is at least one dot and one X around coordinates x,y'''
        X, dot = False, False
        if To_See(x-2, y, 'X'):  # up
            X = True
        if To_See(x+2, y, 'X'):  # down
            X = True
        if To_See(x, y-2, 'X'):  # left
            X = True
        if To_See(x, y+2, 'X'):  # right
            X = True
        if To_See(x-2, y, '.'):  # up
            dot = True
        if To_See(x+2, y, '.'):  # down
            dot = True
        if To_See(x, y-2, '.'):  # left
            dot = True
        if To_See(x, y+2, '.'):  # right
            dot = True
        return (X, dot)

    def Check_any_X_in_Grid(Grid):
        '''Outputs True if there is an X in Grid{dict}, False otherwise'''
        nonlocal x_max, y_max
        for i in range(x_max):
            for j in range(y_max):
                if Grid[(i, j)] == 'X':
                    return True
        return False

    def Check_around_E():
        '''Will check if the End is blocked. Outputs True if it is, False otherwise.'''
        nonlocal x_max, y_max
        # - 2 is done with - 1 since 1 is added initially for range purposes.
        if Grid[(x_max - 2, y_max - 1)] == '◻' and Grid[(x_max - 1, y_max - 2)] == '◻':
            return True
        else:
            return False

    def Break_to_dot(x, y):
        '''Checks where there is a dot next to position with x,y coordinates and breaks the wall in between'''
        if To_See(x-2, y, '.'):  # up
            Break(x-1, y)
            return
        if To_See(x+2, y, '.'):  # down
            Break(x+1, y)
            return
        if To_See(x, y-2, '.'):  # left
            Break(x, y-1)
            return
        if To_See(x, y+2, '.'):  # right
            Break(x, y+1)
            return

    while Check_any_X_in_Grid(Grid):
        Check = Check_X(Position[0], Position[1])
        # This will give the indices that have True values.
        Selection_List = [i for i in range(4) if Check[i] == True]
        try:
            # There is a slice sine sample function outputs a list of only one value.
            Selection_Coin = random.sample(Selection_List, 1)[0]
        except:
            Selection_Coin = None
        if Selection_Coin != None:
            if Selection_Coin == 0:  # W
                Break(Position[0] - 1, Position[1])
                # And again, +- 2 due to walls.
                Position = (Position[0] - 2, Position[1])
            if Selection_Coin == 1:  # S
                Break(Position[0] + 1, Position[1])
                Position = (Position[0] + 2, Position[1])
            if Selection_Coin == 2:  # A
                Break(Position[0], Position[1] - 1)
                Position = (Position[0], Position[1] - 2)
            if Selection_Coin == 3:  # D
                Break(Position[0], Position[1] + 1)
                Position = (Position[0], Position[1] + 2)
            Grid[(Position[0], Position[1])] = '.'
            if Build_up_bool == True:
                Grid_Printer(Grid)  # Un-tag this to see this beauty in action.
            # time.sleep(0.25) # Un-tag to see it bit by bit.
        else:
            for i in range(x_max):
                for j in range(y_max):
                    if Check_X_dot(i, j) == (True, True):
                        Position = (i, j)
                        Break_to_dot(i, j)
                        break
    if Check_around_E():
        coin = random.randrange(2)
        if coin == 0:
            Grid[(x_max - 2, y_max - 1)] = '.'
        else:
            Grid[(x_max - 1, y_max - 2)] = '.'
#---------------------------------------------------------------#


#------------------------|Declarations and Organizations|------------------------#
Replay = True
Change_Coordinates = True
Build_up_bool = False
print('You will start from top left in S and must reach the bottom right in E in order to win!')
print('Game works best if u maximize the terminal window.')
while Replay:
    while Change_Coordinates:
        try:
            x = int(input('Put odd x coordinate value (min of 10 is advised): '))
            y = int(input('Put odd y coordinate value (min of 10 is advised): '))
            Build_up = input('Show Maze build up? y/n ')
            if Build_up == 'y':
                Build_up_bool = True
            if Build_up == 'n':
                Build_up_bool = False
            if x % 2 == 0:
                x += 1
            if y % 2 == 0:
                y += 1
            if x < 10 or y < 10:
                raise ValueError
            Change_Coordinates = False
        except ValueError:
            print('Default of x = 13, y = 13 will be selected.')
            time.sleep(2)
            x, y = 13, 13
            Change_Coordinates = False
    G = Grid_Maker(x, y, 'X')
    Wall_Maker(G)
    Maze_Maker(G, Build_up_bool)
    Starting_x_value = Start_End_Setter(G)
    Grid_Printer(G)
    Movement(G, Starting_x_value, 0, '.')
    User_Input = input(
        'Press r for replay, e for exit, otherwise, the game will be replayed. ')
    if User_Input == 'e':
        Replay = False
    elif User_Input == 'r':
        Coordinates_change = input('Change coordinates? y/n ')
        if Coordinates_change == 'y':
            Change_Coordinates = True
print('Made by Nabil Mansour, thank you for playing and goodbye.')
print('Program will exit in 5 seconds.')
time.sleep(5)
#--------------------------------------------------------------------------------#
