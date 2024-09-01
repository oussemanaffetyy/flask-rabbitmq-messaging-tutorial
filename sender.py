from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

def send_message_to_rabbitmq(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')

    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    print(f"Sent: {message}")

    connection.close()

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get('message', 'Hello RabbitMQ!')
    send_message_to_rabbitmq(message)
    return jsonify({'status': 'Message sent!'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
