#####lab 5 q5, expanded to allow user to input temp, convert it to f and give some descriptive regarding temp

def convertAllTable(c):
    ##print (c,"c = ", "%.2f" % (c*1.8+32), "f, ", "%.2f" % (c+273.15), "c, ", "%.2f" % ((c+273.15)*(1.8)), "k.") ## table output for Far,Kel & Rank, at 2 decimal places

    cToF = (c*1.8+32)
    cToK = ((c+273.15)*1.8)
    cToR = ((c+273.15)*1.8)

    cToF = str("%.2f" % cToF)
    cToK = str("%.2f" % cToK)
    cToR = str("%.2f" % cToR)
    c = str(c)

    return print (c.rjust(3),"celcius = " ,cToF.rjust(7), "F, " , cToK.rjust(7), "K, " , cToR.rjust(7), "R.")


def convertuserCtoF (userC):
    return "%.2f" % (userC*1.8+32)  ## farhenight output..


def main ():
    ##askUser = str.lower(input("Do you wish to enter a temperature to convert? Yes or No: "))
    while True:
        askUser = str.lower(input("Do you wish to enter a temperature to convert? Yes or No: "))
        if askUser == "yes":
            askUser = False
            askUser = str("yes")
            break
        elif askUser == "no":
            askUser = False
            askUser = str("no")
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
        print ("Celcius".rjust(c),"Farenheit".rjust(cToF), "Kelvin".rjust(7), "Radline".rjust(7)) #want to take local variable's length and use it as paramater for r.just(n+7)
        for c in range (-30, +60, 10):
          convertAllTable(c)



main()