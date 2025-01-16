from flask import Flask, jsonify, request
from resource_1 import resource_bp  # Import the resource blueprint

# Create the Flask app
app = Flask(__name__)

# Register the blueprint for resources
app.register_blueprint(resource_bp)

# Define a simple route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

if __name__ == '__main__':
    app.run(debug=True)
