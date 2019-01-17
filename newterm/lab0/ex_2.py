class stack:
    def __init__(self):
        self.a = []
    def push(self, input):
        self.a += [input]
    def pop(self):
        hold = self.a[len(self.a) - 1]
        self.a = self.a[:-1]
        return(hold)


stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())
