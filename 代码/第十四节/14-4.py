#实例14-4
n=0
#循环正常结束运行else
while(n<10):
    print(n)
    n+=1
else:
    print("循环结束！")
#循环非正常结束，不运行else
n=0
while(n<10):
    if n==5:
        print("循环非正常结束！")
        break
    print(n)
    n+=1
else:
    print("循环结束！")
