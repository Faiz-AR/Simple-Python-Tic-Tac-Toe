#   FUNCTIONS   #
def game_board(board):
    print('\n')
    print(str(board[0:3])+"\n"+str(board[3:6])+"\n"+str(board[6:9]))
    print('---------------')
    print("[ 1 , 2 , 3 ]\n[ 4 , 5 , 6 ]\n[ 7 , 8 , 9 ]")

def player_choice():
    number_range = list(range(1,10))
    choice = ''

    while choice not in number_range:
        try:
            choice = int(input("Enter a number between 1-9: "))
            if choice not in number_range:
                print("Sorry, the number you entered is out of range! Please try again")
        except:
            print("Please enter a number value!")

    return int(choice)-1   

def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

def replace(board,choice,mark):
    board[choice] = mark

def check(mark):
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
global counter
global m
game = True
m = ''
counter = 1
board = ['-','-','-', '-','-','-','-','-','-']
         
print("Welcome to Tic-Tac-Toe!")
while True:
    player1_marker, player2_marker = player_input()
    while game == True:
        game_board(board)
        if counter % 2 != 0:
            m = player1_marker
            print('Player 1('+m+') turn!')
        else:
            m = player2_marker
            print('Player 2('+m+') turn!')
        choice = player_choice()
        replace(board,choice,m)
        if check(m) == True:
            game = False
            replay = input('Play Again? (Y/N): ')
            if replay == 'Y':
                game = True
                board = ['-','-','-','-','-','-','-','-','-']
                game_board(board)
                break
            else:
                exit()
        else:
            counter +=1     
