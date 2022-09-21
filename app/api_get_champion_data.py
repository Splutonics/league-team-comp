import os
from dotenv import load_dotenv
from riotwatcher import LolWatcher, ApiError
import json
import pprint


load_dotenv()
API_KEY = os.getenv('API_KEY')

lol_watcher = LolWatcher(API_KEY, default_status_v4=True)

my_region = 'na1'

try:

    # First we get the latest version of the game from data dragon
    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']

    # Lets get some champions
    all_champ_info = lol_watcher.data_dragon.champions(champions_version,full=True)

    # dumps ALL champion data into a json, keys are champion codenames
    f = open('data/all_champions_info.json', 'w+')
    f.write(json.dumps(all_champ_info['data']))
    f.close()

    # dumps only champ codenames to json
    f = open('data/all_champs.json', 'w+')
    f.write(json.dumps(list(all_champ_info['data'].keys())))
    f.close()

    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(json.load(open('data/all_champions_from_API.json', 'r')))
    # pp.pprint(json.load(open('data/all_champs.json', 'r')))

# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an
# invalid summoner name, match ID, etc.
#
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").


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
