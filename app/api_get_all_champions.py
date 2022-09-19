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
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)

    # just dumps all the data to a json
    f = open('data/all_champions_info.json', 'w+')
    f.write(json.dumps(current_champ_list))
    f.close()

    # only dumps champ codenames to json
    f = open('data/all_champs.json', 'w+')
    f.write(json.dumps(list(current_champ_list['data'].keys())))
    f.close()

    # champ name conversion in order from fullname to codename (e.g. Cho'Gath to Chogath, Wukong to MonkeyKing)
    converter = dict()
    for champion in current_champ_list['data']:
        converter[current_champ_list['data'][champion]['name']] = champion

    f = open('data/champ_full_to_codename.json', 'w+')
    f.write(json.dumps(converter))
    f.close()

    # champ name conversion in order from id to codename (e.g. ## to Chogath)
    id_converter = dict()
    for champion in current_champ_list['data']:
        id_converter[current_champ_list['data'][champion]['key']] = champion

    f = open('data/champ_id_to_codename.json', 'w+')
    f.write(json.dumps(id_converter))
    f.close()

    # champ name conversion in order from codename to fullname (e.g. Chogath to Cho'Gath)
    converter2 = dict()
    for champion in current_champ_list['data']:
        converter2[champion] = current_champ_list['data'][champion]['name']

    f = open('data/champ_code_to_fullname.json', 'w+')
    f.write(json.dumps(converter2))
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
