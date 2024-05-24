# Chat Engine

This is a live chat engine built using Django, Django Rest Framework, and Django Channels.

## Features

- Real-time messaging with WebSockets
- User authentication
- Message history
- REST API for retrieving and posting messages

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/chat-engine.git
   cd chat-engine
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (if you want to access the admin interface):

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## WebSocket Server

1. **Start the Channels worker**:
   ```bash
   daphne -p 8001 your_project_name.asgi:application
   ```

## Usage

- Open your browser and navigate to `http://127.0.0.1:8000`.
- Use the chat interface to send and receive messages.

## API Endpoints

- **Get messages**: `GET /api/chat/messages/`
- **Post a new message**: `POST /api/chat/messages/`

## WebSocket

- Connect to `ws://127.0.0.1:8000/ws/chat/` for real-time communication.

## Frontend Integration

Here's a basic example of how to connect to the WebSocket in your frontend:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Chat</title>
  </head>
  <body>
    <div id="chat-log"></div>
    <input type="text" id="chat-message-input" />
    <button id="chat-message-submit">Send</button>

    <script>
      const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/"
      );

      chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        document.querySelector("#chat-log").innerHTML +=
          data.message.user + ": " + data.message.content + "<br>";
      };

      document.querySelector("#chat-message-submit").onclick = function (e) {
        const messageInputDom = document.querySelector("#chat-message-input");
        const message = messageInputDom.value;
        chatSocket.send(
          JSON.stringify({
            message: message,
          })
        );
        messageInputDom.value = "";
      };
    </script>
  </body>
</html>
```

### Key Points Covered in the README

1. **Project Overview**: A brief description of what the project is and its features.
2. **Installation Instructions**: Step-by-step guide on how to set up the project locally.
3. **Usage**: Basic instructions on how to use the application.
4. **API Endpoints**: List of available REST API endpoints.
5. **WebSocket Integration**: Instructions and example code for connecting to the WebSocket.
6. **License**: Information about the project's license.

This `README.md` file provides a comprehensive guide to setting up, using, and understanding the chat engine project. You can further customize it based on your specific requirements and additional features you might have.
