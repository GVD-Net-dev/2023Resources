
# 定义一个函数，打印字符串
def write_a_book(character,setting,special_skill):
    print(character+"is in "+setting+" practing her "+special_skill)
# 调用write_a_book函数
write_a_book("chapter01","apple book","fruit")


# 带有返回值的函数
def my_function(x):
    return x+1

print(my_function(10))

# 完成m到n的累加和吧

def sumTest(m,n):
    sum=0
    for i in range(m,n+1):
        sum=sum+i
    return sum

print(sumTest(1,100)) # 计算[1,100]的和