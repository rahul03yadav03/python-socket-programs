#import the socket library
import socket

#now define a function (check_port)
def check_port(ip, port):


    #create a TCP socket for IPv4 connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    #set timeout to 5 second
    s.settimeout(5)


    #now connect port and ip, it will 0 if port is open
    result = s.connect_ex((ip,port))


    #now close the socket
    s.close()


    #if there is zero in result, it means port is open
    if result == 0:

        #and print this line
        print(f"Port {port} is OPEN ON {iP}")


    #otherwise run this block
    else:

        #and print this line
        print(f"Port {port} is CLOSE on {ip}")


# Run the function only if this script is executed directly
if __name__ == "__main__":

    #take input (ip) from the user
    ip = input("Please enter IP: ")

    #take input (port) from the user
    port = int(input("Please enter port number: "))


    #now call the function and pass ip, port
    check_port(ip, port)
