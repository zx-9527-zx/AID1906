"""
2048 游戏核心算法
"""
# 1.定义零元素后移，其他元素保持不变
import random
list_merge = [2, 0, 2, 2]


def the_zero_retrusive(list_target):
    """

    将列表里面的０元素向后移其他元素保持不变
    :param list_target: 需要操作０元素的列表
    :return:
    """
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            list_target.remove(list_target[i])
            list_target.append(0)


#the_zero_retrusive(list_merge)


#2.定义合并相同元素的函数
#[2,2,0,0]---->[4,0,0,0]
#[2,0,0,2]---->[4,0,0,0]
#[2,0,0,2]---->[4,0,0,0]
#[0,2,2,4]---->[4,4,0,0]
#[2,2,0,0]---->[4,0,0,0]

def add_same_num(list_target):
    """
    将列表里面相邻相同的元素相加（只做一次）
    :param list_target:
    :return:
    """
    the_zero_retrusive(list_target)
    for i in range(len(list_target)-1):
        if list_target[i]==list_target[i+1]:
            list_target[i]+=list_target[i+1]
            del list_target[i+1]
            list_target.append(0)



#3.向左移动
map = [
    [2,0,0,2],
    [2,2,0,4],
    [0,4,0,4],
    [2,2,2,0]
]
def move_left():
    """
    将二维列表里面的所有元素左移，即合并相同元素，０元素后移
    :param list_target:
    :return:
    """
    global list_merge
    for line in map:
        add_same_num(line)


#4.向右移动
def move_right():
    global  list_merge
    for line in map:
        list_merge = line[::-1]
        add_same_num(list_merge)
        line[::-1] = list_merge

# def move_right():
#     for line in map:
#         i=line
#         line= i[::-1]
#         add_same_num(line)
#         i[::-1] =line

#5.向下移动
def move_down():
    transpose_phalanx()
    move_right()
    transpose_phalanx()


#6.向上移动
def move_up():
    transpose_phalanx()
    move_left()
    transpose_phalanx()
#7.矩阵转置
def transpose_phalanx():
    """
    方阵转置的函数
    :param map: 将要被转置的方阵
    :return:
    """
    for row in range(len(map)):
        for col in range(row + 1, len(map)):
            map[row][col], map[col][row] = \
                map[col][row], map[row][col]


#8.打印列表
def print_list(list_target):
    for row in list_target:
        print()
        for col in row:
            print(col, end=" ")

#9.重新生成元素
def new_element(list_target):
    for i in range(2,5,2):
        random_num1 = random.choice(range(0, 4))
        random_num2 = random.choice(range(0, 4))
        if list_target[random_num1][random_num2]==0:
            list_target[random_num1][random_num2]=i

print_list(map)
print()
while True:
    instruction = input("""请输入指令""")

    if instruction=="q":
        break
    elif instruction=="w":
        move_up()
        new_element(map)
        print_list(map)
    elif instruction=="a":
        move_left()
        new_element(map)
        print_list(map)
    elif instruction=="s":
        move_down()
        new_element(map)
        print_list(map)
    elif instruction=="d":
        move_right()
        new_element(map)
        print_list(map)