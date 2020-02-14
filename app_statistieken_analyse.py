import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import time

df = pd.read_csv('app_statistieken.csv')

df['unix'] = df.apply(lambda row: time.mktime(date.fromisoformat(row.datum).timetuple()), axis=1)
df['spelers'] = 10 - df.isin([0]).sum(axis=1)
df['correctie'] = 100 / df['spelers']

for speler in ['buddy', 'miljuschka', 'nathan', 'leonie', 'tina', 'anita', 'jaike', 'johan', 'claes', 'rob']:
    df['{}_correctie'.format(speler)] = df[speler] - df['correctie']

print(df)

sns.set()

fig, ax1 = plt.subplots(1, 1)

g = sns.lineplot(x='unix', y='buddy_correctie', data=df, label='buddy', ax=ax1)
sns.lineplot(x='unix', y='miljuschka_correctie', data=df, label='miljuschka', ax=ax1)
sns.lineplot(x='unix', y='nathan_correctie', data=df, label='nathan', ax=ax1)
sns.lineplot(x='unix', y='leonie_correctie', data=df, label='leonie', ax=ax1)
sns.lineplot(x='unix', y='tina_correctie', data=df, label='tina', ax=ax1)
sns.lineplot(x='unix', y='anita_correctie', data=df, label='anita', ax=ax1)
sns.lineplot(x='unix', y='jaike_correctie', data=df, label='jaike', ax=ax1)
sns.lineplot(x='unix', y='johan_correctie', data=df, label='johan', ax=ax1)
sns.lineplot(x='unix', y='claes_correctie', data=df, label='claes', ax=ax1)
sns.lineplot(x='unix', y='rob_correctie', data=df, label='rob', ax=ax1)

box = g.get_position()
g.set_position([box.x0, box.y0, box.width * 0.85, box.height])

plt.xlabel("Unix timestamp")
plt.ylabel("% stemmen")

plt.legend(bbox_to_anchor=(1.35, 0.5), loc='center right', ncol=1)

plt.show()
