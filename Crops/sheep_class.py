from Crops.animal_class import *

class Sheep(Animal):
    def __init__(self):
        super().__init__(1, 3, 3)
        self.type = "Sheep"
        self.name = str(input("What is this cow's name?: "))

    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            if self.status == "Baby":
                self.weight = self.growth_rate * 2
            elif self.status == "Infant":
                self.weight = self.growth_rate * 1.8
            elif self.status == "Mature":
                self.weight = self.growth_rate * 1.5
            self.days_growing += 1
            self.update_status()
