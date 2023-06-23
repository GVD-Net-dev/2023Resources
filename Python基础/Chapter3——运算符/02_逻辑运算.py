score = int(input())

if score >=0 and score <=100:  # 逻辑与 运算
    print('分数是有效范围')
else:
    print('分数是无效范围')

score_xiaoming = 71
score_xiaohong = 30

if score_xiaohong>=60 or score_xiaoming>=60: # 逻辑或 运算
    print('小明和小红其中有一个人及格了')
else:
    print('小明和小红分数都没有及格')