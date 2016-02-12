#####lab 5 q5, expanded to allow user to input temp, convert it to f and give some descriptive regarding temp


def convertAllTable(c):
 ##converts c (c declared as 'for' range loop in main as an else condition, e.g else if user wishes to not input a value, default to convert range to all temps)
    cToF = (c*1.8+32)
    cToK = ((c+273.15)*1.8)
    cToR = ((c+273.15)*1.8)

 ## converting above results to a string to allow right justification of text while printing. to 2 decimal places.
    cToF = str("%.2f" % cToF)
    cToK = str("%.2f" % cToK)
    cToR = str("%.2f" % cToR)
    c = str(c)

 ## justified
    print (c.rjust(len(cToF)),"celcius = " ,cToF.rjust(7), "F, " , cToK.rjust(7), "K, " , cToR.rjust(7), "R.")
    return len(cToF)


def convertuserCtoF (userC):   ## takes user defined temperature and converts it to farenheit
    return "%.2f" % (userC*1.8+32)  ## farhenight output..


def main ():
    ## while true loop used to continue asking a question until desired "boxed in" result is achieved
    while True:
        askUser = str.lower(input("Do you wish to enter a temperature to convert? Yes or No: "))  ##forces lower case so as conditions below can match easily
        if askUser == "yes":
            #askUser = False  ## if user response is yes, variable is then defined as false
            #askUser = str("yes")
            break
        elif askUser == "no":
            #askUser = False
            #askUser = str("no")
            break
        else:
            askUser = True
            print ("Please enter 'yes' or 'no' when prompted")


    if askUser == "yes":
        print()
        userC = float(input("What temp?: "))
        print()
        print (userC, "C in F is", convertuserCtoF(userC))
        if userC <=-20:
            print ("Arctic")
        elif userC >-20 and userC <= -10:
            print ("Baltic")
        elif userC >-10 and userC <= 2:
            print ("Freezing")
        elif userC >2 and userC <= 10:
            print ("Chilly")
        elif userC >10 and userC <= 20:
            print ("Not bad")
        elif userC >20:
            print ("Great Irish summer")
        else:
            print ("wonder where you live?")

    elif askUser == "no":
        print()
        print ("Celcius".rjust(convertAllTable()),"Farenheit".rjust(6), "Kelvin".rjust(7), "Radline".rjust(7)) ###want to take local variable's length and use it as paramater for r.just(n+7)

        for c in range (-30, +60, 10):
            convertAllTable(c)



main()



'''
def celcius_to_faren (c):
    return "%.2f" % (c*9/5+32)  ## farhenight output..

def celcius_to_kelvin (c):
    return "%.2f" % (c+273.15)

def celcius_to_rank (c):
    return "%.2f" % ((c+273.15)*(9/5))



def main ():
    for c in range (-30, +60, 10):
        print (c , "degrees = ", celcius_to_faren(c),"f, ",celcius_to_kelvin(c), "k, ", celcius_to_rank(c), "r.")



main()
'''

'''      ### MUCH SIMPLER WAY OF DOING IT
for c in range (-30, 0, 10):
    f = c * 9/5 + 32
    k = c + 273.15
    r = (k * (9/5))
    print(c , "celcius = ", "%.2f" % f, "f,", "%.2f" % k, "k,", "%.2f" % r, "r,")

for c in range (0, 61, 10):
    f = c * 9/5 + 32
    k = c + 273.15
    r = k * (9/5)
    print(c , " celcius = ", "%.2f" % f, "f,", "%.2f" % k, "k,", "%.2f" % r, "r,")
    '''





''' ## another way to do the above, this time
def conversion(c):
    print (c,"c = ", "%.2f" % (c*9/5+32), "f, ", "%.2f" % (c+273.15), "c, ", "%.2f" % ((c+273.15)*(9/5)), "k.")


def main ():
    for c in range (-30, +60, 10):
        conversion(c)
        #print (c , "degrees = ", celcius_to_faren(c),"f, ",celcius_to_kelvin(c), "k, ", celcius_to_rank(c), "r.")



main()

'''

