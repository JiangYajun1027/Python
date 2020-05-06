# -*- encoding: utf-8 -*-
'''
@File : mysheet.py
@Time : 2020/05/06 17:31:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；完成对这个表记录的增，删，改，查询；
# 用PyMySQL驱动方式

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
 
# 使用 execute()  方法执行 SQL 查询 
#cursor.execute("create table message (ID  varchar(10), theme  varchar(10), name  varchar(10), time  varchar(10))")
#cursor.execute("insert into message (ID,theme,name,time) values ('101', 'python', 'Alice', '2020-5-6')")
# cursor.execute("insert into message (ID,theme,name,time) values ('102', 'C语言', 'Bob', '2020-4-26')")
# cursor.execute("insert into message (ID,theme,name,time) values ('103', 'Java', 'Cindy', '2020-3-13')")
# cursor.execute("select * from message where ID=101")
# results = cursor.fetchall()
# for row in results:
#     ID = row[0]
#     theme = row[1]
#     name = row[2]
#     time = row[3]
#     # 打印结果
#     print ("ID=%s,theme=%s,name=%s,time=%s" % \
#         (ID, theme, name, time ))
#cursor.execute("update message set theme = 'C++' where theme = 'C语言'")
cursor.execute("delete from message where ID='103'")

db.commit()
 
# 关闭数据库连接
db.close()