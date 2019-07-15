# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/10 6:26

import pymysql
import tools.config_tool as config_tool


def connect():
    conf = config_tool.ConfigTool()
    db_info = conf.get_db_dict('DB_GY')
    print(type(db_info))
    conn = pymysql.connect(**db_info)
    return conn


def query_one(sql):
    conn = connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        # 执行sql语句
        cursor.execute(sql)
        row = cursor.fetchone()
        return row
    except Exception as  e:
        # 如果执行sql语句出现问题，则执行回滚操作
        print(e)
    finally:
        # 不论try中的代码是否抛出异常，这里都会执行
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()