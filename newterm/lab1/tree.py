class tree:
    def __init__(self,x):
        self.store = [x,[]]
    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True
    def printsubshell(self,depth):
        print(self.store[0])
        for i in self.store[1]:
            for j in range(0,depth+1,1):
                print('\t', end='')
            i.printsubshell(depth+1)
    def Print_DepthFirst(self):
        self.printsubshell(0)
        return(True)
    def Get_LevelOrder(self):
        lvlorder = []
        q = queue()
        q.enqueue(self)
        while(q.nonempty()):
            a = q.dequeue()
            for i in a.store[1]:
                q.enqueue(i)
            lvlorder += [a]
        for i in range(0,len(lvlorder),1):
            lvlorder[i] = lvlorder[i].store[0]
        return(lvlorder)
    def listConv(self,A):
        from binary_tree import binary_tree
        B = A[-1].ConvertToBinaryTree()
        for i in reversed(A[:-1]):
            storage = i.ConvertToBinaryTree()
            storage.AddRight(B)
            B = storage
        return(B)
    def ConvertToBinaryTree(self):
        from binary_tree import binary_tree
        if(len(self.store[1]) == 0):
            return(binary_tree(self.store[0]))
        A = binary_tree(self.store[0])
        A.AddLeft(self.store[1][0].ConvertToBinaryTree())
        A.store[1].AddRight(self.listConv(self.store[1][1:]))
        return(A)

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

#print(a.Get_LevelOrder())
