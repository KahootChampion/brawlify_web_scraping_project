import pandas as pd
import numpy as np

df = pd.read_excel('Power_League_Stats.xlsx', sheet_name='Power League Stats')
df['Count'] = np.zeros(len(df))
df = df.groupby(['Brawler'])['Count'].count()
df = df.sort_values(ascending=False)

with open('Power_League_Best_Brawlers.txt', 'w') as f:
    f.write('The number of times each brawler was used for any map in power league:\n\n')
    for name, times_used in df.items():
        string = f"{name}: {times_used}\n\n"
        f.write(string)

