import pandas as pd

# print(pd.__version__)

# a = {'x': 1, 'y': 7, 'z':2}
# variablia = pd.Series(a, index=a.keys())
# variablia = pd.Series(a, index=['x', 'y'])
# print(variablia)

# data = {
#     'key1': [0, 1, 2],
#     'key2': [3, 4, 5]
# }
# vaal = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
# print(vaal['key2']) # valorile de pe key2, coloana
# print(vaal.loc['linie2'])

# df = pd.read_csv('EXEMPLU.csv')
# print(df)
# df1 = None
df = pd.read_csv('test.csv')
# print(df)
# for x in df.index:
#   print(df.loc[x,'AL'])
  # if df.loc[x,'AL'] == ': ':
  #   df.drop(x, inplace=True)
# print(df)
# df1 = df.to_csv('test1.csv')
# print(df.corr())
# print(df.describe())
# print(df.mean())
# import matplotlib.pyplot as plt
# df.plot(kind='scatter', x='AT', y='BE')
# df['AT'].plot(kind='hist')
# plt.show()
# print(df.head(2))
# print(df.tail(2))
# new_df = df.dropna(inplace=True)
# print(df)
df.fillna((0), inplace=True)
print(df.fillna(0))
# df['AL'].fillna(0, inplace=True)
# print(df)
# df.loc[7, 'AL'] = 45
# print(df)
df.replace(': ', 0, inplace=True)
df.replace(':', 0, include=True)
print(df)
print(df.transpose())
df.to_csv('test1.csv')