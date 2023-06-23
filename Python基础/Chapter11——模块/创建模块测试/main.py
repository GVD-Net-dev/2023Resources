# import  myModules.theFirstModules as mM  # 使用import导入模块
from myModules import  theFirstModules # 使用from...import导入模块
def main():
    print('主函数')
    # mM.get_info() # 调用刚刚定义的模块中的get_info()函数
    theFirstModules.get_info()


if __name__ == '__main__':
    main()