
def GetPlayerPositions(board,player):
    return([i for i,x in enumerate(board) if(x >= player and x < player + 10)])
def player(value):
    if(value >= 20):
        return(-1)
    elif(value >= 10):
        return(1)
    else:
        return(0)
def piece(value):
    if(value < 20):
        return(value - 10)
    elif(value >= 20):
        return(value - 20)
def GetPieceLegalMoves(board,position):
    value = board[position]
    legalmoves = []
    pl = player(value)
    pi = piece(value)

    #Pawns:
    if(pi == 0):

        # CHECK DIRECTLY IN FRONT
        if(board[position + pl * 8] == 0):
            legalmoves.append(position + pl * 8)

        # CHECK TO LEFT
        c = board[position + pl * 8 - 1]
        a = player(c)
        if(c != 0 and a != pl and a != 0):
            legalmoves.append(position + pl * 8 - 1)

        # CHECK TO RIGHT
        c = board[position + pl * 8 + 1]
        a = player(c)
        if((c != 0) and a != pl and a != 0):
            legalmoves.append(position + pl * 8 + 1)

    #Knights:
    elif(pi == 1):

        #Forward:
        # pl (forwards/backwards) * 8 (length of row) * 2 (number of rows)
        if(64 > position + pl * 8 * 2 > 0):

            #2forward 1left:
            move = position + pl * 8 * 2 - 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #2forward 1right:
            move = position + pl * 8 * 2 + 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        if(64 > position + pl * 8 * 1 > 0):

            #1forward 2left
            move = position + pl * 8 * 1 - 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #1forward 2right
            move = position + pl * 8 * 1 + 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        #Backward:

        # pl (forwards/backwards) * 8 (length of row) * 2 (number of rows)
        if(64 > position + -1 * pl * 8 * 2 > 0):

            #2backward 1left:
            move = position + -1 * pl * 8 * 2 - 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #2backward 1right:
            move = position + -1 * pl * 8 * 2 + 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        if(64 > position + -1 * pl * 8 * 1 > 0):

            #1backward 2left
            move = position + -1 * pl * 8 * 1 - 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #1backward 2right
            move = position + -1 * pl * 8 * 1 + 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

    #Bishops:
    elif(pi == 2):
        rows = (position // 8)
        cols = (position % 8)

        for i in range(1,min(8 - rows, cols + 1),1):
            move = position + pl * 8 * i - i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftForwardDiag:
        for i in range(1,min(8 - rows, 8- cols),1):
            move = position + pl * 8 * i + i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftBackwardDiag:
        for i in range(1,min(rows + 1, 8 - cols),1):
            move = position + -1 * pl * 8 * i + i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #RightBackwardDiag:

        for i in range(1,min(rows + 1, cols + 1),1):
            move = position + -1 * pl * 8 * i - i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break

    elif(pi == 3):
        #Forward:

        for i in range(1, 8 - (position // 8), 1):
            move = position + 8 * i
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Backward:
        for i in range(1, (position // 8) + 1, 1):
            move = position + 8 * i * -1
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Left:
        for i in range(1, 8 - (position % 8), 1):
            move = position + i
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Right:
        for i in range(1, position % 8 + 1, 1):
            move = position - i
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

    elif(pi == 4):
        rows = (position // 8)
        cols = (position % 8)

        for i in range(1,min(8 - rows, cols + 1),1):
            move = position + 8 * i - i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftForwardDiag:
        for i in range(1,min(8 - rows, 8- cols),1):
            move = position + 8 * i + i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftBackwardDiag:
        for i in range(1,min(rows + 1, 8 - cols),1):
            move = position + -1 * 8 * i + i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #RightBackwardDiag:

        for i in range(1,min(rows + 1, cols + 1),1):
            move = position + -1 * 8 * i - i
            if(board[move] == 0):
                legalmoves.append(move)
            elif(player(board[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break

        for i in range(1, 8 - rows, 1):
            move = position + 8 * i
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Backward:
        for i in range(1, rows + 1, 1):
            move = position + 8 * i * -1
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Left:
        for i in range(1, 8 - cols, 1):
            move = position + i
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Right:
        for i in range(1, cols + 1, 1):
            move = position - i
            if(board[move] == 0):
                legalmoves += [move]
            elif(player(board[move]) != pl):
                legalmoves += [move]
                break
            else:
                break
    if(pi==5):
        moves = [position + 8, position + 8 + 1, position + 8 - 1,
                position - 8, position - 8 + 1, position - 8 - 1,
                position + 1, position - 1
                ]
        for move in moves:
            if(move < 64 and move >= 0 and not(abs(move // 8 - position // 8) > 1 or abs(move % 8 - position % 8) > 1)):
                if(board[move] == 0 or player(board[move]) != pl):
                    legalmoves += [move]

    return(legalmoves)
def min(a,b):
    if(a<=b):
        return a
    else:
        return b
def IsPositionUnderThreat(board,position,player):
    if(player == 10):
        for i in GetPlayerPositions(board,20):
            if position in GetPieceLegalMoves(board,i):
                return(True)
    elif(player == 20):
        for i in GetPlayerPositions(board,10):
            if(position in moves):
                return(True)
    return(False)
def time(a, repetitions, *argv):
    import time
    average = 0
    for i in range(0,repetitions,10):
        start = time.process_time()
        a(*argv)
        end = time.process_time()
        average += (end - start)
    print(average/repetitions)
    return(0)
def printb(b):
    for i in range(0,8,1):
        for j in range(0,8,1):
            spacing = (3 - len(str(b[i*8+j]))) * ' '
            print(b[i*8 + j], end=spacing)
        print('')


def chess():
    import os
    board = [
    13,11,12,15,14,12,11,13,
    10,10,10,10,10,10,10,10,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    20,20,20,20,20,20,20,20,
    23,21,22,25,24,22,21,23,
    ]
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
                board[position],board[move] = board[move],board[position]
                break
            else:
                print("Invalid Move.")
                position = input('current position ')
                move = input('move to ')

        os.system('clear')
        printb(board)
        print('Valid Positions ' + str(GetPlayerPositions(board,20)))
        position = int(input('current position '))
        print('Valid Moves: ' + str(GetPieceLegalMoves(board,position)))
        move = int(input('move to '))
        while(True):
            if position in GetPlayerPositions(board,20) and move in GetPieceLegalMoves(board,position):
                board[position],board[move] = board[move],board[position]
                break
            else:
                print("Invalid Move.")
                position = input('current position ')
                move = input('move to ')

def main():


    b = [
    0, 0, 0, 0, 0, 0, 0, 0,
    8, 0, 0, 0, 0, 0, 0, 0,
    16, 0, 0, 10, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 24, 0, 23, 0, 20, 20, 20,
    0, 0, 0, 0, 0, 24, 0, 0,
    0, 22, 0, 22, 22, 22, 25, 0,
    ]
    #time(GetPlayerPositions, 10000, b, 20)
    #print(GetPieceLegalMoves(b,19))
    #print(IsPositionUnderThreat(b,19,10))
    #time(IsPositionUnderThreat, 10000, b, 19,10)
    chess()
    return(0)

main()

"""
def GetPlayerPositions(board,player):
    positions = []
    addition = 0
    for i in range(0,len(board),1):
        x = board[i]
        if(x >= player and x < player + 10):
            positions+=[i]
    return(positions) """
