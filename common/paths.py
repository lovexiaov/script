# coding: utf-8
"""
This is module docs.
"""
__author__ = u'lovexiaov'

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

if __name__ == u'__main__':
    pass