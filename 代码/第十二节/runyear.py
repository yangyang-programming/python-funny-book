#runyear.py
year=eval(input("请输入一个年份（4位整数）："))
if year>9999 or year<1000:
    print("年份输入错误")
else:
    if year%400==0:
        print("%d是闰年" %year)
    else:
        if year%100!=0 and year%4==0:
            print("%d是闰年" %year)
        else:
            print("%d不是闰年" %year)
