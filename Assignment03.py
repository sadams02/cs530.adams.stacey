import socket, logging, random, time
from datetime import datetime

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO)

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 8080))

clients = {}

def send_timestamp_to_clients():
    while True:
        if clients:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"Timestamp: {timestamp}"
            for client in clients.values():
                server_socket.sendto(message.encode(), client)
            logging.info(f"Sent to clients: {message}")
        time.sleep(random.randint(5, 30))