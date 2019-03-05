def min(a,b):
    if(a<=b):
        return a
    else:
        return b
def max(a,b):
    if(a<=b):
        return b
    else:
        return a
def oppositepl(pl):
    if(pl == 10):
        return(20)
    elif(pl == 20):
        return(10)
    else:
        return(0)
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
def printb(b):
    for i in range(7,-1,-1):
        print(i + 1, end= '   ')
        for j in range(0,8,1):
            spacing = (3 - len(str(b[i*8+j]))) * ' '
            print(str(pieceletter(b[i*8 + j])), end=spacing)
        print('')
    print('     A   B   C   D   E   F   G   H')
def coordmap(position):
    letter = position[0]
    letter = ord(letter) - 65
    number = int(position[1]) - 1
    return(number * 8 + letter)
def lettermap(position):
    return(chr(position % 8 + 65) + str(position // 8 + 1))
def pieceletter(value):
    if(value == 0):
        return(' 0')
    returnable = ''
    b = piece(value)
    if(player(value) == 1):
        if(b == 0):
            returnable += ' \u2659 '
        elif(b == 1):
            returnable += ' \u2658 '
        elif(b == 2):
            returnable += ' \u2657 '
        elif(b == 3):
            returnable += ' \u2656 '
        elif(b == 4):
            returnable += ' \u2655 '
        elif(b == 5):
            returnable += ' \u2654 '
    elif(player(value) == -1):
        if(b == 0):
            returnable += ' \u265F '
        elif(b == 1):
            returnable += ' \u265E '
        elif(b == 2):
            returnable += ' \u265D '
        elif(b == 3):
            returnable += ' \u265C '
        elif(b == 4):
            returnable += ' \u265B '
        elif(b == 5):
            returnable += ' \u265A '



    return(returnable)
def piecescore(value):
    if(value == 0):
        return(100)
    elif(value == 1):
        return(350)
    elif(value == 2):
        return(350)
    elif(value == 3):
        return(525)
    elif(value == 4):
        return(1000)
    elif(value == 5):
        return(10000)
    else:
        return(0)
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
