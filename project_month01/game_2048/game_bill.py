"""
负责处理游戏核心逻辑
    步骤：
    １．创建项目game2048，创建模块game_controller
    ２．将之前完成的面向过程的核心算法,移动到GameController类
    数据作为实例变量，操作作为实例方法
    3.产生新数字
        在随机的空白位子（零元素）上
        产生随机的数字（2的概率９０％　4的概率１０％）
    4.判断游戏是否结束
        如果有空位置不能结束
        若果水平方向,相邻具有相同元素，不能结束
        若果垂直方向,相邻具有相同元素，不能结束
        以上都不满足
    5.完成GameConsoleView
    6.重构update方法
    7.如果地图没有变化，则不生成新数字/不更新地图

"""
import copy
import random

from project_month01.game_2048.game_model import LocationModel, MoveDirection


class GameController:
    """
    负责处理游戏的核心逻辑
    """

    def __init__(self):
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_merge = [2, 4, 16, 8]
        self.__list_empty_location = []
        self.__is_change = False
    @property
    def is_change(self):
        return self.__is_change


    @property
    def map(self):
        return self.__map  # 类外可以修改 map[0][1] = 100
        # return copy.deepcopy(self.__map)#返回深拷贝,不可修改源数据

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):  # 0  1  2
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
        向左移动
        :return:
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
        向右移动
        :return:
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    # 5. 向上移动
    def move_up(self):
        """
        向上移动
        :return:
        """
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    # 6. 向下移动
    def move_down(self):
        """
        向下移动
        :return:
        """
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            矩阵转置
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = \
                    self.__map[c - 1][r], self.__map[r][c - 1]

    def new_element(self):
        """
        生成新元素
        :return:
        """
        self.__calculate_empty_locataon()
        if len(self.__list_empty_location) == 0: return
        random_location = random.choice(self.__list_empty_location)
        self.__map[random_location.r][random_location.c] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.remove(random_location)

    def __calculate_empty_locataon(self):
        """
        计算空位置
        :return:
        """
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(LocationModel(r, c))


    def judge_end(self):
        """
        False游戏结束
        :return:

            判断游戏是否结束
        :return: True 游戏结束　　False　游戏不结束
        """
        if len(self.__list_empty_location): return False

        # 水平方向判断　的同时　垂直方向判断
        for r in range(4):
            for c in range(3):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False

        return True  # 以上条件都不满足，则游戏结束

        """
        # 水平方向
        for r in range(4):
            for c in range(3):
                if self.__map[r][c] == self.__map[r][c + 1]:
                    return False
        # 垂直方向
        for c in range(4):
            for r in range(3):
                if self.__map[r][c] == self.__map[r + 1][c]:
                    return False
        """
    def move(self,move_direction):
        original_map = copy.deepcopy(self.__map)
        if move_direction==MoveDirection.UP:
            self.move_up()
        elif move_direction==MoveDirection.LEFT:
            self.move_left()
        elif move_direction==MoveDirection.DOWN:
            self.move_down()
        elif move_direction==MoveDirection.RIGHT:
            self.move_right()
        self.__is_change= self.__map != original_map#True代表有变化
