def piece(value):
    if(value < 20):
        return(value - 10)
    elif(value >= 20):
        return(value - 20)
def player(value):
    if(value >= 20):
        return(-1)
    elif(value >= 10):
        return(1)
    else:
        return(0)
def convertToBitBoard(b):
    bitboard = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,64,1):
        pi = piece(b[i])
        pl = player(b[i])
        if(pi == 0 and pl == 1):
            bitboard[0] += 2**i
        elif(pi == 1 and pl == 1):
            bitboard[1] += 2**i
        elif(pi == 2 and pl == 1):
            bitboard[2] += 2**i
        elif(pi == 3 and pl == 1):
            bitboard[3] += 2**i
        elif(pi == 4 and pl == 1):
            bitboard[4] += 2**i
        elif(pi == 5 and pl == 1):
            bitboard[5] += 2**i
        elif(pi == 0 and pl == -1):
            bitboard[6] += 2**i
        elif(pi == 1 and pl == -1):
            bitboard[7] += 2**i
        elif(pi == 2 and pl == -1):
            bitboard[8] += 2**i
        elif(pi == 3 and pl == -1):
            bitboard[9] += 2**i
        elif(pi == 4 and pl == -1):
            bitboard[10] += 2**i
        elif(pi == 5 and pl == -1):
            bitboard[11] += 2**i
    return(bitboard)
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
convertToBitBoard(board)
time(convertToBitBoard,10000,board)
