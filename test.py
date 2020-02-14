import pickle
import pandas as pd

df = pd.read_pickle('resultuptoseason18.pkl')
df.to_csv('test.csv')
