#实例14-2，判断闰年
year=1
while(year<1000 or year>9999):
    year=eval(input("请输入一个年份（4位整数）："))
if year%400==0:
    print("%d是闰年" %year)
else:
    if year%100!=0 and year%4==0:
        print("%d是闰年" %year)
    else:
        print("%d不是闰年" %year)
