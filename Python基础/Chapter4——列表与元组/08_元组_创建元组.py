tupleName = ('小明',3.1415926,True)
print('创建的元组:',tupleName)
print('type(tupleName)=',type(tupleName))
# 创建的元组: ('小明', 3.1415926, True)
# type(tupleName)= <class 'tuple'>

tupleName2 = tuple(range(10,20,2))
print('创建的数值元组为: ',tupleName2)
# 创建的数值元组为:  (10, 12, 14, 16, 18)

tupleName = ('小明',3.1415926,True)
del tupleName # 删除元组