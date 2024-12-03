from urllib.parse import urlparse
from flask import Flask, request, jsonify, render_template
import requests
import os  

app = Flask(__name__)

@app.route('/')
def index():
    print("Rendering index page")
    return render_template('index.html')  

def get_request(api_url, id_instance, api_token_instance, action):
    url = f"{api_url}/waInstance{id_instance}/{action}/{api_token_instance}"
    print(f"Making GET request to: {url}")
    try:
        response = requests.get(url)
        print("Received response:", response.text)
        return response
    except Exception as e:
        print(f"Error while making GET request: {e}")
        return None

def post_request(api_url, id_instance, api_token_instance, action, payload):
    url = f"{api_url}/waInstance{id_instance}/{action}/{api_token_instance}"
    print(f"Making POST request to: {url} with payload: {payload}")
    headers = {'Content-Type': 'application/json'}  
    try:
        response = requests.post(url, json=payload, headers=headers) 
        print("Received response:", response.text)
        return response
    except Exception as e:
        print(f"Error while making POST request: {e}")
        return None

def get_file_name_from_url(url):
    parsed_url = urlparse(url)
    return os.path.basename(parsed_url.path)


@app.route('/handle_action', methods=['POST'])
def handle_action():
    api_url = request.form.get('apiUrl')
    id_instance = request.form.get('idInstance')
    api_token_instance = request.form.get('apiTokenInstance')
    action = request.form.get('action')

    print("Received request data:")
    print(f"API URL: {api_url}")
    print(f"idInstance: {id_instance}")
    print(f"apiTokenInstance: {api_token_instance}")
    print(f"Action: {action}")

    response = None

    if action == 'getSettings':
        response = get_request(api_url, id_instance, api_token_instance, 'getSettings')
    elif action == 'getStateInstance':
        response = get_request(api_url, id_instance, api_token_instance, 'getStateInstance')
    elif action == 'sendMessage':
        phone_number = request.form.get('phoneNumber')
        message = request.form.get('message')
        payload = {
            "chatId": f"{phone_number}@c.us",
            "message": message
        }
        response = post_request(api_url, id_instance, api_token_instance, 'sendMessage', payload)
    elif action == 'sendFileByUrl':
        file_phone_number = request.form.get('filePhoneNumber')
        file_url = request.form.get('fileUrl')
        file_name = get_file_name_from_url(file_url)
        caption = request.form.get('caption', 'File')
        payload = {
            "chatId": f"{file_phone_number}@c.us",
            "urlFile": file_url,
            "fileName": file_name,
            "caption": caption
        }
        response = post_request(api_url, id_instance, api_token_instance, 'sendFileByUrl', payload)
    else:
        print("Unknown action")
        return jsonify({"error": "Unknown action"})

    if response:
        print("Final response:", response.json())
        return jsonify(response.json())
    return jsonify({"error": "No response from API"})

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=8000, debug=True)

