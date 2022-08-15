#!/usr/bin/env python3
import asyncio
import socket
socket.setdefaulttimeout(100000)
import time
request_str = 'Hello World!'*10


def client(id, request_str):
    HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
    PORT = 9000        # 服务器使用的端口

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f'client{id},data:{request_str}'.encode())
        response_str = s.recv(1024)
        print('Received', repr(response_str))

if __name__ == "__main__":
    # 实验
    client_num = 3000

    start_time = time.time()
    for client_id in range(client_num):
        client(client_id, request_str)
    end_time = time.time()

    print(f'cost time:{end_time-start_time}')