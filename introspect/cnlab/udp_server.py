import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP Server listening on port 12345...")

    while True:
        message, addr = server_socket.recvfrom(1024)
        print(f"Client ({addr}): {message.decode()}")
        response = input("Server: ")
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    udp_server()
