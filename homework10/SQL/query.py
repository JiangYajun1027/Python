#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 1 查询所有男生的姓名，年龄，所在班级名称；
# 2 查询所有查询编号小于4或没被删除的学生；
# 3 查询姓黄并且“名”是一个字的学生；
# 4 查询编号是1或3或8的学生
# 5 查询编号为3至8的学生
# 6 查询未删除男生信息，按年龄降序
# 7 查询女生的总数
# 8 查询学生的平均年龄
# 9 分别统计性别为男/女的人年龄平均值
# 10 按照性别来进行人员分组如下显示（group by + group_concat()）；
#         | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
# 	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
# 	| 中性   | 金星                                                       |
# 	| 保密   | 凤姐                                                       |

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "exercise")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
try:
    sql1='''select name,age,cls_id from students where gender="男"'''
    sql2='''select * from students where id<4 or is_delete=0'''
    sql3='''select * from students where name like "黄_"'''
    sql4='''select * from students where id in(1,3,8)'''
    sql5='''select * from students where id between 3 and 8'''
    sql6='''select * from students where gender="男" and is_delete=0 order by age desc'''
    sql7='''select count(*) from students where gender="女"'''
    sql8='''select avg(age) as avgage from students'''
    sql9='''select avg(age) as avgage,gender from students group by gender'''
    sql10='''select gender,group_concat(name separator ';') from students group by gender'''
    # 使用 execute()  方法执行 SQL 查询
    #cursor.execute(sql1)
    #cursor.execute(sql2)
    #cursor.execute(sql3)
    #cursor.execute(sql4)
    #cursor.execute(sql5)
    #cursor.execute(sql6)
    #cursor.execute(sql7)
    #cursor.execute(sql8)
    #cursor.execute(sql9)
    cursor.execute(sql10)

    # 获取数据.
    results = cursor.fetchall()
    for r in results:
        print(r)
except Exception as e:
    print(e)

# 关闭数据库连接
db.close()