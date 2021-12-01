from interface import admin_interface
from lib import common


def register():
    while True:
        usr = input('请输入用户名：')
        if usr == 'q':
            break
        pwd = input('请输入密码：')
        re_pwd = input('请确认密码：')
        if pwd != re_pwd:
            print('两次密码输入不一致，请重试')
        flag, msg = admin_interface.register_interface(usr, pwd)
        print(msg)
        if flag:
            break


def login():
    while True:
        usr = input('请输入用户名：')
        if usr == 'q':
            break
        pwd = input('请输入密码：')
        flag, msg = admin_interface.login(usr, pwd)
        print(msg)
        if flag:
            login_dict['name'] = usr
            break


login_dict = {
    'name': None,
    'login': login
}


@common.login_auth(login_dict)
def create_school():
    while True:
        name = input('请输入学校名称：')
        if name == 'q':
            break
        address = input('请输入学校地址：')
        flag, msg = admin_interface.create_school_interface(login_dict['name'], name, address)
        print(msg)
        if flag:
            break


@common.login_auth(login_dict)
def create_course():
    while True:
        school_name = input('请选择创建课程的学校：')
        if school_name == 'q':
            break
        course_name = input('请输入创建课程的名称：')
        flag, msg = admin_interface.create_course_interface(login_dict['name'], school_name, course_name)
        print(msg)
        if flag:
            break


@common.login_auth(login_dict)
def create_teacher():
    while True:
        name = input('请输入讲师的名字：')
        if name == 'q':
            break
        pwd = input('请输入讲师的密码：')
        flag, msg = admin_interface.create_teacher_interface(login_dict['name'], name, pwd)
        print(msg)
        if flag:
            break


func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def run():
    while True:
        print('''
        =======欢迎来到管理员界面=======
            1.注册
            2.登录
            3.创建学校
            4.创建课程（先选择学校）
            5.创建讲师
        ============end=================
        ''')
        choice = input('请输入您的选择：')
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误请重新输入')
            continue
        func_dict[choice]()
