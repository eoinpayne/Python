##page 35 6.24

from cmath import *


'''def quadratic (num1, num2, num 3):
    quad = (num1 x**2 + bx + c)
    return quad '''

def calcDiscriminator (a, b, c):
    discriminator = (b**2) - (4*a*c)

    sol1 = (-b - sqrt(discriminator)) / (2*a)
    sol2 = (-b + sqrt(discriminator)) / (2*a)

    print ("discriminator = ", discriminator)

    if discriminator < 0:

         print (complex(sol1), complex(sol2))
    elif discriminator > 0:
        print(sol1, sol2)

    elif discriminator == 0: ## then go with the real one? try to find which of the 2 roots is real to use that, query how to do this mathematically.
        None




def main():
    a = int(input(" Enter number 1: "))
    b = int(input(" Enter number 2: "))
    c = int(input(" Enter number 3: "))

    '''
    discriminator = calcDiscriminator (a, b, c)

    print ("discriminator = ", int(discriminator))
    print()
    '''
    #discriminator = calcDiscriminator (a, b, c)

'''
    if discriminator > 0:
        print ("2 real")
    elif discriminator == 0:
        print ("1 real, 1 complex")
    else:
        print ("2 complex")
'''
    #calcDiscriminator (a, b, c)

main()