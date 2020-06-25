#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区该职位的平均薪酬

import multiprocessing
import requests
from bs4 import BeautifulSoup
import job_add
import job_avg
import time
from multiprocessing import Pool

def data_producer(old_data_queue, key):

    baseurl='https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,'
    for i in range(1, 39):
        url=baseurl+str(i)+'.html?'
        old_data_queue.put(url)

    key.value = 'False'

def getHtml(url,index):
    try:
        print('-------------------------第%d页-------------------------' % index)
        dicx = {}
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
        try:
            response = requests.get(url, headers=headers)
        except:
            print('faild:%s' % url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        txt = response.text
        soup = BeautifulSoup(txt, "html.parser")

        for i in range(1, 51):
            try:
                x = soup.find_all(class_='t1')[i].text
                y = str(x).split()
                dicx['position'] = ''.join(y)
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
            if(dicx['company'] == '' and dicx['site'] == '' and dicx['wages'] == ''):
                break
            print('start:%d' % i)
            job_add.add(dicx['position'], dicx['company'], dicx['site'], dicx['wages'])
            time.sleep(3)
            print('insert success!')
            print('end:%d' % i)

    except Exception as error:
        print(error)

def data_consumer(old_data_queue, key):
    index = 0
    while key.value != 'False' or old_data_queue.empty() == False:

        old_data = old_data_queue.get()
        index += 1
        getHtml(old_data, index)


if __name__ == "__main__":

    consumer = 4
    manager = multiprocessing.Manager()

    # 程序引擎钥匙
    key = manager.Value('c', 'True')

    # 待处理数据队列
    old_data_queue = manager.Queue(10000000)

    # 任务进度队列
    taskProgressQueue = manager.Queue()

    # 生产者进程池
    producerPool = Pool(1)

    # 消费者进程池
    consumerPool = Pool(consumer)

    # 启动生产者
    producerPool.apply_async(data_producer, args=(old_data_queue, key,))

    # 启动消费者
    for i in range(consumer):
        consumerPool.apply_async(data_consumer, args=(old_data_queue, key,))

    time.sleep(1)

    producerPool.close()
    consumerPool.close()

    producerPool.join()
    consumerPool.join()

    job_avg.query()

