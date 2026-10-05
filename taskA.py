from flask import Flask, jsonify, request

app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.post('/check/')
def check_number():
    if not request.is_json:
        return jsonify({
            "error": "Invalid input. Please provide JSON data."
        }), 400

    data = request.get_json()

    if 'number' not in data:
        return jsonify({
            "error": "Missing 'number' field in the request data."
        }), 400

    number = data['number']

    if not isinstance(number, int) or isinstance(number, bool):
        return jsonify({
            "error": "'number' field must be an integer."
        }), 400
    
    if number < 1 or number > 1000:
        return jsonify({
            "error": "'number' field must be between 1 and 1,000."
        }), 400
        
    result = is_prime(number)
    return jsonify({'is_prime': result})