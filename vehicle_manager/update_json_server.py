from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

data = {
    'item1': {'name': 'Item 1', 'price': 10.99},
    'item2': {'name': 'Item 2', 'price': 24.99},
}

# JSON-Server URL
json_server_url = 'http://0.0.0.0:8081/vehicles'

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # Get JSON data from the POST request
        new_data = request.get_json()
        print(new_data)

        vehicle_data = requests.get(json_server_url)

        print(vehicle_data.text)

        # Send a POST request to JSON-Server to add the new data
        response = requests.post(f'{json_server_url}', json=new_data)

        # Check the response from JSON-Server and return it to the client
        if response.status_code == 201:
            return jsonify({'message': 'Data added successfully'}), 201
        else:
            return jsonify({'message': 'Error adding data', 'error': response.text}), 500
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
