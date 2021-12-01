from db import models


def register_interface(stu_name, pwd):
    stu_obj = models.Student.load(stu_name)
    if stu_obj:
        return False, '注册失败，该学生用户已存在！'
    else:
        stu_obj = models.Student(stu_name, pwd)
        stu_obj.save()
        return True, f'学生用户[{stu_name}]注册成功！'


def login_interface(stu_name, pwd):
    student_obj = models.Student.load(stu_name)
    if student_obj:
        if pwd == student_obj.pwd:
            return True, f"学生用户[{stu_name}]登录成功"
        else:
            return False, f"学生用户[{stu_name}]登录失败， 密码错误"
    else:
        return False, f"学生用户[{stu_name}]登录失败，该用户不存在"


def choose_school_interface(stu_name, school_name):
    student_obj = models.Student.load(stu_name)
    school_obj = models.School.load(school_name)
    if not school_obj:
        return False, f"学校[{school_name}]不存在！"
    student_obj.choose_school(school_name)
    return True, f"学生[{stu_name}]选择学校[{school_name}]成功！"


def choose_course_interface(stu_name, course_name):
    student_obj = models.Student.load(stu_name)
    if student_obj.school is None:
        return False, '请先选择学校，不然无法选择课程！'
    school_obj = models.School.load(student_obj.school)
    if course_name not in school_obj.courses:
        return False, f'您所在的学校[{school_obj.name}]并不存在课程[{course_name}]'
    elif course_name in student_obj.courses:
        return False, f'您已选择课程[{course_name}]，请勿重复选择！'
    student_obj.choose_course(course_name)
    course_obj = models.Course.load(f'{school_obj.name}_{course_name}')
    course_obj.relate_student(stu_name)
    return True, f'学生用户[{stu_name}]选择课程[{course_name}]成功'


def check_grade(stu_name, course_name):
    student_obj = models.Student.load(stu_name)
    if course_name not in student_obj.courses:
        return False, f'学生用户[{stu_name}]并没有选择课程[{course_name}]'
    else:
        return True, f'学生用户[{stu_name}]的成绩为[{student_obj.check_score(course_name)}]分'