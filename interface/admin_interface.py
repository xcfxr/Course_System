from db import models

def register_interface(name, pwd):
    admin_obj = models.Admin.load(name)
    if admin_obj:
        return False, '创建失败，该管理员用户已存在！'
    else:
        admin_obj = models.Admin(name, pwd)
        admin_obj.save()
        return True, f'管理员用户[{name}]创建成功！'


def login(name, pwd):
    admin_obj = models.Admin.load(name)
    if admin_obj:
        if pwd == admin_obj.pwd:
            return True, f'管理员用户[{name}]登陆成功！'
        else:
            return False, f'登录失败， 密码错误！'
    else:
        return False, f'登录失败，管理员用户[{name}]不存在！'


def create_school_interface(admin, name, address):
    school_obj = models.School.load(name)
    if school_obj:
        return False, f'创建失败， 学校[{name}]已存在！'
    admin_obj = models.Admin.load(admin)
    admin_obj.create_school(name, address)
    return True, f'学校[{name}]创建成功！'


def create_course_interface(admin, school, course):
    school_obj = models.School.load(school)
    if not school_obj:
        return False, f'创建课程失败，学校[{school}]不存在！'
    admin_obj = models.Admin.load(admin)
    if course in (each for each in school_obj.courses):
        return False, f'创建课程失败，学校[{school}]已存在课程[{course}]'
    admin_obj.create_course(school_obj, course)
    return True, f'学校[{school}]创建课程[{course}]成功'


def create_teacher_interface(admin, name, pwd):
    teacher_obj = models.Teacher.load(name)
    if teacher_obj:
        return False, f'讲师[{name}]已存在!'
    admin_obj = models.Admin.load(admin)
    admin_obj.create_teacher(name, pwd)
    return True, f'讲师[{name}]创建成功！'
