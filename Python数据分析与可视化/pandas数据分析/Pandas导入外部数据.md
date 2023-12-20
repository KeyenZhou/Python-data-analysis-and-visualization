# Pandas导入外部数据

pandas支持方便快速的从多种格式的外部文件中读取数据形成DataFrame，或将DataFrame写入不同格式的外部文件。
下表是Pandas官方手册上给出的一张表格，表格描述的是Pandas中对各种数据文件类型的读、写函数。

| Format Type |   Data Description    |     Reader     |     Writer      |
|:-----------:|:---------------------:|:--------------:|:---------------:|
|    text     |          CSV          |    read_csv    |     to_csv      |
|    text     | Fixed-Width Text File |    read_fwf    |                 |
|    text     |         JSON          |   read_json    |     to_json     |
|    text     |         HTML          |   read_html    |     to_html     |
|    text     |         LaTeX         |                | Styler.to_latex |
|    text     |          XML          |    read_xml    |     to_xml      |
|    text     |    Local clipboard    | read_clipboard |  to_clipboard   |
|   binary    |       MS Excel        |   read_excel   |    to_excel     |
|   binary    |     OpenDocument      |   read_excel   |                 |
|   binary    |      HDF5 Format      |    read_hdf    |     to_hdf      |
|   binary    |    Feather Format     |  read_feather  |   to_feather    |
|   binary    |    Parquet Format     |  read_parquet  |   to_parquet    |
|   binary    |      ORC Format       |    read_orc    |                 |
|   binary    |         Stata         |   read_stata   |    to_stata     |
|   binary    |          SAS          |    read_sas    |                 |
|   binary    |         SPSS          |   read_spss    |                 |
|   binary    | Python Pickle Format  |  read_pickle   |    to_pickle    |
|     SQL     |          SQL          |    read_sql    |     to_sql      |
|     SQL     |    Google BigQuery    |    read_gbq    |     to_gbq      |

本节仅介绍几种常用文件的读取方式，其他方法大家如需使用可自行查询[相关文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)。

## 读取txt或csv文件

```python
pandas.read_csv(filepath_or_buffer, sep=NoDefault.no_default, delimiter=None, header='infer',
                names=NoDefault.no_default, index_col=None, usecols=None, squeeze=None, prefix=NoDefault.no_default,
                mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None,
                skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True,
                na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False,
                keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None,
                compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0,
                doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None,
                error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True,
                memory_map=False, float_precision=None, storage_options=None)
```

该方法参数较多，下面简单介绍一些常用参数，其他参数含义可自行查询文档。

* filepath_or_buffer：读取的文件路径,URL（包含http,ftp,s3）链接等
* sep：指定分隔符，默认逗号分隔。
* delimiter：定界符，备选分隔符（如果指定该参数，则sep参数失效）
* delim_whitespace：boolean, 是否指定空白字符作为分隔符，如果为Ture那么delimiter参数失效。
* header：指定作为整个数据集列名的行，默认为第一行.如果数据集中没有列名，则需要设置为None
* names：用于结果的列名列表。如果数据文件中没有列标题行，就需要设置header=None
* index_col：指定数据集中的某列作为行索引
* usecols：指定只读取文件中的某几列数据
* dtype：设置每列数据的数据类型
* skiprows：设置需要忽略的行数（从文件开始处算起），或需要跳过的行号列表（从0开始）
* skipfooter：设置需要忽略的行数（从文件尾部处算起）
* nrows：设置需要读取的行数（从文件头开始算起）
* skip_blank_lines：如果为True，则跳过空行；否则记为NaN

本节结合如下csv文件，仅讲解最简单用法，其他参数大家可结合数据文件自行尝试其效果。
![](./数据集/image%20(19).png)

数据下载：

[2020各手机参数对比.xls](./数据集/2020各手机参数对比.xls)

[wine point.csv](./数据集/wine%20point.csv)

```python
import pandas as pd

wine_reviews = pd.read_csv("/data/bigfiles/wine point.csv")
# 读取/data/bigfiles/wine point.csv
print(wine_reviews.shape)
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.width', None)  # 显示宽度是无限
print(wine_reviews)  # 返回DataFrame
```

```python
# 明确规定某列做行索引
wine_reviews = pd.read_csv("/data/bigfiles/wine point.csv", index_col=0)
print(wine_reviews)  # 返回DataFrame
```

## 读取excel文件

```python
pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=None, dtype=None,
                  engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None,
                  na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False,
                  date_parser=None, thousands=None, decimal='.', comment=None, skipfooter=0, convert_float=None,
                  mangle_dupe_cols=True, storage_options=None)
```

该函数大部分参数与read_csv()方法相同。其中sheet_name用于指定要读取的sheet，默认读取Excel文件中的第一个sheet。
需要注意的是，使用该方法读取.xlsx文件需要借助openpyxl模块，读取.xls文件需要借助xlrd模块。

本节结合文件“2020各手机参数对比.xls”，仅讲解最简单用法，其他参数大家可结合数据文件自行尝试其效果。

```python
import pandas as pd

phone_infos = pd.read_excel("/data/bigfiles/2020各手机参数对比.xls", skiprows=1)  # 跳过第一行的表格标题
# 读取/data/bigfiles/wine point.csv
print(phone_infos.shape)
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.width', None)  # 显示宽度是无限
pd.set_option('display.unicode.east_asian_width', True)  # 显示时列对齐
print(phone_infos)  # 返回DataFrame
```

### 读取HTML网页

```python
pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False,
                 thousands=',', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True,
                 displayed_only=True)
```

该函数是将HTML的表格转换为DataFrame的一种快速方便的方法，不需要用爬虫获取站点的HTML。match参数通过正则表达式匹配需要的表格；flavor参数设置解析器，默认为lxml。

本节以[ESPN网站的中超排名表](https://www.espn.com/soccer/team/_/id/21506/wuhan-three-towns)为例，讲解其基本用法。

```python
import pandas as pd

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.width', None)  # 显示宽度是无限
pd.set_option('display.unicode.east_asian_width', True)  # 显示时列对齐
# 函数会将每个table转化为一个DataFrame，返回由两个DataFrame构成的列表
CSL_2022 = pd.read_html('https://www.espn.com/soccer/team/_/id/21506/wuhan-three-towns')  # 该页面只有1个table 
print(type(CSL_2022), type(CSL_2022[0]))
print(CSL_2022[0])
```
