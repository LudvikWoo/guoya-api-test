# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/18 18:24

import subprocess

##############################
# 初始化环境：第三方依赖包+果芽工具包
##############################
def init_env():
    cmd = 'pip install --upgrade guoya-api-test'
    try:
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        print(output)
        return o
    except Exception as e:
        print('执行命令失败，请检查环境配置')
        print(e)
        raise

if __name__ == '__main__':
    init_env()
