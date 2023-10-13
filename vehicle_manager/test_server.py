from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_json', methods=['GET'])
def get_json_data():
    try:
        # Define the URL of the REST API you want to call
        api_url = 'https://0.0.0.0:8081/vehicles'  # Replace with your API URL
        print("api called")
        # Make a GET request to the API
        response = requests.get(api_url)
        print(response)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            return jsonify(json_data), 200
        else:
            return jsonify({'error': 'API request failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
