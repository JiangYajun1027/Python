# -*- encoding: utf-8 -*-
'''
@File : sell.py
@Time : 2020/04/10 11:03:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class Dog():
    listx=[
        {'color':'黑色','price':100,'number':5},
        {'color':'白色','price':500,'number':3},
        {'color':'棕色','price':300,'number':2}
    ]
    def buydog(self,c,n):
        for x in self.listx:
            if x['color']==c:
                print('%s的狗价格为%d,数量为%d'%(x['color'],x['price'],x['number']))
                print('请支付%d元'%(x['price']*n))
                a=int(input())
                if a==(x['price']*n):
                    print('购买成功')
                x['number']=x['number']+n
    def selldog(self,c,n):
        for x in self.listx:
            if x['color']==c:
                print('%s的狗价格为%d,数量为%d'%(x['color'],x['price'],x['number']))
                if n>x['number']:
                    print('数量超出，请重新选择卖出数量')
                else:
                    print('卖出%d元'%(x['price']*n))
                    x['number']=x['number']-n


dog1=Dog()
dog1.buydog('黑色',2)
dog2=Dog()
dog2.selldog('棕色',1)
for i in dog2.listx:
    print(i)