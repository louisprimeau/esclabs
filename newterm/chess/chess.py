
def GetPlayerPositions(board,player):
    return([i for i,x in enumerate(board) if(x >= player and x < player + 10)])

"""
def GetPlayerPositions(board,player):
    positions = []
    addition = 0
    for i in range(0,len(board),1):
        x = board[i]
        if(x >= player and x < player + 10):
            positions+=[i]
    return(positions) """

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
            legalmoves += [position + pl * 8]

        # CHECK TO LEFT
        c = board[position + pl * 8 - 1]
        a = player(c)
        if(c != 0 and a != pl and a != 0):
            legalmoves += [position + pl * 8 - 1]

        # CHECK TO RIGHT
        c = board[position + pl * 8 + 1]
        a = player(c)
        if((c != 0) and a != pl and a != 0):
            legalmoves += [position + pl * 8 + 1]


    return(legalmoves)



def time(a, repetitions, *argv):
    import time
    average = 0
    for i in range(0,repetitions,10):
        start = time.process_time()
        a(*argv)
        end = time.process_time()
        average += (start-end)
    print(average/repetitions)
    return(0)



def main():
    b = [
    13,11,12,15,14,12,11,13,
    10,10,10,10,10,10,10,10,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 10, 0, 10, 0, 0,
    20,20,20,20,20,20,20,20,
    23,21,22,25,24,22,21,23,
    ]
    time(GetPlayerPositions, 10000, b, 20)
    time(GetPieceLegalMoves,10000,b,52)

    time(player,100000, 23)
    return(0)

main()
