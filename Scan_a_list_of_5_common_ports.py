#import socket library
import socket


#ask user to enter ip
ip = input("Please enter ip: ")


#here are 5 common port
common_port = [21, 22, 23, 80, 443]


#print that scanning has been started
print(f"Scanning common port on localhost {ip}\n")


#make a loop for port
for port in common_port:


    #create a tcp socket using IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    #set time out to 2 seconds
    s.settimeout(2)


    #now run this "try" block
    try:

        #connect ip and port, and result will receive numbers
        result = s.connect_ex((ip, port))

        #if result receive 0 then it means port is open on given ip
        if result == 0:
            print(f"Port {port} is open on ip {ip}")


        #otherwise port is close on localhost
        else:
            print(f"Port {port} is close on ip {ip}")


    #finally close tcp socket
    finally:
        s.close()


#print that scan has been finished
print("\nScan Completed")

        
