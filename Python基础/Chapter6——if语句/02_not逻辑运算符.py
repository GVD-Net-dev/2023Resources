num = int(input())
# num = None
if num is not None:# 第一种表达
    print('输入的数字不为空')
else:
    print('输入的数字为空')

if not num:# 第二种表达
    print('输入的数字为空')
else:
    print('输入的数字不为空')