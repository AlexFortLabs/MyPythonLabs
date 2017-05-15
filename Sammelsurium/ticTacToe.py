theBoard = {'tL': ' ', 'tM': ' ', 'tR': ' ',
            'mL': ' ', 'mM': ' ', 'mR': ' ',
            'lL': ' ', 'lM': ' ', 'lR': ' '}

def printBoard(board):
    print(board['tL'] + '|' + board['tM'] + '|' + board['tR'])
    print('-+-+-')
    print(board['mL'] + '|' + board['mM'] + '|' + board['mR'])
    print('-+-+-')
    print(board['lL'] + '|' + board['lM'] + '|' + board['lR'])
    
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
