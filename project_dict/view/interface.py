class Interface:
    def __init__(self):
        pass


    def main_interface(self):
        print("""
================================
            网络词典
[0] 登录    [1] 注册  [2] 退出
================================       
        """)

    def handle_interface(self):
        print("""
================================
            网络词典
[3] 查询单词          [4] 历史记录
[5] 注销登录 
================================         
        """)


if __name__ == '__main__':
    s = Interface()
    s.main_interface()
    s.handle_interface()