from flask import Blueprint, render_template, jsonify, request

main = Blueprint('main', __name__)

# Home route
@main.route('/')
def index():
    return render_template('index.html')

# About page
@main.route('/about')
def about():
    return render_template('about.html')

# Sample REST API
@main.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Flask Docker App",
        "version": "1.0",
        "status": "running"
    }
    return jsonify(data)

# Example POST API
@main.route('/api/echo', methods=['POST'])
def echo():
    req_data = request.get_json()
    message = req_data.get("message", "No message provided")
    return jsonify({"echo": message})
