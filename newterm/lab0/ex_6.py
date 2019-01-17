class stack:
    def __init__(self):
        self.stack = []
    def push(a):
        self.stack += [a]
    def pop():
        a = self.stack[len(self.stack)]
        self.stack = self.stack[:-1]
        return(a)

class queue:
    def __init__(self):
        self.queue = []
    def enqueue(a):
        self.stack += [a]
    def dequeue():
        a = self.stack[0]
        self.stack = self.stack[1:]
        return(a)

def traverse_breadth(T):
     x=Queue()
     x.enqueue(T)
     while x.empty() == False:
          r=x.dequeue()
          print(r[0])
          for i in r[1:len(r)]:
               x.enqueue(i)


def traverse_depth(T):
    x=Stack()
    x.pushs(T)
    while x.empty() == False:
    r=x.pop()
        print(r[0])
        for i in r[1:len(r)]:
            x.push(i)
