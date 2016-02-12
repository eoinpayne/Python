

def convert_temp(c):
    fromCtoF = ((c * (9/5)) +32)
    fromCtoK = (c + 273.15)
    fromCtoR = (fromCtoK * (9/5))



    #print(fromCtoF, fromCtoK, fromCtoR)

    return fromCtoF, fromCtoK, fromCtoR


def temp_table():
    print ("Temperature Conversions".center(50))
    print("Celcius \t".rjust(2), "Farenheight".rjust(13),"\t" , "Kelvin".rjust(10), "Rankline".rjust(11))
    for c in range (-30, 60, 10):
        fromCtoF, fromCtoK, fromCtoR = convert_temp(c)
        fromCtoF = str("%.2f" % fromCtoF)
        fromCtoK = str("%.2f" % fromCtoK)
        fromCtoR = str("%.2f" % fromCtoR)
        c = str(c)
        #if c == 0:
            #print(c,"c =  \t\t", fromCtoF,"F =  \t\t" , fromCtoK, "K =  \t\t", fromCtoR, "R")
        #else:
        print(c.rjust(3),"c  =  \t", fromCtoF.rjust(11),"F\t" , fromCtoK.rjust(8), "K\t", fromCtoR.rjust(8), "R")



    # for c in range (-30, 60, 10):
    #     fromCtoF, fromCtoK, fromCtoR = convert_temp(c)
    #     fromCtoF = str(round(fromCtoF, 1))
    #     fromCtoK = str(round(fromCtoK, 3))
    #     fromCtoR = str(round(fromCtoR, 8))
    #     print(c,"c =  \t", fromCtoF.rjust(5),"F =  \t" , fromCtoK.rjust(5), "K =  \t", fromCtoR.rjust(5), "R")

        #print(c,"c =  \t", (str(round(fromCtoF, 4)).rjust) , "F =  \t" , str(round(fromCtoK, 4)), "K =  \t", str(round(fromCtoR, 4)), "R")

def main ():
    temp_table()

main()

