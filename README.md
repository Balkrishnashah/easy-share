
# Easy Share

This is a simple Flask web application that allows users to send, view, and delete messages. The app provides a basic user interface to share messages with others. Users are prompted to enter their name when they visit the page for the first time. Once authenticated, users can send and delete messages, and the messages are displayed with timestamps.

## Features

- **User Authentication**: Users can enter their name, which is stored locally in the browser.
- **Message Sharing**: Users can type messages and send them to a shared message board.
- **Message Deletion**: Users can delete their messages from the board.
- **Responsive UI**: The UI is designed to be simple and user-friendly, with a clean layout.
- **Toast Notifications**: After deleting a message, a toast notification is shown confirming the deletion.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/your-username/your-repository-name.git
   ```

2. Navigate to your project directory:
   ```sh
   cd your-repository-name
   ```

3. Set up a virtual environment:
   ```sh
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - **On macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```
   - **On Windows**:
     ```sh
     venv\Scripts\activate
     ```

5. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

6. Run the Flask application:
   ```sh
   python app.py
   ```

7. Open your browser and go to `http://127.0.0.1:5000/` to start using the app.

## File Structure

```
/your-repository-name
│
├── app.py            # Main Flask application
├── index.html        # Frontend HTML file
├── static/           # Static assets (CSS, JS, etc.)
│   └── css/          # Stylesheet directory
│       └── styles.css
└── requirements.txt  # List of Python dependencies
```

## How to Use

1. When you open the app, you will be prompted to enter your name.
2. After entering your name, you will be able to see the message board.
3. Type a message in the input field and click "Send Message" to share it.
4. To delete a message, click the trash icon next to the message.
5. To log out, click the "Sign Out" button at the top-right corner of the page.

## Notes

- The app uses **localStorage** in the browser to remember the user's name, so the user does not need to re-enter it after refreshing the page.
- The backend Flask app handles the sending and deletion of messages.

## Troubleshooting

- If you encounter issues with the app not displaying messages, ensure that the backend is correctly set up and running.
- If the app doesn't load, make sure all required dependencies are installed, and Flask is properly configured.
