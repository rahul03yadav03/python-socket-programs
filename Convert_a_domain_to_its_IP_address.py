#import the socket library
import socket


#now make a function which convert domain to ip
def domain_to_ip(domain):

    # Try to resolve the domain name using DNS
    try:

        ip = socket.gethostbyname(domain)
        
        print(f"The IP for domain {domain} is {ip}")

     # Handle error if the domain name is invalid or DNS lookup fails
    except socket.gaierror:
        print("Invalid domain name or DNS lookup failed")


# Run the program only when this file is executed directly
if __name__ == "__main__":

    # Ask the user to enter a domain name
    domain = input("Please enter domain name: ")

    # Call the function to convert domain to IP
    domain_to_ip(domain)
