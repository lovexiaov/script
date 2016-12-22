# coding: utf-8
import os, sys

# sys.path.append(os.path.join(os.path.abspath(os.getcwd()), 'common'))
# sys.path.append(os.path.join(os.path.abspath(os.getcwd()), 'advanced'))

# import objects
# import decorator

# print(os.path.abspath(os.getcwd()))

def get_abs_project_path(file_, depth):
    """
    Get the abs path of the project root dir.
    :param file_: You should pass `__file__`
    :param depth: How depth your current file away from the project root. Must be a number, if it was 1, that says it was in a sub directory of the project.
    :return: the abs path of the project root dir
    """
    current_path = os.path.realpath(file_)
    print(current_path)
    dirs = os.path.split(current_path)
    print(dirs)
    print(os.path.split(dirs[0]))
