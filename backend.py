import os

from flask import Flask, request, jsonify

# Configure Gemini API


# Import custom functions
from model.fitness import predict_calories
from model.diet import get_diet_recommendation
from model.sleep import predict_sleep_quality
from model.dieases import predict_disease_risk

app = Flask(__name__)

@app.route('/predict_calories', methods=['POST'])
def calories():
    try:
        data = request.json
        steps = data['steps']
        if steps < 0:
            return jsonify({'error': 'Steps cannot be negative'}), 400
        return jsonify({'calories_burned': predict_calories(steps)})
    except KeyError:
        return jsonify({'error': 'Missing required data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/diet', methods=['GET'])
def diet():
    try:
        goal = request.args.get('goal', 'balanced')
        if goal not in ['weight_loss', 'muscle_gain', 'balanced']:
            return jsonify({'error': 'Invalid goal'}), 400
        return jsonify({'diet_plan': get_diet_recommendation(goal)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sleep', methods=['POST'])
def sleep():
    try:
        data = request.json
        hours = data['hours']
        if hours < 0:
            return jsonify({'error': 'Sleep hours cannot be negative'}), 400
        return jsonify({'sleep_quality': predict_sleep_quality(hours)})
    except KeyError:
        return jsonify({'error': 'Missing required data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/disease', methods=['POST'])
def disease():
    try:
        data = request.json
        age = data['age']
        bmi = data['bmi']
        if age < 0 or bmi < 0:
            return jsonify({'error': 'Age and BMI cannot be negative'}), 400
        return jsonify({'disease_risk': predict_disease_risk(age, bmi)})
    except KeyError:
        return jsonify({'error': 'Missing required data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
