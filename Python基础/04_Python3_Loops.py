# break <==> 停止循环

numbers = [0,254,2,-1,3]

for num in numbers:
    if(num<0):
        print("Negative number detected!")
        break
    print(num) # 不会输出-1

################################

result = [x**2 for x in range(10) if x%2==0]
print(result)

# for 语句
# 例如：计算1-100之和

result=0
for num in range(100+1):
    if(num>100):
        break
    else:
        result+=num

print(result)

# while 语句
# 例如： 同样计算1-100累加和

result =0
num = 0
while(num<100):
    num = num + 1
    if(num>100):
        break
    else:
        result+=num


print("result=",result)