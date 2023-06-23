# test1:
age = 65
# test2:
# age = None

if age is not None:
    if age>=18 and age <=70:
        print('可以申领小汽车')
    else:
        print('年龄不够格')

else:
    print('年龄为空!')