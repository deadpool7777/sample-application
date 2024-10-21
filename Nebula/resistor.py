# resistor.py

class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance

    def calculate_power_dissipation(self, current):
        #power equation
        Calculate power dissipation in the resistor using P = I^2 * R
        
        power = current ** 2 * self.resistance
        return power  
