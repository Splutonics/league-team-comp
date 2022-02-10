from operator import index
import pandas as pd
import numpy as np
import json
import random
from itertools import permutations

from lookup_summoner import *
from helper.uprod import *

import time


# TODO import synergies


def create_synergy_dataframe(*summoners: str, min_level: int):

    if len(summoners) != 5:
        raise Exception('Not enough summoners entered')

    try:
        champs_1 = lookup_summoner(summoners[0], min_level=min_level)
        champs_2 = lookup_summoner(summoners[1], min_level=min_level)
        champs_3 = lookup_summoner(summoners[2], min_level=min_level)
        champs_4 = lookup_summoner(summoners[3], min_level=min_level)
        champs_5 = lookup_summoner(summoners[4], min_level=min_level)
        print(champs_1)
        print(champs_2)
        print(champs_3)
        print(champs_4)
        print(champs_5)
    except:
        raise Exception('Error during summoner lookup')

    # start timer after summoner lookup
    start_time = time.time()

    imported_data_df = pd.read_json('data/champ_data.json')

    # indices
    wins_lane = 0
    loses_lane = 1
    best_with = 2
    wins_more_against = 3
    loses_more_against = 4

    # transposes df, pulls only "best with" column, expands it so every synergy is one row
    temp = imported_data_df.T[best_with].explode().to_frame(
    ).reset_index().rename(columns={'index': 'champion'})
    # TODO: either add this as necessary too all var's
    del imported_data_df

    # splits the synergy data and other champion name into discrete columns
    # ?: this only works for current form of pulled data, may break if data looks different
    temp2 = temp.join(pd.DataFrame(temp[best_with].to_list(), columns=[
        'other_champion', 'synergy'])).drop(best_with, axis=1)
    # turns the percentage string into a float
    temp2['synergy'] = temp2['synergy'].str.rstrip('%').astype('float')/100.0
    # TODO
    del temp

    # ensure all names are codenames
    convert = json.load(open('data/champ_full_to_codename.json', 'r'))
    synergy_df = temp2.copy()
    # TODO Figure out a way to get rid of this annoying warning
    for i in range(len(temp2)):
        synergy_df['other_champion'][i] = convert[temp2['other_champion'].iloc[i]]
    # TODO
    # del convert, temp2

    # // only useful for seeding
    # // all_champs = json.load(open('data/all_champs.json', 'r'))
    # // random.seed(43)
    # // champs_1 = random.choices(all_champs,k=10)
    # // champs_2 = random.choices(all_champs,k=10)
    # // champs_3 = random.choices(all_champs,k=10)
    # // champs_4 = random.choices(all_champs,k=10)
    # // champs_5 = random.choices(all_champs,k=10)
    #// #
    # // del all_champs

    pared_champs_combos = list(uprod(
        champs_1, champs_2, champs_3, champs_4, champs_5))

    print("Approximate runtime: ", len(
        pared_champs_combos)*90/10000, " seconds")
    # print(len(pared_champs_combos))

    all_combo_scores = pd.DataFrame()
    all_combo_scores['champs'] = None
    all_combo_scores['scores'] = None
    all_combo_scores['total_score'] = None
    idx = 0
    for combo in pared_champs_combos:

        # ? currently ~80-90 seconds per 10000 combos
        # // make sure to delete in production
        # // if idx == 100:
        # //     break
        # if idx == 100:
        #     break

        scores = list()
        for champ1, champ2 in permutations(combo, 2):
            try:
                # lookup the synergy from champ1 to champ2
                synergy_score = synergy_df.loc[(synergy_df.champion == champ1) & (
                    synergy_df.other_champion == champ2)]['synergy'].iloc[0]
                scores.append(synergy_score)
            except:
                continue
        idx += 1

        # add the champ combo, score, and score sum to the dataframe
        all_combo_scores = all_combo_scores.append(
            {'champs': combo, 'scores': scores, 'total_score': sum(scores)}, ignore_index=True)

    # sort by highest score
    all_combo_scores.sort_values('total_score', inplace=True, ascending=False)

    # # created a list of column names champ0 - champ4
    cols = [''.join(['champ', str(i)]) for i in range(5)]

    all_combo_scores = all_combo_scores.join(pd.DataFrame(
        all_combo_scores['champs'].to_list(), columns=cols)).drop('champs', axis=1)

    print("Actual Runtime: %s seconds" % (time.time() - start_time))
    return all_combo_scores


if __name__ == '__main__':
    champs = ['hastalapasta0', 'thorthepriest',
              'chanchachan', 'shmoff', 'armadakt']

    # #testing error
    # create_synergy_dataframe('hastalapasta0', min_level=5)

    create_synergy_dataframe(
        *champs, min_level=6).to_csv('data/scores.csv', index=False)
    print('Successfully exported to data/scores.csv')
