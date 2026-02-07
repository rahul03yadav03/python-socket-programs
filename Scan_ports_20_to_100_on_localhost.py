#import socket library
import socket


#here it is a ip of local host
local_host = "127.0.0.1"


#make a loop for port from 20 to 100
for port in range(20,101):

    #create a tcp socket using IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #set time out to 2 seconds
    s.settimeout(2)

    #now run this "try" block
    try:

        #connect localhost and port, and result will receive numbers
        result = s.connect_ex((local_host,port))

        #if result receive 0 then it means port is open on localhost
        if result == 0:
            print(f"Port {port} is open on localhost {local_host}")


        #otherwise port is close on localhost
        else:
            print(f"Port {port} is close on localhost {local_host}")


    #finally close tcp socket
    finally:
        s.close()


        

    


    
