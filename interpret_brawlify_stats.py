import pandas as pd
import numpy as np

df = pd.read_excel('Power_League_Stats.xlsx', sheet_name='Power League Stats')
df['Count'] = np.zeros(len(df))
best_brawlers = df.groupby(by=["Brawler"]).count()['Count']
best_brawlers = best_brawlers.sort_values(ascending=False)
best_brawlers_per_map = df.groupby(by=['Brawler', 'Map Type']).count()['Count']
print(best_brawlers_per_map)



with open('Power_League_Best_Brawlers.txt', 'w') as f:
     f.write('The number of times each brawler was used for any map in power league:\n\n')
     for name, times_used in best_brawlers.items():
         string = f"{name}: {times_used}\n\n"
         f.write(string)

with open('Power_League_Best_Brawlers_Per_Map.txt', 'w') as f:
    f.write('Per Brawler breakdown:\n\n')
    for name, times_used in best_brawlers_per_map.items():
        string = f"{name}: {times_used}\n\n"
        f.write(string)

