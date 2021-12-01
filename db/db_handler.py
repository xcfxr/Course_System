import os
import pickle

from conf import settings


def load(cls, name):
    load_path = os.path.join(settings.DB_PATH, cls.__name__, f'{name}.pkl')
    if os.path.exists(load_path):
        with open(load_path, 'rb') as fp:
            return pickle.load(fp)
    else:
        return None


def save(obj):
    dir_path = os.path.join(settings.DB_PATH, obj.__class__.__name__)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    save_path = os.path.join(dir_path, f'{obj.name}.pkl')
    with open(save_path, 'wb') as fp:
        pickle.dump(obj, fp)