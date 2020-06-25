#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区该职位的平均薪酬

import requests
from bs4 import BeautifulSoup
import job_add
from multiprocessing import Pool
import time

def getHtml(url,index):
    try:
        dicx = {}
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
        try:
            response = requests.get(url, headers=headers)
        except:
            print('faild:%s' % url)
        response.raise_for_status()
        # print(response.status_code)
        response.encoding = response.apparent_encoding
        txt = response.text
        # print(txt)
        soup = BeautifulSoup(txt, "html.parser")
        label = soup.select("a")
        # print(label)

        for i in range(1, 50):
            x = soup.find_all(class_='t1')[i].text
            y = str(x).split()
            dicx['position'] = ''.join(y)
            try:
                dicx['company'] = soup.find_all(class_='t2')[i].text
            except:
                dicx['company'] = ''
            try:
                dicx['site'] = soup.find_all(class_='t3')[i].text
            except:
                dicx['site'] = ''
            try:
                dicx['wages'] = soup.find_all(class_='t4')[i].text
            except:
                dicx['wages'] = ''
            # print(dicx)
            # print('**********************************************')

            print('start:%d' % index)
            job_add.add(dicx['position'], dicx['company'], dicx['site'], dicx['wages'])
            time.sleep(3)
            print('insert success!')
            print('end:%d' % index)

    except Exception as error:
        pass
        print(error)

if __name__ == '__main__':
    urllist=[]
    baseurl='https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,'
    for i in range(1,39):
        url=baseurl+str(i)+'.html?'
        urllist.append(url)

    pool = Pool(processes=4)
    num = len(urllist)
    for i in range(0, 4):
        print(urllist[i])
        pool.apply_async(getHtml, (url, i))

    print('STARTED PROCESS')
    pool.close()
    pool.join()
    print('SUBPROCESS DONE')
