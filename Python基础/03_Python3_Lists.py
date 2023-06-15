# 列表
primes = [2,3,5,7,11]
print(primes)

empty_list = [] # 空列表
print(empty_list)

# 列表添加元素
items = ['cake','cookie','bread']
total_items = items + ['biscuit','tart'] # 通过+方式
print(total_items)
total_items.append('apple') # 通过append方式
print(total_items)

# 列表中可以存放不同的类型，甚至是再放置一个列表

newList = [1,2,3.14,'helloWorld',['a',1],['b',2] ] # 包含多种数据类型的列表
print(newList)

########################################
# 访问；列表
name = ['mike','jack','tom','xiaoming','xiaohong','xiaolan']
print('name=',name)
print('name[0]=',name[0]) # 列表的下标从0开始
print('name[1]=',name[1]) # 访问第二个数据
print('name[-1]=',name[-1])# 访问倒数第一个数据
print('name[-2]=',name[-2]) # 访问倒数第二个数据

print('name[-2:]=',name[-2:])#访问从倒数第二个数据到倒数第一个数据结束
print('name[:-2]=',name[:-2])#访问第一个数据到倒数第二个数据的前一个

# 删除

name = ['mike','jack','tom','xiaoming','xiaohong','xiaolan']
name.remove('xiaolan') #删除
print('name=',name)
name.append('tom')
print('name=',name)
print(name.count('tom')) #统计
print(len(name)) # 列表大小
name.sort() #按字典序排序
print('name=',name)

################

num = [5,1,9,2,3,8,4,2]
num.sort() #对列表排序
print('num=',num)

# 在指定位置插入元素

num2 = [1,2,4,5]
num2.insert(2,3) # 在第三个位置（坐标为2）插入元素3
print('num2=',num2)

remove_num = num2.pop(4)# 弹出第5个元素并返回
print('remove_num=',remove_num)
print('num2=',num2)
