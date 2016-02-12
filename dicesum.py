from random import randint

class Die:#
    def __init__(self):
        self.roll()

    def roll(self):
        self.value = randint (1,6)

    def __str__(self):
        return str(self.value)

def main():
    rolls = int(input("enter number of times to roll: "))
    die1 = Die()
    die2 = Die()
    counts = [0]*13
    for i in range(rolls):
        die1.roll()
        die2.roll()
        counts[die1.value + die2.value] += 1   #adds both rolls, goes to that position in list, and increments it's count by 1
        #counts[3] += 1
        print(counts)
    for i in range (2,13):                      #from 2 as it is the mionimum value of both dice @ 1
        print(str(i) + ": " + str(counts[i]))

main()
