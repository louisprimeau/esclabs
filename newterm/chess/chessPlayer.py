from chessHelper import *

def GetPlayerPositions(board,player):
    return([i for i,x in enumerate(board) if(x >= player and x < player + 10)])
def GetPieceLegalMoves(board,position):
    value = board[position]
    legalmoves = []
    pl = player(value)
    pi = piece(value)
    #Pawns:
    if(pi == 0):

        # CHECK DIRECTLY IN FRONT
        move = position + pl * 8
        if(board[move] == 0 and move >= 0 and move < 64):
            legalmoves.append(move)

        # CHECK TO LEFT
        c = board[move - 1]
        a = player(c)
        if(c != 0 and a != pl and a != 0 and (-10 < (position - (move - 1) < 10))):
            legalmoves.append(move - 1)

        # CHECK TO RIGHT
        c = board[move + 1]
        a = player(c)
        if((c != 0) and a != pl and a != 0 and (-10 < (position - (move + 1) < 10))):
            legalmoves.append(move + 1)

    #Knights:
    elif(pi == 1):

        #Forward:
        # pl (forwards/backwards) * 8 (length of row) * 2 (number of rows)
        if(64 > position + 8 * 2 > 0):

            #2forward 1left:
            move = position + 8 * 2 - 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #2forward 1right:
            move = position + 8 * 2 + 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        if(64 > position + 8 * 1 > 0):

            #1forward 2left
            move = position + 8 * 1 - 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #1forward 2right
            move = position + 8 * 1 + 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        #Backward:

        # pl (forwards/backwards) * 8 (length of row) * 2 (number of rows)
        if(64 > position + -1 * 8 * 2 > 0):

            #2backward 1left:
            move = position + -1 * 8 * 2 - 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #2backward 1right:
            move = position + -1 * 8 * 2 + 1
            if(abs(move % 8 - position % 8) == 1):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        if(64 > position + -1 * 8 * 1 > 0):

            #1backward 2left
            move = position + -1 * 8 * 1 - 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #1backward 2right
            move = position + -1 * 8 * 1 + 2
            if(abs(move % 8 - position % 8) == 2):
                c = board[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

    #Bishops:
    elif(pi == 2):
        rows = (position // 8)
        cols = (position % 8)
        #RightForwardDiag
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
def score(b,pl):

    wpawn = [0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -25, -25, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 25, 25, 0, 0, 0,
    5, 5, 10, 27, 27, 10, 5, 5, 10, 10, 20, 30, 30, 20, 10, 10, 50, 50, 50, 50, 50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0]
    wknight = [-50, -40, -20, -30, -30, -20, -40, -50, -40, -20, 0, 5, 5, 0, -20, -40,-30, 5, 10, 15, 15, 10, 5, -30,-30, 0, 15, 20, 20, 15, 0, -30,-30, 5, 15, 20, 20, 15, 5, -30,-30, 0, 10, 15, 15, 10, 0, -30,-40, -20, 0, 0, 0, 0, -20, -40,-50, -40, -30, -30, -30, -30, -40, -50]
    wbishop = [ -20, -10, -40, -10, -10, -40, -10, -20, -10, 5, 0, 0, 0, 0, 5, -10,-10, 10, 10, 10, 10, 10, 10, -10,-10, 0, 10, 10, 10, 10, 0, -10, -10, 5, 5, 10, 10, 5, 5, -10,-10, 0, 5, 10, 10, 5, 0, -10,-10, 0, 0, 0, 0, 0, 0, -10,20, -10, -10, -10, -10, -10, -10, -20]
    wking = [20, 30, 10, 0, 0, 10, 30, 20,20, 20, 0, 0, 0, 0, 20, 20,-30, -40, -40, -50, -50, -40, -40, -30,-30, -40, -40, -50, -50, -40, -40, -30,-30, -40, -40, -50, -50, -40, -40, -30,-30, -40, -40, -50, -50, -40, -40, -30,-10, -20, -20, -20, -20, -20, -20, -10,-20, -30, -30, -40, -40, -30, -30, -20]


    bpawn = [0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 20, 30, 30, 20, 10, 10, 5, 5, 10, 27, 27, 10, 5, 5, 0, 0, 0, 25, 25, 0, 0, 0, 5, -5, -10, 0, 0, -10, -5, 5, 5, 10, 10, -25, -25, 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0]
    bknight = [-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 0, 0, 0, -20, -40, -30, 0, 10, 15, 15, 10, 0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5, 10, 15, 15, 10, 5, -30, -40, -20, 0, 5, 5, 0, -20, -40, -50, -40, -20, -30, -30, -20, -40, -50]
    bbishop = [-20, -10, -10, -10, -10, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 10, 10, 5, 0, -10, -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 10, 10, 10, 10, 10, 10, -10, -10, 5, 0, 0, 0, 0, 5, -10, -20, -10, -40, -10, -10, -40, -10, -20]
    bking = [-30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -20, -30, -30, -40, -40, -30, -30, -20, -10, -20, -20, -20, -20, -20, -20, -10, 20, 20, 0, 0, 0, 0, 20, 20, 20, 30, 10, 0, 0, 10, 30, 20]

    score = 0
    a = 0
    if(pl == 10):
        a = 1
    elif(pl == 20):
        a = -1
    for i in range(0,64,1):
        if(b[i] != 0):
            pie = piece(b[i])
            pla = player(b[i])
            if(pie == 0):
                if(pla == 1):
                    score += 100 + wpawn[i] * 0.4
                elif(pla == -1):
                    score += 100 * -1 + bpawn[i] * -1 * 0.4
            elif(pie == 1):
                if(pla == 1):
                    score += 350 + wknight[i] * 0.4
                elif(pla == -1):
                    score += 350 * -1 + bknight[i] * -1 * 0.4
            elif(pie == 2):
                if(pla == 1):
                    score += 350 + wbishop[i] * 0.4
                elif(pla == -1):
                    score += 350 * -1 + bbishop[i] * -1 * 0.4
            elif(pie == 3):
                score += 525 * pla * a
            elif(pie == 4):
                score += 1000 * pla * a
            elif(pie == 5):
                if(pla == 1):
                    score += 10000 + wking[i] * 0.4
                elif(pla == -1):
                    score += 10000 * -1 + bking[i] * -1 * 0.4

    return(score * a)
def move(b,position,newmove):
    bnew = list(b)
    bnew[position],bnew[newmove] = 0,bnew[position]
    return(bnew)
def search(b,pl,depth):

    newmove = [-1,-1]

    moves = getmoves(b,pl)
    moves.sort(key = lambda x: x[2], reverse = True)
    moves = moves[0:3] #Pick 7 best moves.


    if(depth > 1):
        for i in range(0,len(moves),1):
            newboard = move(b,moves[i][0],moves[i][1])
            moves[i].append(search(newboard, oppositepl(pl),depth-1))
            moves[i][2] = -maxscore(moves[i][3])
    return(moves)
def levelorder(t):
    for i in t:
        print(i[0:3])
def maxscore(t):
    score = t[0][2]
    for i in range(0,len(t),1):
        if(t[i][2] > score):
            score = t[i][2]
    return(score)
def maxscoremove(t):
    score = t[0][2]
    move = t[0][0:2]
    for i in range(1,len(t),1):
        if(t[i][2] > score):
            score = t[i][2]
            move = t[i][0:2]
    return(move)
def getmoves(b, pl):
    moves = []
    for i in GetPlayerPositions(b,pl):
        for j in GetPieceLegalMoves(b,i):
            moves.append([i,j,score(move(b,i,j),pl)])
    return(moves)
def treeprint(t,depth):
    print(t[0:3])
    if(len(t) > 3):
        for i in t[3]:
            for j in range(0,depth,1):
                print('\t',end='')
            treeprint(i,depth+1)
    return(0)
def forestprint(t):
    for i in t:
        treeprint(i,1)
def standardboard():
    return([
13,11,12,15,14,12,11,13,
10,10,10,10,10,10,10,10,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0,
20,20,20,20,20,20,20,20,
23,21,22,25,24,22,21,23,
])
#t = search(board,10,4)
#time(search,100,board,10,4)

def chessPlayer(b,pl):
    candidateMoves = [a[0:2] for a in getmoves(b,pl)]
    move = search(b,pl,4)
    print(move)
    levelorder(move)
    #evalTree = levelorder(move)
    move = maxscoremove(move)
    return([True, move, candidateMoves, 1])


#time(chessPlayer,1,standardboard(),10)
#print(chessPlayer(standardboard(),10))
#forestprint(t)
