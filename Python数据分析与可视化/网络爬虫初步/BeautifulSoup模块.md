# 6. BeautifulSoup模块

通过正则表达式从网页中提取数据主要是利用字符串的方法，通过分析网页源代码，编写正则表达式提取其中有用的数据。BeautifulSoup是一个能够解析网页源代码结构的第三方库，可用于解析和提取HTML/XML文档中的数据。该模块支持HTML解析器和许多功能强大的第三方解析器，下面实例中使用lxml解析器将网页源代码加载为BeautifulSoup对象，再使用对象方法提取数据。使用前先要通过“pip install lxml”安装这个模块。
pip install beautifulsoup4
## 6.1 实例化

实例化BeautifulSoup对象就是使用解析器分析指定的网页源代码，得到该 源代码的结构模型。


```python
import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
# 浏览器传递参数，'limit': '2'表示只返回前2条数据，修改数字可以得到更多数据
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 用获取的网页源代码实例化BeautifulSoup对象

```

## 6.2 定位标签

实例化一个BeautifulSoup对象后，就可以使用该对象来定位网页中的标签元素。

1. 通过标签名进行定位

网页源代码中可能会有多个同名标签，通过标签名定位只能返回其中第一个标签。


```python
import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
# 浏览器传递参数，'limit': '2'表示只返回前2条数据，修改数字可以得到更多数据
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
# 用获取的网页源代码实例化BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')
print(soup.h3)  # 返回第一个<h3>标签下的数据
# <h3><a href="/chaxun/list/3578.html">《渔家傲·塞下秋来风景异》</a> </h3>

```

2. 通过标签属性进行定位

标签属性有class、id等，主要使用class属性来定位标签。因为class是python关键字，所以此处应用时在单词末尾加下划线，写为class_以示区分。也可以同时使用标签名和属性进行定位。


```python
import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
# 用获取的网页源代码实例化BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')

# 返回第一个属性名为class_="shici_content"的标签下的数据
print(soup.find(class_="shici_content"))
print(soup.find('div',class_="shici_content"))

# 以列表返回全部属性名为class_="shici_content"的标签下的数据
print(soup.find_all(class_="shici_content"))


```

输出结果
<div class="shici_content">
塞下秋来风景异，衡阳雁去无留意。四面边声连角起。千嶂里，长烟落日孤城闭。<br/>
浊酒一杯家万里，燕然未勒归无计，羌管悠悠霜满地。人不寐，将军白发征夫泪。
</div>

[<div class="shici_list_main">
<h3><a href="/chaxun/list/3578.html">《渔家傲·塞下秋来风景异》</a> 
 ......
</div>]
3. 通过选择器进行定位

使用select()函数可以根据指定的选择器返回所有符合条件的标签。常用的选择器有id、class、标签和层级选择器。id选择器可以根据标签的id属性进行定位，使用方法为select('#id名')，括号中的“#”代表id选择器，后面内容为id属性值，返回一个列表。

class选择器可以根据标签的class属性进行定位，使用方法为select('.class名')，返回满足条件的所有标签的列表。


```python

import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
# 用获取的网页源代码实例化BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')

print(soup.select('.shici_content'))
```

用标签选择器进行定位与只用标签名进行定位的不同之处在于该方法可以返回所有该类型的标签。HTML中经常是一个标签包含另一个标签，形成层层嵌套的结构，利用层级选择器可以先定位外层的标签，再定位内层的标签，逐层定位，精确定位到内层标签。


```python
import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
# 用获取的网页源代码实例化BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')

print(soup.select('h3>a'))
print(soup.select('h3 a'))
```

获取到所有包含词名的数据
[<a href="/chaxun/list/3578.html">《渔家傲·塞下秋来风景异》</a>, <a href="/chaxun/list/3627.html">《醉花阴·薄雾浓云愁永昼》</a>, <a href="/chaxun/list/3638.html">《声声慢·寻寻觅觅》</a>, <a href="/chaxun/list/3710.html">《念奴娇·赤壁怀古》</a>, <a href="/chaxun/list/3733.html">《雨霖铃·寒蝉凄切》</a>, <a href="/chaxun/list/6223.html">《浣溪沙》</a>, <a href="/chaxun/list/6414.html">《永遇乐·落日熔金》</a>, <a href="/chaxun/list/6549.html">《临江仙 夜登小阁，忆洛中旧游》</a>, <a href="/chaxun/list/31981.html">《水龙吟·次歆林圣予惜春》</a>, <a href="/chaxun/list/32003.html">《忆少年·无穷官柳》</a>, <a href="/chaxun/list/32013.html">《临江仙·忆昔西池池上饮》</a>, <a href="/chaxun/list/32024.html">《绿头鸭·咏月》</a>, <a href="/chaxun/list/32070.html">《苏幕遮·碧云天》</a>, <a href="/chaxun/list/32085.html">《御街行·纷纷坠叶飘香砌》</a>, <a href="/chaxun/list/32107.html">《凤箫吟》</a>, <a href="/chaxun/list/32126.html">《薄幸·淡妆多态》</a>, <a href="/chaxun/list/32146.html">《喋恋花》</a>, <a href="/chaxun/list/32170.html">《浣溪沙》</a>, <a href="/chaxun/list/32177.html">《浣溪沙》</a>, <a href="/chaxun/list/32197.html">《天门谣·牛渚天门险》</a>]
## 6.3 从标签中提取文本

定位到标签后可以利用标签的string属性或text属性从标签中提取文本内容。string属性返回的是直接存储于该标签中的文本，而不是存于标签下其他标签中的文本。如果当前标签没有直系文本，或者当前标签包含子标签，导致string属性无法确定要提取哪些文本，会返回None。


```python
import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
# 用获取的网页源代码实例化BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')

print(soup.select('.shici_list_main')[0].string)  # None，无直接存储的数据
```

text属性返回的是指定标签下的所有文本。


```python
import requests  # 导入requests模块
from bs4 import BeautifulSoup

# 网页头，模拟浏览器行为
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.9 Safari/537.36'}
url = 'https://www.shicimingju.com/shicimark/songcisanbaishou.html'
response = requests.get(url=url, timeout=1.0)
response.encoding = 'utf-8'
# 用获取的网页源代码实例化BeautifulSoup对象
soup = BeautifulSoup(response.text, 'lxml')

print(soup.select('.shici_list_main')[0].text)    # 所有文本，如输出结果所示
```

输出

《渔家傲·塞下秋来风景异》 
塞下秋来风景异，衡阳雁去无留意。四面边声连角起。千嶂里，长烟落日孤城闭。浊酒一杯家万里，燕然未勒归无计，羌管悠悠霜满地。人不寐，将军白发征夫泪。


```python

```
