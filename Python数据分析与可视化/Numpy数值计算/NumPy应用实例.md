# NumPy应用实例——NumPy处理图像

计算机中的图像是由若干呈行列排列的像素组成的，每个像素都有一个明确的位置和被分配的色彩数值。因此，每张图像都可以构成一个像素数组。下图中分别展示了彩色图片和灰度图片中的像素块及其所对应的数组。

![](./数据集/image%20(1).png)

从上左图中可以看出，彩色图片的数据是一个三维数组，每个单元格对应一个像素点。每个像素点的颜色值为一个包含三个整形元素的一维数组，分别对应红、绿、蓝三种颜色（RGB颜色）。

从上右图中可以看出，灰度图片的数据是一个二维数组，每个单元格对应一个像素点。每个像素点的颜色值为一个0~255的整数。其中0为黑色，255为白色，其他值为不同的灰度，值越小越暗。

像素的颜色和位置就决定了图像所呈现出来的样子，因此，如果我们改变图像对应的数组元素的排列顺序或者元素值就可以实现对图像的处理。

下面介绍几种利用NumPy处理图像的方法。

+ ###  图像灰度处理

图像灰度化意味着需要将RGB颜色数组转化为0~255之间的灰度值，将三维数组转化为二维数组。常见的处理方法主要有四种：

1. 标准方法：每个像素点的RGB颜色值按公式计算出对应的灰度值Gray。计算公式为$Gray = R *  0.299  + G * 0.587  + B * 0.114 $。
2. 简化方法：使用每个像素点的RGB颜色中的最大值作为对应的灰度值Gray。即$Gray = max(R,G,B)$。
3. 简化方法：使用每个像素点的RGB颜色中的最小值作为对应的灰度值Gray。即$Gray = min(R,G,B)$。
4. 简化方法：使用每个像素点的RGB颜色的平均值作为对应的灰度值Gray。即$Gray = mean(R,G,B)$。


```python
!tar -xvf /data/bigfiles/9b3764a8-e2c0-4a28-80a6-4efea7e28340.tar
```


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
print(color_array.shape)  # 彩色图像对应三维数组，形状为(226, 226, 3)
plt.imshow(color_array)   # 该方法可将数组转换为图像并绘制出来
plt.show()
```

下面分别使用四种方法将上图转化为灰度图并显示。


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
gray_1 = color_array @ np.array([0.299, 0.587, 0.114])  # 标准方法,对位相乘再相加，利用数组矩阵乘法
gray_2 = np.max(color_array, axis=2)   # 简化方法：使用最大值代替整个最低维 
gray_3 = np.min(color_array, axis=2)   # 简化方法：使用最小值代替整个最低维 
gray_4 = np.mean(color_array, axis=2)  # 简化方法：使用平均值代替整个最低维
print(gray_1.shape, gray_2.shape, gray_3.shape, gray_4.shape)  # 均为二维数组
plt.rcParams['font.sans-serif'] = ['SimSun']   # 用仿宋体显示中文
fig, ax = plt.subplots(2, 2)      # 设置4个子图
ax[0, 0].set_title('标准方法')
ax[0, 0].imshow(gray_1, cmap='gray')  # 每个子图显示一张转换后的灰度图，需设置cmap='gray'
ax[0, 1].set_title('最大值法')
ax[0, 1].imshow(gray_2, cmap='gray')
ax[1, 0].set_title('最小值法')
ax[1, 0].imshow(gray_3, cmap='gray')
ax[1, 1].set_title('平均值法')
ax[1, 1].imshow(gray_4, cmap='gray')
plt.tight_layout()
plt.show()
```

+ ### 图像复制

图像复制可通过数组的复制和拼接来实现。


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
gray_1 = color_array @ np.array([0.299, 0.587, 0.114])  # 标准方法转灰度图,对位相乘再相加，利用数组矩阵乘法
h_repeat = np.hstack((gray_1, gray_1, gray_1))   # 数组水平拼接，将图像沿着水平方向重复三次    
v_repeat = np.vstack((gray_1, gray_1))  # 数组垂直拼接，将图像沿着垂直方向重复两次     
fig, ax = plt.subplots(1, 2)
ax[0].set_title(str(h_repeat.shape))
ax[0].imshow(h_repeat, cmap='gray')
ax[1].set_title(str(v_repeat.shape))
ax[1].imshow(v_repeat, cmap='gray')
plt.show()
```

+ ### 图像镜像

图像复制可通过调整数组的行列位置来实现。将图像水平镜面转换，只需要将列进行颠倒，行位置不变；将图像垂直镜面转换，只需要将行进行颠倒，列不变。


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
gray_1 = color_array @ np.array([0.299, 0.587, 0.114])  # 标准方法转灰度图,对位相乘再相加，利用数组矩阵乘法
h_mirror = gray_1[:, ::-1]       # 水平镜像，切片实现所有行位置不变，每行所有列逆序（左右交换）   
v_mirror = gray_1[::-1, :]       # 垂直镜像，切片实现所有列位置不变，每列所有行逆序（上下交换）
fig, ax = plt.subplots(1, 2)
plt.rcParams['font.sans-serif'] = ['SimSun']   # 用仿宋体显示中文
ax[0].set_title('水平镜像')
ax[0].imshow(h_mirror, cmap='gray')
ax[1].set_title('垂直镜像')
ax[1].imshow(v_mirror, cmap='gray')
plt.tight_layout()
plt.show()
```

+ ### 图像旋转

图像旋转也可通过调整数组的行列位置来实现，主要通过转置和切片来处理。


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
gray_1 = color_array @ np.array([0.299, 0.587, 0.114])  # 标准方法转灰度图,对位相乘再相加，利用数组矩阵乘法
rotate_left_90 = (gray_1.T)[::-1, :]     # 将图像向左旋转90，先转置，此时头还在原位置，所以再垂直颠倒
rotate_right_90 = (gray_1.T)[:, ::-1]    # 将图像向右旋转90，先转置，此时头还在原位置，所以再水平颠倒  
rotate_180 = (gray_1[::-1, :])[:, ::-1]  # 将图像旋转180，将图像分别进行水平和垂直颠倒，顺序不限 
fig, ax = plt.subplots(1, 3)
plt.rcParams['font.sans-serif'] = ['SimSun']   # 用仿宋体显示中文
ax[0].set_title('左旋90')
ax[0].imshow(rotate_left_90, cmap='gray')
ax[1].set_title('右旋90')
ax[1].imshow(rotate_right_90, cmap='gray')
ax[2].set_title('旋转180')
ax[2].imshow(rotate_180, cmap='gray')
plt.tight_layout()
plt.show()
```

+ ### 图像添加马赛克

图像添加马赛克可通过生成一个指定大小的随机数组，再用随机数组的值替换原始数组中与需要打马赛克的部分相对应的区域即可。如有需要，替换前可先为被替换部分创建一个副本，用于后面还原图像。


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
gray_1 = color_array @ np.array([0.299, 0.587, 0.114])  # 标准方法转灰度图,对位相乘再相加，利用数组矩阵乘法
mosaic = np.random.randint(0, 256, (80, 80), dtype=np.uint8)  # 创建一个80 x 80，值在[0.255]区间内的整型数组，作为马赛克数组
gray_1[10:90, 50:130] = mosaic  # 通过切片赋值的形式，用马赛克数组替换该区域原始值。
plt.imshow(gray_1, cmap='gray')
plt.show()
```

+ ### 图像混淆

图像混淆可先对数组进行切分成多个数组，然后随机打乱切分结果，最后再将打乱的多个数组拼接成一个数组即可。


```python
import numpy as np
import matplotlib.pyplot as plt  # 绘图库，用于展示处理结果

color_array = plt.imread('test.jpg') # 该方法可将图像文件读取为数组
gray_1 = color_array @ np.array([0.299, 0.587, 0.114])  # 标准方法转灰度图,对位相乘再相加，利用数组矩阵乘法
height,width = gray_1.shape  # 获取数组行数
split_result = np.vsplit(gray_1, range(5, height, 5)) # 将原始数组每5行一组，纵向切分成多个数组组成的序列
np.random.shuffle(split_result)  # 对结果序列进行随机打乱
shuffle_result = np.vstack(split_result)  # 将打乱的多个数组组成的序列，纵向拼接起来
# 可以横向再做一遍，效果更好
split_result = np.vsplit(shuffle_result, range(5, width, 5)) # 将原始数组每5列一组，横向切分成多个数组组成的序列
np.random.shuffle(split_result)  # 对结果序列进行随机打乱
shuffle_result = np.vstack(split_result)  # 将打乱的多个数组组成的序列，横向拼接起来
plt.imshow(shuffle_result, cmap='gray')
plt.show()
```
