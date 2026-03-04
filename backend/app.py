from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/cube_root', methods=['GET'])
def cube_root():
    number = float(request.args.get('number'))
    result = number ** (1/3)
    return jsonify(result=result)

@app.route('/find_a_by_cubes', methods=['POST'])
def find_a_by_cubes():
    data = request.json
    result = your_logic_to_find_a(data['b'], data['c'])
    return jsonify(result=result)

@app.route('/find_b_by_substitution', methods=['POST'])
def find_b_by_substitution():
    data = request.json
    result = your_logic_to_find_b(data['a'], data['c'])
    return jsonify(result=result)

@app.route('/algebraic_linear_guess_b', methods=['POST'])
def algebraic_linear_guess_b():
    data = request.json
    result = your_logic_to_guess_b(data['x'])
    return jsonify(result=result)

@app.route('/algebraic_quadratic_upper_h', methods=['POST'])
def algebraic_quadratic_upper_h():
    data = request.json
    result = your_logic_to_find_upper_h(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/newton_iter', methods=['POST'])
def newton_iter():
    data = request.json
    result = your_logic_for_newton(data['initial_guess'])
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)