class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, a):
        self.queue += [a]
    def dequeue(self):
        a = self.queue[0]
        self.queue = self.queue[1:]
        return(a)
    def nonempty(self):
        return(bool(len(self.queue)))

class binary_tree:
    def __init__(self,x):
        self.store = [x,None,None]
    def AddRight(self,x):
        self.store[2] = x
        return True
    def AddLeft(self,x):
        self.store[1] = x
        return True
    def printsubshell(self,depth):
        print(self.store[0])
        for i in self.store[1:]:
            #if(i != None):
            for j in range(0,depth+1,1):
                print('\t', end='')
            if(i!=None):
                i.printsubshell(depth+1)
            else:
                print('None')
    def Print_DepthFirst(self):
        self.printsubshell(0)
        return(True)
    def Get_LevelOrder(self):
        lvlorder = []
        q = queue()
        q.enqueue(self)
        while(q.nonempty()):
            a = q.dequeue()
            for i in a.store[1:]:
                if(i != None):
                    q.enqueue(i)
            lvlorder += [a]
        for i in range(0,len(lvlorder),1):
            lvlorder[i] = lvlorder[i].store[0]
        return(lvlorder)
    def ConvertToTree(self):
        from tree import tree
        if((self.store[1] == None) and (self.store[2] == None)):
            return(tree(self.store[0]))
        A = tree(self.store[0])
        if(self.store[1]!=None):
            A.AddSuccessor(self.store[1].ConvertToTree())
            B = self.store[1]
            while(B.store[2] != None):
                A.AddSuccessor(B.store[2].ConvertToTree())
                B = B.store[2]

        return(A)
