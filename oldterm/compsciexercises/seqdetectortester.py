from seqdetectorlib import *

words = ["here","are","the","solutionsa","to","the","next","exam","abc","here","are","the","solutions","to","the","next","exam"]
def main():
    x = seqdetector()
    n = 0
    for i in words:
        status = x.evolve(i)
        if status == True:
            print("Detected: end position is ", n)
        n = n + 1
    return True
main()
