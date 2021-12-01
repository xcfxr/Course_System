from core import student
from core import admin
from core import teacher

fun_dict = {
    '1': admin.run,
    '2': student.run,
    '3': teacher.run,
}


def run():
    while True:
        print('''
        =====欢迎来到选课系统=========
            1.管理员功能
            2.学生功能
            3.教师功能
        ===========end==================
        ''')
        choice = input('请输入您的选择：')
        if choice == 'q':
            break
        if choice not in fun_dict:
            print('输入有误，请重新输入')
            continue
        fun_dict[choice]()
