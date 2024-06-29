from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getSettings', methods=['POST'])
def get_settings():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('ApiTokenInstance')
    response = requests.get(f'https://api.green-api.com/waInstance{id_instance}/getSettings/{api_token_instance}')
    return jsonify(response.json())

@app.route('/getStateInstance', methods=['POST'])
def get_state_instance():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('ApiTokenInstance')
    response = requests.get(f'https://api.green-api.com/waInstance{id_instance}/getStateInstance/{api_token_instance}')
    return jsonify(response.json())

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('ApiTokenInstance')
    phone_number = data.get('phoneNumber')
    message = data.get('message')
    payload = {
        "chatId": f"{phone_number}@c.us",
        "message": message
    }
    response = requests.post(f'https://api.green-api.com/waInstance{id_instance}/sendMessage/{api_token_instance}', json=payload)
    return jsonify(response.json())

@app.route('/sendFileByUrl', methods=['POST'])
def send_file_by_url():
    data = request.json
    id_instance = data.get('idInstance')
    api_token_instance = data.get('ApiTokenInstance')
    phone_number = data.get('phoneNumber')
    file_url = data.get('fileUrl')
    file_name = file_url.split('/').pop()
    payload = {
        "chatId": f"{phone_number}@c.us",
        "urlFile": file_url,
        "fileName": file_name
    }
    response = requests.post(f'https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{api_token_instance}', json=payload)
    return jsonify(response.json())

#if __name__ == '__main__':
#    app.run(debug=True)
