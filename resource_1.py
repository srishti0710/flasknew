from flask import Blueprint, jsonify, request

# Create a Blueprint for the resource
resource_bp = Blueprint('resource', __name__)

@resource_bp.route('/api/resource', methods=['GET', 'POST'])
def resource():
    if request.method == 'GET':
        return jsonify({"resource": "This is a sample resource."})

    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"received": data}), 201