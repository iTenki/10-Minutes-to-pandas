# 10 Minutes to pandas

十分钟快速入门 Pandas
==========


# 导入Pandas


```python
import pandas as pd # This is the standard
```

这是导入 pandas 的标准方法。我们不想一直写 pandas 的全名，但是保证代码的简洁和避免命名冲突都很重要，所以折中使用 pd 。如果你去看别人使用 pandas 的代码，就会看到这种导入方式。

# Pandas 中的数据类型

Pandas 基于两种数据类型，*series* 和 *dataframe*。

**series** 是一种一维的数据类型，其中的每个元素都有各自的标签。如果你之前看过这个系列关于 Numpy 的推文，你可以把它当作一个由带标签的元素组成的 numpy 数组。标签可以是数字或者字符。

**dataframe** 是一个二维的、表格型的数据结构。Pandas 的 dataframe 可以储存许多不同类型的数据，并且每个轴都有标签。你可以把它当作一个 series 的

# 将数据导入 Pandas

在对数据进行修改、探索和分析之前，我们得先导入数据。多亏了 Pandas ，这比在 Numpy 中还要容易。


```python
df = pd.read_csv('/Users/iTenki/Documents/GitHub/10-Minutes-to-pandas/uk_rain_2014.csv', header = 0)
```

# 准备好要进行探索和分析的数据

查看前 x 行的数据：


```python
# Getting first x rows.
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Water Year</th>
      <th>Rain (mm) Oct-Sep</th>
      <th>Outflow (m3/s) Oct-Sep</th>
      <th>Rain (mm) Dec-Feb</th>
      <th>Outflow (m3/s) Dec-Feb</th>
      <th>Rain (mm) Jun-Aug</th>
      <th>Outflow (m3/s) Jun-Aug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1980/81</td>
      <td>1182</td>
      <td>5408</td>
      <td>292</td>
      <td>7248</td>
      <td>174</td>
      <td>2212</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1981/82</td>
      <td>1098</td>
      <td>5112</td>
      <td>257</td>
      <td>7316</td>
      <td>242</td>
      <td>1936</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1982/83</td>
      <td>1156</td>
      <td>5701</td>
      <td>330</td>
      <td>8567</td>
      <td>124</td>
      <td>1802</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1983/84</td>
      <td>993</td>
      <td>4265</td>
      <td>391</td>
      <td>8905</td>
      <td>141</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1984/85</td>
      <td>1182</td>
      <td>5364</td>
      <td>217</td>
      <td>5813</td>
      <td>343</td>
      <td>4313</td>
    </tr>
  </tbody>
</table>
</div>



>译者注：如果你的数据集中有中文的话，最好在里面加上 encoding = 'gbk' ，以避免乱码问题。后面的导出数据的时候也一样。

查看后 x 行的数据：


```python
# Getting last x rows.
df.tail(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Water Year</th>
      <th>Rain (mm) Oct-Sep</th>
      <th>Outflow (m3/s) Oct-Sep</th>
      <th>Rain (mm) Dec-Feb</th>
      <th>Outflow (m3/s) Dec-Feb</th>
      <th>Rain (mm) Jun-Aug</th>
      <th>Outflow (m3/s) Jun-Aug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>28</th>
      <td>2008/09</td>
      <td>1139</td>
      <td>4941</td>
      <td>268</td>
      <td>6690</td>
      <td>323</td>
      <td>3189</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2009/10</td>
      <td>1103</td>
      <td>4738</td>
      <td>255</td>
      <td>6435</td>
      <td>244</td>
      <td>1958</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2010/11</td>
      <td>1053</td>
      <td>4521</td>
      <td>265</td>
      <td>6593</td>
      <td>267</td>
      <td>2885</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2011/12</td>
      <td>1285</td>
      <td>5500</td>
      <td>339</td>
      <td>7630</td>
      <td>379</td>
      <td>5261</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2012/13</td>
      <td>1090</td>
      <td>5329</td>
      <td>350</td>
      <td>9615</td>
      <td>187</td>
      <td>1797</td>
    </tr>
  </tbody>
</table>
</div>



跟 head 一样，我们只需要调用 tail 并且传入想要查看的行数即可。<br>
**注意，它并不是从最后一行倒着显示的，而是按照数据原来的顺序显示.**

你通常使用列的名字来在 Pandas 中查找列。这一点很好而且易于使用，但是有时列名太长，比如调查问卷的一整个问题。不过你把列名缩短之后一切就好说了。


```python
# Changing column labels.
df.columns = ['water_year','rain_octsep', 'outflow_octsep',
              'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']

df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1980/81</td>
      <td>1182</td>
      <td>5408</td>
      <td>292</td>
      <td>7248</td>
      <td>174</td>
      <td>2212</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1981/82</td>
      <td>1098</td>
      <td>5112</td>
      <td>257</td>
      <td>7316</td>
      <td>242</td>
      <td>1936</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1982/83</td>
      <td>1156</td>
      <td>5701</td>
      <td>330</td>
      <td>8567</td>
      <td>124</td>
      <td>1802</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1983/84</td>
      <td>993</td>
      <td>4265</td>
      <td>391</td>
      <td>8905</td>
      <td>141</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1984/85</td>
      <td>1182</td>
      <td>5364</td>
      <td>217</td>
      <td>5813</td>
      <td>343</td>
      <td>4313</td>
    </tr>
  </tbody>
</table>
</div>



你通常会想知道数据的另一个特征——它有多少条记录。在 Pandas 中，**一条记录对应着一行**，所以我们可以对数据集调用 len 方法，它将返回数据集的**总行数：**


```python
# Finding out how many rows dataset has.
len(df)
```




    33



上面的代码返回一个表示数据行数的整数，在我的数据集中，这个值是 33 。

你可能还想知道数据集的一些基本的统计数据，在 Pandas 中，这个操作简单到哭：


```python
# Finding out basic statistical information on your dataset.
pd.options.display.float_format = '{:,.3f}'.format # Limit output to 3 decimal places.
df.describe()
# 这将返回一张表，其中有诸如总数、均值、标准差之类的统计数据：
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>33.000</td>
      <td>33.000</td>
      <td>33.000</td>
      <td>33.000</td>
      <td>33.000</td>
      <td>33.000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1,129.000</td>
      <td>5,019.182</td>
      <td>325.364</td>
      <td>7,926.545</td>
      <td>237.485</td>
      <td>2,439.758</td>
    </tr>
    <tr>
      <th>std</th>
      <td>101.900</td>
      <td>658.588</td>
      <td>69.995</td>
      <td>1,692.800</td>
      <td>66.168</td>
      <td>1,025.914</td>
    </tr>
    <tr>
      <th>min</th>
      <td>856.000</td>
      <td>3,479.000</td>
      <td>206.000</td>
      <td>4,578.000</td>
      <td>103.000</td>
      <td>1,078.000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1,053.000</td>
      <td>4,506.000</td>
      <td>268.000</td>
      <td>6,690.000</td>
      <td>193.000</td>
      <td>1,797.000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1,139.000</td>
      <td>5,112.000</td>
      <td>309.000</td>
      <td>7,630.000</td>
      <td>229.000</td>
      <td>2,142.000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1,182.000</td>
      <td>5,497.000</td>
      <td>360.000</td>
      <td>8,905.000</td>
      <td>280.000</td>
      <td>2,959.000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1,387.000</td>
      <td>6,391.000</td>
      <td>484.000</td>
      <td>11,486.000</td>
      <td>379.000</td>
      <td>5,261.000</td>
    </tr>
  </tbody>
</table>
</div>



# 过滤

有时你想提取一整列，使用列的标签可以非常简单地做到：


```python
# Getting a column by label
df['rain_octsep'][:5]
```




    0    1182
    1    1098
    2    1156
    3     993
    4    1182
    Name: rain_octsep, dtype: int64



注意，当我们提取列的时候，**会得到一个 series** ，而不是 dataframe 。记得我们前面提到过，你可以把** dataframe 看作是一个 series 的字典**，*所以在抽取列的时候，我们就会得到一个 series。*

还记得我在命名列标签的时候特意指出的吗？不用空格、破折号之类的符号，这样我们就可以像访问对象属性一样访问数据集的列——只用一个点号。


```python
# Getting a column by label using .
df.rain_octsep[:5]
```




    0    1182
    1    1098
    2    1156
    3     993
    4    1182
    Name: rain_octsep, dtype: int64



这句代码返回的结果与前一个例子完全一样——是我们选择的那列数据。

如果你读过这个系列关于 *Numpy* 的推文，你可能还记得一个叫做 **布尔过滤（boolean masking）**的技术，通过在一个数组上运行条件来得到一个*布林数组*。在 Pandas 里也可以做到。


```python
# Creating a series of booleans based on a conditional
df.rain_octsep[:5] < 1000 # Or df['rain_octsep] < 1000
```




    0    False
    1    False
    2    False
    3     True
    4    False
    Name: rain_octsep, dtype: bool



上面的代码将会返回一个由*布尔值*构成的 **Series**。  
True 表示在十月-九月降雨量小于 1000 mm，False 表示大于等于 1000 mm


```python
# Using a series of booleans to filter
df[df.rain_octsep < 1000]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>1983/84</td>
      <td>993</td>
      <td>4265</td>
      <td>391</td>
      <td>8905</td>
      <td>141</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1988/89</td>
      <td>976</td>
      <td>4330</td>
      <td>309</td>
      <td>6465</td>
      <td>200</td>
      <td>1440</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1995/96</td>
      <td>856</td>
      <td>3479</td>
      <td>245</td>
      <td>5515</td>
      <td>172</td>
      <td>1439</td>
    </tr>
  </tbody>
</table>
</div>



也可以通过复合条件表达式来进行过滤：


```python
# Filtering by multiple conditionals
# Can't use the keyword 'and'
df[(df.rain_octsep < 1000) & (df.outflow_octsep < 4000)] 
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>1995/96</td>
      <td>856</td>
      <td>3479</td>
      <td>245</td>
      <td>5515</td>
      <td>172</td>
      <td>1439</td>
    </tr>
  </tbody>
</table>
</div>



这条代码只会返回 rain_octsep 中小于 1000 的和 outflow_octsep 中小于 4000 的记录,

***注意重要的一点：这里不能用 and 关键字，因为会引发操作顺序的问题。必须用 & 和圆括号。***


如果你的数据中字符串，好消息，你也可以使用字符串方法来进行过滤：


```python
# Filtering by string methods
df[df.water_year.str.startswith('199')]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>1990/91</td>
      <td>1022</td>
      <td>4418</td>
      <td>305</td>
      <td>7120</td>
      <td>216</td>
      <td>1923</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1991/92</td>
      <td>1151</td>
      <td>4506</td>
      <td>246</td>
      <td>5493</td>
      <td>280</td>
      <td>2118</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1992/93</td>
      <td>1130</td>
      <td>5246</td>
      <td>308</td>
      <td>8751</td>
      <td>219</td>
      <td>2551</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1993/94</td>
      <td>1162</td>
      <td>5583</td>
      <td>422</td>
      <td>10109</td>
      <td>193</td>
      <td>1638</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1994/95</td>
      <td>1110</td>
      <td>5370</td>
      <td>484</td>
      <td>11486</td>
      <td>103</td>
      <td>1231</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1995/96</td>
      <td>856</td>
      <td>3479</td>
      <td>245</td>
      <td>5515</td>
      <td>172</td>
      <td>1439</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1996/97</td>
      <td>1047</td>
      <td>4019</td>
      <td>258</td>
      <td>5770</td>
      <td>256</td>
      <td>2102</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1997/98</td>
      <td>1169</td>
      <td>4953</td>
      <td>341</td>
      <td>7747</td>
      <td>285</td>
      <td>3206</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1998/99</td>
      <td>1268</td>
      <td>5824</td>
      <td>360</td>
      <td>8771</td>
      <td>225</td>
      <td>2240</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1999/00</td>
      <td>1204</td>
      <td>5665</td>
      <td>417</td>
      <td>10021</td>
      <td>197</td>
      <td>2166</td>
    </tr>
  </tbody>
</table>
</div>



*** 注意，你必须用 .str.[string method] ，而不能直接在字符串上调用字符方法。上面的代码返回所有 90 年代的记录. ***

# 索引

之前的部分展示了如何通过列操作来得到数据，但是 Pandas 的行也有标签。*行标签可以是基于数字的或者是标签，而且获取行数据的方法也根据标签的类型各有不同。**

如果你的行标签是**数字型**的，你可以通过*** iloc ***来引用：


```python
# Getting a row via a numerical index
df.iloc[30]
```




    water_year        2010/11
    rain_octsep          1053
    outflow_octsep       4521
    rain_decfeb           265
    outflow_decfeb       6593
    rain_junaug           267
    outflow_junaug       2885
    Name: 30, dtype: object



***iloc*** 只对***数字型*** 的标签有用。它会返回给定行的*** series***，**行中的每一列都是返回 series 的一个元素。**

也许你的数据集中有年份或者年龄的列，你可能想通过这些年份或者年龄来引用行，这个时候我们就可以设置一个（或者多个）新的索引：


```python
#Setting a new index from an existing column
df = df.set_index(['water_year'])
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
    <tr>
      <th>water_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980/81</th>
      <td>1182</td>
      <td>5408</td>
      <td>292</td>
      <td>7248</td>
      <td>174</td>
      <td>2212</td>
    </tr>
    <tr>
      <th>1981/82</th>
      <td>1098</td>
      <td>5112</td>
      <td>257</td>
      <td>7316</td>
      <td>242</td>
      <td>1936</td>
    </tr>
    <tr>
      <th>1982/83</th>
      <td>1156</td>
      <td>5701</td>
      <td>330</td>
      <td>8567</td>
      <td>124</td>
      <td>1802</td>
    </tr>
    <tr>
      <th>1983/84</th>
      <td>993</td>
      <td>4265</td>
      <td>391</td>
      <td>8905</td>
      <td>141</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>1984/85</th>
      <td>1182</td>
      <td>5364</td>
      <td>217</td>
      <td>5813</td>
      <td>343</td>
      <td>4313</td>
    </tr>
  </tbody>
</table>
</div>



上面的代码将 water_year 列设置为索引。***注意，列的名字实际上是一个列表***，虽然上面的例子中只有一个元素。如果你想设置多个索引，只需要在列表中加入列的名字即可。

上例中我们设置的索引列中都是字符型数据，这意味着我们不能继续使用 iloc 来引用，那我们用什么呢？用 loc 。


```python
# Getting a row via a label-based index
df.loc['2000/01']
```




    rain_octsep       1239
    outflow_octsep    6092
    rain_decfeb        328
    outflow_decfeb    9347
    rain_junaug        236
    outflow_junaug    2142
    Name: 2000/01, dtype: int64



和 ***iloc*** 一样，***loc*** 会返回你引用的列，唯一一点不同就是此时你使用的是基于字符串的引用，而不是基于数字的。

还有一个引用列的常用常用方法—— ix 。如果 loc 是基于标签的，而 iloc 是基于数字的，那 ix 是基于什么的？***事实上，ix 是基于标签的查询方法，但它同时也支持数字型索引作为备选。***


```python
# Getting a row via a label-based or numerical index
df.ix['1999/00'] # Label based with numerical index fallback *Not Recommended
```




    rain_octsep        1204
    outflow_octsep     5665
    rain_decfeb         417
    outflow_decfeb    10021
    rain_junaug         197
    outflow_junaug     2166
    Name: 1999/00, dtype: int64



如果 ix 可以同时起到 loc 和 iloc 的作用，那为什么还要用后两个？***一大原因就是 ix 具有轻微的不可预测性***。还记得我说过它所支持的数字型索引只是备选吗？这一特性可能会导致 ix 产生一些奇怪的结果，比如讲一个数字解释为一个位置。而使用 iloc 和 loc 会很安全、可预测并且让人放心。*** 但是我要指出的是，ix 比 iloc 和 loc 要快一些。***

将索引排序通常会很有用，在 Pandas 中，我们可以对 dataframe 调用 sort_index 方法进行排序。


```python
# inplace = True to apply the sorting in place
df.sort_index(ascending = False).head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
    <tr>
      <th>water_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012/13</th>
      <td>1090</td>
      <td>5329</td>
      <td>350</td>
      <td>9615</td>
      <td>187</td>
      <td>1797</td>
    </tr>
    <tr>
      <th>2011/12</th>
      <td>1285</td>
      <td>5500</td>
      <td>339</td>
      <td>7630</td>
      <td>379</td>
      <td>5261</td>
    </tr>
    <tr>
      <th>2010/11</th>
      <td>1053</td>
      <td>4521</td>
      <td>265</td>
      <td>6593</td>
      <td>267</td>
      <td>2885</td>
    </tr>
    <tr>
      <th>2009/10</th>
      <td>1103</td>
      <td>4738</td>
      <td>255</td>
      <td>6435</td>
      <td>244</td>
      <td>1958</td>
    </tr>
    <tr>
      <th>2008/09</th>
      <td>1139</td>
      <td>4941</td>
      <td>268</td>
      <td>6690</td>
      <td>323</td>
      <td>3189</td>
    </tr>
  </tbody>
</table>
</div>



我的索引本来就是有序的，为了演示，我将***参数 ascending 设置为 false，这样我的数据就会呈降序排列。***

当你将一列设置为索引的时候，它就不再是数据的一部分了。如果你想将索引恢复为数据，调用*** set_index ***相反的方法*** reset_index ***即可：


```python
# Returning an index to data
df = df.reset_index('water_year')
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1980/81</td>
      <td>1182</td>
      <td>5408</td>
      <td>292</td>
      <td>7248</td>
      <td>174</td>
      <td>2212</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1981/82</td>
      <td>1098</td>
      <td>5112</td>
      <td>257</td>
      <td>7316</td>
      <td>242</td>
      <td>1936</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1982/83</td>
      <td>1156</td>
      <td>5701</td>
      <td>330</td>
      <td>8567</td>
      <td>124</td>
      <td>1802</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1983/84</td>
      <td>993</td>
      <td>4265</td>
      <td>391</td>
      <td>8905</td>
      <td>141</td>
      <td>1078</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1984/85</td>
      <td>1182</td>
      <td>5364</td>
      <td>217</td>
      <td>5813</td>
      <td>343</td>
      <td>4313</td>
    </tr>
  </tbody>
</table>
</div>



# 对数据集应用函数

有时你想对数据集中的数据进行改变或者某种操作。比方说，你有一列年份的数据，你需要新的一列来表示这些年份对应的年代。Pandas 中有两个非常有用的函数*** apply 和 applymap ***。


```python
# Applying a funciton to a column
def base_year(year):
    base_year = year[:4]
    base_year = pd.to_datetime(base_year).year
    return base_year

df['year'] = df.water_year.apply(base_year)
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1980/81</td>
      <td>1182</td>
      <td>5408</td>
      <td>292</td>
      <td>7248</td>
      <td>174</td>
      <td>2212</td>
      <td>1980</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1981/82</td>
      <td>1098</td>
      <td>5112</td>
      <td>257</td>
      <td>7316</td>
      <td>242</td>
      <td>1936</td>
      <td>1981</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1982/83</td>
      <td>1156</td>
      <td>5701</td>
      <td>330</td>
      <td>8567</td>
      <td>124</td>
      <td>1802</td>
      <td>1982</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1983/84</td>
      <td>993</td>
      <td>4265</td>
      <td>391</td>
      <td>8905</td>
      <td>141</td>
      <td>1078</td>
      <td>1983</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1984/85</td>
      <td>1182</td>
      <td>5364</td>
      <td>217</td>
      <td>5813</td>
      <td>343</td>
      <td>4313</td>
      <td>1984</td>
    </tr>
  </tbody>
</table>
</div>



# 操作数据集的结构

另一常见的做法是重新建立数据结构，使得数据集呈现出一种更方便并且（或者）有用的形式。

掌握这些转换最简单的方法就是观察转换的过程。比起这篇文章的其他部分，接下来的操作需要你跟着练习以便能掌握它们。

首先，是*** groupby ***：

***groupby ***会按照你选择的列对数据集进行分组。上例是按照年代分组。不过仅仅这样做并没有什么用，我们必须对其调用函数，比如 max 、 min 、mean 等等。例中，我们可以得到 90 年代的均值。




```python
#Manipulating structure (groupby, unstack, pivot)
#Groupby
df.groupby(df.year // 10 * 10).max()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
      <th>year</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980</th>
      <td>1989/90</td>
      <td>1210</td>
      <td>5701</td>
      <td>470</td>
      <td>10520</td>
      <td>343</td>
      <td>4313</td>
      <td>1989</td>
    </tr>
    <tr>
      <th>1990</th>
      <td>1999/00</td>
      <td>1268</td>
      <td>5824</td>
      <td>484</td>
      <td>11486</td>
      <td>285</td>
      <td>3206</td>
      <td>1999</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>2009/10</td>
      <td>1387</td>
      <td>6391</td>
      <td>437</td>
      <td>10926</td>
      <td>357</td>
      <td>5168</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>2012/13</td>
      <td>1285</td>
      <td>5500</td>
      <td>350</td>
      <td>9615</td>
      <td>379</td>
      <td>5261</td>
      <td>2012</td>
    </tr>
  </tbody>
</table>
</div>



你也可以按照多列进行分组：


```python
# Grouping bu mutileple columns
decade_rain = df.groupby([df.year // 10* 10, df.rain_octsep // 1000*1000])[['outflow_octsep', 'outflow_decfeb', 'outflow_junaug']].mean()
decade_rain                                                      
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>outflow_octsep</th>
      <th>outflow_decfeb</th>
      <th>outflow_junaug</th>
    </tr>
    <tr>
      <th>year</th>
      <th>rain_octsep</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1980</th>
      <th>0</th>
      <td>4,297.500</td>
      <td>7,685.000</td>
      <td>1,259.000</td>
    </tr>
    <tr>
      <th>1000</th>
      <td>5,289.625</td>
      <td>7,933.000</td>
      <td>2,572.250</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1990</th>
      <th>0</th>
      <td>3,479.000</td>
      <td>5,515.000</td>
      <td>1,439.000</td>
    </tr>
    <tr>
      <th>1000</th>
      <td>5,064.889</td>
      <td>8,363.111</td>
      <td>2,130.556</td>
    </tr>
    <tr>
      <th>2000</th>
      <th>1000</th>
      <td>5,030.800</td>
      <td>7,812.100</td>
      <td>2,685.900</td>
    </tr>
    <tr>
      <th>2010</th>
      <th>1000</th>
      <td>5,116.667</td>
      <td>7,946.000</td>
      <td>3,314.333</td>
    </tr>
  </tbody>
</table>
</div>



接下来是*** unstack ***，最开始可能有一些困惑，它可以将一列数据设置为列标签。最好还是看看实际的操作：


```python
# Unstacking
decade_rain.unstack(0)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">outflow_octsep</th>
      <th colspan="4" halign="left">outflow_decfeb</th>
      <th colspan="4" halign="left">outflow_junaug</th>
    </tr>
    <tr>
      <th>year</th>
      <th>1980</th>
      <th>1990</th>
      <th>2000</th>
      <th>2010</th>
      <th>1980</th>
      <th>1990</th>
      <th>2000</th>
      <th>2010</th>
      <th>1980</th>
      <th>1990</th>
      <th>2000</th>
      <th>2010</th>
    </tr>
    <tr>
      <th>rain_octsep</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4,297.500</td>
      <td>3,479.000</td>
      <td>nan</td>
      <td>nan</td>
      <td>7,685.000</td>
      <td>5,515.000</td>
      <td>nan</td>
      <td>nan</td>
      <td>1,259.000</td>
      <td>1,439.000</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>1000</th>
      <td>5,289.625</td>
      <td>5,064.889</td>
      <td>5,030.800</td>
      <td>5,116.667</td>
      <td>7,933.000</td>
      <td>8,363.111</td>
      <td>7,812.100</td>
      <td>7,946.000</td>
      <td>2,572.250</td>
      <td>2,130.556</td>
      <td>2,685.900</td>
      <td>3,314.333</td>
    </tr>
  </tbody>
</table>
</div>



让我们再操作一次。这次使用第 1 列，也就是* rain_octsep *列：


```python
# More unstacking
decade_rain.unstack(1)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">outflow_octsep</th>
      <th colspan="2" halign="left">outflow_decfeb</th>
      <th colspan="2" halign="left">outflow_junaug</th>
    </tr>
    <tr>
      <th>rain_octsep</th>
      <th>0</th>
      <th>1000</th>
      <th>0</th>
      <th>1000</th>
      <th>0</th>
      <th>1000</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980</th>
      <td>4,297.500</td>
      <td>5,289.625</td>
      <td>7,685.000</td>
      <td>7,933.000</td>
      <td>1,259.000</td>
      <td>2,572.250</td>
    </tr>
    <tr>
      <th>1990</th>
      <td>3,479.000</td>
      <td>5,064.889</td>
      <td>5,515.000</td>
      <td>8,363.111</td>
      <td>1,439.000</td>
      <td>2,130.556</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>nan</td>
      <td>5,030.800</td>
      <td>nan</td>
      <td>7,812.100</td>
      <td>nan</td>
      <td>2,685.900</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>nan</td>
      <td>5,116.667</td>
      <td>nan</td>
      <td>7,946.000</td>
      <td>nan</td>
      <td>3,314.333</td>
    </tr>
  </tbody>
</table>
</div>



在进行下次操作之前，我们先创建一个用于演示的 dataframe :


```python
# Create a new dataframe containing entries which
# has rain_octsep values of greater than 1250
high_rain = df[df.rain_octsep > 1250]
high_rain
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>water_year</th>
      <th>rain_octsep</th>
      <th>outflow_octsep</th>
      <th>rain_decfeb</th>
      <th>outflow_decfeb</th>
      <th>rain_junaug</th>
      <th>outflow_junaug</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>1998/99</td>
      <td>1268</td>
      <td>5824</td>
      <td>360</td>
      <td>8771</td>
      <td>225</td>
      <td>2240</td>
      <td>1998</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2006/07</td>
      <td>1387</td>
      <td>6391</td>
      <td>437</td>
      <td>10926</td>
      <td>357</td>
      <td>5168</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2011/12</td>
      <td>1285</td>
      <td>5500</td>
      <td>339</td>
      <td>7630</td>
      <td>379</td>
      <td>5261</td>
      <td>2011</td>
    </tr>
  </tbody>
</table>
</div>



我们将会在上面演示轴向旋转***（pivoting）***.
轴旋转其实就是我们之前已经看到的那些操作的一个集合。
1. 首先，它会设置一个新的索引（set_index()）.
2. 然后对索引排序（sort_index()）.
3. 最后调用 unstack 。
以上的步骤合在一起就是 pivot 。接下来看看你能不能搞清楚下面的代码在干什么：


```python
# Pivoting
# dose set_index, sort_index and unstack in a row
high_rain.pivot('year', 'rain_octsep')[['outflow_octsep', 'outflow_decfeb', 'outflow_junaug']].fillna('')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">outflow_octsep</th>
      <th colspan="3" halign="left">outflow_decfeb</th>
      <th colspan="3" halign="left">outflow_junaug</th>
    </tr>
    <tr>
      <th>rain_octsep</th>
      <th>1268</th>
      <th>1285</th>
      <th>1387</th>
      <th>1268</th>
      <th>1285</th>
      <th>1387</th>
      <th>1268</th>
      <th>1285</th>
      <th>1387</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1998</th>
      <td>5,824.000</td>
      <td></td>
      <td></td>
      <td>8,771.000</td>
      <td></td>
      <td></td>
      <td>2,240.000</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2006</th>
      <td></td>
      <td></td>
      <td>6,391.000</td>
      <td></td>
      <td></td>
      <td>10,926.000</td>
      <td></td>
      <td></td>
      <td>5,168.000</td>
    </tr>
    <tr>
      <th>2011</th>
      <td></td>
      <td>5,500.000</td>
      <td></td>
      <td></td>
      <td>7,630.000</td>
      <td></td>
      <td></td>
      <td>5,261.000</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



***注意，最后有一个 .fillna('') 。pivot 产生了很多空的记录，也就是值为 NaN 的记录。我个人觉得数据集里面有很多 NaN 会很烦，所以使用了 fillna('') 。你也可以用别的别的东西，比方说 0 。我们也可以使用 dropna(how = 'any') 来删除有 NaN 的行，不过这样就把所有的数据都删掉了，所以不这样做。***

Pivot 等价于 以下代码：


```python
# Equal to pivot
high_rain.set_index(['rain_octsep','year']).sort_index().unstack(['rain_octsep'])[['outflow_octsep', 'outflow_decfeb', 'outflow_junaug']].fillna('')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">outflow_octsep</th>
      <th colspan="3" halign="left">outflow_decfeb</th>
      <th colspan="3" halign="left">outflow_junaug</th>
    </tr>
    <tr>
      <th>rain_octsep</th>
      <th>1268</th>
      <th>1285</th>
      <th>1387</th>
      <th>1268</th>
      <th>1285</th>
      <th>1387</th>
      <th>1268</th>
      <th>1285</th>
      <th>1387</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1998</th>
      <td>5,824.000</td>
      <td></td>
      <td></td>
      <td>8,771.000</td>
      <td></td>
      <td></td>
      <td>2,240.000</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2006</th>
      <td></td>
      <td></td>
      <td>6,391.000</td>
      <td></td>
      <td></td>
      <td>10,926.000</td>
      <td></td>
      <td></td>
      <td>5,168.000</td>
    </tr>
    <tr>
      <th>2011</th>
      <td></td>
      <td>5,500.000</td>
      <td></td>
      <td></td>
      <td>7,630.000</td>
      <td></td>
      <td></td>
      <td>5,261.000</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



上面的 dataframe 展示了所有降雨超过 1250 的 outflow 。诚然，这并不是讲解 pivot 实际应用最好的例子，但希望你能明白它的意思。看看你能在你的数据集上得到什么结果。

# 合并数据集

有时你有两个相关联的数据集，你想将它们放在一起比较或者合并它们。好的，m没问题，在 Pandas 里很简单：


```python
# Merging two datasets together
rain_jpn = pd.read_csv('jpn_rain.csv')
rain_jpn.columns = ['year', 'jpn_rainfall']

uk_jpn_rain = df.merge(rain_jpn, on='year')
uk_jpn_rain.head(5)
```

首先你需要通过 *** on *** 关键字来指定需要合并的列。通常你可以省略这个参数，Pandas 将会自动选择要合并的列。

如下图所示，两个数据集在年份这一类上合并了。**jpn_rain** 数据集只有年份和降雨量两列，通过年份列合并之后，**jpn_rain** 中只有降雨量那一列合并到了 **UK_rain** 数据集中。

# 使用 Pandas 快速作图

<font color = red>***Matplotlib*** </font> 很棒，但是想要绘制出还算不错的图表却要写不少代码，而有时你只是想粗略的做个图来探索下数据，搞清楚数据的含义。Pandas 通过 *plot* 来解决这个问题：


```python
# Using pandas to quickly plot graphs
uk_jpn_rain.plot(x='year', y=['rain_octsep', 'jpn_rainfall'])
```

这会调用 Matplotlib 快速轻松地绘出了你的数据图。通过这个图你就可以在视觉上分析数据，而且它能在探索数据的时候给你一些方向。比如，看到我的数据图，你会发现在 1995 年的英国好像有一场干旱。

![uk_jpn_rain](http://liubj2016.github.io/Akuan/images/tu.png)

你会发现英国的降雨明显少于日本，但人们却说英国总是下雨。

# 保存你的数据集

在清洗、重塑、探索完数据之后，你最后的数据集可能会发生很大改变，并且比最开始的时候更有用。你应该保存原始的数据集，但是你同样应该保存处理之后的数据。


```python
# Saving your data to a csv
df.to_csv('uk_rain.csv')
```

上面的代码将会保存你的数据到 csv 文件以便下次使用。

我们对 Pandas 的介绍就到此为止了。就像我之前所说的， Pandas 非常强大，我们只是领略到了一点皮毛而已，不过你现在知道的应该足够你开始清洗和探索数据了。

像以前一样，我建议你用自己感兴趣的数据集做一下练习，坐下来，一杯啤酒配数据。这确实是你唯一熟悉 Pandas 以及这个系列其他库的方式。而且你也许会发现一些有趣的东西。


```python

```
