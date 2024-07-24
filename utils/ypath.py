import os
import re


def files(path, pattern=r'.*', rescursion=False, full=True, ret=[]):
    """
    返回指定路径下的所有文件
    :param path:
    :param pattern:
    :param rescursion:
    :param full:
    :param ret:
    :return:
    """
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            if re.match(pattern, item):
                ret.append(item_path if full else item)
        elif rescursion:
            files(item_path, pattern, True, full, ret)
    return ret


def dirs(path, pattern=r'.*', rescursion=False, full=True, ret=[]):
    """
    返回指定路径下的子目录
    :param path:
    :param pattern:
    :param rescursion:
    :param full:
    :param ret:
    :return:
    """
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if re.match(pattern, item):
                ret.append(item_path if full else item)
            if rescursion:
                dirs(item_path, pattern, True, full, ret)
    return ret


def parent_folder(path):
    """
    返回路径的[父文件夹]名称
    :param path:
    :return:
    """
    return os.path.basename(os.path.dirname(path))


def filename(path):
    return os.path.basename(path)


def name_ext(path):
    return os.path.splitext(filename(path))


def join(*args):
    return os.path.join(*args)


def syncfolder(path):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.mkdir(dirname)