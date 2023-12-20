# pandas数据可视化

pandas的DataFrame、Series对象自带plot，可根据DataFrame、Series对象的值绘图。绘制时，图像会按照数据的每一列绘制一条曲线，默认按照列columns的名称在适当的位置展示图例，比matplotlib绘制节省时间。

下面以文件“scoregroup.csv”为例讲解常用图形的绘制。

数据下载：  
[scoregroup.csv](./数据集/scoregroup.csv)
[score_3.csv](./数据集/score_3.csv)

```python
import pandas as pd

score_df = pd.read_csv('/data/bigfiles/scoregroup.csv',dtype={'学号':str}, encoding='utf-8')
columns_dict={'姓名':'name', '学号':'stu_no', '课程名':'course_name', '分数':'score'}
score_df.rename(columns=columns_dict, inplace=True)           # 根据columns参数的字典重命名列索引
score_df = score_df.pivot(index='stu_no', columns='course_name', values='score')
columns_dict={'高数':'Math', '英语':'English', '物理':'Physics', '程序设计':'Programming', '经济':'Economy'}
score_df.rename(columns=columns_dict, inplace=True)           # 根据columns参数的字典重命名列索引
score_df.index=score_df.index.str[-4:]   # 保留学号后4位为行索引
score_df
```

## 1. 绘制线型图
```python
plot.line(x=None, y=None, **kwargs)
```


```python
score_df['Programming'].plot.line()  # 绘制程序设计课成绩线型图
```


```python
score_df[['Math', 'English']].plot.line()  # 两列数据绘制两条线，高数与英语课成绩线型图
```

## 2. 绘制散点图
```python
plot.scatter(x, y, s=None, c=None, **kwargs)
```


```python
score_df.plot.scatter(x='Programming', y='Math')  # 程序设计成绩做横坐标，数学成绩做纵坐标
```

## 3. 绘制条形图或水平条形图
```python
plot.bar(x=None, y=None, **kwargs)
plot.barh(x=None, y=None, **kwargs)
```


```python
score_df[['Math', 'English']].plot.bar()  # 垂直条形图
```


```python
score_df['Programming'].plot.barh()  # 水平条形图
```

## 4. 绘制箱线图
```python
plot.box(by=None, **kwargs)
```


```python
score_df['Programming'].plot.box()  # 五条横线从上到下分别表示最大值、第三四分位数、中位数、第一四分位数、最小值
```

## 5. 绘制直方图
```python
plot.hist(by=None, bins=10, **kwargs)
```


```python
score_df['Programming'].plot.hist() # 绘制程序设计课直方图，统计不同分数段成绩的人数
```

## 6. 绘制密度图
密度图用于显示数据在连续时间段内的分布状况。这种图表是直方图的变种，使用平滑曲线来绘制数值水平，从而得出更平滑的分布。密度图的峰值显示数值在该时间段内最为高度集中的位置。


```python
score_df[['Programming','Math']].plot.kde()  # 绘制程序设计、高数成绩分布密度图
```

## 7. 绘制饼图


```python
# pandas.cut用来把一组数据分割成离散的区间
# 把程序设计课成绩分割成(0, 59]、(59, 89]、(89, 100]三个区间，并统计每个学生所在的区间
score_interval = pd.cut(score_df['Programming'], [0, 59, 89, 100]) 
score_interval
```


```python
score_interval_counts = pd.value_counts(score_interval) # 统计每个分数段人数
score_interval_counts
```


```python
score_interval_counts.plot.pie()  # 绘制程序设计课成绩分布饼图
```
