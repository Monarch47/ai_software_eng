from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import conv

app = Flask(__name__)
CORS(app)  # Enable CORS on all routes

last_response = None  # Global variable to hold the last processed response

@app.route('/send_string', methods=['GET'])
def send_string():
    global last_response
    if last_response:
        return last_response
    else:
        return "No message processed yet!"

@app.route('/input_t', methods=['POST'])
def input_t():
    global last_response
    if request.is_json:
        data = request.get_json()
        last_response = conv(data['message'])
        print(last_response)
        return last_response, 200
    return "Invalid data", 400

@app.route('/input_m', methods=['POST'])
def input_m():
    if 'document' not in request.files:
        return "No document part", 400
    file = request.files['document']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = file.filename
        file.save(f"./{filename}")
        return f"Document {filename} received and saved.", 200

if __name__ == '__main__':
    app.run(debug=True)
