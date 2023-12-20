#  1. scikit-learn简介

![](./数据集/image%20(2).png)

scikit-learn，又写作sklearn，是一个开源的基于python语言的机器学习工具包。它通过NumPy, SciPy和Matplotlib等python数值计算的库实现高效的算法应用，并且涵盖了几乎所有主流机器学习算法。

sklearn库的API设计友好，所有对象的接口简单，集成了常用的机器学习方法。在进行机器学习任务时,并不需要实现算法,只需要简单的调用sklearn库中提供的模块就能完成大多数的机器学习任务，很适合新手上路。

sklearn有一个完整而丰富的官网([scikit-learn: machine learning in Python](https://link.zhihu.com/?target=http%3A//scikit-learn.org/stable/index.html))，里面讲解了基于sklearn对所有算法的实现和简单应用。


sklearn中常用的模块如下表所示。
![](./数据集/image%20(3).png)

|模块|功能|常用算法或模块|应用领域|
|:-----:|:-----|:-----|:-----|
|分类|识别特定对象所属于的类别|SVM（支持向量机）<br>nearest neighbors（最近邻）<br>random forest（随机森林）等|垃圾邮件识别、图像识别等|
|回归|预测与对象相关联的连续值属性|SVR（支持向量机）<br>ridge regression（岭回归）<br>Lasso等|药物反应，预测股价|
|聚类|将相似对象自动分组|k-Means<br>spectral clustering<br>mean-shift等|客户细分，分组实验结果等|
|降维|减少要考虑的随机变量的数量|PCA（主成分分析）<br>feature selection（特征选择）<br>non-negative matrix factorization（非负矩阵分解）等|可视化，提高效率|
|模型选择|比较，验证，选择参数和模型|grid search（网格搜索）<br>cross validation（交叉验证）<br>metrics（度量）等|通过参数调整提高精度|
|预处理|特征提取和归一化|preprocessing<br>feature extraction等|将输入数据转换为机器学习算法可用的数据|

#  2. 安装scikit-learn

sklearn库是在Numpy、Scipy和matplotlib的基础上开发而成的，因此在介绍sklearn的安装前，需要先安装这些依赖库。此外，一些功能（如绘图）和例子也需要其它依赖库的支持。常见的依赖库见下表。

|  依赖   | 最小版本 |      依赖       | 最小版本 |
| :-----: | :------: | :-------------: | :------: |
|  numpy  |  1.17.3  |      scipy      |  1.3.2   |
| matplotlib    |  3.1.2   |pandas  |  1.0.5   |   
| seaborn |  0.9.0   |  scikit-image   |  0.16.2  |
| joblib  |  1.0.0   |  threadpoolctl  |  2.0.0   |
| cython  | 0.29.24  | memory_profiler |  0.57.0  |

如果已安装了numpy和scipy，那么安装scikit-learn的最简单方法就是使用如下命令:
```
pip install -U scikit-learn
```
需要注意的是：
Scikit-learn 0.20 是最后一个同时支持Python 2.7和Python 3.4的版本。Scikit-learn 0.21支持Python 3.5-3.7；Scikit-learn 0.22支持Python 3.5-3.8；Scikit-learn 0.23-0.24需要Python 3.6以上；Scikit-learn 1.0支持3.7-3.10；Scikit-learn 1.1和后续版本需要Python 3.8以上。


```python
import sklearn

sklearn.show_versions() # 输出版本等相关信息
```

# 3. 机器学习简介

“机器学习之父”汤姆·米切尔对机器学习的定义是：

      A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E.
      对于某类任务 Task 和性能度量 Performace ,如果一个计算机程序在任务中，性能能够随着经验 Experience 而自我完善，那么我们就称为程序在经验中学习 。

机器学习的核心思想是创造一种算法，只是把数据传递给这个算法，它就能从数据中挖掘出有规律的东西，会在数据上建立自己的逻辑，而不需要针对某个问题去写代码。机器学习可以看作是寻找一个函数，输入是样本数据，输出是期望的结果。只是这个函数过于复杂，以至于不太方便形式化表达。

![](./数据集/image%20(4).png)


需要注意的是，机器学习的目标是使学到的函数很好地适用于“新样本”，而不仅仅是在训练样本上表现很好。学到的函数适用于新样本的能力，称为泛化（Generalization）能力。

从机器学习算法本身来看，可分为监督学习、非监督学习、半监督学习、强化学习。
* 监督学习：给机器的训练数据拥有标签。主要处理分类和回归问题。
* 非监督学习：给机器的训练数据没有任何标签。通常做聚类分析、异常值检测或降维。
* 半监督学习：给机器的训练数据部分有标签。一般先用无监督学习处理数据，再用监督学习做模型的训练和预测。
* 强化学习：是一个学习最优策略，让本体在特定环境中，根据当前状态做出行动，从而获得最大回报。如AlphaGo内部的算法、无人驾驶，机器人等。



# 4. 算法模型选择

2001年，微软的一个研究团队发表的一篇著名论文提出，对于一个有效的机器学习算法，只要给足够的数据进行训练，它们最后的准确率都是逐步上升接近100%的。因此有人提出数据即算法，大数据时代拉开帷幕，人们开始意识到数据是可以产生价值的，算法也开始对数据本身越来越重视。大数据时代对数据的处理强调：全样而非抽样、效率而非精确、相关而非因果。现有大多数机器学习算法都是数据驱动型的，算法的性能高度依赖数据质量。对复杂问题而言，数据甚至比算法重要。

不过获得大量数据不是一件容易的事，算法本身依然很重要。再好的数据都要有高效优秀的算法作为辅助，才能最大程度发挥数据本身的作用。有些问题即使没有数据，算法也可以生成数据，例如AlphaGoZero。

sklearn实现了很多算法，选择的主要考虑的就是需要解决的问题以及数据量的大小。sklearn官方提供了一个选择算法的引导图。

![](./数据集/image%20(5).png)



```python

```
