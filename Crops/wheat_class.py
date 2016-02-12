from Crops.crop_class import *

class Wheat(Crop):
    def __init__(self):
        super().__init__(2, 2, 3)
        self._type = "Wheat"

    def grow(self, light, water):
        if light>= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water >  self._water_need:
                self._growth += self._growth_rate *2
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 2.2
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()