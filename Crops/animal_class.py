from Crops.crop_class import *

class Animal:

    def __init__(self, growth_rate, food_need, water_need):
        self.weight = 0
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self.status = "Baby"
        self.type = "Ceneric"
        self.name = "Name"

    def needs(self):
        return {"food need" : self.food_need, "water need": self.water_need}

    def report(self):
        return {"Weight" : self.weight, "Days Growing": self.days_growing, \
                "Status" : self.status, "Type" : self.type, "Name" : self.name}


    def update_status(self):
        if self.days_growing > 50:
            self.status =  "Old"
        elif self.days_growing > 20:
            self.status =  "Mature"
        elif self.days_growing > 5:
            self.status =  "Infant"


    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            self.weight += self.growth_rate
        self.days_growing += 1
        self.update_status()


def manual_grow(self):
    option_valid = False
    while not option_valid:
        try:
            food = int(input("How much food?: "))
            if 1 <= food <= 20:
                option_valid = True
            else:
                print ("Please enter valid number from 1-20")
        except ValueError:
                print ("Please enter valid number from 1-20")
    option_valid = False
    while not option_valid:
        try:
            water = int(input("How much water?: "))
            if 1 <= water <= 20:
                option_valid = True
            else:
                print ("Please enter valid number from 1-20")
        except ValueError:
                print ("Please enter valid number from 1-20")
    Animal.grow(food, water)
    Animal.update_status()

def automatic_grow(Animal, days = 30):
    for day in days:
        food = randint(1,20)
        water = randint(1,20)
        Animal.grow(food, water)
    Animal.update_status()

def display_menu():
    print ("1. Grow animal over 1 day")
    print ("2. Grow animal auto over 30 day")
    print ("3. Report Status")
    print ("9. Return to animal creation")
    print ("0. Exit")
    print()
    print("Please select an option from above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Animal choice : "))
            if choice in (1,2):
                option_valid = True
            else:
                print ("Please enter valid choice")
        except ValueError:
                print ("Please enter valid choice")
        return choice

def manage_animals(new_animal):
    noexit = True
    display_menu()
    while noexit:
        choice = get_menu_choice()
        if choice == 1:
            manual_grow(Animal)
        elif choice == 2:
            automatic_grow(Animal)
        elif choice ==3:
            print(Animal.report)
        elif choice == 0:
            noexit = False
    print("Animal mgt closing")









