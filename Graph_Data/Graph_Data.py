import statistics
from collections import Counter

def result(num):
  col_name = '사용일자'
  col_name2 = '승차총승객수'
  slt_list = list(set(df[col_name]))
  lst = list()

  if num == 0:
    for slt in slt_list:
      _list = list(df.loc[df[col_name] == slt][col_name2])
      lst.append([slt, round(statistics.mean(_list),3)])
    return lst
  elif num == 1:
    for slt in slt_list:
      _list = list(df.loc[df[col_name] == slt][col_name2])
      lst.append([slt, statistics.median(_list)])
    return lst
  elif num == 2:
    for slt in slt_list:
      _list = list(df.loc[df[col_name] == slt][col_name2])
      lst.append([slt, max(_list)])
    return lst
  elif num == 3:
    for slt in slt_list:
      _list = list(df.loc[df[col_name] == slt][col_name2])
      lst.append([slt, min(_list)])
    return lst
  elif num == 4:
    for slt in slt_list:
      _list = list(df.loc[df[col_name] == slt][col_name2])
      lst.append([slt, np.bincount(_list).argmax()])
    return lst
  
result_data = pd.DataFrame({'mean':result(0),
                            'median':result(1),
                            'max':result(2),
                            'min':result(3),
                            'mode':result(4)})
print(result_data)
