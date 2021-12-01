from interface import teacher_interface
from lib import common


def login():
    while True:
        usr = input('请输入用户名：')
        pwd = input('请输入密码：')
        flag, msg = teacher_interface.login_interface(usr, pwd)
        print(msg)
        if flag:
            login_dict['name'] = usr
            break


login_dict = {
    'name': None,
    'login': login,
}


@common.login_auth(login_dict)
def check_course():
    teacher_interface.check_course_interface(login_dict['name'])


@common.login_auth(login_dict)
def choose_course():
    while True:
        school_name = input('请输入选择的校区：')
        if school_name == 'q':
            break
        course_name = input('请输入选择的课程：')
        flag, msg = teacher_interface.choose_course_interface(login_dict['name'], school_name, course_name)
        print(msg)
        if flag:
            break


@common.login_auth(login_dict)
def check_students_of_course():
    while True:
        school_name = input('请输入查询的校区：')
        if school_name == 'q':
            break
        course_name = input('请输入查询的课程：')
        flag, msg = teacher_interface.check_student_of_course_interface(login_dict['name'], school_name, course_name)
        print(msg)
        if flag:
            break


@common.login_auth(login_dict)
def modify_grade():
    while True:
        stu_name = input('请输入需修改学生的姓名：')
        course_name = input('请输入需要修改的课程：')
        score = input('请输入需要修改的分数：')
        if not score.isdigit():
            print("分数必须为整数，请重新输入")
            continue
        score = int(score)
        flag, msg = teacher_interface.modify_grade_interface(login_dict['name'], stu_name, course_name, score)
        print(msg)
        if flag:
            break


func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_students_of_course,
    '5': modify_grade,
}


def run():
    while True:
        print('''
        =======欢迎来到教师界面==========
            1.登录
            2.查看教授课程
            3.选择教授课程
            4.查看该课程下的学生
            5.修改学生分数
        ===========end==================
        ''')
        choice = input('请输入您的选择：')
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue
        func_dict[choice]()
