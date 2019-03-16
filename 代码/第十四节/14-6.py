#实例14-6
#用while来保证输入的两个数是整数
a="a"  #随便给a,b赋值一个非整数
b="a"
while(type(a)!=type(1)):
    a=eval(input("请输入第1个数："))
else:
    while(type(b)!=type(1)):
        b=eval(input("请输入第2个数："))
if a<b: #如果a<b，那么a和b交换值
    a,b=b,a
n=b
while(a%n!=0): #只要余数不为为0,就继续除下去
    n=a%n
print("%d和%d的最大公约数：%d"%(a,b,n))
print("%d和%d的最小公倍数：%d"%(a,b,a*b/n))
