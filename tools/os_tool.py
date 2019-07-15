# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/11 18:31
import os

def get_root_path():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)).replace('\\', '/')
    return root_path+'/'

def mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
