import socket
from multiprocessing import Pool


socket.setdefaulttimeout(100000)
import time
response_str = 'Hello World!'*10

def server_program():

    pool = Pool(100)
    print('v2 server socket start!')
    print('---'*10)
    # get the hostname
    host = '127.0.0.1'
    port = 9999

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1000)

    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        pool.apply_async(func=handle_con, args=(conn,))
    print('---'*10)
    print('v2 server socket end!')


def handle_con(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        conn.send(response_str.encode())  # send data to the client
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()