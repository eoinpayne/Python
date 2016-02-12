## q 3.15 page 18   & page 35 q 6.25

def calcMaxBpm (y):  #calculates max bpm based on input age.
    max_bpm = (208 - (0.7*y))
    return max_bpm

def zone(age, rate, max_bpm):
    if rate >= (.90*max_bpm):
        print ("interval training")
    elif (.70*max_bpm) <= rate <(.90*max_bpm) :
        print("threshold")
    elif (.50*max_bpm) <= rate <(.70*max_bpm) :
        print("aerobic")
    elif rate < (.50*max_bpm):
        print ("couch potato")


def main ():
    age = float(input("what is your age in years?: "))
    rate = float(input("what is your training heart rate?: "))

    max_bpm = calcMaxBpm (float(age))
    print (max_bpm)

    zone(age,rate, max_bpm)


main()