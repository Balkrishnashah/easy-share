from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Path to store messages (on server side)
messages_file = 'messages.json'

# Load or create the messages.json file to store user-specific messages
if not os.path.exists(messages_file):
    with open(messages_file, 'w') as f:
        json.dump({}, f)  # Create an empty dictionary to store messages for users

# Function to load messages from the JSON file
def load_messages():
    with open(messages_file, 'r') as f:
        return json.load(f)

# Function to save messages to the JSON file
def save_messages(data):
    with open(messages_file, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_messages')
def get_messages():
    user = request.args.get('user')
    messages_data = load_messages()
    
    if user in messages_data:
        return jsonify({'messages': messages_data[user]})
    else:
        return jsonify({'messages': []})

@app.route('/send_message', methods=['POST'])
def send_message():
    user = request.form.get('user')
    message = request.form.get('message')
    
    if not user or not message:
        return jsonify({'status': 'error', 'message': 'Missing user or message'}), 400

    messages_data = load_messages()
    
    if user not in messages_data:
        messages_data[user] = []
    
    # Get the current timestamp when the message is sent
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Store the message with its timestamp
    messages_data[user].append({'message': message, 'timestamp': timestamp})
    
    save_messages(messages_data)
    
    return jsonify({'status': 'success', 'message': 'Message sent successfully'})

@app.route('/delete_message', methods=['POST'])
def delete_message():
    user = request.form.get('user')
    index = int(request.form.get('index'))
    
    if not user or index is None:
        return jsonify({'status': 'error', 'message': 'Missing user or index'}), 400
    
    messages_data = load_messages()
    
    if user not in messages_data or index >= len(messages_data[user]):
        return jsonify({'status': 'error', 'message': 'Message not found'}), 404
    
    del messages_data[user][index]
    
    # If there are no messages left, remove the user from the messages data
    if not messages_data[user]:
        del messages_data[user]
    
    save_messages(messages_data)
    
    return jsonify({'status': 'success', 'message': 'Message deleted successfully'})

@app.route('/logout')
def logout():
    return jsonify({'status': 'success', 'message': 'Logged out successfully'})

if __name__ == '__main__':
    app.run(debug=True)
