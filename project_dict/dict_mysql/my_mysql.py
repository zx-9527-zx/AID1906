"""
dict 所有数据库的交互
提供数据库的交互,以及数据库操作
"""
import pymysql
import hashlib

salt = b"*#06#"  # 机密专用盐


class MySql:
    def __init__(self):
        # 链接数据库
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8")
        # 创建游标
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        # 判断用户名
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        resule = self.cur.fetchone()
        if resule:
            return False

        passwd = self.encryption(passwd)

        # 插入用户
        try:
            sql = "insert into user (name,passwd) values (%s,%s)"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 加密处理函数
    def encryption(self, passwd):
        # 对密码进行加密处理
        hash = hashlib.md5(salt)
        hash.update(passwd.encode())
        passwd = hash.hexdigest()  # 获取存储密码
        return passwd

    def login(self, name, passwd):
        passwd = self.encryption(passwd)
        sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return True
        else:
            return False

    def check(self, words):
        sql = "select mean from words where word = '%s'" % words
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return result
        else:
            return False

    def insert_hist(self,name,word):
        try:
            sql = "insert into hist (name , word) values (%s,%s)"
            self.cur.execute(sql, [name, word])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def view_hist(self):
        sql = "select * from hist order by id desc limit 10"
        self.cur.execute(sql)
        result = self.cur.fetchmany(10)
        return result
