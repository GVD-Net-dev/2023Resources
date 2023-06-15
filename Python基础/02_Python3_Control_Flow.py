# 否则如果表述
pet_type = "fish"

if pet_type == "dog":
    print("You have a dog")
elif pet_type =="cat":
    print("You have a cat")
elif pet_type == "fish":
    print("You have a fish")
else:
    print("Not sure!")

# or: 只要有一个为真，则结果为真
print(True or True)
print(True or False)
print(1<2 or 3<1)
print(1==1 or 1<2)
print(3<1 or 1>6)

# （1）=是赋值语句
# （2） == 是判断语句
mike_age = 21 # 赋值语句

if mike_age== 22: # 判断语句
    print("Mike今年22岁")
elif mike_age ==21:
    print("Mike今年21岁")
else:
    print("Not sure")


# ！是不等于号

a =100
if a!=100:
    print("a!=100")
else:
    print("a==100")