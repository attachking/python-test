class Student(object):

    def __init__(self):
        self.name = '鸡你太美'
        self.age = 12

    def print_file(self):
        print(self.name)
        print(self.age)
        return self

    @staticmethod
    def sta():
        print()


student = Student()
student.print_file()
print(student)


class BoyStudent(Student):

    count = 0

    def __init__(self):
        super(BoyStudent, self).__init__()
        self.sex = '女'
        self.met()

    @classmethod
    def met(cls):
        cls.count += 1


boy_student = BoyStudent()
boy_student2 = BoyStudent()
boy_student.print_file()
boy_student.met()
BoyStudent.met()
print(BoyStudent.__dict__)
print(boy_student.__dict__)
print(boy_student2.__dict__)
print(boy_student2.count)
print(boy_student.__class__)


class Pro(object):

    # 双下划线开头表示私有属性
    __score = 0

    def __init__(self):
        self.__score = 0

    # 相当于js的Object.defineProperty
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def test(self):
        print(self.__score)


p = Pro()
p.score = 10
p.__score = 4
print('Pro.__dict__:', Pro.__dict__)
print('p.__score:', p.__score)
print('p._Pro__score:', p._Pro__score)
print('p.__dict__:', p.__dict__)
print('score:', p.score)
p.test()
