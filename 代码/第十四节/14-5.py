#实例14-5
import random
n=1#第几道题
score=0 #记录得分
while(n<=10):
    #随机产生加数与被加数
    a=random.randint(0,100)
    b=random.randint(0,100)
    result=eval(input("第%d题 %d+%d=" %(n,a,b)))
    if result==a+b:
        print("正常，得10分！")
        score+=10
    else:
        print("错误，不得分！")
    n+=1
print("您的最终得分：%d" %score)
