# resistor.py

class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance

    def calculate_power_dissipation(self, current):
        """
        Calculate power dissipation in the resistor using P = I^2 * R
        Args:
            current (float): Current flowing through the resistor in Amperes
        Returns:
            float: Power dissipation in Watts
        """
        power = current ** 2 * self.resistance
        return power
