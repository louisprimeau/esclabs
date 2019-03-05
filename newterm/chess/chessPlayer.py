from chessHelper import *

def GetPlayerPositions(b,pl):
    return([i for i,x in enumerate(b) if(x >= pl and x < pl + 10)])
def GetPieceLegalMoves(b,position):
    value = b[position]
    legalmoves = []
    pl = player(value)
    pi = piece(value)
    #Pawns:
    if(pi == 0):

        # CHECK DIRECTLY IN FRONT
        move = position + pl * 8
        if(move >= 0 and move < 64 and b[move] == 0):
            legalmoves.append(move)

        # CHECK TO LEFT
        if(0 <= move-1 <64):
            c = b[move - 1]
            a = player(c)
            if(c != 0 and a != pl and a != 0 and (-10 < (position - (move - 1) < 10))):
                legalmoves.append(move - 1)

        # CHECK TO RIGHT
        if(0 <= move+1 <64):
            c = b[move + 1]
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
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #2forward 1right:
            move = position + 8 * 2 + 1
            if(abs(move % 8 - position % 8) == 1):
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        if(64 > position + 8 * 1 > 0):

            #1forward 2left
            move = position + 8 * 1 - 2
            if(abs(move % 8 - position % 8) == 2):
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #1forward 2right
            move = position + 8 * 1 + 2
            if(abs(move % 8 - position % 8) == 2):
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        #Backward:

        # pl (forwards/backwards) * 8 (length of row) * 2 (number of rows)
        if(64 > position + -1 * 8 * 2 > 0):

            #2backward 1left:
            move = position + -1 * 8 * 2 - 1
            if(abs(move % 8 - position % 8) == 1):
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #2backward 1right:
            move = position + -1 * 8 * 2 + 1
            if(abs(move % 8 - position % 8) == 1):
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

        if(64 > position + -1 * 8 * 1 > 0):

            #1backward 2left
            move = position + -1 * 8 + 2
            if(abs(move % 8 - position % 8) == 2):
                c = b[move]
                a = player(c)
                if(a != pl):
                    legalmoves.append(move)

            #1backward 2right
            move = position + -1 * 8 - 2
            if(abs(move % 8 - position % 8) == 2):
                c = b[move]
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
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftForwardDiag:
        for i in range(1,min(8 - rows, 8- cols),1):

            move = position + 8 * i + i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftBackwardDiag:
        for i in range(1,min(rows + 1, 8 - cols),1):
            move = position + -1 * 8 * i + i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #RightBackwardDiag:

        for i in range(1,min(rows + 1, cols + 1),1):
            move = position + -1 * 8 * i - i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break

    elif(pi == 3):
        #Forward:

        for i in range(1, 8 - (position // 8), 1):
            move = position + 8 * i
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Backward:
        for i in range(1, (position // 8) + 1, 1):
            move = position + 8 * i * -1
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Left:
        for i in range(1, 8 - (position % 8), 1):
            move = position + i
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Right:
        for i in range(1, position % 8 + 1, 1):
            move = position - i
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

    elif(pi == 4):
        rows = (position // 8)
        cols = (position % 8)

        for i in range(1,min(8 - rows, cols + 1),1):
            move = position + 8 * i - i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftForwardDiag:
        for i in range(1,min(8 - rows, 8- cols),1):
            move = position + 8 * i + i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #LeftBackwardDiag:
        for i in range(1,min(rows + 1, 8 - cols),1):
            move = position + -1 * 8 * i + i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break
        #RightBackwardDiag:

        for i in range(1,min(rows + 1, cols + 1),1):
            move = position + -1 * 8 * i - i
            if(b[move] == 0):
                legalmoves.append(move)
            elif(player(b[move]) != pl):
                legalmoves.append(move)
                break
            else:
                break

        for i in range(1, 8 - rows, 1):
            move = position + 8 * i
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Backward:
        for i in range(1, rows + 1, 1):
            move = position + 8 * i * -1
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Left:
        for i in range(1, 8 - cols, 1):
            move = position + i
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break

        #Right:
        for i in range(1, cols + 1, 1):
            move = position - i
            if(b[move] == 0):
                legalmoves += [move]
            elif(player(b[move]) != pl):
                legalmoves += [move]
                break
            else:
                break
    elif(pi==5):
        moves = [position + 8, position + 8 + 1, position + 8 - 1,
                position - 8, position - 8 + 1, position - 8 - 1,
                position + 1, position - 1
                ]
        for move in moves:
            if(move < 64 and move >= 0 and not(abs(move // 8 - position // 8) > 1 or abs(move % 8 - position % 8) > 1)):
                if(b[move] == 0 or player(b[move]) != pl):
                    legalmoves += [move]

    return(legalmoves)
def IsPositionUnderThreat(b,position,pl):
    if(pl == 10):
        for i in GetPlayerPositions(b,20):
            if position in GetPieceLegalMoves(b,i):
                return(True)
    elif(pl == 20):
        for i in GetPlayerPositions(b,10):
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


    bpawn = [0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 27, 27, 10, 5, 5,
    0, 0, 0, 25, 25, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 10, 10, -25, -25, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]
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
def boardmove(b,position,newmove):
    bnew = list(b)
    bnew[position],bnew[newmove] = 0,bnew[position]
    return(bnew)
def isKingUnderThreat(b,pl):
    king = b.index(pl + 5)
    for i in GetPlayerPositions(b,pl):
        for j in GetPieceLegalMoves(b,i):
            if j == king:
                return(True)
    return(False)
def levelorder(t):
    traversal = []
    q = []
    for i in t:
        q.append(i)
    counter = 5
    while(len(q) != 0):
        pop = q.pop(0)
        traversal.append(pop[0:3])
        if(counter < 5 + 5**2):
            if(len(pop) > 3):
                for i in pop[3]:
                    q.append(i)
                    counter += 1
    return(traversal)
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
            moves.append([i,j,score(boardmove(b,i,j),pl)])
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

"""def chessPlayer(b,pl):
    #DEPTH = Number of moves looked ahead; must be an even number.
    depth = 6
    candidateMoves = [[a[0:2], a[2]] for a in getmoves(b,pl)]
    move = search(b,pl,depth)
    tree = levelorder(move)
    move = maxscoremove(move)
    return([True, move, candidateMoves, tree]) """

def search(b,pl,depth):

    moves = getmoves(b,pl)
    moves.sort(key = lambda x: x[2], reverse = True)
    moves = moves[0:5] #Pick 5 best moves.

    if(depth > 1):
        for i in range(0,len(moves),1):
            newboard = boardmove(b,moves[i][0],moves[i][1])
            moves[i].append(search(newboard, oppositepl(pl),depth-1))
            moves[i][2] = -maxscore(moves[i][3])
    return(moves)

def chessPlayer2(b,pl):
    candidateMoves = [[a[0:2], a[2]] for a in getmoves(b,pl)]
    move = alphabetaroot(b,pl)[0:2]
    tree = levelorder(search(b,pl,2))
    return([True,move,candidateMoves,tree])


def alphabetaroot(b,pl):
    move = alphabetasearch(b,pl,-100000,100000,7)
    return(move)
def alphabetasearch(b,pl,alpha,beta,depth):

    moves = getmoves(b,pl)
    moves.sort(key = lambda x: x[2], reverse = True)
    moves = moves[0:5]

    bestscore = -100000
    bestmove = []

    for move in moves:
        bnew = boardmove(b,move[0],move[1])
        if(depth == 0):
            movescore = score(bnew,pl)
        else:
            movescore = -(alphabetasearch(bnew, oppositepl(pl), -beta, -alpha, depth-1)[2])
        if(movescore > bestscore): bestscore,bestmove = movescore,move
        if(bestscore > alpha): alpha = bestscore
        if(alpha >= beta): return([bestmove[0], bestmove[1], alpha])

    return([bestmove[0], bestmove[1], bestscore])
