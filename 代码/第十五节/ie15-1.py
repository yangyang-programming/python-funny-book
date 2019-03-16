#实例15-1
mynum=1 #输入的数
firstnum=0  #存储第一个素数
secondnum=0  #存储第二个素数
while(mynum%2!=0 or mynum<=2):
    mynum=eval(input("请输入一个偶数(n>2)："))
if mynum==4:
    print("4=2+2")
else:
    for i in range(2,mynum//2):#从mynum的前一半个数中找素数
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                break  #说明i不是素数
        else:#如果循环正常执行完，说明i一定是素数
            firstnum=i
            secondnum=mynum-firstnum
            #判断secondnum是不是素数
            for j in range(2,int(secondnum**(1/2))+1):
                if secondnum%j==0:
                    break
            else:
                print("%d=%d+%d" %(mynum,firstnum,secondnum))

        
