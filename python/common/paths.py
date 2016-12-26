# coding: utf-8
"""
This is module docs.
"""
__author__ = u'lovexiaov'

import os

def get_abs_project_path(file_, depth):
    """
    Get the abs path of the project root dir.
    :param file_: You should pass `__file__`
    :param depth: How depth your current file away from the project root. Must be an integer whose value >= 0, if it was 1, that says it was in a sub directory of the project.
    :return: the abs path of the project root dir
    """
    file_path = os.path.realpath(file_)
    if (isinstance(depth, int) and depth >= 0):
        parent_dir = os.path.split(file_path)[0]
        for i in range(depth):
            parent_dir = os.path.split(parent_dir)[0]    

        return parent_dir

if __name__ == u'__main__':
    print(get_abs_project_path(__file__, 1))