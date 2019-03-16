#循环中的else使用
print("循环中正常完成的情况：")
for i in range(5):
    print(i)
else:
    print("循环全部完成！")

print("循环中有break的情况：")
for i in range(5):
    print(i)
    break
else:
    print("循环全部完成！")
