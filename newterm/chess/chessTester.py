from chessPlayer import *

def chess():
    import os
    board = standardboard()
    done = False
    while not(done):
        os.system('clear')
        printb(board)
        print('Valid Positions ' + str(GetPlayerPositions(board,10)))
        position = int(input('current position '))
        print('Valid Moves: ' + str(GetPieceLegalMoves(board,position)))
        move = int(input('move to '))
        while(True):
            if position in GetPlayerPositions(board,10) and move in GetPieceLegalMoves(board,position):
                board[position],board[move] = 0,board[position]
                break
            else:
                print("Invalid Move.")
                position = int(input('current position '))
                print('Valid Moves: ' + str(GetPieceLegalMoves(board,position)))
                move = int(input('move to '))

        os.system('clear')
        computermove = chessPlayer(board,20)
        position,move = computermove[1][0],computermove[1][1]
        while(True):
            if position in GetPlayerPositions(board,20) and move in GetPieceLegalMoves(board,position):
                board[position],board[move] = 0,board[position]
                print(computermove)
                break
            else:
                print("Chess player broken")
                print("position: " + str(position))
                print("move: " + str(move))
                print(computermove)
                break


#chess()

b = [
13,11,12,15,14,12,11,13,
10,10,10,0,10,10,10,10,
0, 0, 0, 10, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
20,20,20,20,20,20,20,20,
23,21,22,25,24,22,21,23,
]
#print(GetPieceLegalMoves(b,2))
#print(score(b,10))
printb(b)
print(chessPlayer(b,10))
