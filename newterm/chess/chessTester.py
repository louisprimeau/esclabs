from chessPlayer import *

def chess():
    import os
    import time
    board = standardboard()
    done = False
    while not(done):
        os.system('clear')
        printb(board)

        print('Valid Positions: ', end='')
        for i in GetPlayerPositions(board,10):
            print(lettermap(i),end=' ')
        print(' ')

        position = coordmap(input('current position '))

        print('Valid Moves: ', end='')
        for i in GetPieceLegalMoves(board,position):
            print(lettermap(i),end=' ')
        print(' ')


        newmove = coordmap(input('move to '))
        while(True):
            if position in GetPlayerPositions(board,10) and newmove in GetPieceLegalMoves(board,position):
                board[position],board[newmove] = 0,board[position]
                break
            else:
                print("Invalid Move.")
                position = coordmap(input('current position '))

                print('Valid Moves: ', end='')
                for i in GetPieceLegalMoves(board,position):
                    print(lettermap(i),end=' ')
                print(' ')

                newmove = coordmap(input('move to '))

        if not(25 in list(b[i] for i in GetPlayerPositions(board,20))):
            print('White Wins')
            break

        os.system('clear')
        start = time.process_time()
        computermove = chessPlayer(board,20)
        position,newmove = computermove[1][0],computermove[1][1]
        while(True):
            if position in GetPlayerPositions(board,20) and newmove in GetPieceLegalMoves(board,position):
                board[position],board[newmove] = 0,board[position]
                #print(computermove)
                break
            else:
                print("Chess player broken")
                print("position: " + str(position))
                print("move: " + str(newmove))
                print(computermove)
                break
        end = time.process_time()
        print(end - start)

        if not(15 in list(b[i] for i in GetPlayerPositions(board,10))):
            print('Black Wins')
            break

chess()
b = [
13,11,12,15,14,12,11,13,
10,10,10,10,10,10,10,10,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
20,20,20,20,20,20,20,20,
23,21,22,25,24,22,21,23,
]

time(chessPlayer,1,b,10)
