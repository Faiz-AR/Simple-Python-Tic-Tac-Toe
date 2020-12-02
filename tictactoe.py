'''
A SIMPLE TIC-TAC-TOE GAME
'''
import sys
#   FUNCTIONS   #
def game_board(board):
    '''
    To display/update gameboard after each turn
    '''
    print('\n')
    print(str(board[0:3])+"\n"+str(board[3:6])+"\n"+str(board[6:9]))
    print('---------------')
    print("[ 1 , 2 , 3 ]\n[ 4 , 5 , 6 ]\n[ 7 , 8 , 9 ]")

def player_choice():
    '''
    To return the player's choice and notify if the choice is out of range or isn't a number
    '''
    number_range = list(range(1,10))
    choice = ''
    while choice not in number_range:
        try:
            choice = int(input("Enter a number between 1-9: "))
            if choice not in number_range:
                print("Sorry, the number you entered is out of range! Please try again")
        except TypeError:
            print("Please enter a number value!")
    return int(choice)-1   

def player_input():
    '''
    To record player 1 and player 2 marker
    '''
    marker = ''

    while marker not in ['X','O']:
        marker = input('Player 1, choose X or O: ')
        if marker not in ['X','O']:
            print("Enter X or O!")
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def replace(board,choice,mark):
    '''
    Replace the '-' in the board with the player's marker and position choice
    '''
    valid = False

    if board[choice] != '-':
        valid = False
    else:
        board[choice] = mark
        valid = True

    return valid

def check(mark):
    '''
    To check for win/draw conditions after each turn
    '''
    #HORIZONTAL WIN
    if board[0] == mark and board[1] == mark and board[2] == mark or  board[3] == mark and board[4] == mark and board[5] == mark or  board[6] == mark and board[7] == mark and board[8] == mark:
        print("Congrats! Player "+ mark + " wins the game!")
        return True

    #VERTICAL WIN
    elif board[0] == mark and board[3] == mark and board[6] == mark or  board[1] == mark and board[4] == mark and board[7] == mark or  board[2] == mark and board[5] == mark and board[8] == mark:
        print("Congrats! Player "+ mark + " wins the game!")
        return True

    #DIAGONAL WIN
    elif board[0] == mark and board[4] == mark and board[8] == mark or  board[2] == mark and board[4] == mark and board[6] == mark:
        print("Congrats! Player "+ mark + " wins the game!")
        return True

    #DRAW
    elif board[0] != '-' and board[1] != '-'  and board[2] != '-'  and  board[3] != '-'  and board[4] != '-'  and board[5] != '-' and board[6] != '-'  and board[7] != '-'  and board[8] != '-':
        print("Game ends in a draw!")
        return True
    else:
        return False

#   GAME   #
global COUNTER
global MARK
MARK = ''
COUNTER = 1
GAME = True
board = ['-','-','-', '-','-','-','-','-','-']
print("Welcome to Tic-Tac-Toe!")
while True:
    player1_marker, player2_marker = player_input()
    while GAME is True:
        game_board(board)
        if COUNTER % 2 != 0:
            MARK = player1_marker
            print('Player 1('+MARK+') turn!')
        else:
            MARK = player2_marker
            print('Player 2('+MARK+') turn!')
        CHOICE = player_choice()
        if replace(board,CHOICE,MARK) is  False:
            print('Space taken! Try again')
            continue
        if check(MARK) is True:
            GAME = False
            replay = input('Play Again? (Y/N): ')
            if replay == 'Y':
                GAME = True
                board = ['-','-','-','-','-','-','-','-','-']
                game_board(board)
                break
            else:
                sys.exit()
        else:
            COUNTER +=1
