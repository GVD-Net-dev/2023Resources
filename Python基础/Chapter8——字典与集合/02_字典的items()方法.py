dictionary={'小明':'21岁','小王':'20岁','小李':'19岁'}

for i in dictionary.items():  # 使用items()函数输出全部的键值对
    print(i)

# ('小明', '21岁')
# ('小王', '20岁')
# ('小李', '19岁')

for key,value in dictionary.items(): # 分别输出键和值
    print('键:',key,'   值:',value)
# 键: 小明    值: 21岁
# 键: 小王    值: 20岁
# 键: 小李    值: 19岁