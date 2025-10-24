import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("TCP Server listening on port 12345...")
    
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        print(f"Client: {message}")
        response = input("Server: ")
        conn.send(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    tcp_server()

