from db import models


def modify_grade_interface(teacher_name, stu_name, course_name, score):
    student_obj = models.Student.load(stu_name)
    if not student_obj:
        return False, f'该学生[{stu_name}]不存在'
    if course_name not in student_obj.courses:
        return False, f'学生[{stu_name}]并未选择课程[{course_name}]'
    teacher_obj = models.Teacher.load(teacher_name)
    teacher_obj.modify_score(student_obj, course_name, score)
    return True, f'修改学生[{stu_name}]课程[{course_name}]的成绩为[{score}]分'


def choose_course_interface(teacher_name, school_name, course_name):
    school_obj = models.School.load(school_name)
    if not school_obj:
        return False, f'校区[{school_name}]不存在'
    if course_name not in school_obj.courses:
        return False, f'校区[{school_name}]不存在课程[{course_name}]'
    teacher_obj = models.Teacher.load(teacher_name)
    teacher_obj.choose_course(school_name, course_name)
    return True, f'教师用户[{teacher_name}]成功选择[{school_name}]校区的[{course_name}]课程'


def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.load(teacher_name)
    if teacher_obj.courses:
        teacher_obj.check_courses()
        return True, "查询成功"
    else:
        return False, "该教师暂未选择任何课程，查询失败"


def check_student_of_course_interface(teacher_name, school_name, course_name):
    school_obj = models.School.load(school_name)
    if not school_obj:
        return False, f'校区[{school_name}]不存在'
    if course_name not in school_obj.courses:
        return False, f'校区[{school_name}]不存在课程[{course_name}]'
    teacher_obj = models.Teacher.load(teacher_name)
    teacher_obj.check_student_of_course(school_name, course_name)
    return True, "查询成功"


def login_interface(teacher_name, pwd):
    student_obj = models.Teacher.load(teacher_name)
    if student_obj:
        if pwd == student_obj.pwd:
            return True, f"教师用户[{teacher_name}]登录成功"
        else:
            return False, f"教师用户[{teacher_name}]登录失败， 密码错误"
    else:
        return False, f"教师用户[{teacher_name}]登录失败，该用户不存在"
