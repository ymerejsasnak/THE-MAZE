import random as r


MAX_FUEL_LEVEL = 15


class Inventory:
    
    def __init__(self):
        self.paint = 0
        self.fuel = 1  # sight range is equal to fuel, max 10
        self.magic_paint = 0   
        self.pickaxes = 0
    
    def items(self):
        return (self.fuel, self.paint, self.magic_paint, self.pickaxes)

    def get_paint(self):
        self.paint += r.randint(2, 5)

    def get_fuel(self):
        self.fuel = min(self.fuel + 1, MAX_FUEL_LEVEL) 
    
    def get_magic_paint(self):
        self.magic_paint += r.randint(1, 5)
    
    def get_pickaxe(self):
        self.pickaxes += 1
        

