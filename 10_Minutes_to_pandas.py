# 导入
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

'''创造对象'''
# 序列
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# 数据框
dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list('ABCD') )
df2 = pd.DataFrame({
					'A': 1.,
					'B': pd.Timestamp('20130102'),
					'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
					'D': np.array([3] * 4, dtype = 'int32'),
					'E': pd.Categorical(["test", "train", "test", "train"]),
					'F': 'foo'
	})
'''
print(df)
print(df2)
print(df2.dtypes)
'''

'''
# 查看数据

df.head(2) # 数据前几行
df.tail(3) # 数据后几行
print(df.index) # 输出数据框索引
print(df.columns) # 输出数据框列名
print(df.values) # 输出数据框的值
df.describle() # 显示数据概要
print(df.T) # 和Numpy一样，可以方便得到转置
print(df.sort_index(axis = 1, ascending = False)) # 对axis按照index排序（axis = 1 指第二个维度，即： 列）
print(df.sort_values(by = 'B')) # 按值排序
'''
