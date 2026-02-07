# import the socket library for TCP networking
import socket


# Ask the user for server IP address and port number
server_ip = input("Enter Server ip. ")
server_port = int(input("Enter server port: "))


# Create a TCP socket using IPv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:

    # Attempt to connect to the server
    client_socket.connect((server_ip,server_port))
    print("connected to server")


    # Take a message from the user and send it to the server
    message = input("Enter message to send: ")
    client_socket.send(message.encode())


    # Receive response from the server (up to 1024 bytes)
    response = client_socket.recv(1024)
    print("Received from server: ", response.decode())

# Raised when DNS resolution of the server name fails
except socket.gaierror:
    print("Invalid server name (DNS resolution failed)")


# Raised when the server is not accepting connections on the given port
except ConnectionRefusedError:
    print("Connection refused. Server may not be running")


# Raised when the connection attempt takes too long
except TimeoutError:
    print("Connection time out")


# Always close the socket, whether an error occurred or not
finally:
    client_socket.close()

