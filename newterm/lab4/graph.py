def flatten(d):
    flat = []
    if(type(d) != list):
        return([d])
    for i in d:
        flat += flatten(i)
    return(flat)

class graph:
    def __init__(self):
        self.store = []
        self.addVertexC = 0
    def print(self):
        for i in self.store:
            print(i)
        return(True)
    def addVertex(self,n):
        if(n < 1): return(-1)
        a = len(self.store)
        self.store += [[0]*a] * n
        self.store = [s + [0]*n for s in self.store]
        self.addVertexC += 1
        return(self.addVertexC)
    def addEdge(self,from_idx,to_idx,directed,weight):
        if((weight == 0) or (from_idx > len(self.store)) or (to_idx > len(self.store)) or (type(directed) != type(True))): return False
        self.store[from_idx][to_idx], self.store[to_idx][from_idx] = weight, weight*(not directed)
        return(True)
    def traverse(self,start,typeBreadth):
        c = [] if start == None else [start]
        d,p = [],[]
        if(start != None):
            while(len(c) != 0):
                w = c.pop(0)
                if (w not in p):
                    p += [w]
                for i in range(0,len(self.store[w]),1):
                    if(self.store[w][i] != 0):
                        if (i not in d):
                            c = c + [i] if(typeBreadth) else [i] + c
                            d += [i]
        else:
            for i in range(0,len(self.store),1):
                if(i not in flatten(d)):
                    d += [[i]]
                    p += [[]]
                    c += [i]
                while(len(c) != 0):
                    w = c.pop(0)
                    if (w not in flatten(p)):
                        p[len(p)-1] += [w]
                    for i in range(0,len(self.store[w]),1):
                        if(self.store[w][i] != 0):
                            if (i not in d):
                                c = c + [i] if(typeBreadth) else [i] + c
                                d += [i]
        return(p)
    def connectivity(self,vx,vy):
        a = [False, False]
        if(vx in self.traverse(vy,True)): a[1] = True
        if(vy in self.traverse(vx,True)): a[0] = True
        return(a)
    def forwardpath(self,vx,vy,visited,depth):
        if(self.connectivity(vx,vy)[0] == False):
            return([])
        t = [vx]
        visited += [vx]
        if(vx == vy):
            return([vx])
        for i in range(0,len(self.store[vx]),1):
            if(self.store[vx][i] != 0 and i not in visited):
                a = self.forwardpath(i,vy,visited,depth+1)
                if(vy in a): t += a
        return(t)
    def path(self,vx,vy):
        return([self.forwardpath(vx,vy,[],0),self.forwardpath(vy,vx,[],0)])
