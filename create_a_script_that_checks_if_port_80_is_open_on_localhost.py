# Import the socket library
import socket


#define a function (check_port)
def check_port(local_host, port):
    
   # Create a TCP socket for IPv4 connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #set timeout to 2 second
    s.settimeout(2)

    #now connect port and local_host, it will 0 if port is open
    result  = s.connect_ex((local_host, port))

    #close the socket
    s.close()


    #if there is nothing in result , it means port is open
    if result == 0:

        #and print this line
        print(f"Port {port} is OPEN on {local_host}")

    #otherwise run this one
    else:

        #and print this line
        print(f"Port {port} is CLOSED  on {local_host}")

# Run the function only if this script is executed directly
if __name__ == "__main__":

    #call function and  pass thgese two input
    check_port("127.0.0.1", 80)
