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