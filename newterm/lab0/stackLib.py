class stack:
    def __init__(self):
        self.a = []
    def push(self, input):
        self.a += [input]
    def pop(self):
        hold = self.a[len(self.a) - 1]
        self.a = self.a[:-1]
        return(hold)
