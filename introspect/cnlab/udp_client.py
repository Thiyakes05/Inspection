import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        message = input("Client: ")
        client_socket.sendto(message.encode(), ('localhost', 12345))
        if message.lower() == 'exit':
            break
        response, addr = client_socket.recvfrom(1024)
        print(f"Server: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    udp_client()
