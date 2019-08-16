"""
用户界面
"""
import os
import copy
from project_month01.game_2048.game_bill import GameController
from project_month01.game_2048.game_model import MoveDirection


class GameConsoleView:
    """
    负责处理界面逻辑
    """
    def __init__(self):
        self.__controller = GameController()

    def star(self):
        self.__controller.new_element()
        self.__controller.new_element()
        self.__print_map()

    def __print_map(self):
        #清空界面
        #os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item,end=" ")
            print()

    def update(self):
        while True:
            #获取输入
            #移动地图
            #产生新数字
            #判断游戏是否结束
            #如果结束，退出循环
            if self.__controller.judge_end():
                print("游戏结束!")
                break

            self.input_control()
            if not self.__controller.is_change:
                continue
            self.__controller.new_element()
            self.__print_map()


    def input_control(self):
        instruction = input("""请输入指令""")
        if instruction == "w":
            self.__controller.move(MoveDirection.UP)
        elif instruction == "a":
            self.__controller.move(MoveDirection.LEFT)
        elif instruction == "s":
            self.__controller.move(MoveDirection.DOWN)
        elif instruction == "d":
            self.__controller.move(MoveDirection.RIGHT)