#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

#定义Jobinfo对象:
class Jobinfo(Base):
    # 表的名字:
    __tablename__ = 'jobinfo'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    position = Column(String(100))
    company = Column(String(500))
    site = Column(String(100))
    wages = Column(String(100))

# 数据库连接定义
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/jobset?charset=utf8")

Base.metadata.create_all(engine)

def creare_session():
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    return session

def commit_session(session):
    # 提交即保存到数据库:
    session.commit()

# 初始化连接池的容量
POOL_SIZE=5

# 连接池的最大溢出容量： 该容量+初始容量= 最大容量；  超出会堵塞等待，timeout默认值30秒
MAX_OVERFLOW = 10