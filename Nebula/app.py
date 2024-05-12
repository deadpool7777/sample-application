# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from resistor import Resistor
from circuit import Circuit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///components.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    specifications = db.Column(db.String(10))

# def init_db():
#     db.create_all()


circuit = Circuit()

def megaohms_to_ohms(resistance):
    return resistance * 1000000

def kiloohms_to_ohms(resistance):
    return resistance * 1000

@app.route('/')
def index():
    db.create_all()
    # components = Component.query.filter_by(type='Resistor').all()
    return render_template('index.html')

@app.route('/add_resistor', methods=['POST'])
def add_resistor():
    resistance = float(request.form['resistance'])
    unit = request.form['unit']  # Get the selected unit from the form
    if unit == 'kiloohms':
        resistance = kiloohms_to_ohms(resistance)
    elif unit == 'megaohms':
        resistance = megaohms_to_ohms(resistance)
    resistor = Resistor(resistance)
    circuit.add_resistor(resistor)

     # Save resistor details to the database
    component_type = 'Resistor'
    specifications = f"{resistance} Ohms"
    new_component = Component(type=component_type, specifications=specifications)
    db.session.add(new_component)
    db.session.commit()

    return render_template('index.html', message="Resistor added to circuit.")

@app.route('/calculate', methods=['POST'])
def calculate():
    current = float(request.form['current'])
    connection_type = request.form['connection_type'] 
    # Component.query.delete()
    total_power = circuit.calculate_total_power(current,connection_type)
    components = Component.query.filter_by(type='Resistor').all() 
    # components = Component.query.all() 
    return render_template('result.html', total_power=total_power,components=components)

@app.route('/calculate_series_resistance')
def calculate_series_resistance():
    series_eq_resistance = circuit.calculate_series_resistance()
    return render_template('series_resistance.html', series_eq_resistance=series_eq_resistance)

@app.route('/calculate_parallel_resistance')
def calculate_parallel_resistance():
    parallel_eq_resistance = circuit.calculate_parallel_resistance()
    return render_template('parallel_resistance.html', parallel_eq_resistance=parallel_eq_resistance)

@app.route('/delete_all_components', methods=['POST'])
def delete_all_components():
    try:
        # Delete all data from the Component table
        Component.query.delete()
        db.session.commit()
        message = "All components deleted."
    except Exception as e:
        db.session.rollback()
        message = f"Error deleting components: {str(e)}"
    
    return redirect(url_for('index', message=message))

if __name__ == '__main__':
    app.run(debug=True)
