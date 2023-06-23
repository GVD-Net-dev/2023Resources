def isPrime(x):
    x = int(x)  # 转换为正整数
    if x<=1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
    return True
##################################
def main():
    N = int(input()) # 输入一个正整数
    for i in range(0,N):
        x = int(input())
        if isPrime(x)==True:
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    main()
    
# 3
# 19
# True
# 20
# False
# 16
# False