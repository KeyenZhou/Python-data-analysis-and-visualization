# pandas概述

## 1. pandas简介

![](./数据集/image%20(58).png)

 pandas是一个建立在Python编程语言之上，快速、强大、灵活且易于使用的开源数据分析和操作工具，pandas名字衍生自术语“panel data”（面板数据）和“Python data analysis”（Python 数据分析）。

pandas的优势在于：
* 用于分析和操作大型结构化数据集的强大工具集
* 基础是NumPy，提供了高性能矩阵的运算
* 提供大量函数和方法，可以快速轻松地处理数据
* 应用于数据挖掘、数据分析
* 提供数据清洗功能

本课程仅介绍常用部分，其余请查阅[pandas官方文档](https://pandas.pydata.org/docs/index.html)。

通常推荐用以下的方式导入pandas，库名被缩写为pd是一个被广泛采用的约定。
```python
import pandas as pd
```

##  2. pandas提供的数据结构

pandas库主要提供Series和DataFrame两类数据结构对象。

* **Series**：Series是一维标记数组，可以存储任意数据类型，与Numpy中的数组（Array）相似数组中只允许存储相同的数据类型。Series增加了一个标签用于索引，使Pandas除了通过位置索引外，还可以通过标签索引进行元素存取。
* **DataFrame**：DataFrame是二维标记数据结构，相当于表格。主体分数据和索引两部分。数据以行（Row）和列（Column）的表格方式排列，潜在的列可以是不同的数据类型。索引分行索引（Row Index）和列索引（Column Index）。

Pandas 所有数据结构的值都是可变的，但数据结构的大小并非都是可变的，比如，Series 的长度不可改变，但 DataFrame 里就可以插入列。Pandas 里，绝大多数方法都不改变原始的输入数据，而是复制数据，生成新的对象。 一般来说，原始输入数据不变更稳妥。

![](./数据集/image%20(59).png)
