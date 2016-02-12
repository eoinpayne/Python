from math import log

def main():
    n = 0
    for n in range (10, 201, 10):
        #print ("n = ", str(n.rjust(4)), ", log(n) = ", str(log(n).rjust(4)), ", n*log(n) = ", str((n*log(n)).rjust(4)), "n**2", str((n**2).rjust(4)), "2**n", str((2**n).rjust(4)))
        print (("n = {0:^8.2f} | log({0}) = {1:^8.2f} | {0}*log({0}) =  {2:^8.2f} | {0}**2  = {3:^8.2f} | 2**{0} = {4:^2.2f}" ).format( n,(log(n)), (n*log(n)), (n**2), (2**n) ))
main()







