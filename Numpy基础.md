# Numpy基础

<h5 align="center">郑钦元 <br>北京交通大学</h5>



## 目录

* [一. Numpy介绍](#p0)

* [二. 数组对象ndarray](#p1)
  
  1. [创建数组ndarray](#p11)
  2. [数组的常用属性](#p12)
  
* [三. 数组数据类型](#p2)
  1. [Dtype](#p21)
  2. [Numpy支持的数据类型](#p22)
  3. [数组数据类型的转换](#p23)
  4. [其他创建ndarray数组的方法](#p24)
     * 4.1 [arrange函数](#p241)
     * 4.2 [zeros函数](#p242)
     * 4.3 [ones函数](#p243)
     * 4.4 [empty函数](#p244)
     * 4.5 [eye函数](#p245)
     * 4.6 [full函数](#p246)
     * 4.7 [linespace函数](#p247)
     * 4.8 [logspace函数](#p248)
  
* [四. Numpy生成伪随机数](#p3)
  1. [使用random模块生成伪随机数创建数组](#p31)
  2. [综合例子](#p32)
  
* [五. 数组的访问与形态变换](#p4)
  1. [访问一维数组](#p41)
  2. [通过索引和切片方式修改数组元素](#p42)
  3. [变换数组形态](#p43)
     * [第一种 改变数组形状](#p431)
     * [第二种 展平数组](#p432)
     * [第三种 组合数组](#p433)
     * [第四种 分割数组](#p434)
  
* [六. 使用函数进行简单统计分析](#p6)

  1. [排序](#p61)

  2. [去重](#p62)

  3. [重复数据](#p63)

  4. [数组的集合操作](#p64)

* [七. 通用函数ufunc的运算](#p7)
  1. [什么是通用函数ufunc](#p71)
  2. [ufunc函数种类](#p72)
  3. [ufunc函数特点](#p73)
  4. [ufunc函数运算](#p74)
  5. [常用的统计函数](#p75)
* [八. 用于数组的文件输入输出](#p8)
  1. [读取二进制文件](#p81)
  2. [读取文本文件（或CSV文件）](#p82)



---



## 一.<span id="p0">Numpy介绍</span>

Numpy是Python数值计算最重要的基础包，提供了一种存储单一数据类型的多维数组ndarray。Numpy的数组比python内置序列占用的内存更少，执行的速度更快。Numpy可以在整个数组上执行复杂的计算，而不需要python的for循环。基于Numpy的算法要比纯Python快10到100倍，甚至更快。

<b>测试</b>(同学们可以在jupyter notebook 上测试)

```python
import numpy as np

nums = np.array(100000)  # 用numpy创建数组
nums_list = list(range(100000))  #用python内置序列创建数组

print("(1) Numpy执行速度: ")
%time for i in range(10): nums=nums*2   # %time 是ipython的特殊功能，用于测试语句运行的时间
print("(2) Python内置序列执行速度: ")
%time for i in range(10): nums_list = [j*2 for j in nums_list]  # %time 是ipython的特殊功能，用于测试语句运行的时间
```

<b>执行结果如下:</b>

```
(1) Numpy执行速度: 
CPU times: total: 0 ns
Wall time: 0 ns
(2) Python内置序列执行速度: 
CPU times: total: 31.2 ms
Wall time: 27 ms
```





---



## 二.<span id="p1">数组对象ndarray</span>

### 1. <span id="p11">创建数组ndarray</span>

语法: 

```python
numpy.array(p_object, dtype=None, copy=True,order='K',subok=False,ndmin=0)
```

| 参数名称 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| object   | 序列型对象，表示想要创建的数组数据，无默认                   |
| dtype    | 接收data-type.表示数组所需的数据类型，如果未给定，则选择保存对象所需的最小类型，默认未None |
| ndmin    | 接收int，指定生成数组应该具有的最小维数，默认为None          |

<b>例子1</b> 创建一维数组

```python
import numpy as np  #导入numpy库

arr =np.array([2,4,6,8]) #创建一个一维数组
print(str.format("新创建的数组为： {0}",arr))
```

<b>执行结果</b>

```
新创建的数组为： [2 4 6 8]
```



<b>例子2</b> 创建二维数组

```python
import numpy as np  #导入numpy库

arr =np.array([ [2,4,6,8],[1,2,3,4],[5,6,7,8] ]) #创建一个二维数组
print(str.format("新创建的二维数组为： \n{0}",arr))
```

<b>执行结果</b>

```
新创建的二维数组为： 
[[2 4 6 8]
 [1 2 3 4]
 [5 6 7 8]]
```



---



### 2. <span id="p12">数组的常用属性</span>



| 属性     | 说明                                                    |
| -------- | ------------------------------------------------------- |
| ndim     | 返回int，表示数组的维数                                 |
| shape    | 返回true，表示数组的尺寸，对于n行m列的矩阵，形状为(n,m) |
| size     | 返回int，表示数组的元素总数，等于数组形状的乘积         |
| dtype    | 返回data-type,描述数组中的元素类型                      |
| itemsize | 返回int，表示数组的每个元素的大小（以字节为单位）       |

<b>例子</b> 数组属性综合例子



```c++
import numpy as np #导入numpy库

arr = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]) # 创建一个3行4列的数组

print(str.format("数组的维数为:{0} ",arr.ndim)) # ndim: 返回int，表示数组的维数
print(str.format("数组的形状为:{0} ",arr.shape))# shape:返回true，表示数组的尺寸，对于n行m列的矩阵，形状为(n,m)
print(str.format("数组的元素总数为:{0} ",arr.size))# size: 返回int，表示数组的元素总数，等于数组形状的乘积
print(str.format("数组的元素类型为:{0} ",arr.dtype))# dtype: 返回data-type,描述数组中的元素类型
print(str.format("数组的每个元素大小为:{0} ",arr.itemsize))# itemsize: 返回int，表示数组的每个元素的大小（以字节为单位）
```



<b>执行结果</b>

```
数组的维数为:2 
数组的形状为:(3, 4) 
数组的元素总数为:12 
数组的元素类型为:int32 
数组的每个元素大小为:4 
```



---



## 三.<span id="p2">数组的数据类型</span>

### 1.  <span id="p21">Dtype</span>



* Dtype -- (数据类型)：是一个特殊的对象，它含有ndarray将一块内存解释为特定数据类型所需的信息

* Dtype -- (数值类型)：命名方式相同，一个类型名（如float或int），后面跟一个用于表示各元素位长的数字



<b>例子</b>

```python
import numpy as np # 导入Numpy库

arr1 = np.array( [1,2.5,3,4],dtype=np.float64) # dtype指定数据类型
print(arr1)
print(arr1.dtype) #打印数据类型
```



<b>执行结果</b>

```
[1.  2.5 3.  4. ]
float64
```



### 2.<span id="p22">Numpy支持的数据类型</span>

| 类型                                    | 类型代码             | 说明                                         |
| --------------------------------------- | -------------------- | -------------------------------------------- |
| int8、uint8                             | i1、u1               | 有符号和无符号的8位整型                      |
| int16、uint16                           | i2、u2               | 有符号和无符号的16位整型                     |
| int32、uint32                           | i4、u4               | 有符号和无符号的32位整型                     |
| int64、uint64                           | i8、u8               | 有符号和无符号的64位整型                     |
| float16                                 | f2                   | 半精度的浮点数                               |
| float32                                 | f4/f                 | 单精度浮点数、与C的浮点数兼容                |
| float64                                 | f8/d                 | 双精度浮点数，与C的double和python的float兼容 |
| float128                                | f16/g                | 扩张精度浮点数                               |
| Complex64<br/>Complex128<br/>Complex256 | c8<br>c16<br>c32<br> | 用两个32位、64位或128位的浮点数表示的复数    |
| bool                                    | ?                    | 布尔类型，值是True和False                    |
| object                                  | O                    | Python对象类型                               |
| string                                  | S                    | 固定长度的字符串类型，每个字符1个字节        |
| unicode_                                | U                    | 固定长度的unicode_类型                       |



---



### 3.<span id="p23">数组数据类型的转换</span>

* ndarray对象的astype方法实现数据类型转换

<b>例子</b>

```python
import numpy as np # 导入numpy库

arr = np.array([1,2,3,4])
print(str.format("数组元素为:{0}",arr))
print(str.format("数组的类型为:{0}",arr.dtype))

print(str.format("将数组转换为float64"))

arr=arr.astype(np.float64)
print(str.format("数组元素为:{0}",arr))
print(str.format("数组的类型为:{0}",arr.dtype))

```

<b>执行结果</b>

```
数组元素为:[1 2 3 4]
数组的类型为:int32
将数组转换为float64
数组元素为:[1. 2. 3. 4.]
数组的类型为:float64
```



* numpy的转换函数，实现单个数据的类型转换

<b>例子</b>

```python
import numpy as np

print("整型转浮点型:",np.float(100))

print("整型转布尔:",np.bool(1000)) # 大于0则为true

```

<b>执行结果</b>

```
整型转浮点型: 100.0
整型转布尔: True
```



---





### 4.<span id="p24">其他创建ndarray数组的方法</span>



#### ① <span id="#p241">arrange函数：创建指定范围的数组</span> <br>

语法：<br>

```python
arrange(start = n, stop = m, step = d)
```

例子:

```python
import numpy as np

arr = np.arange(start=10,stop=100,step=5)

print("创建后的数组: ",arr)
# 执行结果：
# 创建后的数组:  [10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]
```



#### ② <span id="#p242">zeros函数：创建指定行列的全0数组</span>

语法:<br>

```python
zeros(shape,dtype=float,order='C')
```

<b>例子</b>

```python
import numpy as np

arr = np.zeros(5,dtype=float,order='C')

print("创建后的数组: ",arr)

# 执行结果
# 创建后的数组:  [0. 0. 0. 0. 0.]
```





#### ③ <span id="#p243">ones函数：创建全1数组</span>

语法:<br>

```python
ones(shape,dtype=None,order='C')
```

* 这里的shape值表示列数

<b>例子</b>

```python
import numpy as np

arr = np.ones(5) # 代表列数

print("创建后的数组: ",arr)

# 执行结果
# 创建后的数组:  [1. 1. 1. 1. 1.]
```



#### ④ <span id="#p244">empty函数：创建一个拥有趋近于0值的空数组，值都是垃圾值</span>

语法:<br>

```python
empty(shape,dtype=None,order='C')
```



<b>例子</b>

```python
import numpy as np

arr = np.empty(5,dtype=None,order='C')

print("创建后的数组: ",arr)

# 执行结果
# 创建后的数组:  [1.27734658e-152 4.24051614e+175 3.62484582e+228 2.35567922e+251
#  6.01347002e-154]
```



#### ⑤ <span id="#p245">eye函数：创建一个对角矩阵，对角线上值为1</span>

语法:<br>

```python
eye(N,M=None,K=0,dtype=float,order='C')
```

* N代表行，M代表列，K偏移量默认值为0
* 正1时向主对角线右上偏移1,位，负1时向主对角线左下偏移1位

<b>例子</b>

```python
import numpy as np

arr = np.eye(4,4,k=1)

print("创建后的数组: ")
print(arr)

# 执行结果
# 创建后的数组: 
# [[0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]
#  [0. 0. 0. 0.]]
```





#### ⑥ <span id="#p246">full函数：创建指定填充值的数组</span>

语法:<br>

```python
full(shape,fill_value,dtype=None,order='C')
```



<b>例子：</b>

```python
import numpy as np

arr = np.full(5,fill_value=10,dtype=None,order='C')

print("创建后的数组: ")
print(arr)

# 执行结果
# 创建后的数组: 
# [10 10 10 10 10]
```





#### ⑦ <span id="#p247">linespace函数：创建指定范围的一维等差数组</span>

语法:<br>

```python
linespace(起始值，终止值，元素总数)
```

<b>例子</b>



```python
import numpy as np

arr = np.linspace(start=1,stop=10,num=10)

print("创建后的数组: ")
print(arr)

# 执行结果
# 创建后的数组: 
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
```





#### ⑧ <span id="#p248">logspace函数：创建知道范围的一维等比数组</span>

语法：<br>

```python
logspace(起始值，终止值，元素总数)
```

<b>例子</b>

```python
import numpy as np

arr = np.logspace(start=10,stop=100,num=10)

print("创建后的数组: ")
print(arr)

# 执行结果
# 创建后的数组: 
# [1.e+010 1.e+020 1.e+030 1.e+040 1.e+050 1.e+060 1.e+070 1.e+080 1.e+090
#  1.e+100]
```



---





## <span id="p3">四. Numpy生成伪随机数</span>



### <span id="p31">1.使用random模块生成伪随机数创建数组</span>



| 函数                            | 说明                                           |
| ------------------------------- | ---------------------------------------------- |
| seed                            | 确定随机数生成器的种子                         |
| permutation                     | 返回一个序列的随机排列或返回一个随机排列的范围 |
| shuffle(x)                      | 对一个序列进行随机排序                         |
| random(数量)                    | 产生[0,1)之间指定数量的随机数                  |
| rand(dim0,dim1,....)            | 产生均匀分布的样本值的多维数组                 |
| randint(low [ , high , size ] ) | 产生指定范围的随机整数                         |
| randn(dim0,dim1,...)            | 产生正态分布的样本值的多维数组                 |
| binomial                        | 产生二项分布的随机数                           |
| normal                          | 产生正态（高斯）分布的随机数                   |
| beta                            | 产生beta分布的随机数                           |
| chisquare                       | 产生卡方分布的随机数                           |
| gamma                           | 产生gamma分布的随机数                          |
| uniform                         | 产生在[0,1)中均匀分布的随机数                  |



### <span id="p32">2.综合例子</span>

```python
import numpy as np  # 导入numpy库

# 产生[0,1)之间指定数量的随机数

arr1 = np.random.random(10)

print("[1] 产生[0,1)之间指定数量的随机数  Result:")
print(arr1)

####################################################################
####################################################################

# 产生均匀分布的样本值

arr1 = np.random.rand(3,5) # 3行5列

print("[2] 产生均匀分布的样本值  Result:")
print(arr1)


# 产生指定范围的随机数

arr1 = np.random.randint(low=10,high=20,size=10)
print("[3] 产生指定范围的随机数  Result:")
print(arr1)

# 产生状态分布的随机数的数组

arr1 = np.random.randn(3)
print("[4] 产生状态分布的随机数的数组  Result:")
print(arr1)

# numpy.random.randn(d0, d1,…, dn)
# 
# randn函数返回一个或一组样本，具有标准正态分布。
# dn表格每个维度
# 返回值为指定维度的array

```



<b>执行结果</b>

```
[1] 产生[0,1)之间指定数量的随机数  Result:
[0.62790239 0.52586526 0.79230844 0.03983545 0.22820672 0.42601992
 0.9617291  0.50270595 0.21224575 0.2695119 ]
[2] 产生均匀分布的样本值  Result:
[[0.85680165 0.87407949 0.85544577 0.01335674 0.43682043]
 [0.29687094 0.76285744 0.37283367 0.16464525 0.17370965]
 [0.92769034 0.31701163 0.0553485  0.85729922 0.05176725]]
[3] 产生指定范围的随机数  Result:
[11 14 11 10 13 16 13 11 15 11]
[4] 产生状态分布的随机数的数组  Result:
[ 0.0229648  -0.65395488  1.13253709]
```





---



## <span id="p4">五. 数组的访问和形态变换</span>

```
索引与切片两种形式
```



### <span id="p41">1.访问一维数组</span>

* 与列表的操作类似，支持双向索引
* 数组名[下标]，下标从0开始；下标从-1开始，从右往左取
* 数组名[start:end] 从索引start取到end, 但不包括end
* 数组名[:] 取所有的元素





### <span id="p42">2.通过索引和切片方式修改数组元素</span>



* 数组名 [下标] =值
* 数组名 [m: n] = 值



<b>注意：</b>

跟列表最重要的区别在于，数组切片是原始数组的视图。这意味着数据不会被复制，视图上任何修改都会直接反映到源数组上。



<b>例子</b>

```python
import numpy as np

arr = np.arange(10)

print("初始数组: ",arr)
print("通过索引访问数组的一个元素",arr[4])

print("从右往左访问数组的一个元素",arr[-2])

print("获得数组的一个切片",arr[2:5],arr[:5],arr[2:],arr[:])

print("等步长的切片操作：",arr[::2],arr[3::2],arr[8:2:-3])

# 通过索引和切片修改元素

arr[0] = 11
print(arr)

arr[0:2]=17,13
print(arr)
```



<b>执行结果</b>

```
初始数组:  [0 1 2 3 4 5 6 7 8 9]
通过索引访问数组的一个元素 4
从右往左访问数组的一个元素 8
获得数组的一个切片 [2 3 4] [0 1 2 3 4] [2 3 4 5 6 7 8 9] [0 1 2 3 4 5 6 7 8 9]
等步长的切片操作： [0 2 4 6 8] [3 5 7 9] [8 5]
[11  1  2  3  4  5  6  7  8  9]
[17 13  2  3  4  5  6  7  8  9]
```



---



### <span id="p43">3.变换数组形态</span>

#### <b><span id="p431">第一种 改变数组形状</span></b>

* 利用数组的shape属性
* 利用reshape函数改变数组形状
* .T属性实现数组转置



<b>例子</b>

```python
import numpy as np
arr = np.arange(16)

print("原数组: \n",arr)

# 改变shape属性
arr.shape=4,4
print("改变后的数组：\n",arr)


# reshape函数改变
arr=arr.reshape(2,8)
print("reshape函数改变:\n",arr)

```

<b>执行结果</b>

```
原数组: 
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
改变后的数组：
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
reshape函数改变:
 [[ 0  1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14 15]]
```



<b>例子</b>

```python
import numpy as np

arr =np.arange(12).reshape(3,4)

print("数组:\n",arr)

print("数组转置（行列互换）:\n",arr.T)

```

```
数组:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
数组转置（行列互换）:
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
```

---

#### <span id="p432">第二种 展平数组</span>

* ndarray.ravel()
* ndarray.flatten()：返回一份拷贝，不影响原始矩阵，可实现横向、纵向展平



<b>例子</b>

```python
import numpy as np

arr =np.random.randint(0,10,(3,4))

print("原数组:\n",arr)

print("ravel展平数组:\n",arr.ravel())

print("flatten横向展平:\n",arr.flatten())

print("flatten纵向展平:\n",arr.flatten("F"))

```



<b>执行结果</b>

```
原数组:
 [[9 1 2 2]
 [9 2 2 9]
 [7 0 9 1]]
ravel展平数组:
 [9 1 2 2 9 2 2 9 7 0 9 1]
flatten横向展平:
 [9 1 2 2 9 2 2 9 7 0 9 1]
flatten纵向展平:
 [9 9 7 1 2 0 2 2 9 2 9 1]
```



---



#### <span id="p433">第三种 组合数组</span>

* 横向组合：np.hstack((arr1,arr2))    arr1和arr2行数相同
* 纵向组合：np.vstack((arr1,arr2))     arr1和arr2列数相同
* 横向组合： np.concatenate((arr1,arr2),axis=1)
* 纵向组合:    np.concatenate((arr1,arr2),axis=0)  arr1和arr2要形状相同



<b>例子</b>

```python
import numpy as np

arr1 =np.arange(9).reshape(3,3)

print("第一个数组:\n ",arr1)

arr2 = np.random.randint(10,20,(3,4))

print("第二个数组:\n",arr2)

# 行数相同，都是3行，可以横向组合
print("hstack横向组合:\n",np.hstack((arr1,arr2)))

arr2=arr2.reshape(4,3)  # 将arr2变成4行3列，此时两个数组都是4列，可以进行纵向组合

print("变换后的arr2:\n",arr2)

print("vstack纵向组合:\n",np.vstack((arr1,arr2)))


#################################################

arr3=np.arange(20).reshape(4,5)

arr4=np.random.randint(40,100,(4,5))
print("arr3=: \n",arr3)
print("arr4=:\n",arr4)

print("arr3和arr4横向组合: \n",np.concatenate((arr3,arr4),axis=1))
print("arr3和arr4纵向组合: \n",np.concatenate((arr3,arr4),axis=0))
```

<b>执行结果</b>

```
第一个数组:
  [[0 1 2]
 [3 4 5]
 [6 7 8]]
第二个数组:
 [[17 11 10 18]
 [12 13 15 12]
 [11 11 12 14]]
hstack横向组合:
 [[ 0  1  2 17 11 10 18]
 [ 3  4  5 12 13 15 12]
 [ 6  7  8 11 11 12 14]]
变换后的arr2:
 [[17 11 10]
 [18 12 13]
 [15 12 11]
 [11 12 14]]
vstack纵向组合:
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [17 11 10]
 [18 12 13]
 [15 12 11]
 [11 12 14]]
arr3=: 
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
arr4=:
 [[81 61 55 63 48]
 [77 65 80 95 49]
 [73 95 41 71 50]
 [95 76 96 78 98]]
arr3和arr4横向组合: 
 [[ 0  1  2  3  4 81 61 55 63 48]
 [ 5  6  7  8  9 77 65 80 95 49]
 [10 11 12 13 14 73 95 41 71 50]
 [15 16 17 18 19 95 76 96 78 98]]
arr3和arr4纵向组合: 
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [81 61 55 63 48]
 [77 65 80 95 49]
 [73 95 41 71 50]
 [95 76 96 78 98]]
```

---



#### <span id="p434">第四种 分割数组</span>

* 横向分割: np.hsplit(arr,2)
* 纵向分割：np.vsplit(arr,2)
* 横向分割: np.split(arr,2,axis=1)
* 纵向分割：np.split(arr,2,axis=0)



<b>例子</b>

```python
import numpy as np

arr = np.arange(16).reshape(4,4)
print("原始数组:\n",arr)

print("hsplit实现横向分割:\n",np.hsplit(arr,2)) # 0 1这两列是一份、2 3 这两列是一份

print("split实现横向分割:\n",np.split(arr,2,axis=1))

print("vsplit实现纵向分割:\n",np.hsplit(arr,2)) # 上面两行是一份、下面两行是一份

print("split实现纵向分割:\n",np.split(arr,2,axis=0))
```



<b>执行结果</b>

```
原始数组:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
hsplit实现横向分割:
 [array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
split实现横向分割:
 [array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
vsplit实现纵向分割:
 [array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
split实现纵向分割:
 [array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]
```

----



## <span id="p6">六.使用函数进行简单统计分析</span>

### <span id="p61">1.排序</span>

* 直接排序
  * arr.sort(axis=1) 沿横轴排序
  * arr.sort(axis=0) 沿纵轴排序
* 间接排序
  * arr.argsort函数返回值为重新排序值的下标
  * np.lexsort(a,axis=-1,kind='quicksort',order=None)函数   返回值是按照最后一个传入数据排序



<b>例子</b>

```python
import numpy as np

arr = np.random.randint(0,20,size=10)

print("原始数组:\n",arr)

arr.sort()
print("排序后:\n",arr)

# * arr.sort(axis=1) 沿横轴排序
# * arr.sort(axis=0) 沿纵轴排序

arr2 = np.random.randint(10,100,(3,4))
arr3=arr2
print("arr2=\n",arr2)
arr2.sort(axis=1)
print("沿横轴排序:\n",arr2)
arr3.sort(axis=0)
print("沿纵轴排序:\n",arr3)

# arr.argsort函数返回值为重新排序值的下标

print("#############################")
arr4 =np.random.randint(0,10,size=4)
arr5=arr4
print("arr4=\n",arr4)
arr4.sort()
print("排序后的arr4=\n",arr4)

print("排序后的下标=\n",arr5.argsort())


print("##################################")

a = [1,5,1,4,3,4,4] # First column
b = [9,4,0,4,0,2,1] # Second column
ind = np.lexsort((b,a)) # Sort by a, then by b
print(ind)
```



<b>执行结果</b>

```
原始数组:
 [15 14 11 13  3  3  7  6  5 12]
排序后:
 [ 3  3  5  6  7 11 12 13 14 15]
arr2=
 [[71 81 93 80]
 [54 31 50 27]
 [31 68 30 57]]
沿横轴排序:
 [[71 80 81 93]
 [27 31 50 54]
 [30 31 57 68]]
沿纵轴排序:
 [[27 31 50 54]
 [30 31 57 68]
 [71 80 81 93]]
#############################
arr4=
 [3 5 8 1]
排序后的arr4=
 [1 3 5 8]
排序后的下标=
 [0 1 2 3]
##################################
[2 0 4 6 5 3 1]
```



---



### <span id="p62">2.去重</span>

* np.unique函数：找出数组中的唯一值并返回已排序的结果

<b>例子</b>

```python
import numpy as np

arr = np.array([9,4,4,4,6,1,2,2,10,13,21,20,20])

print("原始数组:\n" ,arr)

print("去重后的数组:\n",np.unique(arr))
```



<b>执行结果</b>

```
原始数组:
 [ 9  4  4  4  6  1  2  2 10 13 21 20 20]
去重后的数组:
 [ 1  2  4  6  9 10 13 20 21]
```



---



### <span id="p63">3.重复数据</span>

* np.tile(A,reps)函数： A指定重复的数组，reps指定重复的次数
* np.repeat(a,repeats,axis=None)函数：a是需要重复的数组元素，repeats是重复次数，axis指定沿着哪个轴进行重复（0：行，1：列）

<b>例子</b>

```python
import numpy as np

arr1=np.array([1,2,3,4])

arr2=np.tile(arr1,reps=2) # 重复的数组元素是arr1,重复次数为2

print("arr2=\n",arr2)

############################
arr1 = np.arange(12).reshape(3,4)
print("原始数组:\n",arr1)
arr2= np.repeat(arr1,2,axis=0) #沿着行重复
print("沿着行重复arr2=\n",arr2)

arr2= np.repeat(arr1,2,axis=1) #沿着列重复

print("沿着列重复arr2=\n",arr2)
```



<b>执行结果</b>

```
arr2=
 [1 2 3 4 1 2 3 4]
原始数组:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
沿着行重复arr2=
 [[ 0  1  2  3]
 [ 0  1  2  3]
 [ 4  5  6  7]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [ 8  9 10 11]]
沿着列重复arr2=
 [[ 0  0  1  1  2  2  3  3]
 [ 4  4  5  5  6  6  7  7]
 [ 8  8  9  9 10 10 11 11]]
```



---



### <span id="p64">4.数组的集合运算</span>

* np.intersect1d(x,y) :返回x和y的交集，并排序
* np.union1d(x,y)：返回集合x和y的并集，并排序
* np.in1d(x,y)：返回一个x包含于y的布尔型数组
* np.setdiff1d(x,y)：集合的差，包含于x但不包含于y
* np.setxor1d(x,y)：对称差，就是x和y交集之外的部分

<b>例子</b>

```python
import numpy as np

arr1 = np.array([1,3,4,5,9,10,22,13,22,29])
arr2 = np.array([2,4,6,8,9,10,22,11,100,139])

print("arr1=",arr1)
print("arr2=",arr2)
print("arr1和arr2的交集=",np.intersect1d(arr1,arr2))
print("arr1和arr2的并集=",np.union1d(arr1,arr2))
print("返回一个arr1包含于arr2的布尔型数组=",np.in1d(arr1,arr2))
print("集合的差，包含于arr1但不包含于arr2=",np.setdiff1d(arr1,arr2))
print("对称差，就是arr1和arr2交集之外的部分=",np.setxor1d(arr1,arr2))
# np.intersect1d(x,y) :返回x和y的交集，并排序
# np.union1d(x,y)：返回集合x和y的并集，并排序
# np.in1d(x,y)：返回一个x包含于y的布尔型数组
# np.setdiff1d(x,y)：集合的差，包含于x但不包含于y
# np.setxor1d(x,y)：对称差，就是x和y交集之外的部分

```



<b>执行结果</b>

```
arr1= [ 1  3  4  5  9 10 22 13 22 29]
arr2= [  2   4   6   8   9  10  22  11 100 139]
arr1和arr2的交集= [ 4  9 10 22]
arr1和arr2的并集= [  1   2   3   4   5   6   8   9  10  11  13  22  29 100 139]
返回一个arr1包含于arr2的布尔型数组= [False False  True False  True  True  True False  True False]
集合的差，包含于arr1但不包含于arr2= [ 1  3  5 13 29]
对称差，就是arr1和arr2交集之外的部分= [  1   2   3   5   6   8  11  13  29 100 139]
```



---



## <span id="p7">七.通用函数ufunc的运算</span>

### 1. <span id="p71">什么是通用函数ufunc</span>

通用函数(ufunc)是一种对ndarray中的数据执行元素级运算的函数，返回值也是ndarray数组



### <span id="p72">2.ufunc函数种类</span>

* 数组运算函数
* 三角函数
* 位操作函数
* 逻辑与比较运算函数
* 浮动运算函数



### <span id="p73">3.ufunc函数特点</span>

不需要对数组的每一个元素做操作，只需要对整个数组操作。对数组做重复运算时，比math库的函数效率更高

<b>例子</b>

```python
import numpy as np
arr= np.array([1,2,3,4])

print("对整个数组的元素做运算: ",arr*2, arr//2)
```

结果:

```
对整个数组的元素做运算:  [2 4 6 8] [0 1 1 2]
```



### <span id="p74">4.ufunc函数运算</span>

* 四则运算： 加(+), 减(-), 乘(*),除(/),幂(**)  形状要相同
* 比较运算: >, < , == , >= ,<= ,!=
* 逻辑运算: np.any 表示逻辑'or', np.all表示逻辑‘and'



### <span id="p75">5.常用的统计函数</span>

通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算

| 方法           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| sum            | 对数组全部或某轴向的元素求和<br>横轴求和： axis=1 纵轴求和： axis=0 |
| mean           | 求算数平均数                                                 |
| std, var       | 求标准差、方差                                               |
| min, max       | 求数组最小值、最大值                                         |
| argmin, argmax | 求最大、最小元素的索引                                       |
| cumsum         | 求所有元素的累计和                                           |
| cumprod        | 求所有元素的累计积                                           |



---



## <span id="p8">八.用于数组的文件输入输出</span>

Numpy能够读写磁盘上的文本数据或二进制数据

### <span id="p81">1. 读写二进制文件</span>

* np.save(path,arr)函数: 将数组的数据以二进制的格式保存
* np.load(path)函数：从二进制的文件中读取数据到数组
* np.savez(path,arr1,arr2...)函数: 可以将多个数组保存到一个文件中

用load读取保存了多个数组的二进制文件时得到的不是一个数组，而是<class 'numpy.llib.npyio.NpzFile'>类型，第一个数组的键arr_0,以此类推，也可以为每一个数组设置键，如np.save(path,a=arr1,b=arr2)

* 存储时可以省略扩展名，默认为.npy，但读取时不能省略扩展名。如果用savez保存，默认为.npz



<b>例子</b>

```python
import numpy as np

arr = np.random.rand(3,4)

print("原始数组: \n" ,arr)

# 保存二进制文件

import os

try:
    os.mkdir("file")
    np.save("file/data",arr)
    print("保存完成")
except(FileExistsError):
    print("目录已经存在!")
except:
    print("保存时有误!")


print("#####################")

# 读取二进制数据

arr_now= np.load("file/data.npy")
print("从文件读取的数据为:\n",arr_now)
```



<b>执行结果</b>

```
原始数组: 
 [[0.24691883 0.79723734 0.48524809 0.89016276]
 [0.26476342 0.66807029 0.39699836 0.19593967]
 [0.35740223 0.34946823 0.90663193 0.74912478]]
保存完成
#####################
从文件读取的数据为:
 [[0.22861369 0.98080088 0.48784524 0.02089874]
 [0.06466771 0.63922526 0.58108819 0.03602499]
 [0.77763266 0.66487448 0.63186597 0.8468985 ]]
```



---



### <span id="p82">2.读写文本文件（或CSV文件）</span>

* np.savetxt( path, arr, fmt="%.18e", delimiter=" ") 将数组写到某种分隔符隔开的文本文件中，数值格式默认为%18.e，分隔符默认空格
* np.loadtxt(path, delimiter = "," )： 从文本文件中读取数据到数组



<b>例子</b>

```python
import numpy as np

arr = np.random.rand(3,4)

print("原始数组: \n" ,arr)

# 保存二进制文件

import os

try:
    os.mkdir("file_txt")
    np.savetxt("file_txt/datas.txt",arr,delimiter=",")
    print("保存完成")
except(FileExistsError):
    print("目录已经存在!")
except:
    print("保存时有误!")


print("#####################")

# 读取二进制数据

arr_now= np.loadtxt("file_txt/datas.txt",delimiter=",")
print("从文件读取的数据为:\n",arr_now)
```

<b>执行结果</b>

```
原始数组: 
 [[0.25215994 0.39300453 0.6815338  0.71617135]
 [0.92453866 0.17361439 0.51014464 0.98164805]
 [0.06388626 0.71209757 0.27746651 0.36017111]]
目录已经存在!
#####################
从文件读取的数据为:
 [[0.37096793 0.98957892 0.26652605 0.84144371]
 [0.48977396 0.24650103 0.58169573 0.55009748]
 [0.70260296 0.09826307 0.85254984 0.26836472]]
```



---

