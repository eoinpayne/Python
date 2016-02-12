
def triangular(n):
    total = 0
    for i in range (1, n+1):
        #print ("total", total, "+ i", i, " = ", total+i)
        print ( "{0:4>} {1:4>} {2:4>} {3:4>} = {4:4>}".format("(total)", total, "+ (i)", i, total+i))
        total += i

#def triangular_table():


def main():
    n = 20
    triangular(n)

main()
