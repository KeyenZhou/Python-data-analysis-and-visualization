# NumPy概述


### NumPy简介

![](./数据集/image%20(2).png)

NumPy(Numerical Python)是科学计算和数据分析的基础库，是进行数据处理与可视化的基础，也是科学Python生态系统的基础，支撑着几乎所有进行科学计算的 Python 库，包括 SciPy、Matplotlib、 pandas、 scikit-learn和 scikit-image等。

|![](./数据集/image%20(3).png) |![](./数据集/image%20(4).png)|
|::|:----:|

NumPy主要支持功能包括：
+ 提供快速、节约空间的多维数组，并具有矢量运算和复杂广播能力；
+ 为基于数组的计算提供了大量的标准数学函数；
+ 提供了线性代数、傅里叶变换、随机生成等高级数学功能；
+ 提供了C、C++、Fortran等语言的接口支持

Python中的列表（List）可以保存一组数据，可以用来当作数组使用。但由于列表的元素可以是任何对象，因此列表中保存的是对象的指针，这种结构不适合做数值运算。Python也提供了array模块，能直接保存数值，但它不支持多维数组，也没有各种运算函数，也不适合做数值运算。NumPy的诞生弥补了这些缺陷，它提供了两种基本对象：
+ ndarray：n-dimensional array obiect，用于存储单一数据类型的多维数组。
+ ufunc：universal function obiect，能够能够对数组进行处理的标准函数。

### NumPy导入

通常推荐用以下的方式导入NumPy函数库，库名被缩写为np是一个被广泛采用的约定。
```python
import numpy as np 
```
导入NumPy后，可使用NumPy库中相关帮助函数的获取相关文档与源码。

+ **np.\_\_version\_\_**

查看NumPy库的版本。


```python
import numpy as np

np.__version__
```

+ **numpy.lookfor(what, module=None, import_modules=True, regenerate=False, output=None)**

对NumPy文档执行关键字what搜索，返回搜索的结果。


```python
np.lookfor('lookfor')
```

+ **numpy.info(object=None, maxwidth=76, output=None, toplevel='numpy')**

获取并返回函数、类或模块的帮助信息。


```python
np.info(np.info)   # 运行将返回numpy.info()函数相关文档
```

+ **numpy.source(object, output=<_io.TextIOWrapper>)**
    
打印NumPy对象的源代码或将其写入文件。仅用 Python 编写的对象可返回源代码，库中许多用C语言定义的函数和类不会返回有用的信息。


```python
np.source(np.source)  #  运行将返回numpy.source()函数源代码
```


```python
np.source(np.array)  #  numpy.array()函数由C语言实现，运行将返回'Not available for this object.'
```

学习NumPy可以帮助我们理解面向数组的编程思想，不过对于一般的数据分析与可视化而言，并不需要深入学习NumPy，掌握其中常用方法即可，如需相关具体信息可自行查阅[NumPy官方文档](https://numpy.org/devdocs/index.html)。

### 数组的基本概念

与列表不同，**数组在创建时具有固定的大小，且数组中的所有元素的数据类型都要相同**。常见的包括一维数组、二维数组和三维数组。更高维度的数组使用比较少，此处不赘述。
![](./数据集/image%20(5).png)


NumPy库axis表示轴的意思，**指定某个axis，就是沿着这个axis的方向做相关操作**。一维数组、二维数组和三维数组的axis见上图，明显可以发现，数组有几维就有几个轴。

由于在数组中所有元素的数据类型都是一样的，所以数组的运算和存储效率相对于列表来说要高得多。而且，NumPy专门针对数组的操作和运算进行了设计，存储效率和输入输出性能远优于Python中的嵌套列表。通常数组越大，NumPy的优势就越明显。

分别对有100000个数据的列表和数组，分别对其中每个数字求平方值。根据程序执行所消耗时间对比来比较其运行效率。


```python
import datetime # 导入datetime，用于计算程序运行时间

start = datetime.datetime.now()    # 记录程序开始时间
b = list(range(100000))            # 生成包含100000个数据的列表
a = [i**2 for i in b]              # 使用列表推导式生成平方值列表
end = datetime.datetime.now()      # 记录程序结束时间
during = (end - start).seconds * 1000 + (end - start).microseconds / 1000   # 计算耗时，精确到毫秒 
print(f'\n耗时：{during}毫秒')
```


```python
import datetime # 导入datetime，用于计算程序运行时间
import numpy as np

start = datetime.datetime.now()   # 记录程序开始时间
a = np.arange(100000)             # 生成包含100000个数据的数组
b = a**2                          # 使用数组运算生成平方值数组
end = datetime.datetime.now()  # 记录程序结束时间
during = (end - start).seconds * 1000 + (end - start).microseconds / 1000   # 计算耗时，精确到毫秒 
print(f'\n耗时：{during}毫秒')
```
