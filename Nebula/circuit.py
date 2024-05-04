# circuit.py

class Circuit:
    def __init__(self):
        self.resistors = []

    def add_resistor(self, resistor):
        self.resistors.append(resistor)

    def calculate_total_power(self, current, connection_type):
        total_power = 0
         
        if connection_type == 'series':
            total_power = sum(resistor.calculate_power_dissipation(current) for resistor in self.resistors)
        elif connection_type == 'parallel':
            equivalent_resistance = self.calculate_parallel_resistance()
            total_power = (current ** 2) * equivalent_resistance

        self.resistors.clear()  

        return total_power

    def calculate_series_resistance(self):
        series_resistance = sum(resistor.resistance for resistor in self.resistors)
        self.resistors.clear()  # Clear the list of resistors after calculation
        return series_resistance

    def calculate_parallel_resistance(self):
        reciprocal_sum = sum(1 / resistor.resistance for resistor in self.resistors)
        parallel_resistance = 1 / reciprocal_sum
        self.resistors.clear()  # Clear the list of resistors after calculation
        return parallel_resistance
