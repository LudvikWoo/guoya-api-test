# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/15 10:46
# !/usr/bin/python


from distutils.core import setup

setup(
    name="guoya-api-test",  # 这里是pip项目发布的名称
    version="1.0.0",  # 版本号，数值大的会优先被pip
    keywords=("api", "tools"),
    description="to simplify api auto test",
    long_description="A tools package,to simplify develope api auto test",
    license="MIT Licence",

    url="https://github.com/LudvikWoo/guoya-api-test",  # 项目相关文件地址，一般是github
    author="wuling",
    author_email="wuling@guoyasoft.com",

    packages=['tools'],
    include_package_data=True,
    platforms="python",
    install_requires=[
        'requests==2.22.0',
        'pymysql==0.9.3',
        'pytest==5.0.1',
        'allure-pytest==2.7.0',
        'xlrd==1.2.0',
        'pinyin==0.4.0'
    ]
)
