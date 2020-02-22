import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('poules.csv')

validate(df)

import os
os.exit()

df = df.drop("anita", axis=1)
df = df.drop("tina", axis=1)
df = df.drop("jaike", axis=1)
df = df.drop("johan", axis=1)
df = df.drop("claes", axis=1)
df = df.drop("aflevering", axis=1)

df = df[df.poule.isin(['all', 'luursema'])]

grouped = df.groupby('speler').sum()

grouped.transpose().plot(kind='bar')
plt.savefig('../storage/pictures/poules.png')

def validate(df):
    for speler in df.speler:
        print(speler)