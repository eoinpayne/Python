import datetime

def age_fact (age):
    heartbeats = age * 42000000   ##average of 42 million per year
    return heartbeats

def weight_fact (weight):
    weight_compare = 453592370 / weight # burj khalifa = 453592370 kilos
    return weight_compare

def height_fact (height):
    height_compare = 32598.4 / height ##burj khalifa 828M (32598.4 ") ## build a converter and link.
    return height_compare


def main ():
    age = int(input("What is your age ?"))  ## learn to do DOB and convert dates to get exact calc's
    weight = float(input("What is your weight in kilos?"))
    height = float(input("What is your height in inches?"))

    heartbeats = age_fact(age)
    print ("In your lifetime, your hear has beeten " , heartbeats, "times.")

    height_compare = height_fact (height)
    print ("It would take ", height_compare , "of you to match the height of the tallest building in the world.")

    weight_compare = weight_fact(weight)
    print ("It would take ", weight_compare, "of you to match the weight of the tallest building in the world")

main()



def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)