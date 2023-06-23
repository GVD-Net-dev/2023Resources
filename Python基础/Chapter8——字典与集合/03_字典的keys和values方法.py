dictionary={'小明':'21岁','小王':'20岁','小李':'19岁'}

print("（1）字典的键为：")
# 利用keys()函数分别输出字典的键
for i in dictionary.keys():
    print(i,end=" ")

print("\n （2）字典的值为:")
# 利用values()函数分别输出字典的值
for i in dictionary.values():
    print(i,end=" ")

# （1）字典的键为：
# 小明 小王 小李 
#  （2）字典的值为:
# 21岁 20岁 19岁 