import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('poules.csv')
df = df.drop("anita", axis=1)
df = df.drop("tina", axis=1)
df = df.drop("jaike", axis=1)
df = df.drop("johan", axis=1)
df = df.drop("aflevering", axis=1)

grouped = df.groupby('speler').sum()

grouped.transpose().plot(kind='bar')
plt.show()
