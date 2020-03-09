import random
from copy import deepcopy


def b_display():  # - Used to print the main board
    for i, value in enumerate(vboard1, 1):
        if(i%3 == 1):
            print('||' + value, end='||')
        else:
            print(value, end='||')
        if i % 3 == 0: print()

def action_h():  # - allowing the human player(x) to play his/her turn
    c = int(input('Dear Human, your turn! Choose where to place (1 - 9): '))
    print("--------------------------")
    if c == vboard[c - 1]:
        vboard[c - 1] = current_player
        vboard1[c - 1] = current_player

def action_a():  # - allowing the computer(o) to play its turn
    print("AI plays move:")
    c = minimax(vboard, depth(vboard), True)
    c = c[1]
    vboard[c - 1] = current_player
    vboard1[c - 1] = current_player

def minimax(b, depth_of_the_board, max_player):  # - the minimax algorithm that searches the game space and returns the best move possible
    if (depth(b) == 0) or (is_terminal(b) == True):
        return evaluate(b)

    if max_player:
        max_eval, best_move = float("-inf"), -1
        for move, child in moves_boards(b):
            ev = minimax(child, depth_of_the_board - 1, False)[0]
            max_eval = max(ev, max_eval)
            if ev == max_eval:  best_move = move
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move, child in moves_boards(b, 'X'):
            ev = minimax(child, depth_of_the_board - 1, True)[0]
            min_eval = min(ev, min_eval)
        return min_eval, -1

def depth(b):  # - return the number of non taken values in a board
    d = 0
    for i in b:
        if isinstance(i, int): d += 1
    return d

def is_terminal(b):  # - returns true if a winning combination is reached
    w_c = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for c in w_c:
        if b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]]:   return True

def evaluate(b):  # - assigning values to boards based on the favorability of player x
    w_c = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for c in w_c:
        if b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]] and b[c[2]] == 'O':
            return [20 - depth(b), -1]
        elif b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]] and b[c[2]] == 'X':
            return [-10 + depth(b), -1]
    return [10 - depth(b), -1]

def moves_boards(b, player='O'):  # returns a list that has pairs of the actions taken and the lists resulted from taking those moves for example:  [ [1,['x',2,3,4,5,6,7,8,9,]], [1,[1,'x',3,4,5,6,7,8,9,]], ... ]
    available_values = [x for x in b if isinstance(x, int)]
    possible_boards = []
    output = []
    for i in available_values:
        c = deepcopy(b)
        c[i - 1] = player
        output.append([i, c])
    return output

def win(b, current_player):  # - returning true if one of the players has won, otherwise returning false
    if (b[0] == current_player and b[1] == current_player and b[2] == current_player) or \
            (b[3] == current_player and b[4] == current_player and b[5] == current_player) or \
            (b[6] == current_player and b[7] == current_player and b[8] == current_player) or \
            (b[0] == current_player and b[3] == current_player and b[6] == current_player) or \
            (b[1] == current_player and b[4] == current_player and b[7] == current_player) or \
            (b[2] == current_player and b[5] == current_player and b[8] == current_player) or \
            (b[0] == current_player and b[4] == current_player and b[8] == current_player) or \
            (b[2] == current_player and b[4] == current_player and b[6] == current_player):
        return True
    else:
        return False


print("Welcome")
print("Randomly selecting which player will go first...")
player = random.choice([1,2])
first = ['', 'AI', 'Human']
print("Random choice selected:",first[player],'\n')

#1 = computer
#2 = player
#print(player)

#if player == 1:


#else:


vboard = [1,2,3,4,5,6,7,8,9]
vboard1 = [" "," "," "," "," "," "," "," "," "]

for turn in range(len([a for a in vboard if isinstance(a, str)]) + 1, 10):
    #print(turn)

    if player == 1:
        if turn % 2 == 0:
            current_player = 'X'
            action_h()
        else:
            current_player = 'O'
            action_a()

    else:
        if turn % 2 == 0:
            current_player = 'O'
            action_a()
        else:
            current_player = "X"
            action_h()


    b_display()

    if win(vboard, current_player) == True:
        print('player {} has won the match'.format(current_player))
        break
    elif (depth(vboard) == 0):
        print("It's a tie!")
        break
    else:
        print(" ")