from db import db_handler


class IOMixin:
    @classmethod
    def load(cls, name):
        return db_handler.load(cls, name)

    def save(self):
        db_handler.save(self)


class Admin(IOMixin):
    """
        - 1.注册
        - 2.登录
        - 3.创建学校
        - 4.创建课程（先选择学校）
        - 5.创建讲师
    """

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def create_school(self, name, address):
        school_obj = School(name, address)
        school_obj.save()

    def create_course(self, school_obj, course):
        course_name = f'{school_obj.name}_{course}'
        school_obj.courses.append(course)
        Course(course_name).save()
        school_obj.save()

    def create_teacher(self, name, pwd):
        teacher_obj = Teacher(name, pwd)
        teacher_obj.save()


class School(IOMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.courses = []


class Student(IOMixin):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school = None
        self.courses = []
        self.scores = {}

    def choose_school(self, school_name):
        self.school = school_name
        self.save()

    def choose_course(self, course_name):
        self.courses.append(course_name)
        self.scores[course_name] = 0
        self.save()

    def check_score(self, course_name):
        return self.scores[course_name]


class Course(IOMixin):
    def __init__(self, name):
        self.name = name
        self.students = []

    def relate_student(self, stu_name):
        self.students.append(stu_name)
        self.save()


class Teacher(IOMixin):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.courses = []

    def check_courses(self):
        print("您所教授的课程有：")
        for idx, course in enumerate(self.courses):
            school_name, course_name = course.split('_')
            print(f'{idx + 1}:{school_name} {course_name}', end=' ')

    def choose_course(self, school_name, course_name):
        self.courses.append(f'{school_name}_{course_name}')
        self.save()

    def modify_score(self, stu_obj, course_name, score):
        stu_obj.scores[course_name] = score
        stu_obj.save()

    def check_student_of_course(self, school_name, course_name):
        course_obj = Course.load(f'{school_name}_{course_name}')
        print('选择该课程的学生有：')
        for idx, student in enumerate(course_obj.students):
            print(f'{idx + 1}:{student}')
