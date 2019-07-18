# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/15 10:46
# !/usr/bin/python

from distutils.core import setup

setup(
    name="guoya-api-test",  # 这里是pip项目发布的名称
    version="1.0.7",  # 版本号，数值大的会优先被pip
    keywords=["api", "tools"],
    description="to simplify api auto test",
    long_description="A tools package,to simplify develope api auto test",
    license="MIT Licence",

    url="https://github.com/LudvikWoo/guoya-api-test",  # 项目相关文件地址，一般是github
    author="wuling",
    author_email="wuling@guoyasoft.com",

    packages=['tools'],
    platforms="python",
    install_requires=[

        'allure-pytest==2.7.0',
        'allure-python-commons==2.7.0',
        'atomicwrites==1.3.0',
        'attrs==19.1.0',
        'bleach==3.1.0',
        'certifi==2019.6.16',
        'chardet==3.0.4',
        'colorama==0.4.1',
        'docutils==0.14',
        'idna==2.8',
        'importlib-metadata==0.18',
        'more-itertools==7.1.0',
        'packaging==19.0',
        'pinyin==0.4.0',
        'pkginfo==1.5.0.1',
        'pluggy==0.12.0',
        'py==1.8.0',
        'Pygments==2.4.2',
        'PyMySQL==0.9.3',
        'pyparsing==2.4.0',
        'pytest==5.0.1',
        'readme-renderer==24.0',
        'requests==2.22.0',
        'requests-toolbelt==0.9.1',
        'six==1.12.0',
        'tqdm==4.32.2',
        'twine==1.13.0',
        'urllib3==1.25.3',
        'wcwidth==0.1.7',
        'webencodings==0.5.1',
        'xlrd==1.2.0',
        'zipp==0.5.2'
    ]
)
# 'requests==2.22.0',
#         'pymysql==0.9.3',
#         'pytest==5.0.1',
#         'allure-pytest==2.7.0',
#         'xlrd==1.2.0',
#         'pinyin==0.4.0'
