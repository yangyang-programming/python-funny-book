#three2min.py
a=eval(input("第1个整数："))
b=eval(input("第2个整数："))
c=eval(input("第3个整数："))
temp=0 #用于存放三个数的最小值
if (a>b):
    temp=b
else:
    temp=a
if(temp<c):
    print("最小数为：%d" %temp)
else:
    print("最小数为：%d" %c)
