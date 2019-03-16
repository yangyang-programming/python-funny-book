#任意两数的最小公倍数
a=eval(input("第一个数："))
b=eval(input("第二个数："))
if (a>b):
    a,b=b,a   #交换a,b的值，始终让b是a和b的最大值
for i in range(b,a*b+1,b):
    if i%a==0:
        print("%d和%d的最小公倍数是%d" %(a,b,i))
        break
    
    
