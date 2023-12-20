# NumPy读写文本文件

NumPy提供了多种文本文件操作函数，用于从文本文件中读取数据形成数组，或将数组数据按相应的格式写入文本文件保存。

## 读文本文件

NumPy中用于读取文本文件的方法主要有loadtxt()和genfromtxt()，两者都可以用于读取txt或者csv文件。

### 1. loadtxt()方法

该方法用于从文本文件加载数据到二维数组中，文本文件中的每一行必须具有相同数量的值。函数原型为：
```python
numpy.loadtxt（fname， dtype=<class 'float'>， comments='#'， delimiter=None， converters=None， skiprows=0， usecols=None， unpack=False， ndmin=0， encoding='bytes'， max_rows=None， *， quotechar=None， like=None)
```
文件<a href="https://data.educoder.net/api/attachments/3400630?type=office&disposition=inline" target="_blank">8.5 score.csv</a>中保存学生成绩数据，其数据部分包括整数、浮点数和缺失数据（郑君 C 语言和 VB 成绩缺失），文件中数据见下图。下面以对这个文件的读取为例介绍几个主要参数的含义。

![](./数据集/image%20(6).png)


```python
!tar -xvf /data/bigfiles/15b3ee0f-8ce0-41ab-bba7-c48188bb3f0d.tar
```

+ **fname：**要读取的文件、文件名、列表或生成器。其中，生成器必须返回字节或字符串，列表中或由生成器生成的字符串被视为行。如果是.gz或.bz2的压缩文件，则会先解压缩文件。
+ **dtype：**生成数组的数据类型，默认值是 dtype=float。设置 dtype=None 时，每个列的类型从每行的各列数据中迭代确定。函数依次检查各列数据是否可以转换为布尔值、整数、浮点数、复数和字符串，直到满足条件为止。但这种方法处理速度明显慢于明确设置 dtype 数据类型。
+ **delimiter：**用于分隔值的字符串，默认值为空格。用于定义按什么字符拆分数据行。
+ **encoding：**值为字符串，用于指定解码输入文件的编码类型，当“fname”是文件对象时不可使用此参数。默认值为“bytes”，此时启用向后兼容的方案，确保在可能的情况下接收字节数据，并将拉丁编码的字符串传给转换器。当值设置为“None”时，应用操作系统的默认编码，一般windows系统默认使用GBK编码。重写此值将可以接收 unicode 数组并将字符串作为输入传递给转换器。


```python
import numpy as np
 
file = '8.5 score.csv'
data = np.loadtxt(file, dtype=str, delimiter=',', encoding='utf-8') # 字符串类型，逗号分隔，utf-8编码
print(data)
```

+ **skiprows：**值为整数。文件开头数据描述的存在可能阻碍数据处理，此时可以使用skiprows参数。参数的值为读取文件时跳过的行数，缺省值为 skip_header=0，表示不略过任何行。


```python
import numpy as np
 
file = '8.5 score.csv'
data = np.loadtxt(file, dtype=str, delimiter=',', skiprows=1, encoding='utf-8') # 跳过标题行
print(data)
```

+ **usecols：**整数序列，指明哪些列将被读取，序号从 0 开始。在某些情况下，只希望返回其中的几个列的数据，可以使用 usecols 参数选择要导入哪些列。此参数接受单个整数或对应于要导入的列的索引的整数序列。例如：“usecols = (1, 4, 5)”将读取第 2 列、第 5 列和第 6 列数据。


```python
import numpy as np
 
file = '8.5 score.csv'
data = np.loadtxt(file, dtype=str, delimiter=',', skiprows=1, usecols=range(2,8), encoding='utf-8') # 仅读取成绩部分（2-7列）
print(data)
```

+ **converters：**转换器，用于对数据进行预处理。值为函数名或包含键值对“列索引:函数名”的字典。


```python
import numpy as np
 
file = '8.5 score.csv'
data = np.loadtxt(file, dtype=float, delimiter=',', skiprows=1, usecols=range(2,8), 
                  converters=lambda s: float(s.strip() or 0), # 将所有列数据转换为浮点数，并处理空值为0.0
                  encoding='utf-8') 
print(data)
data_1 = np.loadtxt(file, dtype=str, delimiter=',', skiprows=1, usecols=range(2,8), 
                  converters={7:lambda s: round(float(s)/5, 2)}, # 将第7列转换为5门课的平均分，并保留最多2位小数
                  encoding='utf-8') 
print(data_1)
```

+ **unpack：**布尔值，默认值为 False，当该值为 True 时，返回的数组将被转置，以便可以使用 x, y, z = genfromtxt(...) 解压参数。当 unpack 参数与记录数据类型一起使用时，每个字段都返回数组。


```python
import numpy as np
 
file = '8.5 score.csv'
data = np.loadtxt(file, dtype=str, delimiter=',', unpack=True, encoding='utf-8') # 数组转置
print(data)
java_scores, python_scores = np.loadtxt(file, dtype=float, delimiter=',', skiprows=1, 
                                       usecols=(3, 4), unpack=True,   # 仅读取java与python成绩，并赋值给不同对象
                                       encoding='utf-8') 
print(java_scores)
print(python_scores)
```

+ **max_rows：**在跳过skiprows指定的行之后，最多读取max_rows行内容。默认值为None，表示读取所有行。


```python
import numpy as np
 
file = '8.5 score.csv'
data = np.loadtxt(file, dtype=str, delimiter=',', max_rows=3, skiprows=1, encoding='utf-8') # 跳过标题行后，只读取3行
print(data)
```

+ **comments：**字符串或字符串序列，用于指明注释开始的字符，默认值为'#'。注释标记可以出现在该行的任何地方，读取时注释符号后面的所有字符都会被忽略。
+ **ndmin：**整形值，用于指定返回的ndarray至少包含特定维度，值域 0/1/2，默认为 0。
+ **quotechar：**值为字符，定义用于表示引用项的开始和结束的字符。在一对quotechar包围的项中，出现的分隔符或注释字符将被忽略。默认值为None，表示禁用该功能。如果在一对quotechar包围的字段中发现两个连续的quotechar实例，则第一个实例将被视为转义字符。


### 2. genfromtxt()方法

与loadtxt()类似，从文本文件加载数据到数组，并可按指定方式处理缺失值，面向的是结构化数组和缺失数据的处理。函数原型为：
```python
numpy.genfromtxt（fname， dtype=<class 'float'>， comments='#'， delimiter=None， skip_header=0， skip_footer=0， converters=None， missing_values=None，filling_values=None， usecols=None， names=None， excludelist=None， deletechars="！#$%&'（）*+， -./：;<=>？@[\\]^{|}~"， replace_space='_'， autostrip=False， case_sensitive=True， defaultfmt='f%i'， unpack=None， usemask=False， loose=True， invalid_raise=True， max_rows=None， encoding='bytes'， *， ndmin=0， like=None)
```
该方法部分主要参数的含义和用法与 loadtxt() 方法的参数类似，下面对其独有的常用参数做简单介绍。

+ **delimiter：**值为字符串、整数或序列。其值为字符串时，与loadtxt()方法中的delimiter参数作用相同。处理具有固定宽度的数据文件时，可用整数或整数序列确定每个字段的宽度。当所有列具有相同宽度时，值可设为单个整数；当各列宽度具有不同大小时，值可设为一个整数的序列。
+ **skip_header：**值为整数。文件开头数据描述的存在可能阻碍数据处理，此时可以使用 skip_header 参数。参数的值对应于在执行任何其他操作之前在文件开头跳过的行数，缺省值为 skip_header=0，表示不略过任何行。
+ **skip_footer：**与skip_header类似，可以使用 skip_footer 参数来跳过文件的最后若干行，缺省值为 skip_footer=0，表示不跳过任何行。


```python
import numpy as np

file = '8.5 score.csv'
data = np.genfromtxt(file, dtype=str, delimiter=',', encoding='utf-8', # 字符串类型，逗号分隔，utf-8编码
                    skip_header=1, skip_footer=2)                      # 跳过第一行和最后2行
print(data)
```

+ **missing_values：**设置哪些字符串被视为缺失数据。默认情况下，任何空字符串都被标记为缺失。但文件中也有可能有更复杂的字符串，比如 "N/A" 或 "???" 也代表丢失或无效的数据。missing_values 参数接受三种值：单个字符串或逗号分隔的字符串，该字符串将用作所有列缺失数据的标记；字符串序列，此时序列中每个项目都按顺序与列关联；字典，字典的值是字符串或字符串序列，相应的键可以是列索引（整数）或列名称（字符串），也可以使用特殊键 None 来定义适用于所有列的默认值。
+ **filling_values：**为缺失数据提供一个默认值。默认情况下，缺失值根据dtype参数确定（如int对应-1，string对应'???'，float对应np.nan）。通过 filling_values参数，我们可以更好地控制缺失值的转换。filling_values参数接受三种值：单个值，所有列的默认值；序列，序列中每个项目都按顺序与列关联，作为相应列的默认值；字典类型，每个键可以是列索引或列名称，并且相应的值应该是单个对象做默认值，也可以使用特殊键None为所有列定义默认值。


```python
import numpy as np

file = '8.5 score.csv'
data = np.genfromtxt(file, dtype=float, delimiter=',', skip_header=1, 
                      usecols=range(2,8), filling_values=0, encoding='utf-8')  # 仅保留成绩，转为浮点数，缺失值填充默认值0.0
print(data)
```

+ **names：**值为None、True、字符串或序列之一，当值为“True”时，跳过文件开头的 skip_header 设定的行数后读取的第1行作为字段名。这行也可选被注释符号注释的行。如果 names 参数的值为序列或是被逗号分隔的字符串序列，那么这些字符串将被用于定义结构化类型的字段名。如果 names 参数的值为None，将使用原字段的数据类型作为字段名。
+ **defaultfmt：**值为字符串，定义初始化field names的格式。当 names = None 的时候，可通过此参数来设置字段名。
+ **deletechars：**给出一个字符串，将所有要从字段名称中删除的字符组合在一起。默认情况下，无效字符是\~!@#$\%^&\*()-=+~\\|\]\}[{';: /?.>,<
+ **excludelist：**给出要排除的字段名称列表，如 return，file，print……。如果其中一个输入名称是该列表的一部分，则会附加一个下划线字符（‘_’）。
+ **case_sensitive：**字段名是否区分大小写（case_sensitive = True），转换为大写（case_sensitive = False 或 case_sensitive = ‘upper’）或小写（case_sensitive = ‘lower’）。
+ **replace_space：**为字段名中的空格设置替换的字符，默认为下划线。


```python
import numpy as np

file = '8.5 score.csv'
# 仅保留成绩，转为浮点数，缺失值填充默认值0.0，第一行做字段名
data = np.genfromtxt(file, dtype=float, delimiter=',', names=True,  
                      usecols=range(2,8), filling_values=0, encoding='utf-8')  
print(data)
print(data.dtype)          # 输出每列的字段名称和类型，deletechars使用默认值，C++中的加号将被去除
print(data['Python'])      # 可通过字段名索引并输出对应列数据
```

+ **usemask：**设置是否使用mask，默认值为False。为True时，使用‘–-’代替传统的nan，输出数组将成为 MaskedArray。我们可通过相关操作获取一个布尔数组，该数组中为True的位置表示缺少数据，否则为False。使用此数组，我们可跟踪丢失数据的位置。


```python
import numpy as np

file = '8.5 score.csv'
# 跳过第一行，仅读取成绩列，使用mask
data = np.genfromtxt(file, dtype=float, delimiter=',', skip_header=1, usecols=range(2,8), usemask=True, encoding='utf-8')  
print(data) # --替换nan
print(data.view(np.ma.MaskedArray).mask)  # 得到布尔数组
```

+ **autostrip**：是否保留数据中前导或尾随的空白字符。默认值为False，保留前导或尾随的空白字符；设置为True时，自动去除前导或尾随的空白字符。
+ **loose：**是否针对invalid values报错，默认值为True，则不要针对无效值引发错误。
+ **invalid_raise：**默认值为True。如果为 True，则在某行检测到列数不一致时，将引发异常；如果为 False，则发出警告并跳过有问题的行。

## 写文本文件

NumPy中用于将数组写入文本文件的方法主要是savetxt()。

### 1. savetxt()方法

将数组数据按指定的格式写入文本文件，一般存储为txt或者csv格式。函数原型为：
```python
numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
```

+ **fname：**文件名或文件句柄。如果文件名结束.gz，文件将自动以压缩gzip格式保存。
+ **X：**一维或者二维数组，要保存到文本文件的数据。
+ **fmt：**字符串或字符串序列，用于设置数据写入文件时的格式。可以为单个格式化输出字符串、一个格式化输出字符串序列或一个多格式字符串。
+ **delimiter：**值为字符串，设置分隔列的字符串或字符，默认值为空格。
+ **newline：**值为字符串，设置字符串或字符分隔线，默认值为'\n'。
+ **header：**值为字符串，设置将在文件开头写入的字符串。
+ **footer：**值为字符串，设置将写入文件末尾的字符串。
+ **comments：**值为字符串，设置附加到header和footer的字符串，标记其为注释。默认值为'#'。
+ **encoding：**值为字符串，用于指定编码输出文件的编码。

### 实例：利用 NumPy 读写数据文件

文件[8.5 scoreLoad.csv](./数据集/8.5%20scoreLoad.csv)保存学生成绩数据，中文编码类型为utf-8，分隔符为英文逗号“,”，文件的内容如下，按要求完成以下操作：
1. 将文件读入数组，数据以字符串形式输出
2. 读取除学号和总分以外的数据到数组中
3. 返回只包含成绩数据的数组，数据转为浮点型
4. 将第3步读取的数组中的数据以浮点类型（保留两位小数）写入文本文件“scoresave.txt”中，用Tab作分隔符，编码为'utf-8。
5. 写入文件时，在文件头部增加字符串'成绩表'，在文件尾部增加字符串'武汉理工大学'，并设置注释字符为'@@'。


![](./数据集/image%20(7).png)


```python
!tar -xvf /data/bigfiles/0c378009-4c19-451f-b565-b41f5521d330.tar
```


```python
import numpy as np
 
file = '8.5 scoreLoad.csv'
# 文件无缺失数据，使用loadtxt()读文件到数组
data = np.loadtxt(file, float, delimiter=',',    # 读取类型为浮点数，以英文逗号为分隔符          
                  usecols=(2, 3, 4, 5, 6, 7),    # 仅读取成绩列 
                  skiprows=1, encoding='utf-8')  # 跳过第一行，编码为utf-8    
print(data)
# 将成绩数组写入文件'8.5 scoresave.txt'
np.savetxt('8.5 scoresave.txt', data,     # 数据data写入文件'8.5 scoresave.txt'
           fmt="%.2f", delimiter='\t',    # 设置写入格式为浮点数保留2位小数，分隔符为'\t'
           header='成绩表',               # 文件头部写入'成绩表'
           footer='武汉理工大学',         # 文件尾部写入'武汉理工大学'
           comments='@@',                 # 注释字符设置为'@@'
           encoding='utf-8')              # 编码为utf-8

# 读取文件内容，观察写入的数据
print("文件'8.5 scoresave.txt'中的内容：")
with open('8.5 scoresave.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```
