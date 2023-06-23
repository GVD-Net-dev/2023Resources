import random  # 导入random标准库
randomdict  = {i:random.randint(10,100) for i in range(1,5)} # 生成4个随机数
print('生成的字典为:',randomdict)
# 生成的字典为: {1: 66, 2: 70, 3: 94, 4: 91}