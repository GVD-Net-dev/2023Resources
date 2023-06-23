number = {i:0 for i in range(0,10)} # 使用字典推导式创建一个字典
# 初始化为每个数字只出现一次
# {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
m_str = input() # 输入的一个字符串

for subStr in m_str:
    tmpNum = int(subStr) # 转换为整数
    number[tmpNum]=number[tmpNum]+1 # 出现次数+1

# 分别输出键和值
for key,value in number.items():
    print(key,':',value)

# 31313917317001138102381378127381290456452896677213517
# 0 : 4
# 1 : 12
# 2 : 5
# 3 : 9
# 4 : 2
# 5 : 3
# 6 : 3
# 7 : 7
# 8 : 5
# 9 : 3