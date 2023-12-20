# Series对象的基本操作

## 创建Series

```python
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```
**data**：Series中包含的数据，支持列表、Numpy数组、字典和标量值

**index**：行标签（索引）。值必须是可哈希的，并且具有与数据相同的长度。允许使用非唯一索引值。如果未提供，将默认产生正整数序号。如果数据类似于字典，并且索引为 None，则数据中的键将用作索引。

**dtype**：指定Series数据产生时的数据类型。如果未指定，将自动从数据中推断出来。

**name**：指定索引名称。

**copy**：是否对data进行复制，默认False，此时为视图方式，对Series中数据的修改将影响data。


```python
import pandas as pd
import numpy as np

print('-'*10+'s1'+'-'*10)
s1 = pd.Series([1,10,100,1000])  # 由列表创建。未指定index，自动整数序号；未指定dtype，由数据决定
print(s1)
print('-'*10+'s2'+'-'*10)
s2 = pd.Series(np.arange(3), index=['a', 'b', 'c'])  # 由数组创建。指定索引
print(s2)
print('-'*10+'s3'+'-'*10)
s3 = pd.Series({'Tom': 95, 'Jack': 68, 'Alice': np.nan}, dtype=float, name='score')  # 字典创建，同时指定name和数据类型
print(s3)
```

## 获取Series常用属性

| 方法             | 功能                                                   |
| :----------------: | :------------------------------------------------------ |
| Series.index   | 返回Series对象的索引                                   |
| Series.values  | 返回Series对象的值                                     |
| Series.dtype  | 返回Series对象的数据类型                               |
| Series.hasnans | 当Series对象的值中存在NaN时，返回True；否则，返回False |
| Series.name    | 返回Series对象的名称                                   |


```python
print('-'*10+'index'+'-'*10)
print(s1.index, s2.index, s3.index, sep='\n')
print('-'*10+'values'+'-'*10)
print(s1.values, s2.values, s3.values, sep='\n')
print('-'*10+'name'+'-'*10)
print(s1.name, s2.name, s3.name)
print('-'*10+'dtype'+'-'*10)
print(s1.dtype, s2.dtype, s3.dtype)
print('-'*10+'hasnans'+'-'*10)
print(s1.hasnans, s2.hasnans, s3.hasnans)
```

## 索引Series数据

**位置索引**：类似一维数组的下标索引。


```python
import pandas as pd
import numpy as np

s4 = pd.Series({'高数':95, '英语':85, 'python':96, '物理':88, 'java':78, 'C语言':90}, name='score')
print('-'*10+'s4'+'-'*10)
print(s4)
print('-'*10+'s4[3]'+'-'*10)
print(s4[3])      # 按位置索引获取
print('-'*10+'s4[1:5:2]'+'-'*10)
print(s4[1:5:2])  # 支持切片
print('-'*10+'s4[np.arange(0, 4, 2)]'+'-'*10)
print(s4[np.arange(0, 4, 2)])  # 支持整数数组花式索引
```

**标签索引**：使用字符串标签索引。


```python
import pandas as pd
import numpy as np

s4 = pd.Series({'高数':95, '英语':85, 'python':96, '物理':88, 'java':78, 'C语言':90}, name='score')
print('-'*10+'s4'+'-'*10)
print(s4)
print('-'*10+"s4['英语']"+'-'*10)
print(s4['英语'])  # 按字符串标签索引获取
print('-'*10+"s4['英语':'C语言':2]"+'-'*10)
print(s4['英语':'C语言':2])  # 支持切片，此时包含end
print('-'*10+"s4[['高数', 'python', 'C语言']]"+'-'*10)
print(s4[['高数', 'python', 'C语言']])  # 支持多个标签构成的列表
```

**布尔索引**：通过运算获得的布尔数组索引。


```python
import pandas as pd
import numpy as np

s4 = pd.Series({'高数':95, '英语':85, 'python':96, '物理':88, 'java':78, 'C语言':90}, name='score')
print('-'*10+'s4'+'-'*10)
print(s4)
print('-'*10+"s4[s4 > 90]"+'-'*10)
print(s4[s4 > 90])   # 按比较运算获得的结果索引
print('-'*10+"s4[(s4 >= 80) & (s4 < 90)]"+'-'*10)
print(s4[(s4 >= 80) & (s4 < 90)])    # 多条件组合，每个条件需用括号括起来
print('-'*10+"s4[(s4 > 95) | (s4 < 80)]"+'-'*10)
print(s4[(s4 > 95) | (s4 < 80)])  
```

## 修改Series元素

**通过索引赋值修改**


```python
import pandas as pd
import numpy as np

s4 = pd.Series({'高数':95, '英语':85, 'python':96, '物理':88, 'java':78, 'C语言':90}, name='score')
print('-'*10+'修改前'+'-'*10)
print(s4)
s4['python'] = 90  # 通过索引赋值修改
print('-'*10+'修改后'+'-'*10)
print(s4)
```

**通过replace()方法修改**


```python
import pandas as pd
import numpy as np

s4 = pd.Series({'高数':95, '英语':85, 'python':90, '物理':88, 'java':78, 'C语言':90}, name='score')
print('-'*10+'s4：修改前'+'-'*10)
print(s4)
print('-'*10+'replace返回的新Series'+'-'*10)
print(s4.replace(90, 100))          # 通过replace（）按值修改，默认返回新Series，不修改原Series
print('-'*10+'s4：inplace=False修改后'+'-'*10)
print(s4)
s4.replace(90, 100, inplace=True)  # 设置inplace为True，直接修改原Series，此时函数无返回值
print('-'*10+'s4：inplace=True修改后'+'-'*10)
print(s4)
```

## 删除Series元素

**通过pop(item)方法删除，item为指定的字符串标签。返回该标签对应的值。**


```python
import pandas as pd
import numpy as np

s4 = pd.Series({'高数':95, '英语':85, 'python':90, '物理':88, 'java':78, 'C语言':90}, name='score')
print('-'*10+'s4：修改前'+'-'*10)
print(s4)
print('-'*10+"返回标签'java'对应的值"+'-'*10)
print(s4.pop('java')) 
print('-'*10+'s4：inplace=True修改后'+'-'*10)
print(s4)
```
