name = ['小明','小王','小李','小孙']  # 小明和小王是教师

socre1 = int(input("请输入小明的分数: "))
socre2 = int(input("请输入小王的分数: "))

if socre1>60 or socre2>60:
    print("教师组有人晋级")
else:
    print("教师组无人晋级")
# 请输入小明的分数: 32
# 请输入小王的分数: 98
# 教师组有人晋级