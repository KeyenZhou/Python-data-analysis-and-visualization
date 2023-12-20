# Seaborn风格设置

风格设置可以对绘图的背景色、风格、字体、字型进行设置，Seaborn提供了许多定制的主题和用于控制matplotlib图形外观的高级接口。

## 1. 使用set_theme()修改主题

Seaborn通过set_theme()函数实现风格设置，其函数原型为：
```python
seaborn.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)
```
* context：值为None或{‘paper’, ‘notebook’, ‘talk’, ‘poster’}中的一种, 缺省值为‘notebook’。用于获取控制打印元素缩放的参数，会影响标签、线条等绘图其他元素的大小，但不会影响整体样式。底层通过设置matplotlib rcParams系统实现。
* style：五种可供选择的主题。darkgrid（灰色网格）、whitegrid（白色网格）、dark（黑色）、white（白色）、ticks（十字刻度）。它会影响诸如坐标轴的颜色，网格默认是否开启和其他自定义元素。
* palette：配色方案。可使用6个默认的颜色循环主题：deep、muted、pastel、bright、dark、colorblind。 
* font：字体设置。例如'sans-serif'，'Arial'等。
* font_scale：字号大小设置。单独地对字体缩放大小进行设置。
* color_codes：是否进行颜色代码的映射。如果设置为True，并且设置了seaborn自带的调色盘，将简写的颜色代码(例如“b”、“g”、“r”等)映射到这个调色板中的颜色。
* rc：支持其他rc参数映射的字典，可覆盖上面的设置


```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 定义一绘图函数，绘制曲线y=sin(x+a)
def sinplot(c=1):
    x = np.linspace(0, 20, 50)
    for a in range(c):
        sns.lineplot(x=x, y=np.sin(x + a))

# 风格设置，不同contex参数
plt.figure(figsize=(16, 9))
contexts = ['paper', 'notebook', 'talk', 'poster']
for i in range(4):
    sns.set(context=contexts[i])
    plt.subplot(2, 2, i+1)
    plt.title(f'context={contexts[i]}')
    sinplot()
plt.show()
```

以上为不同context取值对应的效果。


```python
plt.figure(figsize=(16, 9))
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
for i in range(5):
    sns.set(context='poster', style=styles[i])
    plt.subplot(2, 3, i+1)
    plt.title(f'style={styles[i]}')
    sinplot()
plt.subplots_adjust(wspace=0.5, hspace=0.5) # 设置子图间距
plt.show()
```

以上为不同style取值对应的效果。


```python
plt.figure(figsize=(16, 9))
palettes = ['pastel', 'husl', 'Set2', 'flare']
for i in range(4):
    sns.set(context='poster', palette=palettes[i])
    plt.subplot(2, 2, i+1)
    plt.title(f'palette={palettes[i]}')
    sinplot(4)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()
```

以上为不同palette取值对应的效果。

## 2. 轴线设置

Seaborn通过despine()函数实现轴线设置，其函数原型为：
```python
despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
```
* top、right、left、bottom：用来控制四根轴的显示，True为移除，False为保留。
* fig、ax：用来指定需要设置的figure或axes，默认当前figure。
* offset：设置坐标轴偏移量。
* trim： 为True时，若边框没有覆盖整个数据轴的范围，会限制留存的边框范围。


```python
plt.figure(figsize=(16, 9))
sns.set(context='notebook', style='ticks')
sinplot(5)
sns.despine(left=True, right=False, offset=20, trim=True) # 移除左轴，显示右轴，设置偏移量为20，切除多余轴范围
plt.show()
```
