import os
from dotenv import load_dotenv
from riotwatcher import LolWatcher, ApiError
import json
import pprint


def lookup_summoner(name: str, min_level: int):

    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    lol_watcher = LolWatcher(API_KEY, default_status_v4=True)

    my_region = 'na1'

    id_to_codename = json.load(open('data/champ_id_to_codename.json', 'r'))

    try:

        player_all_info = lol_watcher.summoner.by_name(my_region, name)
        player_id = player_all_info['id']
        player_mastery = lol_watcher.champion_mastery.by_summoner(
            my_region, player_id)

        summoner_champs = []

        for champ in player_mastery:
            if champ['championLevel'] >= min_level:
                champ_codename = id_to_codename[str(champ['championId'])]
                summoner_champs.append(champ_codename)

        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(summoner_champs)

        return summoner_champs

    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(
                err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise

        return None


if __name__ == '__main__':

    lookup_summoner('hastalapasta0', 5)
