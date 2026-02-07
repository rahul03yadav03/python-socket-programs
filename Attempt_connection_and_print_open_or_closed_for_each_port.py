#import socket library
import socket


#define a function for port scanning
def port_scan(ip, f_port,l_port):

    
    #create a for loop for scanning port one by one
    for port in range(f_port, l_port+1):

        #create a TCP socket using IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #set timeout to 2 seconds
        s.settimeout(2)


        #attempt to connect to the given ip and port
        #connect_ex returns 0 if the port is open, otherwise non-zero
        result = s.connect_ex((ip, port))


        #if the value of result is zero then run this block and print port is open
        if result == 0:
            print(f"Port {port} is open on {ip}")


        #otherwise run this block and print port is closed
        else:
            print(f"Port {port} is closed on {ip}")


        
        #close the tocp socket 
        s.close()

        
#run this , if this code executed directly
if __name__ == "__main__":


    #ask user to enter ip , starting port and last port
    ip = input("please enter ip : ")
    s_port = int(input("Please enter starting port number: "))
    l_port = int(input("Please enter ending port number: "))


    
    #call to function and pass ip, s_port and l_port
    port_scan(ip, s_port,l_port)

