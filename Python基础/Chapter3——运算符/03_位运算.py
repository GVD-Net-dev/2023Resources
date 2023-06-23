a = 110
b = 111
print("Num1=",bin(a)[2:]) # 因为bin函数以0b开头，从第三位开始才是二进制数
print("Num2=",bin(b)[2:])
print("【1】位与 运算\n Num1 & Num2 = ", bin(a&b)[2:]) # 按位与：两个都为1，结果才为1
print("【2】位或 运算\n Num1 | Num2 = ", bin(a|b)[2:]) # 按位或：有一个为真，则为真；若都为假，才是假
print("【3】异或 运算\n Num1 ^ Num2 = ", bin(a^b)[2:]) # 按位异或：是否为不同？是为真，否则为假
print("【4】对Num1进行位取反操作：")
print("Num1 =",bin(a)[2:])
print("~Num1=",bin(~a)) # 将对应的1改成0,0改成1

#######################################

# 左移： 相当于乘以2的n次幂
num = 10
print('num=',num)
num = num<<3  # 左移三位，相当于乘以2**3 =8，结果为80
print('num<<3:',num)
# 右移： 相当于除以2的n次幂
num = num>>3
print('num>>3:',num)

