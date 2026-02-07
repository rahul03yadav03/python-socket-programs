#import socket and time library 
import socket
import time


#ask user to enter ip and port number
ip = input("Please enter IP: ")
port = int(input("Please enter port number: "))


#set time out 2 seconds
timeout  = 2


#create a TCP socket using IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#now put the value of time out here
s.settimeout(timeout)


#try to connect and measure ping time
try:

    # record start time
    start_time  = time.time()

    # attempt TCP connection
    s.connect((ip, port))

    # record end time
    final_time = time.time()

    
    # convert to milliseconds
    ping_time = (final_time - start_time)*1000

    print(f"Ping to {ip}:{port} successful-time = {ping_time:.2f} ms")

except socket.gaierror:
    print(f" Cannot resolve hostname: {ip}")

except socket.timeout:
    print(f"Ping to {ip}:{port} time out after {timeout} seconds")

except Exception as e:
    print(f"Error pinging {ip}: {e}")


# always close the socket
finally:
    s.close()
    
