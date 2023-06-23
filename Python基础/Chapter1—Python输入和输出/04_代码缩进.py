# coding:utf-8
def fun(x):
    x=int(x)
    if x<=1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
    return True

def main():
    x = int(input("输入一个正整数，判断是否为素数: "))
    if fun(x)==True:
        print(x,"是素数")
    else:
        print(x,"不是素数")

if __name__ == '__main__':
    main()
    
# 执行结果（例如输入4）
# 输入一个正整数，判断是否为素数: 4
# 4 不是素数