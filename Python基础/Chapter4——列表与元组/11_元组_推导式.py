import random
ConstructorM = (random.randint(10,100) for i in range(10)) # <generator object <genexpr> at 0x000001A52E9E69D0>
randomnum = tuple(ConstructorM ) # 转换为元组
m_list = list(randomnum) #转换为列表
print('生成的元组为:',randomnum)
print('生成的列表为:',m_list)
# 生成的元组为: (22, 77, 93, 20, 43, 33, 43, 45, 83, 33)
# 生成的列表为: [22, 77, 93, 20, 43, 33, 43, 45, 83, 33]

number = (i for i in range(3))
print(number.__next__()) # 输出第一个元素
print(number.__next__()) # 输出第二个元素
print(number.__next__()) # 输出第三个元素
num = tuple(number) # 转换为元组
print('转换后:',num)
# 0
# 1
# 2
# 转换后: ()


number = (i for i in range(3))
print(number.__next__()) # 输出第一个元素
print(number.__next__()) # 输出第二个元素
print(number.__next__()) # 输出第三个元素
number = (i for i in range(3))
num = tuple(number) # 转换为元组
print('转换后:',num)
# 0
# 1
# 2
# 转换后: (0, 1, 2)