#import socket library
import socket


#get the local machine hostname
hostanme = socket.gethostname()


#get the IP address using hostname
local_ip = socket.gethostbyname(hostanme)


#print the result
print("Local machine IP address: ", local_ip)
