from m_package import  m_function # 导入模块
def testF():
    num1 = 100
    num2 = 200
    print('num1+num2=',m_function.add(num1,num2))
    print('num1-num2=',m_function.subtract(num1,num2))
    print('num1*num2=',m_function.multiply(num1,num2))
    print('num1/num2=',m_function.divide(num1,num2))

if __name__=='__main__':
    testF()
# num1+num2= 300
# num1-num2= -100
# num1*num2= 20000
# num1/num2= 0.5
