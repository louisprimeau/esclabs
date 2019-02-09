from counterlib import *
def main():

    a = 5
    x = counter(a)
    y = counter(-a)

    b = 1
    x.evolve(b)
    y.evolve(b)

    print("x should be " + str(a+b) + ", is " + str(x.getState()))
    print("y should be " + str(-a+b) + ", is " + str(y.getState()))

    return True


main()
