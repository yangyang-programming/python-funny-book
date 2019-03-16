#判断是否是质数
num=eval(input("请输入要判断的数："))
if num<=1:
    print(str(num)+"不是质数")
elif num==2:
    print(str(num)+"是质数")
else:
    for i in range(2,int(num/2)):
        if num%i==0:
            print(str(num)+"不是质数")
            break
    else:
        print(str(num)+"是质数")
        
    
