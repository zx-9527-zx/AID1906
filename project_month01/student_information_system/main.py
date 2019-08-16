
"""
练习：将学生管理系统，分为４个模块
    game_model.py-------->xxxxModel
    数据模型
    bll.py--------->xxxController
    业务逻辑层business logic　layer
    usl.py-------->xxxView
    界面　处理层user show layer
    main.py ------->调用xxxxView的代码
    程序入口
"""
from usl import StudentManagerView
if __name__ == "__main__":
    StudentManagerView().main()
