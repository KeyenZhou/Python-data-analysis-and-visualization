# 1. 关于seaborn库

![](./数据集/image%20(18).png)

seaborn是一个基于matplotlib的Python可视化库，主要用于统计数据的可视化。seaborn库是构建在matplotlib库之上的，因此函数接口和参数设置都和matplotlib库类似。

seaborn是一个很强大的数据可视化库，能帮助你更好地探索和使用数据，对于pandans数据帧和数组，它会在内部直接进行必要的语义映射和统计聚合，其面向数据集的声明式API让用户只需要关注绘图时不同元素的意义，而忽略如何绘制的细节。

可以通过 https://seaborn.pydata.org/ 获得seaborn的在线文档。

# 2. 依赖关系

seaborn需要python 3.7+版本，不再支持python 2。要安装seaborn需要先安装numpy、pandas和matplotlib，其部分高级统计函数需要scipy和statsmodels库的支持。

# 3. 第一个seaborn图形

在演示seaborn库绘制图形之前，我们先来了解一下需要用到的示例数据。

下面使用pandas库的read_csv()函数读入"tips.csv"文件，并输出前10行数据。

[tips.csv](数据集/tips.csv)

```python
import pandas as pd  #导入pandas，给别名为pd

tips = pd.read_csv("/data/bigfiles/tips.csv") # 读入"tips.csv"文件
print(tips.head(10)) #观察一下示例数据
```

可以看到tips.csv文件保存了tips数据集，该数据集包括账单金额、小费金额、性别、是否抽烟、星期几、就餐时间、就餐人数这七个属性。

下面的代码通过图形展示了tips数据集里账单金额、小费金额、就餐时间、是否抽烟、就餐人数这五个变量之间的关系，但是仅仅只调用了seaborn的relplot()函数。和matplotlib相比，seaborn库简单易用。


```python
# 导入第三方库
import seaborn as sns   #导入seaborn库并指定别名为sns
import matplotlib.pyplot as plt
import pandas as pd

tips = pd.read_csv("/data/bigfiles/tips.csv") #使用示例数据

sns.set_theme()    #使用seaborn的默认主题

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

plt.show()    #显示所绘制的图形
```

## 需要注意的是，在使用seaborn库时，我们仅需要提供变量的名称及其在绘图中的角色。

和直接使用matplotlib不同，seaborn不需要指定color或者marker这些图形元素所对应的属性。在幕后，seaborn自动处理了从数据帧里的值到matplotlib参数的转换。这种仅需声明绘图角色的方法使你只用专注于待解决的问题，而不用关注如何控制matplotlib的细节。

# 4. Seaborn中的绘图函数

Seaborn绘图函数根据图形层级分为两种类型：

* axes级：绘图函数在单个axes上绘图，函数返回值就是axes对象。
* figure级：绘图函数在figure上绘图，返回一个FacetGrid对象，类似Figure对象，可以管理figure。

figure函数直接在figure中绘制图形。axes绘图函数则是在axes中绘图，可以在函数中用ax参数指定要绘图的axes，多个axes级函数可以在同一个axes中叠加绘图，但是figure级函数不行，axes级函数灵活度更高。

figure级函数api统一，功能强大，因此，官方文档建议大多数情况下优先使用figure级函数。但是，当需要绘制复杂的、由多种不同类型图形组合的figure时，建议用matplotlib设置figure，用axes级函数绘图。

Seaborn中共有22种不同的绘图函数，可以分成5各大类。

![](./数据集/image%20(19).png)


```python

```
