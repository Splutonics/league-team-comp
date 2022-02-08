import json
import pandas as pd
import numpy as np

# TODO import synergies

all_champions = json.load(open('data/champ_data.json', 'r'))

# json comes in as strings, so these index as strings
wins_lane = str(0)
loses_lane = str(1)
best_with = str(2)
wins_more_against = str(3)
loses_more_against = str(4)

# champ = 0
# score = 1

# print(all_champions['Aatrox'][best_with])

synergies_df = pd.DataFrame(all_champions)
print(synergies_df.head())

# TODO calc synergies combinations
# ? 2 approaches, ONLY calculate pared champ list synergies (quicker upfront solve time, requires a re-solve for new summoner/changed champ lists)
# ? calculate every single combination synergy, then search/filter (longer upfront solve time, more storage required, quicker runtime lookup)
# ? i think the second option is more alluring

# TODO pare down possible champions for each summoner

# TODO each summoner now has a champ list


# if __name__ == '__main__':
#     print('q')
