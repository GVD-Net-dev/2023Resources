m_book = {'chapter1':'c Language' , 'chapter2':'C++ language','chapter3':'java language'} # 创建一个字典
print(m_book) # 输出字典
# {'chapter1': 'c Language', 'chapter2': 'C++ language', 'chapter3': 'java language'}
emptyDict = dict()  # 创建一个空字典
print(emptyDict)

##################

name = ['小明','小王','小红']  # 作为键的列表
age = [19,20,19]            # 作为值的列表
dictionary = dict(zip(name,age)) # 转换为字典
print(dictionary)
# {'小明': 19, '小王': 20, '小红': 19}

####################
dictionary = dict(小明='20岁',小红='21岁',小王='22岁')
print(dictionary)
# {'小明': '20岁', '小红': '21岁', '小王': '22岁'}

##################
name_list = ['马云','马化腾','马斯克']  # 作为键的列表
dictionary = dict.fromkeys(name_list)
print(dictionary)
# {'马云': None, '马化腾': None, '马斯克': None}

####################
name_list = ('马云','马化腾','马斯克')  # 作为键的元组
power = [3,2,1]
dictionary={name_list:power} # 创建一个字典
print(dictionary)
# {('马云', '马化腾', '马斯克'): [3, 2, 1]}
#######################

dictionary={'小明':'21岁','小王':'20岁','小李':'19岁'}
print('原始字典=',dictionary)
dictionary.pop('小明')
print('删除掉小明后的字典=',dictionary)
# 原始字典= {'小明': '21岁', '小王': '20岁', '小李': '19岁'}
# 删除掉小明后的字典= {'小王': '20岁', '小李': '19岁'}