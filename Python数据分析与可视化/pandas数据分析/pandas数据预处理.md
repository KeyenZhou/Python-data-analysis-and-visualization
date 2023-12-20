# pandas数据预处理

从外部文件中获取的数据往往存在各种问题，无法直接进行数据分析，需要经过数据预处理（包括数据的清洗、合并、重塑与转换等），解决数据缺失、极端值、数据格式不统一等问题，

本节将结合文件，对数据预处理的常见过程进行讲解。
 
## 1. 处理空值和缺失值

空值使用None表示，缺失值使用NaN表示。pandas中判断DataFrame中是否存在空值和缺失值，通常有如下两个函数：

| **函数名**  | **函数效果**                 |
| :-----------: | :---------------------------- |
| isnull()  | 检查空值或缺失值，返回布尔值，该处为缺失值，返回True，该处不为缺失值，则返回False            |
| notnull() | 检查空值或缺失值，返回了布尔值，该处为缺失值，返回False，该处不为缺失值，则返回True             |


数据下载：
[score_1.csv](./数据集/score_1.csv)
[score_2.csv](./数据集/score_2.csv)
[score_3.csv](./数据集/score_3.csv)
[score_4.csv](./数据集/score_4.csv) 


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_1.csv')
print(score_df)
print('-'*40)
print(score_df.isnull())
print('-'*40)
print(score_df.notnull())
```

![](./数据集/image%20(29).png)
![](./数据集/image%20(30).png)

dropna()方法可用于删除含有空值或缺失值的行或列。其函数原型为：
```python
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```
* axis：指定删除包含缺失值的行或列，默认为0。取值为0或index时删除包含缺失值的行；取值为1或columns时删除包含缺失值的列。
* how：确定删除原则，默认为any。取值为any时，则只要存在缺失值就删除该行或该列；取值为all时，则只有当所有值都为缺失值时，才删除该行或该列。
* thresh：设置有效数据的最小值，如果传入了整数n，则要求该行或该列至少有n个有效值时才将其保留。
* subset：表示在特定子集中的寻找缺失值，如指定的某几列。
* inplace:表示是否原地操作，默认为False。如果设为True，则为原地操作，如果设为False，则修改原数据的副本并返回修改后的副本。



```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_1.csv')
print(score_df)
print('-'*40)
print(score_df.dropna()) # 删除包含缺失值的行
print('-'*40)
print(score_df.dropna(axis=1)) # 删除包含缺失值的列
print('-'*40)
print(score_df.dropna(inplace=True)) # 原地操作，无返回值
print(score_df)
```

![](./数据集/image%20(31).png)
![](./数据集/image%20(32).png)


fillna()方法可实现空值或缺失值的填充。其函数原型为：
```python
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
```
* value：用于填充缺失值的数值
* methon：设置缺失值填充方式，默认为None。若设为pad/ffill，用缺失值前面最后一个有效值代替缺失值；若设为backfill/bfill，用缺失值后面第一个有效值值代替缺失值。该参数不可与value参数同时设置。
* limit:可以连续填充的最大个数，默认为None
其他参数含义与dropna()方法一致。
缺失值通常视具体情况，使用零值、平均值、中位数、众数或临近值填充。


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_1.csv')
print(score_df)
print('-'*40)
print(score_df.fillna(0)) # 用0替换缺失值
print('-'*40)
print(score_df.fillna(method='pad', axis=0)) # 用缺失值所在列的前一个有效数据替换缺失值
print('-'*40)
print(score_df.fillna(method='bfill', axis=1)) # 用缺失值所在行的后一个有效数据替换缺失值
```

![](./数据集/image%20(33).png)
![](./数据集/image%20(34).png)
![](./数据集/image%20(35).png)

## 2. 重复值处理

当数据中出现了重复值，会对后续的分析结果产生影响，大多数情况需要删除。pandas提供了两个方法用于处理重复值。

duplicated()方法用于标注出DataFrame中的重复值。其函数原型为：
```python
DataFrame.duplicated(subset=None, keep='first')
```
* subset：设置需识别重复的列标签或列标签序列，默认识别所有列标签。
* keep：设置标记重复的规则，默认值为first。值为first，从前向后查找，除了第一次出现的项其余相同的均标记为重复；值为last，从后往前查找，除了最后一次出现的项其余相同的均标记为重复；值为False，所有相同的标记均标记为重复。


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_1.csv')
print(score_df)
print('-'*40)
print(score_df.duplicated()) # first,除了第一次出现的项其余相同的均标记为重复
print('-'*40)
print(score_df.duplicated(keep='last')) # last,除了最后一次出现的项其余相同的均标记为重复
print('-'*40)
print(score_df.duplicated(keep=False)) # False，所有相同的均标记为重复
```

![](./数据集/image%20(36).png)
![](./数据集/image%20(37).png)
![](./数据集/image%20(38).png)


drop_duplicates()方法用于从DataFrame对象中删除重复值。其函数原型为：
```python
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
```


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_1.csv')
print(score_df)
print('-'*40)
print(score_df.drop_duplicates()) # first,除了第一次出现的项其余相同的均删除
print('-'*40)
print(score_df.drop_duplicates(keep='last')) # last,除了最后一次出现的项其余相同的均删除
print('-'*40)
print(score_df.drop_duplicates(keep=False)) # False，所有相同的均删除
```

![](./数据集/image%20(39).png)
![](./数据集/image%20(40).png)
![](./数据集/image%20(41).png)

## 3. 更改数据类型

在处理数据时可能会遇到数据类型不一致的问题，此时可对指定区域的数据类型进行修改以保持一致。

astype()方法用于设置数据类型，其函数原型为：
```python
DataFrame.astype(dtype, copy=True, errors='raise')
```
* dtype：要设置的数据类型
* copy：设置是否建立副本，默认为True
* errors：设置异常处理方式，默认为raise，允许引发异常；设置为ignore则抑制异常。


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_1.csv')
score_df.fillna(0,inplace=True) # 用0替换缺失值，原地操作
score_df.drop_duplicates(inplace=True) # 删除除第一次外的重复值，原地操作
print(score_df)
print('-'*40)
score_df.loc[:, 'C语言':'C++'] = score_df.loc[:, 'C语言':'C++'].astype(float)  # 将所有成绩设置为float类型，并更新原DataFrame
print(score_df)
```

## 4. 数据合并

使用concat()函数可以沿着一条轴对多个对象进行合并，函数原型为：
```python
pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)
```
* axis：设置连接的轴向，默认为0，纵向合并，为1时横向合并
* join：设置连接方式，inner表示内连接，outer表示外连接，默认外连接
* ignore_index：默认为False，如果设置为True，则表示清除现有索引并重置索引值
* keys：接收序列，表示添加最外层索引
* levels：用于构建多级索引的特定级别
* names：在设置了keys和level参数后，用于创建分层级别的名称
* verify_integerity：检查新的连接轴是否包含重复值。为True时，如果有重复的轴将会抛出错误，默认为False

合并时缺失值使用NaN填充。



```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df_1 = pd.read_csv('/data/bigfiles/score_1.csv')
score_df_2 = pd.read_csv('/data/bigfiles/score_2.csv')
print(score_df_1)
print('-'*40)
print(score_df_2)
print('-'*40)
print(pd.concat([score_df_1, score_df_2]))  # 纵向合并，外连接，行索引会有重复
print('-'*40)
print(pd.concat([score_df_1, score_df_2], join='inner', ignore_index=True))  # 纵向合并，内连接，行索引被重置
print('-'*40)
print(pd.concat([score_df_1, score_df_2], axis=1))  # 横向合并，外连接，行索引会有重复
print('-'*40)
print(pd.concat([score_df_1, score_df_2], axis=1, join='inner'))  # 横向合并，内连接，行索引被重置
```

![](./数据集/image%20(42).png)
![](./数据集/image%20(43).png)
![](./数据集/image%20(44).png)
![](./数据集/image%20(45).png)



使用merge()函数可根据一个或多个键将两个DataFrame对象合并。函数原型为：
```python
pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
```
* left：设置参与合并的左侧DataFrame对象
* right：设置参与合并的右侧DataFrame对象
* how：表示连接方式，默认为inner。值为left，左外连接；值为right，右外连接；值为outer，全外连接；值为inner，内连接。
* on：设置用于连接的列名，必须存在于两个DataFrame对象中
* left_on：设置左侧DataFarme中用作连接键的列
* right_on：设置右侧DataFarme中用作连接键的列
* left_index：为True时，将左侧的行索引用作其连接键
* right_index:为True时，将右侧的行索引用作其连接键
* sort:设置是否根据连接键对合并后的数据进行排序，默认为False。在处理大数据集时，禁用该选项可获得更好的性能
* suffixes:设置用于追加到重叠列名的末尾字符，默认为（‘_x’,‘_y’）.例如，左右两个DataFrame对象都有‘data’，则结果中就会出现‘data_x’，‘data_y’


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df_left = pd.read_csv('/data/bigfiles/score_1.csv')
score_df_right = pd.read_csv('/data/bigfiles/score_3.csv')
score_df_left.drop_duplicates(inplace=True)
score_df_left.loc[:, 'C语言':'C++'] = score_df_left.loc[:, 'C语言':'C++'].astype(float)  # 将所有成绩设置为float类型，并更新原DataFrame
score_df_right.loc[:, '高数':'C语言'] = score_df_right.loc[:, '高数':'C语言'].astype(float)  # 将所有成绩设置为float类型，并更新原DataFrame
print(pd.merge(score_df_left, score_df_right, on='学号')) # 按学号合并，内连接
```

![](./数据集/image%20(46).png)


```python
print(pd.merge(score_df_left, score_df_right, on=['学号', '姓名'])) # 按学号与姓名合并，内连接
```

![](./数据集/image%20(47).png)


* 内连接(inner):匹配两个DataFrame对象中均有的键值并合并
* 外连接(outer):合并两个DataFrame对象中所有的键值，缺失值用NaN填充
* 左连接(left):以merge函数中第一个出现的DataFrame对象的指定键值为标准进行连接，第一个出现的DataFrame表中数据将会全部显示，而第二个出现的DataFrame对象只会显示与重叠数据行索引相同的数据，合并后缺失数据用NaN填充
* 右连接(right):以merge函数中第二个出现的DataFrame对象的指定键值为标准进行连接，第二个出现的DataFrame表中数据将会全部显示，而第一个出现的DataFrame对象只会显示与重叠数据行索引相同的数据，合并后缺失数据用NaN填充


```python
print(pd.merge(score_df_left, score_df_right, how='outer', on='学号')) # 按学号合并，全外连接
```

![](./数据集/image%20(48).png)



```python
print(pd.merge(score_df_left, score_df_right, how='left', on='学号')) # 按学号合并，左外连接
```

![](./数据集/image%20(49).png)



```python
print(pd.merge(score_df_left, score_df_right, how='right', on='学号')) # 按学号合并，右外连接
```

![](./数据集/image%20(50).png)


此外，DataFrame对象还有一个join()方法，可以看作是merge()函数的简化版。merge()包含了join()操作，支持两个DataFrame行方向或列方向的拼接操作，而join只是简化了merge的行方向拼接的操作。join()方法的函数原型如下，参数含义基本与merge()相同，此处不再举例说明。
```python
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
```

## 5. 数据重塑

有时候需要将数据重塑，使其更符合分析处理的需要。

stack()方法可用于将数据的列堆叠到行，其函数原型为：
```python
DataFrame.stack(level=- 1, dropna=True)
```
* level:指定从列轴到行轴的堆栈级别，默认为-1
* dropna:表示是否删除旋转后的缺失值，默认为True


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_3.csv', nrows=2, usecols=['姓名', 'Python', 'C语言']) # 读取文件除标题行外前两行的指定列
s1 = score_df.stack()   # 列堆叠到行
print(s1[0])            # 多重索引，获得Series
print(s1[0]['Python'])  # 获得罗明的Python成绩 
```

![](./数据集/image%20(51).png)


unstack()方法可用于将数据的行堆叠到列，其函数原型为：
```python
DataFrame.unstack(level=- 1, fill_value=None)
```


```python
new_df = s1.unstack()   # 还原
print(new_df)
s2 = score_df.unstack()   # 行堆叠到列
print(s2['Python'])       # 多重索引，获得Series
print(s2['Python'][0])    # 获得罗明的Python成绩 
```

![](./数据集/image%20(52).png)


pivot()方法提供的功能是根据给定行索引或列索引重新组织一个DataFrame对象，类似于excel的数据透视表，返回DataFrame按指定行(index)或列(column)重构的数据透视表。其函数原型为：
```python
DataFrame.pivot(index=None, columns=None, values=None)
```
* index：指定哪一列来做为重构后的新DataFrame的行索引，默认为None，则使用现在的索引
* columns：指定哪一行来做为重构后的新DataFrame的列索引，默认为None，则使用现在的索引
* values：用于填充新Dataframe的值，如果未指定，使用除了index和columns列的其余所有列的值


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_4.csv')
print(score_df.pivot(index='姓名', columns='科目', values='成绩'))
```

![](./数据集/image%20(53).png)


## 6. 重命名轴索引

通过rename()方法可以对列索引或行索引的标签或名称重命名。其函数原型为：
```python
DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore')
```
* mapper：一般为字典值，键表示原索引，值表示新索引。也可以是函数
* index：一般为字典值，键表示原行索引，值表示新行索引。也可以是函数
* columns：一般为字典值，键表示原列索引，值表示新列索引。也可以是函数
* axis：index或0表示行，columns或1表示列
* copy：如果为True，则复制基础数据
* inplace：如果为True，则在原始 DataFrame中进行更改（原地操作）
* level:用于在数据帧具有多个级别索引的情况下指定级别


```python
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
score_df = pd.read_csv('/data/bigfiles/score_3.csv')
print(score_df)
print('-'*40)
index_dict = dict(zip(score_df.index, score_df['学号'])) # 原index与学号列构成字典
print(index_dict)
print('-'*40)
print(score_df.rename(mapper=index_dict, axis='index'))   # 根据mapper参数的字典重命名行索引
print('-'*40)
print(score_df.rename(index=index_dict))                  # 使用index参数，无需设置axis，与上一条语句功能相同
print('-'*40)
print(score_df.rename(mapper=lambda x:f'{x:04d}', axis='index'))  # 支持函数，行索引转为4位数值字符串，不足4位左补0
print('-'*40)
print(score_df.rename(index=lambda x:f'{x:04d}'))                 # 使用index参数，无需设置axis，与上一条语句功能相同
```

![](./数据集/image%20(54).png)
![](./数据集/image%20(55).png)


```python
columns_dict={'姓名':'Name', '学号':'Stu_No', '高数':'Math', '英语':'English', '物理':'Physics', 'C语言':'C_lan'}
print(score_df.rename(mapper=columns_dict, axis='columns'))   # 根据mapper参数的字典重命名列索引
score_df.rename(columns=columns_dict, inplace=True)           # 使用columns参数，无需设置axis，与上一条语句功能相同，但为原地操作
print('-'*40)
print(score_df)
print(score_df.rename(mapper=lambda x:x.lower(), axis='columns'))  # 支持函数，列索引转为全小写
print('-'*40)
print(score_df.rename(columns=lambda x:x.lower()))                 # 使用columns参数，无需设置axis，与上一条语句功能相同
```

![](./数据集/image%20(56).png)
![](./数据集/image%20(57).png)
