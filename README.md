
# Flask RabbitMQ Messaging Tutorial

This repository contains a tutorial for setting up messaging between Flask and RabbitMQ. We will demonstrate how to send and receive messages using Flask and RabbitMQ, all within a Python virtual environment.

## Project Structure
```
flask-rabbitmq-messaging-tutorial/
├── sender.py         # Flask app to send messages to RabbitMQ
├── receiver.py       # Script to receive messages from RabbitMQ
├── README.md         # Project documentation
├── requirements.txt  # Python dependencies
└── venv/             # Python virtual environment
```
## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.x
- RabbitMQ Server installed and running on your machine.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/oussemanaffetyy/flask-rabbitmq-messaging-tutorial.git
   cd flask-rabbitmq-messaging-tutorial
   ```
2. Set up the virtual environment and install dependencies:
      ```
       python3 -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt
      ```
### Running the Project
   #### 1. Start RabbitMQ Server: Ensure that RabbitMQ server is running on your machine:
      ``` sudo systemctl start rabbitmq-server ```
  ####  2. Run the Sender (Flask App): In one terminal window, run the sender:
        ``` python sender.py ```
       This will start the Flask server on http://localhost:5000.
  ####  3. Send a Message: Use the following curl command to send a message:
       
       ``` curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, RabbitMQ!"}' http://localhost:5000/send ```
   #### 4. Run the Receiver: In another terminal window, run the receiver script:
       ``` python receiver.py ```
       You should see the message received in the terminal.
### Video Tutorial
Watch the full video tutorial on setting up and running this project: [Video Link]
### License
This project is licensed under the MIT License - see the LICENSE file for details.