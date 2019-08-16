"""
学生管理系统
1.数据模型类：StudentModel
		数据：编号 id,姓名 name,年龄 age,成绩 score
2.逻辑控制类：StudentManagerController
		数据：学生列表 __stu_list
		行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，修改学生update_student，根据成绩排序order_by_score。
3.界面视图类：StudentManagerView
		数据：逻辑控制对象__manager
		行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
输入学生__input_students，输出学生__output_students，删除学生__delete_student，修改学生信息__modify_student

"""


class StudentModel:
    def __init__(self, name="", age=0, score=0):
        self.id = None
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
    学生管理控制器，对学生的数据进行逻辑处理
    """
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, value):
        """
        添加学生
        :param value:学生对象
        :return:
        """
        value.id = self.__generate_id()
        self.__stu_list.append(value)

    def __generate_id(self):
        """
        生成唯一id
        :return: 返回id
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self,delete_id):
        """
        移除学生信息
        :param delete_id: 学生的id
        :return: 移除成功返回True,错误返回False
        """
        for i in range(len(self.stu_list) - 1, -1, -1):
            if self.stu_list[i].id == delete_id:
                self.__stu_list.remove(self.stu_list[i])
                return True
        return False

    def update_student(self,object): #modify_id,modify_name,modify_age,modify_score（变量传参）
        for i in range(len(self.stu_list)):
            if self.stu_list[i].id == object.modify_id:
                self.stu_list[i].name = object.modify_name
                self.stu_list[i].age = object.modify_age
                self.stu_list[i].score = object.modify_score

    def order_by_score(self,):
        for i in range(len(self.__stu_list) - 1):
            for j in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = self.__stu_list[j], self.__stu_list[i]


class StudentManagerView:
    """
    学生管理视图，处理界面逻辑
    """
    def __init__(self):
       self.__controller = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")

    def __select_menu_item(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名:")
            if not stu.name:
                break
            stu.age = input("请输入年龄:")
            stu.score = input("请输入分数:")
            self.__controller.add_student(stu)

    def __output_students(self):
        for item in self.__controller.stu_list:
            print("id:",item.id,"姓名",item.name,"年龄",item.age,"分数",item.score)

    def __delete_student(self):
        while True:
            delete_id = int(input("请输入删除id："))
            if self.__controller.remove_student(delete_id):
                print("删除成功！")
                break
            else:
                print("删除失败")
    def __modify_student(self):
        stu1 = StudentModel()
        stu1.modify_id = int(input("请输入修改id："))
        stu1.modify_name = input("请输入修改姓名：")
        stu1.modify_age = input("请输入修改年龄：")
        stu1.modify_score = input("请输入修改分数：")
        self.__controller.update_student(stu1)#对象传参
       # 变量传参　self.__controller.update_student(modify_id,modify_name,modify_age,modify_score)
#----------------------------
#测试用例
StudentManagerView().main()

