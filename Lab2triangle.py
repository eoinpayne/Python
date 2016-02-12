__author__ = 'D15123620'

from math import sqrt


def calc_hyp (a, o):
     h = sqrt((a**2) + (o**2))
     return h

def main ():
    a = 0
    while a <=0:
        a = float(input("Enter adjacant : "))
        if a <=0:
            print ("Please enter positive adjacent length value")

    o = 0
    while o <=0:
        o = float(input("Enter opposite: "))
        if o <=0:
            print ("Please enter a positive opposite length value")

    h = calc_hyp(a,o)
    print ("The hypotenuse of a traiangle with the adjacant length of ", a , "and the opposite length of " , o, "is = " , "%.2f" % h)

main()