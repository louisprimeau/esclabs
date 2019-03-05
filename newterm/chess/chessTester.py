from chessPlayer import *
def time(a, repetitions, *argv):
    import time
    import gc
    gc.disable()
    average = 0
    for i in range(0,repetitions,10):
        start = time.process_time()
        a(*argv)
        end = time.process_time()
        average += (end - start)
    print(average/repetitions)
    gc.enable()
    return(0)

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

        if not(25 in list(board[i] for i in GetPlayerPositions(board,20))):
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

        if not(15 in list(board[i] for i in GetPlayerPositions(board,10))):
            print('Black Wins')
            break

def chessAI():
    import os
    import time
    board = standardboard()
    done = False
    while not(done):
        os.system('clear')
        printb(board)
        print("White to move")
        start = time.process_time()
        computermove = chessPlayer(board,10)
        end = time.process_time()
        print(end - start)


        position,newmove = computermove[1][0],computermove[1][1]
        board[position],board[newmove] = 0,board[position]

        if not(25 in list(board[i] for i in GetPlayerPositions(board,20))):
            print('White Wins')
            break


        os.system('clear')
        printb(board)

        print("Black to move")
        start = time.process_time()
        computermove = chessPlayer(board,20)
        end = time.process_time()
        position,newmove = computermove[1][0],computermove[1][1]
        board[position],board[newmove] = 0,board[position]
        print(end - start)

        if not(15 in list(board[i] for i in GetPlayerPositions(board,10))):
            print('Black Wins')
            break

chessAI()
#chess
