from model import *
from bll import *


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
            stu.age =self.get_int_info("年龄")
            stu.score = self.get_int_info("分数")
            self.__controller.add_student(stu)

    def __output_students(self):
        for item in self.__controller.stu_list:
            print("id:", item.id, "姓名", item.name, "年龄", item.age, "分数", item.score)

    def __delete_student(self):
        while True:
            delete_id = self.get_int_info("id")
            if self.__controller.remove_student(delete_id):
                print("删除成功！")
                break
            else:
                print("删除失败")

    def __modify_student(self):
        stu1 = StudentModel()
        stu1.modify_id = self.get_int_info("id")
        stu1.modify_name = input("请输入修改姓名：")
        stu1.modify_age =self.get_int_info("年龄")
        stu1.modify_score =self.get_int_info("成绩")
        self.__controller.update_student(stu1)  # 对象传参

    def get_int_info(self, str_target):
        while True:
            try:
                result = int(input("请输入%s："%str_target))
                return result
            except:
                print("输入有误！")
    # 变量传参　self.__controller.update_student(modify_id,modify_name,modify_age,modify_score)
