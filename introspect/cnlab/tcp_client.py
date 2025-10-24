import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")
        if response.lower() == 'exit':
            break

    client_socket.close()

if __name__ == "__main__":
    tcp_client()

