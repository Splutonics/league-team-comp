import api_get_all_champions
import pull_synergies

if __name__ == '__main__':
    # reads the RIOT API, pulls champion data, converts and saves to JSON for use in other modules
    exec(api_get_all_champions)
    # scrapes champion synergies/counters from leagueofgraphs
    exec(pull_synergies)
