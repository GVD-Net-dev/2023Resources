num = (5,10,1,42,35,40,21,13,2,49)  # num是一个元组
print('元组num= ',num)
num = list(num)  #  将num转换为列表
print('将num转换为列表，num=',num)

print('num的长度, len(num)=',len(num))
print('将列表num排序后的结果为:',sorted(num))
num=sorted(num)
print('列表中的元素之和为:',sum(num))
# 元组num=  (5, 10, 1, 42, 35, 40, 21, 13, 2, 49)
# 将num转换为列表，num= [5, 10, 1, 42, 35, 40, 21, 13, 2, 49]
# num的长度, len(num)= 10
# 将列表num排序后的结果为: [1, 2, 5, 10, 13, 21, 35, 40, 42, 49]
# 列表中的元素之和为: 218