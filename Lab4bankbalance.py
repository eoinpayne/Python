
def simple_interest(p, r, t): # this function calculates the simple interest of the principle after total amount of years t
    return (p + (p * r * t))

def compound_interest(p, r, t, n):  # this function calculates the compound interest after the number of years (t) times the compound periods
    return (p * ((1 + r / n)** (n*t)))

def compound_yield (p,r,t,n):
    for period in range (1, n*t+1):     #period simulating "quarter" or period that is being compounded
        p1 = simple_interest(p, r, (1/n))   # 1/n because we are caluclating the period of time. simple_interest is calculating per year, we want per period, so 1 / n (period)
        print ("period: ", period, "balance: ", "%.2f" % p1 )
        p = p1



def main():
    p = float(input("Enter principle: "))
    t = float(input("Enter years: "))
    n = float(input("Enter compound periods per year: "))

    r_input = float(input("Enter interest %: "))
    r = r_input/100


    print("")
    print("")

    print ("The simple interest new balance of your account is: ", simple_interest(p, r, t))
    print("")
    print ("The compound interest new balance of your account is: ", "%.2f" % compound_interest(p, r, t, n))
    print("")
    compound_yield (p,r,t,n)


main()