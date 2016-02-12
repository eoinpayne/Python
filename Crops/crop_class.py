#from Crops.crops import create_crop
from  random import *

class Crop:
    """this is a generic crop class """

    #constructir
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def __str__(self):
        return self.type

    def needs(self):
        """return dictionary containing light and water needs"""
        return {'light need' : self._light_need,'water need' : self._water_need}

    def report(self):
        """method to report info about current state of crop. return dictionary"""
        return {'type' : self._type, 'status' : self._status, 'growth' : self._growth, 'days growing' : self._days_growing}

        #return "{}{}{}{}".format (self._type,self._status,self._growth,self._days_growing)

    def _update_status(self):
        """method to change the staus attribute, depending on current amount of growth (growth attribute)"""
        #private as this is intended to be used by other methods only.
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
        else:
            self._status = "non-existent"

    def grow(self, light, water):
        """method takes in light/water variables, and mutates appropriate crop attributes. incremments days growing. updates status."""
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing +=1      #increments days growing attribute
        self._update_status()        #updates status


def automatic_grow(Crop, days):         #Crop, not self
    """method to TESTS the crop over a long period of time"""
    #a 'function' and not a 'method' as this is a way to use the "grow method", to test it and see if it works over a period of time
    for day in range(days):
        water = randint(0,20)
        light = randint (1,20)
        Crop.grow(water, light)
    Crop._update_status()


def manual_grow(Crop):
    """provide specific values to crop in 1 day, testing it accepts appropriate range of values, performs as expcted when receiving a particular pairing of light and water"""
    valid = False
    while not valid:
        try:
            light = int(input("Enter light value between 1-20"))
            if 1 <= light <=20:   #same as  -- if light >= 1 and water <=10
                valid = True
            else:
                print ("Invalid input, please enter light value between 1-20")
        except ValueError:
            print ("Invalid input, please enter light value between 1-20")

    valid = False
    while not valid:
        try:
            water = int(input("Enter water value between 1-20"))
            if 1 <= water <= 20:
                valid = True
            else:
                print ("Invalid input, please enter water value between 1-20")
        except ValueError:
            print ("Invalid input, please enter water value between 1-20")
    Crop.grow(light, water)
    Crop._update_status()


def display_menu():         #builds menu to be used in crop managment system
    print ("1. Grow manually over 1 day")
    print ("2. Grow auto over 30 day")
    print ("3. Report Status")
    print ("9. Return to crop creation")
    print ("0. Exit")
    print()
    print("Please select an option from above menu")


def get_menu_choice():   # takes user input, ensures it is within range.
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if choice in (1,2,3,9,0):
                option_valid = True
            else:
                print ("Please enter valid option")
        except ValueError:
            print ("Please enter valid option")
    return choice


def manage_crop(Crop):          #mangement system, uses above functions and performs appropriate methods on objects
    print("WECLCOME to managment system")
    print()
    noexit = True
    while noexit:
        display_menu()

        option = get_menu_choice()
        print()
        if option ==1:
            manual_grow(Crop)
        elif option ==2:
            automatic_grow(Crop, 30)
        elif option == 3:
            print(Crop.report())
        elif option == 9:
            create_crop()
        elif option==0:
            noexit = False
            print()
    print ("Crop management closing")


def main():
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)


if __name__ == "__main__":
    main()
