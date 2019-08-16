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
