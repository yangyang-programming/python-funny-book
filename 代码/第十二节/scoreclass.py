#scoreclass.py
score=eval(input("数学成绩："))
if score>=90:
    print("等级：优秀")
elif score<90 and score>=60:
    print("等级：合格")
else:
    print("等级：不及格")
