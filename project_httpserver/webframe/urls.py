"""
路由模块　声明客户端能够请求的数据
"""
from webframe.view import *
urls = [
    ('/time',show_time),
    ('/guonei',guonei),
    ('/guoji',guoji)
]