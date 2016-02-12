
from Crops.sheep_class import *
from Crops.cow_class import *

def dsiplay_animals_menu():
    print ("Which crop? Potato or Wheat?")
    #print()
    print ("1. Cow")
    print ("2. Sheep")
    print ("0. Exit")
    print()
    print("Please select an option from above menu")

def select_animal_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Animal choice is: "))
            if choice in (1,2,0):
                valid = True
            else:
                print("Please enter valid")
        except ValueError:
                print("Please enter valid")
        return choice


def create_animal():
    while True:
        dsiplay_animals_menu()
        choice = select_animal_option()
        if choice == 1:
            new_animal = Cow()
            manage_animals(new_animal)
            return new_animal
        elif choice == 2:
            new_animal= Sheep()
            manage_animals(new_animal)
            return new_animal
        elif choice == 0:
            print ("Thanks, goodbye.")
            return False


def main():
    new_crop = create_animal()
    #manage_crop(new_crop)

if __name__ == "__main__":
    main()

