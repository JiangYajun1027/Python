# -*- encoding: utf-8 -*-
'''
@File : system.py
@Time : 2020/04/12 19:40:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#六  用面向对象,实现一个学生Python成绩管理系统;
#   学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#   实现对学生信息及成绩的增,删,改,查方法;

class system(object):

    @staticmethod
    def readinfo():
        listx=[]
        with open('F:/Python/homework6/system.txt',"r",encoding="utf-8") as f:
            for line in f.readlines():
                # line = line.strip("\n")  
                # s = line.split('   ')  
                listx.append(line)
            return listx
    
    def add(self,grade,number,name,score):
        with open('F:/Python/homework6/system.txt',"a+",encoding="utf-8") as f:
            f.write(grade+'   '+number+'   '+name+'   '+score+'\n')

    def dele(self,name):
        listx=[]
        with open('F:/Python/homework6/system.txt',"r+",encoding="utf-8") as f:
            for line in f.readlines():
                # line = line.strip("\n")  
                # s = line.split('   ')  
                listx.append(line)
        for con in listx:
            s = con.split('   ')
            for x in s:
                if x==name:
                    listx.remove(con)
                else:
                    continue
        with open('F:/Python/homework6/system.txt',"w",encoding="utf-8") as f1:
            for con in listx:
                f1.write(con)

    def change(self,name,grade):
        listx=[]
        with open('F:/Python/homework6/system.txt',"r+",encoding="utf-8") as f:
            for line in f.readlines():
                # line = line.strip("\n")  
                # s = line.split('   ')  
                listx.append(line)
        for con in listx:
            s = con.split('   ')
            for x in s:
                if x==name:
                    listx.remove(con)
                    listx.append(s[0]+'   '+s[1]+'   '+s[2]+'   '+grade+'\n')
                    break
                else:
                    continue
        with open('F:/Python/homework6/system.txt',"w",encoding="utf-8") as f1:
            for con in listx:
                f1.write(con)
            
    def search(self,name):
        listx=[]
        with open('F:/Python/homework6/system.txt',"r+",encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip("\n")  
                s = line.split('   ')  
                listx.append(s)
        for con in listx:
            for x in con:
                if x==name:
                    print(con)
                else:
                    continue

a=system()
a.add('three','123456','Alice','95')
a.add('four','112233','Bob','84')
a.add('five','445566','Cindy','71')
print(a.readinfo())
a.change('Bob','69')
print(a.readinfo())
a.search('Bob')
a.dele('Bob')
print(a.readinfo())
