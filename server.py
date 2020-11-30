# Name:   Steve Owens           Date:   11/29/2020
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
from random import *


def init():
    total_recv = 0
    # host_addr = '127.0.0.1'
    host_addr = 'localhost'
    host_port = randint(1023, 65535)

    # Create the listening socket
    sock = socket(AF_INET, SOCK_STREAM)

    # Bind socket to the port
    server_address = (host_addr, host_port)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)


    # Wait for a Connection
    print(f'Server listening on {host_addr} on port: {host_port}')
    
    # Accept request and create a new socket
    connection, client_address = sock.accept()

    try:
        print(f'Connected by {client_address}')
        print(f'Waiting for message...')

        # Read message from client
        read = connection.recv(1024)
        read_len = len(read)

        if read_len == 0:
            print(f'Connection closed by client')

        else:
            # Print response to the console
            print(f'{read.decode()}')
            print(f'Type /q to quit')
            msg = input(f'Enter message to send...\n>')

            while read_len > 0 and not msg == '/q':    
                connection.send(msg.encode())
                read = connection.recv(1024)
                read_len = len(read)
                print(f'{read.decode()}')
                msg = input(f'>')

    finally:
        # Close the connection after sending response
        connection.close()


if __name__ == '__main__':
    init()
