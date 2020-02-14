import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("kandidaten.csv")

# Drop seizoen 1-4 (weinig data), 20 huidig
df = df[df.seizoen != 1]
df = df[df.seizoen != 2]
df = df[df.seizoen != 3]
df = df[df.seizoen != 4]
df_huidig = df[df.seizoen == 20]
df = df[df.seizoen != 20]

# Voeg kolommen toe
df_huidig['leeftijd'] = df_huidig.apply(lambda row: row.seizoen + 2000 - row.geboortejaar, axis=1)
df['leeftijd'] = df.apply(lambda row: row.seizoen + 2000 - row.geboortejaar, axis=1)
df['mannelijkheid'] = df.apply(lambda row: 1 if row.geslacht == 'M' else 0, axis=1)
df['mol'] = df.apply(lambda row: row.uitkomst == 0, axis=1)

print(df_huidig)

# Maak subsets
mollen = df[df.uitkomst == 0]
kandidaten = df[df.uitkomst != 0]

finalisten = df[(df.uitkomst != 0) & (df.uitkomst <= 2)]
afgevallenen = df[df.uitkomst > 2]
vroeg_afgevallenen = df[df.uitkomst > 6]


def print_descriptives(name: str, column):
    print('{:<20}: mean={:.2f}, std={:.2f}, sem={:.2f}'.format(name, column.mean(), column.std(), column.sem()))


# Gemiddelde leeftijd mol vs gemiddelde leeftijd kandidaat
print('\n<< Gemiddelde leeftijd >>')
print_descriptives('Mol', mollen['leeftijd'])
print_descriptives('Kandidaat', kandidaten['leeftijd'])
print_descriptives('Finalist', finalisten['leeftijd'])
print_descriptives('Afgevallenen', afgevallenen['leeftijd'])
print_descriptives('Vroeg afgevallenen', vroeg_afgevallenen['leeftijd'])

# Man vs Vrouw voor mol en kandidaat
print('\n<< Gemiddelde mannelijkheid >>')
print_descriptives('Mol', mollen['mannelijkheid'])
print_descriptives('Kandidaat', kandidaten['mannelijkheid'])
print_descriptives('Finalist', finalisten['mannelijkheid'])
print_descriptives('Afgevallenen', afgevallenen['mannelijkheid'])
print_descriptives('Vroeg afgevallenen', vroeg_afgevallenen['mannelijkheid'])

print('\n<< Verwachting mol >>')
min_leeftijd = mollen['leeftijd'].mean()-mollen['leeftijd'].std()
max_leeftijd = mollen['leeftijd'].mean()+mollen['leeftijd'].std()
df_verdenkingen = df_huidig[df_huidig['leeftijd'] > min_leeftijd]
df_verdenkingen = df_verdenkingen[df_verdenkingen['leeftijd'] < max_leeftijd]
print('Leeftijd tussen de {:.1f} en {:.1f}'.format(min_leeftijd, max_leeftijd))

print(df_verdenkingen)

sns.set()

sns.regplot(x='seizoen', y='leeftijd', data=df, x_estimator=np.mean)
plt.savefig("figures/leeftijd_iedereen.png")
plt.clf()
sns.regplot(x='seizoen', y='leeftijd', data=mollen)
plt.savefig("figures/leeftijd_mollen.png")
plt.clf()
sns.swarmplot(x='seizoen', y='leeftijd', hue='mol', data=df)
plt.savefig("figures/leeftijd.png")
plt.clf()
