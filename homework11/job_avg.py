#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区该职位的平均薪酬

from config import *
import re

def query():
    try:
        a = 0.0
        b = 0.0
        list1 = []
        list2 = []

        session = creare_session()
        result = session.query(Jobinfo).filter(Jobinfo.site.like("北京%")).all()

        for i in result:
            if '千' in i.wages:
                m = re.split(r'(\d+)', i.wages)
                if m[2] == '-':
                    a = 0.1 * int(m[1])
                    if m[4] != '.':
                        b = 0.1 * int(m[3])
                    else:
                        b = 0.1 * int(m[3]) + 0.01 * int(m[5])
                else:
                    a = 0.1 * int(m[1]) + 0.01 * int(m[3])
                    if m[6] != '.':
                        b = 0.1 * int(m[5])
                    else:
                        b = 0.1 * int(m[5]) + 0.01 * int(m[7])
                a = round(a, 2)
                b = round(b, 2)
                list1.append(a)
                list2.append(b)

            if '天' in i.wages:
                m = re.split(r'(\d+)', i.wages)
                a = int(m[1]) * 30 / 10000
                a = round(a, 2)
                list1.append(a)

            if '年' in i.wages:
                m = re.split(r'(\d+)', i.wages)
                a = int(m[1]) / 12
                b = int(m[3]) / 12
                a = round(a, 2)
                b = round(b, 2)
                list1.append(a)
                list2.append(b)

            if '万/月' in i.wages:
                m = re.split(r'(\d+)', i.wages)
                if m[2] == '-':
                    a = int(m[1])
                    if m[4] != '.':
                        b = int(m[3])
                    else:
                        b = int(m[3]) + 0.1 * int(m[5])
                else:
                    a = int(m[1]) + 0.1 * int(m[3])
                    if m[6] != '.':
                        b = int(m[5])
                    else:
                        b = int(m[5]) + 0.1 * int(m[7])
                a = round(a, 2)
                b = round(b, 2)
                list1.append(a)
                list2.append(b)


        sumx = 0.0
        sumy = 0.0
        for x in list1:
            sumx = sumx + x
        avgx = sumx / len(list1)
        avgx = round(avgx,2)
        for y in list2:
            sumy = sumy + y
        avgy = sumy / len(list2)
        avgy = round(avgy, 2)

        print('北京地区平均工资范围：%.2f-%.2f' % (avgx, avgy))

        # 关闭session:
        session.close()

    except Exception as e:
        print(e)


