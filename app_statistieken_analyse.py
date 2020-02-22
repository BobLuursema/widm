import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from datetime import date
import time

df = pd.read_csv('app_statistieken.csv')

df['unix'] = df.apply(lambda row: time.mktime(date.fromisoformat(row.datum).timetuple()), axis=1)
df['spelers'] = 10 - df.isin([0]).sum(axis=1)
df['correctie'] = 100 / df['spelers']

for speler in ['buddy', 'miljuschka', 'nathan', 'leonie', 'tina', 'anita', 'jaike', 'johan', 'claes', 'rob']:
    df['{}_correctie'.format(speler)] = df[speler] - df['correctie']

plotdf = df.drop(labels=['spelers', 'unix', 'buddy','miljuschka','nathan','leonie','tina', 'anita', 'jaike', 'johan', 'claes', 'rob', 'correctie'], axis=1)

plt.figure()

ax = plotdf.plot()
ax.legend(bbox_to_anchor=(0.3, 0.5))

plt.savefig("../storage/pictures/plot.png")