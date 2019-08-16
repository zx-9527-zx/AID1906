"""
httpserver3.0 服务器
time :2019-08-16 10:13 am
author:zx
"""
import sys

sys.path.append('/home/tarena/AID1906/month01/code/project_httpserver')
from socket import *
from project_httpserver.httpserver.config import *  # 导入配置文件内容
from threading import Thread
import json,re

#负责和webframe交互,socket客户端
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return
    #将env转换为json发送
    data = json.dumps(env)
    s.send(data.encode())
    #接收webframe反馈的数据
    data = s.recv(1024*1024*10).decode()
    return json.loads(data)

class HttpServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST, PORT)
        # 直接创建出套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        # 端口重用
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.sockfd.listen(5)

    # 启动入口
    def server_forever(self):
        print("等待链接%d:" % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                print("客户端退出")
                break
            except Exception:
                pass
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 处理具体请求
    def handle(self,connfd):
        request = connfd.recv(4096).decode()
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'
        try:
            env = re.match(pattern,request).groupdict()
        except:
            connfd.close()
            return
        else:
            #data就是从webframe得到的数据
            data = connect_frame(env)
            self.response(connfd,data)

    def response(self, connfd, data):
        #data --->{'status':'200','data':'xxxxx'}
        if data['status']=='200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders+="Content-Type:text/html\r\n"
            responseHeaders+="\r\n"
            responseBody = data["data"]
        elif data['status']=='404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data["data"]
        #将数据发送给浏览器
        data = responseHeaders+responseBody
        connfd.send(data.encode())


if __name__ == '__main__':
    httpd = HttpServer()
    httpd.server_forever()
