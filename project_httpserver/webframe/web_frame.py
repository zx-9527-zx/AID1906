"""
模拟网站的后端运用
"""
import sys, json
from select import *

sys.path.append('/home/tarena/AID1906/month01/code/project_httpserver')
from socket import *
from webframe.setting import *
import os
from  webframe.urls import *


# 应用类,实现具体的后端功能
class Application:
    def __init__(self):
        self.port = PORT
        self.host = HOST
        self.dir = DIR
        self.fdmap = {}
        self.ep = epoll()
        self.address = (HOST, PORT)
        # 直接创建出套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.s = socket()
        # 端口重用
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.s.bind(self.address)
        self.s.listen(5)

    # 程序入口,启动服务
    def start(self):
        print("等待链接%d:" % self.port)
        # 关注sockfd
        self.ep.register(self.s, EPOLLIN)
        self.fdmap[self.s.fileno()] = self.s
        while True:
            events = self.ep.poll()
            for fd, event in events:
                if fd == self.s.fileno():
                    connfd, addr = self.s.accept()
                    self.ep.register(connfd)
                    self.fdmap[connfd.fileno()] = connfd
                else:
                    self.handle(self.fdmap[fd])
                    self.ep.unregister(fd)
                    del self.fdmap[fd]

    # 处理请求
    def handle(self, connfd):
        data = connfd.recv(4069).decode()
        data = json.loads(data)
        #data---> {'method':'GET','info':'xxx'}
        if data['method'] == 'GET':
            if data['info'] == "/" or data['info'][-5:] == ".html":
                self.get_html(connfd, data)
            else:
                self.get_data(connfd)
        elif data['method'] == 'POST':
            pass

    # 发送具体请求页面
    def get_html(self, connfd, data):
        if os.path.exists(self.dir + data['info']):
            with open(self.dir + data['info']) as file:
                response = json.dumps({'status': '200', 'data': '%s' % file.read()})
                connfd.send(response.encode())
        else:
            self.get_data(connfd)

    # 处理请求页面不存在,返回404.html
    def get_data(self, connfd):
        file = open(self.dir + '404.html','r')
        data = file.read()
        response = json.dumps({'status': '404', 'data': '%s' % data})
        connfd.send(response.encode())


if __name__ == '__main__':
    app = Application()
    app.start()
