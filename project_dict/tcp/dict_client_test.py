"""
网络词典 客户端
"""
from  socket import *

sockfd = socket()
ADDR =("176.215.155.137",8888)
sockfd.connect(ADDR)
while True:
    data = input("Msg:")
    if not data:break
    sockfd.send(data.encode())
    news=sockfd.recv(1024).decode()
    print(news)