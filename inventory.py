MAX_FUEL_LEVEL = 10


class Inventory:
    
    def __init__(self):
        self.paint = 0
        self.fuel = 1  # sight range is equal to fuel, max 10
        self.charges = 0   
    
    def items(self):
        return (self.fuel, self.paint, self.charges)

    def get_paint(self):
        self.paint += 10

    def get_fuel(self):
        self.fuel = min(self.fuel + 1, MAX_FUEL_LEVEL) 
    
    def get_charge(self):
        self.charges += 1
        

