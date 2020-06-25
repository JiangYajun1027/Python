#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#给定10万个企业的网址（放在数据库表中），请编写一个网络爬虫，爬取该企业的产品及服务信息（即获取该企业能提供的产品和服务）；
#并将爬取到的数据，保存到数据库中；请自行设计数据库表结构

import requests
from bs4 import BeautifulSoup
import re
from sqlalchemy import Column, String, Integer, TIMESTAMP, Text, BigInteger, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# 初始化数据库连接:
engine = create_engine('mysql+cymysql://root:root@localhost:3306/web')
# 创建对象的基类:
Base = declarative_base()

#定义Webinfo对象:
class Webinfo(Base):
    # 表的名字:
    __tablename__ = 'webinfo'

    # 表的结构:
    autoID = Column(BigInteger, primary_key=True)
    enterpriseID = Column(String(32))
    entid = Column(Integer)
    enterpriseName = Column(String(255))
    web_url = Column(Text)
    addtime = Column(TIMESTAMP)

try:

    Webinfo.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()

    result = session.query(Webinfo).filter(Webinfo.autoID == 1).one()
    print(result.enterpriseName)
    print(result.web_url)

    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
except Exception as e:
    print(e)