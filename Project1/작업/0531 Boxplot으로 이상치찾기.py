import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")
data.head()

# -- matplotlib 으로 boxplot
plt.figure(figsize=(20, 5))
data_res = plt.boxplot(data[['Police', 'CCTV', 'Oneperson', 'Pub', 'Crime']].values)
plt.xticks([1, 2, 3, 4, 5], ['Police', 'CCTV', 'Oneperson', 'Pub', 'Crime'])
plt.show()

# -- Crime 만 보기
data_res = plt.boxplot(data[['Crime']].values)
plt.xticks([1], ['Crime'])
plt.show()

# -- seaborn 으로 boxplot
boxplot= sns.boxplot(y='Crime',
                   data=data,
                  )
