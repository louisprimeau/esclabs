class Counter:
    def __init__(self,incr,ctr):
        self.Incr = incr
        self.Ctr = ctr
    def setIncr(self, arg):
        self.Incr = arg
        return(True)
    def setCtr(self, arg):
        self.Ctr = arg
        return(True)
    def evolve(self, type):
        if(type == 0):
            self.Ctr += self.Incr
        elif(type == 1):
            self.Ctr *= self.Incr
        elif(type == -1):
            self.Ctr -= self.Incr
        else:
            return(False)
        return(True)
    def get(self):
        return(self.Ctr)
