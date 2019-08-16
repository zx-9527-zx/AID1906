"""
    project_month01/game_2048_core.py
    2048 游戏核心算法
"""
# 1. 定义零元素后移函数
# [2,0,0,2]  --> [2,2,0,0]
# [2,0,4,2]  --> [2,4,2,0]
# 14:10
list_merge =[2,16,0,4]

def zero_to_end():
    # 思想：从后向前，如果是零元素，删除后末尾追加零.
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

# 测试...
# zero_to_end()
# print(list_merge)

#2. 定义合并相同元素的函数
# [2,2,0,0]  --> [4,0,0,0]
# [2,0,0,2]  --> [4,0,0,0]
# [2,0,2,2]  --> [4,2,0,0]
# [0,2,2,4]  --> [4,4,0,0]
# [2,2,2,2]  --> [4,4,0,0]
# 14：32
def merge():
    zero_to_end()
    for i in range(len(list_merge)-1):#0  1  2
        # 如果相邻 还 相同
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] *=2
            del list_merge[i+1]
            list_merge.append(0)

# merge()
# print(list_merge)

# 3. 向左移动
map = [
    [2,0,0,2],
    [2,2,0,4],
    [0,4,0,4],
    [2,2,2,0],
]
def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()

# move_left()
# print(map)

# 4. 向右移动
def move_right():
    global list_merge
    for line in map:
        # 切片会产生新列表
        list_merge = line[::-1]
        # 合并操作的就是新列表
        merge()
        # 将新列表中的数据赋值给map中的行
        line[::-1] = list_merge

# move_right()
# print(map)

# 5. 向上移动
def move_up():
    square_matrix_transpose()
    move_left()
    square_matrix_transpose()

# 6. 向下移动
def move_down():
    square_matrix_transpose()
    move_right()
    square_matrix_transpose()

def square_matrix_transpose():
    """
        矩阵转置
    """
    for c in range(1, len(map)):
        for r in range(c, len(map)):
            map[r][c - 1], map[c - 1][r] = map[c - 1][r], map[r][c - 1]

# move_down()
# print(map)


