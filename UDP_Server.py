import socket
import sys

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:
                break

            print(f"Received message: {message}")

            if message == "Bye":
                client_socket.sendall("Bye".encode('utf-8'))
                print("Closing connection...")
                break
            else:
                client_socket.sendall(message.upper().encode('utf-8'))
        
        client_socket.close()

    server_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server('127.0.0.1', port)  
