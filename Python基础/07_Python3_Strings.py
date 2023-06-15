# 转义字符
txt = "She said \" Never let go \". "
print(txt)

game = "Popular Nintendo Game: Mario Kart"
print("l" in game)
print("x" in game)

# 下标访问
str = "yellow"
print(str[1])# 访问第二个字符
print(str[-1]) #访问倒数第一个字符
print(str[4:6])# 访问第五到第七个字符
print(str[:4])# 访问第一个到第五个字符
print(str[-3:])#从倒数第三个到结束

# 字符串遍历
str = "hello "
for c in str:
    print(c)


# 字符串拼接
x = "one fish, "
y = "two fish"
z = x + y
print(z)


# format可以替换掉字符串中{ }的位置(中间有空格)
msg = 'mike score is {} and tom score is {}'.format(90,91)
print(msg)

msg2 ='hello {name}, I am {me}'.format(me='tom',name='jack')
print(msg2)

# 转换大小写

str ="ABswCeddwWesFswq"
print(str.lower()) #转小写
print(str.upper()) #转大写

#
text1 = '    apples and oranges   '
print(text1.strip()) #前后去空格

test2='....+...lemons and limes...-...'
print(test2.strip('.')) #去掉前后的.


# 字符分割
text = "Silicon Valley"
print(text.split()) #以空格分割
print(text.split('i'))#以字母i分割

# 查找

mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o"))

# 替换
fruit = "Strawberry"
print(fruit.replace('r','R'))

# join方法
x="+".join(["apple","bird","banana"])
print(x)