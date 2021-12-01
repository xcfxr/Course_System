import os.path
from functools import wraps
BASE_PATH = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_PATH, 'db')


def login_auth(login_dict):
    def auth(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if login_dict['name']:
                res = func(*args, **kwargs)
                return res
            else:
                print('执行功能失败，请先登录')
                login_dict['login']()
        return inner
    return auth
