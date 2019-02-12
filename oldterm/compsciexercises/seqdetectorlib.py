class seqdetector:
    def __init__(self):
        self.state = "NULL"
    def evolve(self,word):
        unlocked = False
        if(self.state == "NULL" and word == "here"):
            self.state = "HERE"
        elif(self.state == "HERE" and word == "are"):
            self.state = "ARE"
        elif(self.state == "ARE" and word == "the"):
            self.state = "THE"
        elif(self.state == "THE" and word == "solutions"):
            self.state = "SOLUTIONS"
        elif(self.state == "SOLUTIONS" and word == "to"):
            self.state = "TO"
        elif(self.state == "TO" and word == "the"):
            self.state = "THE"
        elif(self.state == "THE" and word == "next"):
            self.state = "NEXT"
        elif(self.state == "NEXT" and word == "exam"):
            self.state = "NULL"
            unlocked = True
        else:
            self.state = "NULL"
        return(unlocked)
