def min(a,b):
    if(a<=b):
        return a
    else:
        return b
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
    for i in range(0,8,1):
        print(i * 8, end= '\t')
        for j in range(0,8,1):
            spacing = (3 - len(str(b[i*8+j]))) * ' '
            print(b[i*8 + j], end=spacing)
        print('')
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
