#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 3  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    用SQLAchemy模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# 初始化数据库连接:
engine = create_engine('mysql+cymysql://root:root@localhost:3306/exercise')
# 创建对象的基类:
Base = declarative_base()

#定义Word对象:
class Word(Base):
    # 表的名字:
    __tablename__ = 'word'

    # 表的结构:
    id = Column(String(10), primary_key=True)
    content = Column(String(50))
    name = Column(String(10))
    time = Column(String(10))
    is_delete = Column(Integer)
try:
    Word.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新Leaword对象:
    # new_word1 = Word(id='101', content='python', name='Alice', time='2020-5-6', is_delete=0)
    # new_word2 = Word(id='102', content='C++', name='Bob', time='2020-4-26', is_delete=0)
    # new_word3 = Word(id='103', content='Java', name='Cindy', time='2020-3-13', is_delete=0)

    # 添加到session:
    # session.add(new_word1)
    # session.add(new_word2)
    # session.add(new_word3)

    # 查询

    # 修改
    # target = session.query(Word).filter(Word.name == "Alice").first()
    # target.name = "Kimmy"
    # 删除
    # target = session.query(Word).get("101")
    # session.delete(target)
    result = session.query(Word).filter(Word.id=='103').one()
    print(result.name)

    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
except Exception as e:
    print(e)

