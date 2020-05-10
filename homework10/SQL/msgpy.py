#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

import pymysql

# 打开数据库连接
db = pymysql.connect(
    "localhost",
    "root",
    "root",
    "exercise"
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

try:
    # sql1='''create table leamsg(ID  varchar(10), content  varchar(50), name  varchar(10), time  varchar(10), is_delete  int)'''
    # sql2='''insert into leamsg (ID,content,name,time,is_delete) values ('101', 'python', 'Alice', '2020-5-6',0)'''
    # sql3='''insert into leamsg (ID,content,name,time,is_delete) values ('102', 'C语言', 'Bob', '2020-4-26',0)'''
    # sql4='''insert into leamsg (ID,content,name,time,is_delete) values ('103', 'Java', 'Cindy', '2020-3-13',0)'''
    # sql5='''select * from leamsg where ID="101"'''
    # cursor.execute(sql5)
    # results = cursor.fetchall()
    # for row in results:
    #     ID = row[0]
    #     content = row[1]
    #     name = row[2]
    #     time = row[3]
    #     is_delete = row[4]
    #     # 打印结果
    #     print ("ID=%s,content=%s,name=%s,time=%s,is_delete=%s" % \
    #         (ID, content, name, time, is_delete ))
    # sql6='''update leamsg set content = "C++" where content = "C语言"'''
    sql7='''delete from leamsg where ID="103"'''
    # cursor.execute(sql1)
    # cursor.execute(sql2)
    # cursor.execute(sql3)
    # cursor.execute(sql4)
    # cursor.execute(sql6)
    cursor.execute(sql7)

    db.commit()

except Exception as e:
    print(e)

# 关闭数据库连接
db.close()