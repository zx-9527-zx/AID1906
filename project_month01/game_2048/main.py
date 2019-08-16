"""
游戏入口
"""
from project_month01.game_2048.game_usl import GameConsoleView

#必须是主模块才执行　
if __name__ == '__main__':
    view  = GameConsoleView()
    view.star()
    view.update()
