from random import randint

class Die:
    def __init__(self):
        self.roll()

    def roll(self):
        self.value = randint(1,6)

    def __str__(self):
        return str(self.value)

class Dice:
    def __init__(self, n=3): # default will be 3, unless specified as a parameter
        self.dice = [Die() for i in range(n)]  #dice is the object die * n

    def rollall(self):
        for die in self.dice:
            die.roll()

    def values(self):
        return map(int, self.dice)

    def __str__(self):
        return str(self.values())

def main():
    #test
    dice = Dice(5)
    print ("intial:", dice)
    dice.rollall()
    print("AFter roll: ", dice)
    print("Number of 2's: ", dice.count(2))

if __name__ == "__main__":
    main()
