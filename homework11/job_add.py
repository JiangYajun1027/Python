#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区该职位的平均薪酬

from config import *

def add(a,b,c,d):
    try:

        # 创建新对象:
        new_jobinfo = Jobinfo(position=a, company=b, site=c, wages=d)

        session=creare_session()
        # 添加到session:
        session.add(new_jobinfo)
        commit_session(session)

        # 关闭session:
        session.close()

    except Exception as e:
        print(e)
