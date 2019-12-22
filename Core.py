import os
import random
import msvcrt
import time


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


def Movement(Grid, Position_x, Position_y, trail):
    '''
    Places a head as string 'O' in Grid{dict} and allows for the movement of the head using wsad.
    Utilizes Grid_Printer
    Requires the current position of snake head x and y coordinates.
    The trail can be changed using trail{single char. str}.
    Will not allow movement if a wall exists.
    '''
    while True:
        Choice = msvcrt.getch()
        if str(Choice) == "b'd'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x, Position_y + 1)] = 'O'
            Position_y += 1
        if str(Choice) == "b'a'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x, Position_y - 1)] = 'O'
            Position_y -= 1
        if str(Choice) == "b's'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x + 1, Position_y)] = 'O'
            Position_x += 1
        if str(Choice) == "b'w'":
            Grid[(Position_x, Position_y)] = trail
            Grid[(Position_x - 1, Position_y)] = 'O'
            Position_x -= 1
        Grid_Printer(Grid)


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


def Start_End(Grid):
    '''
    Places strings S and E to indicate the start and end of a maze in places 0,0 and x_max, y_max of Grid{dict}.
    '''
    x_max = list(Grid.keys())[-1][0]
    y_max = list(Grid.keys())[-1][1]
    Grid[(0, 0)] = 'S'
    Grid[(x_max, y_max)] = 'E'


def Maze_Maker(Grid):
    '''
    Creates a Maze given a Grid{dict}
    Will assume the Grid consists of 'X' empty values,'.' as trails in Grid_Maker{func} and Movement{func} and '◻' as walls.
    '''
    Position = (0, 0)  # The start S.
    x_max = list(Grid.keys())[-1][0] + 1
    y_max = list(Grid.keys())[-1][-1] + 1

    def Break(x, y):
        '''Destroys a wall given x,y coordinates'''
        Grid[(x, y)] = '.'

    def To_See(x, y):
        '''Will output True if coordinates x,y show an X, False otherwise'''
        try:
            if Grid[(x, y)] == 'X':
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
        if To_See(x-2, y):  # up
            W = True
        if To_See(x+2, y):  # down
            S = True
        if To_See(x, y-2):  # left
            A = True
        if To_See(x, y+2):  # right
            D = True
        return (W, S, A, D)

    def Check_X_dot(x, y):
        '''Checks if there is at least one dot and one X around coordinates x,y'''
        X, dot = False, False
        if To_See(x-2, y):  # up
            X = True
        if To_See(x+2, y):  # down
            X = True
        if To_See(x, y-2):  # left
            X = True
        if To_See(x, y+2):  # right
            X = True

        def To_See_dot(x, y):
            '''Will output True if coordinates x,y show a dot, False otherwise'''
            try:
                if Grid[(x, y)] == '.':
                    return True
                else:
                    return False
            except:
                return False
        if To_See_dot(x-2, y):  # up
            dot = True
        if To_See_dot(x+2, y):  # down
            dot = True
        if To_See_dot(x, y-2):  # left
            dot = True
        if To_See_dot(x, y+2):  # right
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
            # Grid_Printer(Grid)  # Un-tag this to see this beauty in action.
            # time.sleep(0.25) # Un-tag to see it bit by bit.
        else:
            for i in range(x_max):
                for j in range(y_max):
                    if Check_X_dot(i, j) == (True, True):
                        Position = (i, j)
                        break
    if Check_around_E():
        coin = random.randrange(2)
        if coin == 0:
            Grid[(x_max - 2, y_max - 1)] = '.'
        else:
            Grid[(x_max - 1, y_max - 2)] = '.'


# It is best if x and y are odd numbers.
x = 13
y = 79
G = Grid_Maker(x, y, 'X')
Wall_Maker(G)
Start_End(G)
Maze_Maker(G)
Grid_Printer(G)
# Movement(G, 0, 0, '.')
