

def myfactorial(n):
    total = 1
    factorial_result = 0
    for i in range (1, n+1):
        #print ("total = ", total, "i currently at = ",i, "factorial =  ", total * n)
        factorial_result = total * i
        total = factorial_result
        print ("{0}{1:>2}  {2}{3:^20}  {4}{5:>4}     {6}{7:>4}".format("at n = ", i, "factorial = ", factorial_result, "i**n = ", i**2, "2*n = ",2*i))






def main():
    n = 20
    myfactorial(n)

main()

