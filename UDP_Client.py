import socket
import sys

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")

        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode('utf-8'))

            if message == "Bye":
                response = client_socket.recv(1024).decode('utf-8')
                print(f"Server response: {response}")
                print("Closing connection...")
                break

            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server response: {response}")
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 client.py <server_ip> <port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
