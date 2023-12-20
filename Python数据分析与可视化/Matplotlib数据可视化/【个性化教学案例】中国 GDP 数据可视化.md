# 中国 GDP 数据可视化

[Chinas GDP in Province Zh.csv](./数据集/Chinas%20GDP%20in%20Province%20Zh.csv)<br>
[Chinas GDP in Province En.csv](./数据集/Chinas%20GDP%20in%20Province%20En.csv)<br>
[china_regions.csv](./数据集/china_regions.csv)<br>

/data/bigfiles/Chinas GDP in Province Zh.csv  
/data/bigfiles/Chinas GDP in Province En.csv  
/data/bigfiles/china_regions.csv

# 1.用pandas 查看数据结构


```python
import pandas as pd

df = pd.read_csv('/data/bigfiles/Chinas GDP in Province En.csv')
df.head()
```


```python
df.tail()
```

# 2.读文件到二维列表


```python
def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r') as fr:
        data_ls = [x.strip().split(',') for x in fr]
    return data_ls


if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province En.csv'
    data = read_file(filename)
    print(data[:5])    # 输出前10条数据查看
```

# 3.绘制广东省 GDP曲线


```python
import matplotlib.pyplot as plt

# 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimSun']  # 宋体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号 -
plt.figure(figsize=(14, 9))


def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r') as fr:
        data_ls = [x.strip().split(',') for x in fr]  # 去掉广西上面的引号
    return data_ls


def plot_gdp(data_ls: list) -> None:
    """根据二维列表数据绘制历年各省 gdp 曲线，无返回值"""
    year = [int(i[0]) for i in data_ls[1:]]  # 年份列表，做横坐标
    i = data_ls[0].index('广东省')  # 获取 广东省序号
    gdp_of_guangdong = [float(x[i]) for x in data_ls[1:]]  # 广东省 gdp 数据列表
    plt.plot(year, gdp_of_guangdong, label='广东省 GDP')
    plt.legend(loc='upper left')


if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province Zh.csv'
    data = read_file(filename)
    plot_gdp(data)
    plt.title('Chinas GDP in Province')
    plt.show()

```

# 4.绘制各省历年 GDP 曲线


```python
import matplotlib.pyplot as plt
# 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimSun']    # 宋体
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号 -
plt.figure(figsize=(14, 9))


def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r') as fr:
        data_ls = [x.replace('"', '').replace(',,', ',').strip().split(',') for x in fr]  # 去掉广西上面的引号
    return data_ls


def plot_gdp(data_ls:list)->None:
    """根据二维列表数据绘制历年各省 gdp 曲线，无返回值"""
    provice = data_ls[0] # 省名列表
    year = [int(i[0]) for i in data_ls[1:]]  # 年份列表，做横坐标
    for i in range(1, len(provice)):  # 遍历省名列表长度, i为当前省序号
        gdp_of_pro = [float(x[i]) for x in data_ls[1:]]  # 当前省 gdp 数据列表
        plt.plot(year, gdp_of_pro,label=provice[i])
    plt.legend(loc='upper left')



if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province En.csv'
    data = read_file(filename)
    plot_gdp(data)
    plt.title('Chinas GDP in Province')
    plt.show()
```

![Chinas GDP in Province](./数据集/Chinas%20GDP%20in%20Province.png)

# 5.绘制各省2020年柱形图


```python
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 9))


def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r') as fr:
        data_ls = [x.replace('"', '').replace(',,', ',').strip().split(',') for x in fr]  # 去掉广西上面的引号
    return data_ls


def plot_bar(data_ls:list)->None:
    """根据二维列表数据绘制历年各省 gdp 曲线，无返回值"""
    provice = data_ls[0][1:] # 省名列表
    gdp_of_pro = list(map(float,data_ls[1][1:])) # 当前全部省份2020年 GDP 柱形图
    plt.bar(provice, gdp_of_pro,label='2020')
    plt.legend(loc='upper left')
    plt.xticks(provice,rotation=-45)

    
if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province En.csv'
    data = read_file(filename)
    plot_bar(data)
    plt.title('Chinas GDP in Province')
    plt.legend(loc='upper left')
    plt.show()


```

# 6.设置彩虹色柱形图


```python
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.figure(figsize=(14, 9))


def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r') as fr:
        data_ls = [x.replace('"', '').replace(',,', ',').strip().split(',') for x in fr]  # 去掉广西上面的引号
    return data_ls


def plot_bar(data_ls:list)->None:
    """根据二维列表数据绘制历年各省 gdp 曲线，无返回值"""
    provice = data_ls[0][1:] # 省名列表
    gdp_of_pro = list(map(float,data_ls[1][1:])) # 当前全部省份2020年 GDP 柱形图
    colors = cm.rainbow(np.arange(len(provice)) / len(provice))  # 为每个省分配一个颜色
    plt.bar(provice, gdp_of_pro,color =colors, label='2020')
    plt.legend(loc='upper left')
    plt.xticks(provice,rotation=-45)

    
if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province En.csv'
    data = read_file(filename)
    plot_bar(data)
    plt.title('Chinas GDP in Province')
    plt.legend(loc='upper left')
    plt.show()


```

# 7.标注柱高数据


```python
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.figure(figsize=(14, 9))


def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r') as fr:
        data_ls = [x.replace('"', '').replace(',,', ',').strip().split(',') for x in fr]  # 去掉广西上面的引号
    return data_ls


def plot_bar(data_ls:list)->None:
    """根据二维列表数据绘制历年各省 gdp 曲线，无返回值"""
    provice = data_ls[0][1:] # 省名列表
    gdp_of_pro = list(map(float,data_ls[1][1:])) # 当前全部省份2020年 GDP 柱形图
    provice_gdp = dict(zip(provice, gdp_of_pro))
    colors = cm.rainbow(np.arange(len(provice)) / len(provice))  # 为每个省分配一个颜色
    plt.bar(provice, gdp_of_pro,color =colors, label='2020')
    for x, y in provice_gdp.items():
        plt.text(x, y + 1000, "%s" % y)  # y+1000使数字高于柱顶
    plt.legend(loc='upper left')
    plt.xticks(provice,rotation=-45)

    
if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province En.csv'
    data = read_file(filename)
    plot_bar(data)
    plt.title('Chinas GDP in Province')
    plt.legend(loc='upper left')
    plt.show()





```

# 8.分区域绘制柱形图


```python
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimSun']  # 宋体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号 -
plt.figure(figsize=(14, 9))


def read_file(file: str) -> list:
    """读 csv 文件中的数据到二维列表，返回二维列表"""
    with open(file, 'r', encoding='utf-8') as fr:
        data_ls = [x.replace('"', '').replace(',,', ',').strip().split(',') for x in fr]  # 去掉广西上面的引号
    return data_ls


def region_gdp_bar(data_ls: list) -> None:
    """根据二维列表数据绘制历年各省 gdp 曲线，无返回值"""
    with open('/data/bigfiles/china_regions.csv', 'r', encoding='utf-8') as fr:
        region_data = [x.strip().split(',') for x in fr]  # 去掉广西上面的引号
    region = [x[0] for x in region_data]  # 大区名列表
    provice = data_ls[0][1:]  # 省名列表
    gdp_of_pro = list(map(float, data_ls[1][1:]))  # 当前全部省份2020年 GDP 要柱形提开
    provice_gdp = dict(zip(provice, gdp_of_pro))
    gdp_of_region = []
    for i in range(len(region)):
        gdp_of_region.append(round(sum([v for k, v in provice_gdp.items() if k in region_data[i]])))
    
    colors = cm.rainbow(np.arange(len(region)) / len(region))  # 为每个区分配一个颜色
    plt.bar(region, gdp_of_region, color =colors, label='2020')
    region_gdp_dic = dict(zip(region, gdp_of_region))
    for x, y in region_gdp_dic.items():
        plt.text(x, y + 5000, "%s" % y)  # y+5000使数字高于柱顶
    plt.legend(loc='upper left')


if __name__ == '__main__':
    filename = '/data/bigfiles/Chinas GDP in Province Zh.csv'
    data = read_file(filename)
    region_gdp_bar(data)
    plt.title('Chinas GDP in Province')
    plt.legend(loc='upper left')
    plt.show()

```


```python

```
