# coding: utf-8
filename='14-6.py'
fp=open(filename,'r',encoding="utf-8")
lines=fp.readlines() #读取所有行
index=1
for line in lines: #遍历所有行
    newLine=line.rstrip()   #删除每行右侧的空白字符
    newLine=str(index)+' '*3+newLine  #在每行固定位置添加行号
    index+=1
    print(newLine)
fp.close()
