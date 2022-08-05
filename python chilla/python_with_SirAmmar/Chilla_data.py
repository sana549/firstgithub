# import libraries

#import pandas as pd

#df = pd.read_csv("titanic.csv")
#print(df)


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='ticks', color_codes=True)

p=sns.countplot(x="",hue="age", data="chilla")
plt.show()




