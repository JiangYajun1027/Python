#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区该职位的平均薪酬

import requests
from bs4 import BeautifulSoup
import re
from sqlalchemy import Column, String, Double, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# 初始化数据库连接:
engine = create_engine('mysql+cymysql://root:root@localhost:3306/exercise')
# 创建对象的基类:
Base = declarative_base()

#定义Jobinfo对象:
class Jobinfo(Base):
    # 表的名字:
    __tablename__ = 'jobinfo'

    # 表的结构:
    position = Column(String(20))
    company = Column(String(50))
    site = Column(String(20))
    wages = Column(Double)

try:

    Jobinfo.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新Leaword对象:
    # new_word1 = Word(id='101', content='python', name='Alice', time='2020-5-6', is_delete=0)

    # 添加到session:
    # session.add(new_word1)

    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
except Exception as e:
    print(e)