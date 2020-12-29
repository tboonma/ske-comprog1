import sys
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
numtoboard = ['top-L','top-M','top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R']

def printBoard(board):
    print('\t' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('\t' + '-+-+-')
    print('\t' + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('\t' + '-+-+-')
    print('\t' + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def printguide():
    print()
    print('\t' + '1' + '|' + '2' + '|' + '3')
    print('\t' + '-+-+-')
    print('\t' + '4' + '|' + '5' + '|' + '6')
    print('\t' + '-+-+-')
    print('\t' + '7' + '|' + '8' + '|' + '9')
    print()

def checkBoard(board):
    list_board = list(board.values())
    if list_board[0] == list_board[1] == list_board[2] and list_board[0] != ' ':
        return list_board[0]
    elif list_board[0] == list_board[4] == list_board[8] and list_board[0] != ' ':
        return list_board[0]
    elif list_board[0] == list_board[3] == list_board[6] and list_board[0] != ' ':
        return list_board[0]
    elif list_board[1] == list_board[4] == list_board[7] and list_board[1] != ' ':
        return list_board[1]
    elif list_board[2] == list_board[4] == list_board[6] and list_board[2] != ' ':
        return list_board[2]
    elif list_board[2] == list_board[5] == list_board[8] and list_board[2] != ' ':
        return list_board[2]
    elif list_board[3] == list_board[4] == list_board[5] and list_board[3] != ' ':
        return list_board[3]
    elif list_board[6] == list_board[7] == list_board[8] and list_board[6] != ' ':
        return list_board[6]
    else:
        return False

turn = 'X'
print("Starting Tic Tac Toe")
for i in range(9):
    printguide()
    printBoard(theBoard)
    while True:
        move = int(input('Input a number 1 to 9 to place ' + turn + ' in one of the nine squares: '))
        if theBoard[numtoboard[move-1]] == ' ':
            theBoard.update({numtoboard[move-1]:turn})
            break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    ans = checkBoard(theBoard)
    if ans:
        printguide()
        printBoard(theBoard)
        print(f"\n{ans} wins.")
        sys.exit()
printguide()
printBoard(theBoard)
print("\nBoth tie.")