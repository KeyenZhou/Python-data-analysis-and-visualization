# pandas应用实例

下面以经典数据集“泰坦尼克乘客信息”为例，演示利用pandas进行数据分析的一般过程。

文件‘Titanic.csv’中包含泰坦尼克号上891名乘客的相关信息，每行12列属性，数据字典如下表所示。

| 列名|含义| 列名|含义|
|:-----:|:-----:|:-----:|:-----:|
|PassengerId|乘客Id|	Survived|是否幸存，0：遇难1：幸存|	
|	Name|乘客姓名|Pclass|乘客等级，值1、2、3分别对应一、二、三等仓|	
|Age|乘客年龄|Sex|乘客性别，male：男；female：女|	
|SibSp|堂兄弟妹个数|	Parch|父母与小孩的个数|	
|Ticket|船票信息|	Fare|票价|	
|Cabin|船舱信息|	Embarked|登船港口，C：Cherbourg；Q：Queenstown；S：Southampton|



## 1. 读取数据并查看基本信息

数据下载：  
[Titanic.csv](./数据集/Titanic.csv)

```python
import pandas as pd

passenger_df = pd.read_csv('/data/bigfiles/Titanic.csv', index_col='PassengerId') # 读取文件数据，并将PassengerId列设置为行索引
passenger_df.head() # 输出前5行数据
```


```python
passenger_df.info() # 获取passenger_df的简要摘要
```

从摘要信息从可以看出，Age、Cabin和Embarked列存在缺失值，需要处理。


```python
passenger_df.describe(include='all') # 获取passenger_df的描述性统计数据
```

从基本统计数据可以看出以下几点基本信息：
* 有超过50%的人遇难
* 有超过50%的位于三等舱
* 年龄最小的不到1岁，最大的80岁，大多数乘客在40岁以下
* 有超过50%的乘客是独自一人乘坐
* 有超过75%的乘客票价低于31，票价数据较离散，且存在票价为0的情况
* Name没有重复值，意味着没有重复数据
* 乘客中男性较多，有577人
* 乘客中Southampton登船的人数最多，共644人。

## 2. 数据预处理

#### 2.1 删除数据缺失较多或对数据分析意义不大的列
Cabin列缺失值多，且为文本型数据，很难进行缺失值填充；Ticket信息需结合船舱结构分析，此处也不考虑。


```python
passenger_df.drop(columns=['Cabin', 'Ticket'], inplace=True)  # 删除指定列，原地操作
```

#### 2.2 处理缺失值 
一般对缺失数据的填充有删除、固定值填充、均值/众数/中位数填充等方法。

Embarked列只有两个数据缺失，取该列出现最多的值‘S’填充。

Age列缺失数据较多，采用对应乘客等级的平均年龄填充。


```python
passenger_df['Embarked'].fillna('S', inplace=True)  # 'S'填充缺失值
passenger_df['Age'] = passenger_df.groupby('Pclass')['Age'].apply(lambda x: x.fillna(x.mean())) # 用对应乘客等级的平均年龄填充缺失值
```

#### 2.3 数据含义转换

SibSp和Parch两列为同行的堂兄弟妹个数和父母/小孩的个数，若两列均为0，则该乘客为独自乘坐。根据这两列数据统计并新增一列用于表示该状态，列名为Alone，独自乘坐时值为1，否则值为0。


```python
# SibSp和Parch两列相加，结果转为bool型并取反，取反结果再转为整型，并通过赋值在passenger_df增加Alone列
passenger_df['Alone'] = (~(passenger_df['SibSp']+passenger_df['Parch']).astype(bool)).astype(int)
```

#### 2.4 异常数据处理

前面观察到Fare票价数据较离散，且存在票价为0的情况，可通过绘制箱线图观察异常值的情况。


```python
passenger_df['Fare'].plot.box()
```

从绘制箱线图的结果发现，该列确实是很多数据存在异常。但是考虑到该数据反映的是票价，极端值的存在时有可能的（0可能是员工票或优惠票，极大值可能是VIP船舱的票价）。所以数理层面上的异常并不能确定是错误数据，此处不做处理。

## 3. 数据分析与绘图

先通过corr()方法观察一下属性间相关性。


```python
passenger_df.corr()
```

从结果相关系数可以发现属性间的相关性普遍较低。

#### 1. 统计不同性别人数、遇难人数和幸存人数


```python
sex_count_df = passenger_df.groupby('Sex')['Sex'].count() # 统计男女人数
sex_survived_df = passenger_df.groupby(['Sex', 'Survived'])['Survived'].count().unstack()  # 统计男女遇难人数和幸存人数
print(sex_count_df)
sex_survived_df
```


```python
# 数据合并
sex_result_df = pd.concat([sex_survived_df, sex_count_df], axis=1).rename(mapper={0:'dead', 1:'alive', 'Sex':'total'}, axis=1) 
sex_result_df.plot.bar()
```

从图中可看出女性的存活率远大于男性。

#### 2. 统计不同等级人数、遇难人数和幸存人数


```python
pclass_count_df = passenger_df.groupby('Pclass')['Pclass'].count() # 统计各等级人数
pclass_survived_df = passenger_df.groupby(['Pclass', 'Survived'])['Survived'].count().unstack()  # 统计各等级遇难人数和幸存人数
pclass_result_df = pd.concat([pclass_survived_df, pclass_count_df], axis=1).rename(mapper={0:'dead', 1:'alive', 'Pclass':'total'}, axis=1) 
print(pclass_result_df['alive']/pclass_result_df['total'])  # 计数并输出各等级存活率
pclass_result_df.plot.bar()
```

从结果数据和图中可看出一等舱存活率最高，三等舱存活率最低。

#### 3. 统计各等级独自乘坐和非独自乘坐人数


```python
alone_count_df = passenger_df.groupby(['Pclass', 'Alone'])['Alone'].count() # 统计各等级人数
print(alone_count_df)
alone_count_df.plot.pie()
```

可以看出，三等舱独行人数最多，多为计划在大西洋对岸营造新生活的移民。

#### 4. 按年龄段统计遇难人数和幸存人数


```python
passenger_df['Age'].plot.hist() # 绘制年龄直方图
```

年龄是一个隐型的类别型属性，属性类别值多。因此在分析时，通常对其进行等级划分。这里根据直方图划分了五个阶段，10岁以下代表儿童，10\~20岁代表少年，20\~40代表青年人，40\~60代表中年人，60岁以上代表老年人。


```python
passenger_df['Age_Interval'] = pd.cut(passenger_df['Age'], [0, 10, 20, 40, 60, 100])  # 增加年龄段列
age_survived_df = passenger_df.groupby(['Age_Interval', 'Survived'])['Survived'].count().unstack()  # 统计各年龄段遇难人数和幸存人数
print(age_survived_df)
age_survived_df.plot.barh()
```


```python
age_survived_rate =  age_survived_df[1]/(age_survived_df[0]+age_survived_df[1])  #  计算各年龄段存活率
print(age_survived_rate)
age_survived_rate.plot.line()
```

可见儿童存活率最高，老人存活率最低，其他年龄段差别不大。

#### 5. 分析票价与是否幸存之间的关系

因票价不能确定如何分段，所以分别统计票价最高的100人和票价最低的100人的存活率。


```python
sorted_df = passenger_df.sort_values(by='Fare', ascending=False)
high_fare_survived = sorted_df.head(100)['Survived'].sum()
low_fare_survived = sorted_df.tail(100)['Survived'].sum()
print(f'票价最高的100人中{high_fare_survived}人幸存，存活率{high_fare_survived/100}')
print(f'票价最低的100人中{low_fare_survived}人幸存，存活率{low_fare_survived/100}')
```

由结果可见，高票价的存活率要高得多。

#### 6. 统计不同港口登船人数、遇难人数和幸存人数


```python
embarked_count_df = passenger_df.groupby('Embarked')['Embarked'].count() # 统计各港口人数
embarked_survived_df = passenger_df.groupby(['Embarked', 'Survived'])['Survived'].count().unstack()  # 统计各港口遇难人数和幸存人数
embarked_result_df = pd.concat([embarked_survived_df, embarked_count_df], axis=1).rename(mapper={0:'dead', 1:'alive', 'Embarked':'total'}, axis=1) 
print(embarked_result_df['alive']/embarked_result_df['total'])  # 计数并输出各港口存活率
print(passenger_df.groupby('Embarked')['Fare'].mean())  # 计算并输出各港口平均票价
embarked_result_df.plot.bar()
```

可见Queenstown和Southampton的存活率明显要低一下，相应的其平均票价也较低。
