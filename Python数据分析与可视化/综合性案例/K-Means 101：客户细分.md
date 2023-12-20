# K-Means 101：客户细分

https://www.kaggle.com/code/beachratchata/k-means-101-customer-segmentation


```python
!pip install yellowbrick
```


```python
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

from sklearn.cluster import KMeans
from sklearn.metrics import *
from sklearn.preprocessing import StandardScaler

from yellowbrick.cluster import KElbowVisualizer

```


```python
# 导入数据集

df = pd.read_csv('/data/bigfiles/Mall_Customers.csv')

# 预览数据集
print(df.head())
```


```python
# 查看数据集信息

print(df.info())
```


```python
# 查看是否有缺失值

print(df.isna().sum())
```


```python
# 描述性统计详细信息

print(df.describe().T)
```


```python
# 是否有重复行？

print(df.duplicated().sum())
```


```python
style = plt.style.available[27]
print(style)
plt.style.use(style)
plt.rcParams["figure.figsize"] = (10,7)
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# Show Distribution of Each Feature
# 显示每个特征的分布

fig , axs = plt.subplots(nrows=1 , ncols=3 , figsize=(15,5) , sharey=True)
axs = axs.ravel()

for index , col in enumerate(['Age', 'Annual Income (k$)','Spending Score (1-100)']) : 
    sns.histplot(data=df , x=col ,bins=20 , kde=True, ax=axs[index])
plt.tight_layout()
```


```python
def dist_by_gender(col):
    fig , axs = plt.subplots(nrows=1 , ncols=2 , figsize=(12,5) , sharex=True )
    axs = axs.ravel()

    sns.histplot(data=df , x=col , kde=True ,bins=20, hue='Gender', ax=axs[0])
    sns.boxenplot(data=df , x=col, y='Gender' ,orient='h', ax=axs[1])
    plt.tight_layout() 
    
# Show Distribution of Age by Gender
# 按性别显示年龄分布

dist_by_gender('Age')
```


```python
# Show Distribution of Annual Income by Gender
# 按性别显示年收入分布

dist_by_gender('Annual Income (k$)')
```


```python
# Show Distribution of Spending Score by Gender
# 按性别显示支出得分分布

dist_by_gender('Spending Score (1-100)')
```


```python
# Show Number of Customer by Gender
# 按性别显示客户数量

sns.countplot(data=df , x='Gender')
```


```python
# Show Age vs. Annual Income by Gender
# 按性别显示年龄与年收入

sns.lmplot(data=df , x='Age' , y='Annual Income (k$)' , hue='Gender' , height=8)
```


```python
# Show Age vs. Spending Score by Gender
# 按性别显示年龄与支出得分

sns.lmplot(data=df , x='Age' , y='Spending Score (1-100)' , hue='Gender' , height=8)
```


```python
# Show Annual Income vs. Spending Score by Gender
# 按性别显示年度收入与支出得分

sns.lmplot(data=df , x='Annual Income (k$)' , y='Spending Score (1-100)' , hue='Gender' , height=8)
```


```python
df_corr = df.drop(['CustomerID', 'Gender'] , axis=1).corr()

# Show Correlation of Each Feature
# 显示每个特征的相关性

sns.heatmap(df_corr , mask=np.triu(df_corr) , annot=True , fmt='.2f' ,cmap='Reds_r'  , linewidths=2 )
```


```python
print(df.columns)
```


```python
# Data Preparation

features = df[['Age', 'Annual Income (k$)','Spending Score (1-100)']]
scaler = StandardScaler()
# Data Standardization

features_scaled = scaler.fit_transform(features)

# Create KElbowVisualizer Fucntion

def plot_elbow(model , data , metric='distortion') : 
    
    k_elbow = KElbowVisualizer(model, k=(2,10) , metric=metric)
    k_elbow.fit(data).show()


# Find Elbow

plot_elbow(KMeans() , features_scaled)
plot_elbow(KMeans() , features_scaled, metric='silhouette')
```

From Customer data with two visualize, We got Elbow at k=4
从两个可视化的客户数据中，我们得到了k=4时的弯头


```python
# Create Model

kmeans = KMeans(n_clusters=4)

final_df = df.copy()
final_df['Cluster'] = kmeans.fit_predict(features_scaled)

def count_dist_plot(cluster) :
    
    fig , axs = plt.subplots(nrows=1 , ncols=4 , figsize=(15,5))
    axs = axs.ravel()

    sns.countplot(data=final_df , x=cluster , ax=axs[0], palette='plasma')

    for index , col in enumerate(['Age', 'Annual Income (k$)','Spending Score (1-100)']) :
        sns.boxenplot(data=final_df , x=cluster ,y=col  , ax=axs[index+1] , palette='plasma')

    plt.tight_layout()
# Show Number of Cluster and Distribution 

count_dist_plot('Cluster')
```


```python
# Show 3D Scatter

col_lis = ['Age', 'Annual Income (k$)','Spending Score (1-100)']

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(121,projection='3d')
ax1.scatter(final_df[col_lis[0]] , final_df[col_lis[1]] , final_df[col_lis[2]] , c='grey' , s=200)
ax1.set_xlabel(col_lis[0])
ax1.set_ylabel(col_lis[1])
ax1.set_zlabel(col_lis[2])
ax1.set_title('Customer Data')

ax2 = fig.add_subplot(122,projection='3d')
ax2.scatter(final_df[col_lis[0]] , final_df[col_lis[1]] , final_df[col_lis[2]] ,c=final_df['Cluster'],cmap='plasma', s=200)
ax2.set_xlabel(col_lis[0])
ax2.set_ylabel(col_lis[1])
ax2.set_zlabel(col_lis[2])
ax2.set_title('Customer Data with 4 Segment');
```

## 结论


```python
median_data = final_df.groupby('Cluster')[col_lis].median().T

sns.heatmap(median_data , annot=True , cmap='Blues',linewidths=1 )
plt.title('4 Segment Customer Data \nwith Median Value');
```


```python

```
