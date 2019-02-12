import random
class conway:
    def __init__(self,numlists,lenlists,filler):
        self.store = []
        for i in range(0,numlists,1):
            temp = []
            for j in range(0,lenlists,1):
                if(filler == 'zeros'):
                    temp = temp + [0]
                elif(filler == 'random'):
                    temp = temp + [random.randint(0,1)]
            self.store = self.store + [temp]
    def getDisp(self):
        returnstring = ""
        for i in self.store:
            for j in i:
                if(j == 0):
                    returnstring += " "
                elif(j == 1):
                    returnstring += "*"
            returnstring += "\n"
        return(returnstring[0:len(returnstring)-2])
    def printDisp(self):
        print(self.getDisp())
        return(True)
    def setPos(self,row,col,val):
        if not((val == 0) or (val == 1)):
            return(False)
        self.store[row][col] = val
        return(True)
    def getNeighbors(self,row,col):
        newrow = row + len(self.store) 
        newcol = col + len(self.store[0])
        newstore = list(self.store)
        for i in range(0,len(newstore),1):
            newstore[i] = newstore[i] + newstore[i] + newstore[i]
        newstore = newstore + newstore + newstore
        numbers = []
        numbers += [newstore[newrow-1][newcol-1]]
        numbers += [newstore[newrow-1][newcol]]
        numbers += [newstore[newrow-1][newcol+1]]
        numbers += [newstore[newrow][newcol-1]]
        numbers += [newstore[newrow][newcol+1]]
        numbers += [newstore[newrow+1][newcol-1]]
        numbers += [newstore[newrow+1][newcol]]
        numbers += [newstore[newrow+1][newcol+1]]
        return numbers
                                
