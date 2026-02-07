#import socket library
import socket


#define a function name UPD_sender
def UDP_sender(ip, port):


    #create a upd socket using IPv4
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    #run this try block
    try:
        
        #input message which you want to send
        message = input("Enter message which you want to send: ")

        #send message in encoded form to given ip and port
        client.sendto(message.encode(), (ip, port))

        #and confirm that you have send the message
        print("Message send successfully")


    #in case if it gave any error then run this block
    except Exception as e:
        print("Error:",e)


    #finally close upd socket
    finally:
        client.close()
        

#run this, if the code excecuted directly
if __name__ == "__main__":

    # ask user to enter ip and port
    ip = input("Please Enter ip: ")
    port = int(input("Please enter port number: "))


    #call to function and pass these two value ip and port
    UDP_sender(ip, port)
