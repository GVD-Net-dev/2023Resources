N = int(input()) # 正整数N,表示接下来输入多少个数字
M = int(input()) # 2的m次幂
sum = 0 # 统计合法区间[-1000,1000]内数字之和

for i in range(0, N):
    x = int(input())
    sum += x

sum <<= M  # 左移M位，表示乘以2的M次幂
print(sum)

