from Crops.animal_class import *

class Cow(Animal):
    def __init__(self):
        super().__init__(2, 5, 3)
        self.type = "Cow"
        self.name = str(input("What is this cow's name?: "))

    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            if self.status == "Baby":
                self.weight = self.growth_rate * 2
            elif self.status == "Infant":
                self.weight = self.growth_rate * 1.5
            elif self.status == "Mature":
                self.weight = self.growth_rate * 1.1
            self.days_growing += 1
            self.update_status()
