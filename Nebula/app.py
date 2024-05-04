# app.py

from flask import Flask, render_template, request
from resistor import Resistor
from circuit import Circuit

app = Flask(__name__)
circuit = Circuit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_resistor', methods=['POST'])
def add_resistor():
    resistance = float(request.form['resistance'])
    resistor = Resistor(resistance)
    circuit.add_resistor(resistor)
    return render_template('index.html', message="Resistor added to circuit.")

@app.route('/calculate', methods=['POST'])
def calculate():
    current = float(request.form['current'])
    connection_type = request.form['connection_type'] 
    total_power = circuit.calculate_total_power(current,connection_type)
    return render_template('result.html', total_power=total_power)

@app.route('/calculate_series_resistance')
def calculate_series_resistance():
    series_eq_resistance = circuit.calculate_series_resistance()
    return render_template('series_resistance.html', series_eq_resistance=series_eq_resistance)

@app.route('/calculate_parallel_resistance')
def calculate_parallel_resistance():
    parallel_eq_resistance = circuit.calculate_parallel_resistance()
    return render_template('parallel_resistance.html', parallel_eq_resistance=parallel_eq_resistance)

if __name__ == '__main__':
    app.run(debug=True)
