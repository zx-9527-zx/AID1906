"""
网络词典 客户端
"""
import sys
sys.path.append("/home/tarena/AID1906/month01/code/project_dict")
from socket import *
from view.interface import Interface
import pickle
#from interface import Interface
sockfd = socket()
ADDR = ("176.215.155.137", 8888)
sockfd.connect(ADDR)
view = Interface()

#处理注册
def do_register(sockfd):
    while True:
        name = input("name:")
        passwd = input("passwd:")
        if " " in name or len(passwd) == 0 or len(passwd) > 18:
            print("cd 用户名或密码输入有误!")
            continue
        # 请求类型
        data = "1,%s,%s" % (name, passwd)
        sockfd.send(data.encode())
        data = sockfd.recv(1024).decode()
        if data == "OK":
            print("注册成功!")
            return True
        else:
            print("注册失败!")
            return False

#处理登录
def do_login(sockfd):
    while True:
        name = input("name:")
        passwd = input("passwd:")
        if " " in name or len(passwd) == 0 or len(passwd) > 18:
            print("cd 用户名或密码输入有误!")
            continue
        data = "0,%s,%s" % (name, passwd)
        sockfd.send(data.encode())
        data = sockfd.recv(1024).decode()
        if data == "OK":
            print("登录成功!")
            return name
        else:
            print("登录失败!")
            return False

#处理查单词
def check_words(sockfd,name):
    news ="3,%s"%name
    sockfd.send(news.encode())
    data = sockfd.recv(1024).decode()
    if data=="OK":
        while True:
            data = input("word:")
            if not data:
                sockfd.send(b"No")
                break
            sockfd.send(data.encode())
            data = sockfd.recv(1024).decode()
            print(data)


#查看历史记录
def view_hist(sockfd,name):
    sockfd.send(b"4")
    data = sockfd.recv(1024)
    if data ==b'False':
        print("历史记录为空!")
    else:
        result=pickle.loads(data)
        for item in result:
            print(item)

def Specific_operation(sockfd,name):
    while True:
        view.handle_interface()
        cmd = input("cmd:")
        if cmd == "3":  # 查询单词
            check_words(sockfd,name)
        elif cmd == "4":  # 历史记录
            view_hist(sockfd,name)
        elif cmd == "5":  # 注销登录
            return


def main():
    while True:
        view.main_interface()
        cmd = input("cmd:")
        if cmd == "0":  # 登录
            name=do_login(sockfd)
            if name:
                Specific_operation(sockfd,name)
        elif cmd == "1":  # 注册
            do_register(sockfd)
        elif cmd == "2":  # 退出
            sockfd.send(b"E")
            sockfd.close()
            break


if __name__ == '__main__':
    print(sys.path)
    main()
