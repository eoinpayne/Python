from Crops.potato_class import *
from Crops.wheat_class import *


def display_crops_menu():
    """ displays options of crops to choose --> def get_crop_choice"""
    print ("Which crop? Potato or Wheat?")
    print()
    print ("1. Potato")
    print ("2. Wheat")
    print ("0. Exit")
    print()
    print("Please select an option from above menu")

def select_crop_option():  # takes user input for crop choice, ensures it is within range.
    option_valid = False
    while not option_valid:
        try:
            crop_choice = int(input("Crop option Selection: "))
            if crop_choice in (0,1,2):
                option_valid = True
            else:
                print ("Please enter valid option")
        except ValueError:
                print ("Please enter valid option")
    return crop_choice


def create_crop():
    while True:
        display_crops_menu()
        crop_option = select_crop_option()
        if crop_option == 1:
            new_crop = Potato()
            manage_crop(new_crop)
            return new_crop
        elif crop_option == 2:
            new_crop = Wheat()
            manage_crop(new_crop)
            return new_crop
        elif crop_option == 0:
            print ("Thanks, goodbye.")
            return False


def main():
    new_crop = create_crop()
    #manage_crop(new_crop)

if __name__ == "__main__":
    main()


