from flask import Flask, request, jsonify
import requests
import json
import logging

app = Flask(__name__)

server_url ='http://localhost:4000/vehicles'

# Sample data (replace with your actual data source)
data = {
    'item1': {'name': 'Item 1', 'price': 10.99},
    'item2': {'name': 'Item 2', 'price': 24.99},
}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data), 200

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    if item_id in data:
        return jsonify(data[item_id]), 200
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in data:
        try:
            new_data = request.json
            data[item_id].update(new_data)
            return jsonify({'message': 'Item updated successfully'}), 200
        except Exception as e:
            return jsonify({'message': 'Error', 'error': str(e)}), 500
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/create_vehicle', methods=['POST'])
def create_item():
    try:
        new_item = request.json
        item_id = new_item.get('id')
        if item_id:
            data[item_id] = new_item
            return jsonify({'message': 'Item created successfully'}), 201
        else:
            return jsonify({'message': 'Invalid data, item ID required'}), 400
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500

@app.route('/items/<item_id>', methods=['PATCH'])
def partial_update_item(item_id):
    if item_id in data:
        try:
            update_data = request.json
            data[item_id].update(update_data)
            return jsonify({'message': 'Item partially updated successfully'}), 200
        except Exception as e:
            return jsonify({'message': 'Error', 'error': str(e)}), 500
    else:
        return jsonify({'message': 'Item not found'}), 404


@app.route('/get_vehicles', methods=['GET'])
def get_vehicles():
    print("Get vehicle(s) request received")
    # Make a GET request to the API
    response = requests.get(server_url)
    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()
        return jsonify(json_data), 200
    else:
        return jsonify({'error': 'API request failed'}), 500


@app.route('/get_vehicle/<vehicleid>', methods=['GET'])
def get_vehicle(vehicleid):
    logging.info('vehicle id requested %s', vehicleid)
    response = requests.get(server_url)
    vehicle_data = {}
    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        vehicle_data = response.json()
    else:
        return jsonify({'error': 'API request failed'}), 500

    for vehicle in vehicle_data:
        if vehicle.get("id") == vehicleid:
          return jsonify(vehicle)

    return jsonify("vehicle not found")


@app.route('/vehicle/is_available/<vehicleid>', methods=['GET'])
def is_vehicle_availale(vehicleid):
    response = requests.get(server_url)
    vehicle_data = {}
    found_vehicle = False
    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        vehicle_data = response.json()
    else:
        return jsonify({'error': 'API request failed'}), 500

    for vehicle in vehicle_data:
        if vehicle.get("id") == vehicleid:
            found_vehicle = True
            break
        else:
            found_vehicle = False

    return jsonify({"vehicle_found": found_vehicle})

@app.route('/vehicles/<vehicle_id>/diagnostic', methods=['PUT'])
def update_vehicle_diagnostics(vehicle_id):
    key_to_append = "health"
    response = requests.get(server_url)
    vehicle_data = {}
    found_vehicle = False
    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        vehicle_data = response.json()
    else:
        return jsonify({'error': 'API request failed'}), 500

    try:
        # Get the attribute name and value from the request data
        request_data = request.get_json()
        print(request_data)
        err_code = request_data.get("error_code")
        err_info = request_data.get("error_info")
        err_severity = request_data.get("error_severity")

        # Find the vehicle by ID
        vehicle = next((v for v in vehicle_data if v["id"] == vehicle_id), None)

        if vehicle:
            error = {}
            # Update the vehicle's attribute
            error["error_code"] = err_code
            error["info"] = err_info
            error["severity"] = err_severity

            if key_to_append in vehicle and isinstance(vehicle[key_to_append], list):

                vehicle[key_to_append].append(error)
            else:
                vehicle[key_to_append] = [error]

            print(vehicle)

            update_response = requests.post(server_url, json=vehicle_data)

            if update_response.status_code == 200:
                return jsonify({'message': 'Array updated successfully'}), 200
            else:
                return jsonify({'message': 'Failed to update the array on JSON-Server'}), 500

            return jsonify(vehicle), 200
        else:
            return jsonify({'message': 'Vehicle not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500

@app.route('/vehicles/<vehicle_id>/update_service_required', methods=['PUT'])
def update_vehicle_serv_required(vehicle_id):
    service_required_key = "service_required"
    vehicle_data = {}
    found_vehicle = False
    try:
        response = requests.get(server_url)
        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            vehicle_data = response.json()
        else:
            return jsonify({'error': 'API request failed'}), 500

    except:
        return jsonify({'message': 'Error', 'error': str(e)}), 500

    try:
        # Get the attribute name and value from the request data
        request_data = request.get_json()
        print(request_data)
        is_service_required = request_data.get("service_required")
        print(is_service_required)

        # Loop through the array to find the index of the vehicle with the specified ID
        for index, vehicle in enumerate(vehicle_data):
            if vehicle["id"] == vehicle_id:
                # Update the element at the found index
                index_to_update = index
                break  # Exit the loop once the vehicle is found

        if service_required_key in vehicle and isinstance(vehicle[service_required_key], list):

            vehicle[service_required_key].append(error)
        else:
            vehicle[service_required_key] = is_service_required

        vehicle_data[index_to_update] = vehicle

        server_response = requests.put(server_url, json=vehicle_data)

        return jsonify(vehicle), 200

    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
