from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages in a list (In-memory)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message:
        messages.append(message)
    return jsonify({'status': 'success'})

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': messages})

@app.route('/delete_message', methods=['POST'])
def delete_message():
    try:
        index = int(request.form.get('index'))  # Get the index of the message to delete
        if 0 <= index < len(messages):
            messages.pop(index)  # Remove the message from the list
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Invalid index'}), 400
    except (ValueError, IndexError):
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
