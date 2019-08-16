"""
数据模型
"""


class LocationModel:
    """
    位置
    """

    def __init__(self, r=0, c=0):
        self.r = r
        self.c = c
class MoveDirection:
    """
    移动方向
    """
    UP =0
    DOWN = 1
    LEFT = 2
    RIGHT = 3