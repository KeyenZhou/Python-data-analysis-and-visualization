# pandas数据运算与数据统计

## 1.算术运算

Pandas 库中的算术运算是数据集之间根据索引进行运算。如果存在不同的索引对，运算的结果是相同索引数据和不同索引数据的并集，并且用 NaN 填充运算结果。
当进行对应索引列之间的加减乘除运算时，要注意对应索引列之间的类型是否相同，如果不同类型进行运算时会报类型转换错误，同时，要考虑到该类型是否能进行某种算术运算，比如字符串之间的加法运算是可以的，但是字符串之间是不存在减法、乘法和除法运算的，否则会报错。

Pandas 库中的算术运算可以使用算术运算符，也可以使用算数运算函数，常用的算数运算函数如下表。

| 算术运算函数 | 用法介绍(以DataFrame为例) | 描述                      |
| :------------: | :-------------------------: | :------------------------- |
| add()        | df1.add(df2)              | df1与df2进行加法运算，df1+df2      |
| radd()       | df1.radd(df2)             | df2与df1进行加法运算，df2+df1     |
| sub()        | df1.sub(df2)              | 用df1减df2，df1-df2                |
| rsub()       | df1.rsub(df2)             | 用df2减df1，df2-df1              |
| mul()        | df1.mul(df2)              | df1与df2进行乘法运算，df1\*df2      |
| rmul()       | df1.rmul(df2)             | df2与df1进行乘法运算，df2\*df1      |
| div()        | df1.div(df2)              | 用df1除df2，df1/df2                |
| rdiv()       | df1.rdiv(df2)             | 用df2除df1，df2/df1                |
| truediv()    | df1.truediv(df2)          | 用df1除df2，df1/df2                |
| rtruediv()   | df1.rtruediv(df2)         | 用df2除df1，df2/df1                 |
| floordiv()   | df1.floordiv(df2)         | 用df1除df2，取整除，df1//df2        |
| rfloordiv()  | df1.rfloordiv(df2)        | 用df2除df1，取整除，df2//df1        |
| mod()        | df1.mod(df2)              | 用df1除df2，取余数，df1%df2       |
| rmod()       | df1.rmod(df2)             | 用df2除df1，取余数，df2%df1        |
| pow()        | df1.pow(df2)              | 计算df1的df2次方，df1^df2 |
| rpow()       | df1.rpow(df2)             | 计算df2的df1次方，df2^df1 |

在Pandas中，这些运算的用法和规则都相同，运算结果的数据结构也都相同，所以下面仅以加法举例，其他运算大家可自行尝试。


```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['i1', 'i2', 'i3', 'i4'], columns=['c1', 'c2', 'c3', 'c4'])
df2 = pd.DataFrame(np.eye(4), index=['i1', 'i2', 'i3', 'i4'], columns=['c1', 'c2', 'c3', 'c4'])
df3 = pd.DataFrame(np.arange(9).reshape((3,3)), index=['i1', 'i3', 'i5'], columns=['c2', 'c4', 'c6'])
s1 = pd.Series(np.logspace(1,4,4), index=['i1', 'i2', 'i3', 'i4'])
s2 = pd.Series(np.logspace(1,4,4), index=['c1', 'c2', 'c3', 'c4'])
s3 = pd.Series(np.logspace(1,2,2), index=['i1', 'c4'])
print('-'*10+'df1'+'-'*10)
print(df1)
print('-'*10+'df2'+'-'*10)
print(df2)
print('-'*10+'df3'+'-'*10)
print(df3)
print('-'*10+'df1+10'+'-'*10)
print(df1+10)    # DataFrame与标量运算，每个元素与标量做相同运算，得到一个新的DataFrame
print('-'*10+'df1+df2'+'-'*10)
print(df1+df2)   # 两个形状和对应的索引都一样的DataFrame相加，直接将对应位置的数据相加，得到一个新的DataFrame
print('-'*10+'df1.add(df3)'+'-'*10)
# 两个的形状或索引不完全一样DataFrame相加，只会将两个DataFrame中行索引和列索引对应的数据相加，
#生成一个形状能兼容两个DataFrame的新DataFrame，其他没有运算结果的位置填充空值(NaN)。
print(df1.add(df3)) 
print('-'*10+'df1.add(s1, axis=0)'+'-'*10)
# Series的索引与DataFrame的行索引对应，可以将axis参数设置成0或'index'，
# Series依次与DataFrame中的每一列数据进行运算，得到一个新的DataFrame。
print(df1.add(s1, axis=0))  
print('-'*10+'df1.add(s2)'+'-'*10)
# Series的索引与DataFrame的列索引对应，此时axis参数设置成0（默认值）或'columns'，
# Series依次与DataFrame中的每一行数据进行运算，得到一个新的DataFrame。
print(df1.add(s2))
print('-'*10+'df1.add(s3)'+'-'*10)
# Series的行索引与DataFrame的行索引或列索引不完全相同，根据axis取值，
# 会得到一个形状能兼容DataFrame和Series的新DataFrame。
print(df1.add(s3, axis='index'))
print(df1.add(s3, axis='columns'))
```

![](./数据集/image%20(20).png)
![](./数据集/image%20(21).png)
![](./数据集/image%20(22).png)
![](./数据集/image%20(23).png)
![](./数据集/image%20(24).png)
![](./数据集/image%20(25).png)

## 2. 关系运算与逻辑运算

pandas中的关系运算与Numpy中类似，将返回一个由布尔值组成的Series或DataFrame对象，主要用于条件过滤，即根据条件筛选出符合要求的数据，

pandas的逻辑运算同样主要用于条件过滤，但与Python基础语法中的逻辑运算存在一些差异。进行或（|）、与（&）、非（~）运算时，各个独立逻辑表达式需要用括号。

有关通过比较运算和逻辑运算进行数据筛选，在‘DataFrame的基本操作’中已经举例介绍过，此处不再赘述。

## 3. 常用统计分析方法

pandas提供了一些数据统计分析的函数，这些函数使用于Series和DataFrame类型。下面以文件‘score_3.csv’中的学生成绩分析为例，介绍一些常用的方法。

数据下载：  
[scoregroup.csv](./数据集/scoregroup.csv)
[score_3.csv](./数据集/score_3.csv)


```python
import pandas as pd

score_df = pd.read_csv('/data/bigfiles/score_3.csv')
score_df
```

使用describe()方法，可以获得Series或DataFrame的统计变量。可方便观察这一系列数据的范围、大小、波动趋势等等，为后面的分析打下基础。函数原型为：
```python
DataFrame.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)
```

* percentiles：设定数值型特征的统计量，默认\[.25, .5, .75\],返回25%，50%，75%时候的数据，可修改
* include：默认只输出数值型数据的统计信息,设置参数为'all'则输入的所有列都在输出中,设置为O则只输出离散型变量的统计信息。
* exclude：与include参数相反，用于设置不输出哪些类型。默认不排除任何数据


```python
score_df.describe() # 默认只输出数值型数据的统计信息
```


```python
score_df.describe(include='all') # 输出所有列的统计信息
```


```python
score_df[['Python', 'Java', 'C语言']].describe(percentiles=[0.3, 0.7, 0.9]) # 输出指定列的统计信息，并设置percenttiles
```

统计数据的含义如下：

|名称|含义|名称|含义|
|:-----:|:-----|:-----:|:------|
|top|最常见的值|freq|标识最常见的值的出现频次|
|count|有效值数量|unipue|不同的值数量|
|std|标准差|min|最小值|
|25%|四分之一分位数|50%|二分之一分位数|
|75%|四分之三分位数|max|最大值|
|mean|均值||

其他常用统计分析方法见下表。

|     方法      | 功能                         |   方法   | 功能         |
| :-----------: | :--------------------------- | :------: | :----------- |
|  describe()   | 一次性输出多个描述性统计指标 | count()  | 非空元素计算 |
|     min()     | 最小值                       |  max()   | 最大值       |
|   idxmin()    | 最小值的位置                 | idxmax() | 最大值的位置 |
| quantile(0.1) | 10%分位数                    |  sum()   | 求和         |
|    mean()     | 均值                         | median() | 中位数       |
|    mode()     | 众数                         |  var()   | 方差         |
|     std()     | 标准差                       |  mad()   | 平均绝对偏差 |
|    skew()     | 偏度                         |  kurt()  | 峰度         |
|     abs()     | 求绝对值                     |   prod()   | 元素乘积     |
|    cumsum()     | 累计和                       | cumprod()  | 累计乘积     |

大部分方法的功能与Numpy中的函数功能类似，下面结合例子简单介绍。


```python
print('Python总分：', score_df['Python'].sum(), 'Python平均分：', score_df['Python'].mean()) # 求Python课程的总分和平均分
print('Python最高分：', score_df['姓名'][score_df['Python'].idxmax()], score_df['Python'].max()) # 求Python课程的总分和平均分
print('Python成绩标准差：', score_df['Python'].std())  # 默认ddof=1，无偏方差，与Numpy不同。
```

## 4. 排序与排名

pandas中的常用的排序方法由两个，分别是按索引排序方法sort_index()和按值排序方法sort_values()。函数原型为：
```python
DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
```

* axis：0按照行名排序；1按照列名排序
* ascending：默认True升序排列；False降序排列
* inplace：默认False，否则排序之后的数据直接替换原来的数据框
* kind：默认quicksort，排序的方法
* na_position：缺失值默认排在最后{"first","last"}

```python
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
```
* axis:{0 or ‘index’, 1 or ‘columns’}, default 0，默认按照索引排序，即纵向排序，如果为1，则是横向排序    
* by:str or list of str；如果axis=0，那么by="列名"；如果axis=1，那么by="行名"；  
* ascending:布尔型，True则升序，可以是\[True,False\]，即第一字段升序，第二个降序  
* inplace:布尔型，是否用排序后的数据框替换现有的数据框  
* kind:排序方法，{‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’。 
* na_position : {‘first’, ‘last’}, default ‘last’，默认缺失值排在最后面 


```python
score_df.sort_index(axis=1)
```


```python
score_df.sort_values(by=['C语言','Python'], ascending=False)
```

![](./数据集/image%20(26).png)

rank()方法可用于沿着某个轴（0或者1）计算对象的排名，并返回排名结果。函数原型为：
```python
DataFrame.rank(axis=0, method='average', numeric_only=NoDefault.no_default, na_option='keep', ascending=True, pct=False)
```
* axis：设置沿着哪个轴计算排名（0或者1)
* numeric_only：是否仅仅计算数字型的columns，布尔值
* na_option：NaN值是否参与排序及如何排序（‘keep’，‘top'，’bottom'）
* ascending：设定升序排还是降序排
* pct：是否以排名的百分比显示排名（所有排名与最大排名的百分比）
* method：取值可以为'average'，'first'，'min'， 'max'，'dense'。average，在相等分组中，为各个值分配平均排名 (默认)；min，使用整个分组的最小排名；max，使用整个分组的最大排名；first，按值在原始数据中的出现顺序分配排名；dense，类似 min，但是组之间的等级总是增加1。


```python
score_df.rank()
```

![](./数据集/image%20(27).png)


```python
python_score_df = score_df[['姓名', '学号', 'Python']].copy()  # 提取所有学生Python成绩的副本
python_score_df['排名'] = score_df['Python'].rank(method='min', ascending=False) # 增加一列python成绩排名
python_score_df
```

## 5. 计算相关系数

corr()方法检查指定列之间的相关系数（变化趋势的方向以及程度），返回值各列之间的相关系数DataFrame。值范围-1到+1，0表示两个变量不相关，正值表示正相关，负值表示负相关，值越大相关性越强。函数原型为：
```python
DataFrame.corr(method='pearson', min_periods=1)
```
* method：可选值pearson、kendall或spearman。pearson即皮尔森相关性系数，针对线性数据的相关系数计算，针对非线性数据便会有误差；kendall即肯德尔秩相关系数，用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据；spearman即斯皮尔曼等级相关系数，主要用于非线性的、非正态分布的数据的相关系数。
* min_periods：样本最少的数据量


```python
pd.set_option('display.unicode.east_asian_width', True)  # 设置输出列对齐
score_df['学号'] = score_df['学号'].astype(str)
print(score_df)
score_df.corr()
```

## 6.  数据分组统计

在数据分析中，经常会遇到这样的情况：根据某一列（或多列）标签把数据划分为不同的组别，然后再对其进行数据分析。在 Pandas 中，要完成数据的分组操作，需要使用groupby()方法。其函数原型为：
```python
DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=NoDefault.no_default, observed=False, dropna=True)
```
* by：用于确定groupby的组。如果by是一个函数，它会在行位置索引的每个值上调用。如果传递了dict或Series，则Series或dict VALUES将用于确定组。
* axis：沿行 (0) 或列 (1) 拆分。
* level：如果轴是多级标签索引，则按一个或多个特定级别进行分组。
* as_index：对于聚合输出，返回具有组标签作为索引的对象。
* sort：对组键进行排序。 关闭此功能可获得更好的性能。 
* group_keys：当调用apply时，将组键添加到index以识别片段。
* squeeze：如果可能，降低返回类型的维数，否则返回一致的类型。
* observed：如果为True，仅显示分类分组的观察值；如果为 False，显示分类分组的所有值。
* dropna：如果为True，并且组键包含NA值，则NA值连同行/列将被删除；如果为False，NA值也将被视为组中的键。

下面以文件“scoregroup.csv”为例讲解group()方法的使用，文件部分内容如下图。
![](./数据集/image%20(28).png)


```python
import pandas as pd

score_df = pd.read_csv('/data/bigfiles/scoregroup.csv',dtype={'学号':str}, encoding='utf-8')
score_groups = score_df.groupby('学号')  # 按学号分组
score_groups
```

返回的结果是一个DataFrameGroupBy对象，可通过调用groups属性查看分组结果，其值是一个字典，字典键是用来分类的数据，值是分类对应的行索引值。


```python
score_groups.groups
```

DataFrameGroupBy对象的get_group()方法可以获取分组之后指定组的数据。


```python
score_groups.get_group('0121701100521')
```


```python
score_groups_by2 = score_df.groupby(['学号', '姓名'])  # 按学号和姓名两列分组
score_groups_by2.groups
```


```python
score_groups_by2.get_group(('0121701100623', '孙伟'))
```


```python
# 按函数返回值分组，设置学号位行索引，按学号倒数3、4位班级号分组
score_groups_by_func = score_df.set_index('学号').groupby(lambda x:x[-4:-2])  
score_groups_by_func.groups
```

在得到DataFrameGroupBy对象后，我们就可以根据需要进行相应的统计。

* ### 在DataFrameGroupBy对象后直接加统计分析聚合函数


```python
score_groups_by2 = score_df.groupby(['学号', '姓名'])  # 按学号和姓名两列分组
score_groups_by2.sum()    #  统计每个学生的总分
```


```python
score_groups_by_course = score_df.groupby('课程名')  # 按课程分组
score_groups_by_course.mean()    #  统计每门课的平均分
```

* ### 使用agg()方法对DataFrameGroupBy对象应用多个聚合函数
agg()的功能更加强大，除了可以向agg()函数中传入聚合函数外，也常用列表、字典等形式作为参数。


```python
score_groups_by_course = score_df.drop(['学号', '姓名'], axis=1).groupby('课程名')  # 按课程分组
score_groups_by_course.agg(['mean', 'median', 'max', 'min'])  #  统计每门课的平均分、中位数、最高分和最低分
```


```python
score_groups_by_course = score_df.groupby('课程名')  # 按课程分组
 #  传字典，每列统计不同数据
score_groups_by_course.agg({'分数':['mean', 'sum'], '学号':['count']}) 
```

* ###  使用apply()方法对DataFrameGroupBy对象应用自定义函数


```python
# 统计指定分值区间内的人数
def count_by_interval(df, start=0, end=101):
    return ((df['分数'] >= start) & (df['分数'] < end)).sum()

score_groups_by_course = score_df.groupby('课程名')  # 按课程分组
 #  传字典，每列统计不同数据
score_groups_by_course.apply(count_by_interval, end=60)  # 统计每门课的不及格人数
```

* #### 使用filter()方法对DataFrameGroupBy对象进行数据筛选
根据定义的条件函数过滤数据，并返回一个新的数据集。


```python
score_groups_by2 = score_df.groupby(['学号', '姓名'])  # 按学号和姓名两列分组
score_groups_by2.filter(lambda df:df['分数'].mean()>=85 ) # 返回平均分在85分以上的学生构成的新数据集
```
