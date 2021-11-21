import os
import pandas as pd

from word_cut import *

root = "data/"

name_list = os.listdir(root)

no_list = []
month_list = []
day_list = []
raw_list = []
for name in name_list:
    no_list.append(name[:-4])
    month_list.append(name[4:6])
    day_list.append(name[4:8])
    tmp_list = [line.strip() for line in open(root + name, encoding="UTF-8")]
    tmp_str = "".join(tmp_list)
    raw_list.append(tmp_str)
proc_list = cut_words(raw_list)

no_df = pd.DataFrame(no_list, columns=['no'])
month_df = pd.DataFrame(month_list, columns=['month'])
day_df = pd.DataFrame(day_list, columns=['day'])
data_df = pd.DataFrame(proc_list, columns=['content'])
df = no_df.join(month_df)
df = df.join(day_df)
df = df.join(data_df)
print(df)
df.to_csv('proc_data.csv')

