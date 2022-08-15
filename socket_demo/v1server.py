import socket

socket.setdefaulttimeout(100000)
import time
response_str = 'Hello World!'*10

def server_program():

    print('server socket start!')
    print('---'*10)
    # get the hostname
    host = '127.0.0.1'
    port = 9000

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1000)

    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            conn.send(response_str.encode())  # send data to the client
        conn.close()  # close the connection
    print('---'*10)
    print('server socket end!')


if __name__ == '__main__':
    server_program()