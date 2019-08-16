"""
网络词典 服务器server
"""
import os, sys
from time import *
from socket import *
import signal
from project_dict.dict_mysql.my_mysql import *
import pickle

# 创建套接字
sockfd = socket()
# 设置端口重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
ADDR = ("0.0.0.0", 8888)
sockfd.bind(ADDR)
sockfd.listen(5)
mysql = MySql()
print("服务器启动,等待链接:")


# 处理注册
def do_register(connfd, data):
    tmp = data.split(",")
    name = tmp[1]
    passwd = tmp[2]
    bool = mysql.register(name, passwd)
    if bool:
        connfd.send(b"OK")
    else:
        connfd.send(b"False")


# 处理登录
def do_login(connfd, data):
    tmp = data.split(",")
    name = tmp[1]
    passwd = tmp[2]
    bool = mysql.login(name, passwd)
    if bool:
        connfd.send(b"OK")
    else:
        connfd.send(b"False")


# 处理查询单词
def do_check(connfd, data):
    name = data.split(",")[-1]
    while True:
        data = connfd.recv(1024).decode()
        if not data or data=="No":
            return
        mysql.insert_hist(name, data)
        data = mysql.check(data)
        if data:
            print(data)
            connfd.send(data[0].encode())
        else:
            connfd.send("单词不存在!".encode())

def do_hist(connfd):
    result =mysql.view_hist()
    if not result:
        connfd.send("False")
    else:
        result=pickle.dumps(result)
        connfd.send(result)


# 处理请求
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data or data == "E":
            connfd.close()
            sys.exit("客户端退出!")
        elif data[0] == "1":
            do_register(connfd, data)
        elif data[0] == "0":
            do_login(connfd, data)
        elif data[0] == "3":
            connfd.send(b"OK")
            do_check(connfd, data)
        elif data[0] == "4":
            do_hist(connfd)


def main():
    while True:
        try:
            connfd, addr = sockfd.accept()
            print(addr, "已连接")
        except KeyboardInterrupt:
            print("服务器退出")
            mysql.close()
            os._exit(0)
            break
        except Exception:
            pass
        pid = os.fork()
        if pid < 0:
            print("Error")
        elif pid == 0:
            sockfd.close()
            handle(connfd)
        else:
            pass

    sockfd.close()


if __name__ == '__main__':
    main()
