# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/16 9:09
from config import conf
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
import ssl



def test_sign_up():
    url = 'https://www.dev.guoyasoft.com/signup'
    req = {
        "phone": "18716253222",
        "pwd": "aaa123",
        "rePwd": "aaa123",
        "userName": "wuling96"
    }
    # resp = requests.post(url, json=req)
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    print(body)
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)
    data = body['data']
    if data != '':
        user_id = data['userId']
        assert_tool.assert_not_null(user_id)


test_sign_up()