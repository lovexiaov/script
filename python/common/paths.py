# coding: utf-8
"""
This is module docs.
"""
__author__ = u'lovexiaov'

import os

# get the parent dir of current path
print(os.path.dirname(__file__))


def get_abs_project_path(file_, depth):
    """
    Get the abs path of the project root dir.
    :param file_: You should pass `__file__`
    :param depth: How depth your current file away from the project root. Must be an integer whose value >= 0, if it was 1, that says it was in a sub directory of the project.
    :return: the abs path of the project root dir
    """
    file_path = os.path.realpath(file_)
    if (isinstance(depth, int) and depth >= 0):
        parent_dir = os.path.dirname(file_)
        for i in range(depth):
            parent_dir = os.path.dirname(parent_dir)

        return parent_dir

if __name__ == u'__main__':
    print(get_abs_project_path(__file__, 1))
