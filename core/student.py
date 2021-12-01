from lib import common
from interface import student_interface

'''
    - 1.注册
    - 2.登录功能
    - 3.选择校区
    - 4.选择课程（先选择校区，在选择校区中的一门课程）
        - 学生选择课程，课程绑定学生
    - 5.查看分数
'''


def register():
    while True:
        usr = input('请输入用户名：')
        pwd = input('请输入密码：')
        re_pwd = input('请确认密码：')
        if pwd != re_pwd:
            print('两次密码输入不一致，请重试')
            continue
        flag, msg = student_interface.register_interface(usr, pwd)
        print(msg)
        if flag:
            break


def login():
    while True:
        usr = input('请输入用户名：')
        pwd = input('请输入密码：')
        flag, msg = student_interface.login_interface(usr, pwd)
        print(msg)
        if flag:
            login_dict['name'] = usr
            break


login_dict = {
    'name': None,
    'login': login,
}


@common.login_auth(login_dict)
def choose_school():
    while True:
        school_name = input("请输入选择的学校名称：")
        flag, msg = student_interface.choose_school_interface(login_dict['name'], school_name)
        print(msg)
        if flag:
            break


@common.login_auth(login_dict)
def choose_course():
    while True:
        course_name = input('请输入选择的课程名：')
        if course_name == 'q':
            break
        flag, msg = student_interface.choose_course_interface(login_dict['name'], course_name)
        print(msg)
        if flag:
            break


@common.login_auth(login_dict)
def check_grade():
    while True:
        course_name = input('请输入所要查询课程名：')
        flag, msg = student_interface.check_grade(login_dict['name'], course_name)
        print(msg)
        if flag:
            break


func_dict = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_grade,
}


def run():
    while True:
        print('''
        =======欢迎来到学生界面========
            1.注册
            2.登录
            3.选择校区
            4.选择课程
            5.查看分数
        ''')
        choice = input('请输入你的选择：')
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误')
        func_dict[choice]()
