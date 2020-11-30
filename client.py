# Name:   Steve Owens               Date:   11/29/2020
# Class:  CS 372 - 400
#
# Credit:
# Server and client source does developed from examples provided
# from: Beazley, David M. (2009). Python Essential Reference 4th Edition.
# Addison Wesley Publishing

# Code syntax and structure adapted from source code found at https://www.
# geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-
# module/


from socket import *
import sys

def connect_host(port=0):

    if port == 0:
        port = int(input('Enter port number of server: '))


    total_recv = 0
    target_host = 'localhost'
    target_port = int(port)

    


    # Create a client TCP/IP socket
    client = socket(AF_INET, SOCK_STREAM)

    # Connect socket to the server
    server_address = (target_host, target_port)
    client.connect(server_address)

    print(f'Connected to: {target_host} on port: {target_port}')

    try:
        # Send message to chat server
        print(f'Type /q to quit')
        msg = input('Enter message to send...\n>')
        
        if not msg == '/q':
            client.send(msg.encode())

            # Handle response from server
            response = client.recv(1024)
            resp_len = len(response)

            # Print response to the console
            print(response.decode())

            # Continue to read from socket until recv is zero
            while resp_len > 0 and not response == '/q':
                msg = input(f'>')
                if msg == '/q':
                    break
                client.send(msg.encode())
                response = client.recv(1024)
                resp_len = len(response)
                print(response.decode())

        print(f'Connection closed by server')   

    finally:
        client.close()


if __name__ == '__main__':

    if len(sys.argv) > 2:
        print(f'usage: python3 client.py <server_port>')
        print(f'   or: python3 client.py')

    elif len(sys.argv) == 2:
        connect_host(sys.argv[1])

    else:
        connect_host()