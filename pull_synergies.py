import json
import pprint
from time import sleep
from random import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# add ELO functionality, aka pulls synergies for silver, or gold, etc...

BASE_URL = 'https://www.leagueofgraphs.com/champions/counters'


def champ_scrape(driver, champion_name):
    if not driver:
        driver = webdriver.Chrome()
    champ_url = BASE_URL + '/' + champion_name
    driver.get(champ_url)

    # extracts all the relevent html content
    main_content = driver.find_element(
        By.ID, "mainContent").get_attribute('innerHTML')

    # begin parsing and breaking down the html into desired subparts
    soup = BeautifulSoup(main_content, features="html.parser")
    data_tables = soup.find_all(class_="data_table sortable_table")
    # print(data_tables)

    champ_hash = dict()
    for idx, table in enumerate(data_tables):
        champ_names_html = table.find_all(class_="name")
        champ_names = [champ.string for champ in champ_names_html]

        # ! Fix this to include all hidden elements as well, currently only grabs shown elements
        champ_values_html = table.find_all(class_="progressBarTxt")
        champ_values = [champ.string for champ in champ_values_html]

        champ_hash[idx] = list(zip(champ_names, champ_values))

    return champ_hash


if __name__ == '__main__':

    # instantiate driver
    # make sure to be runnining chromedriver.exe
    driver = webdriver.Chrome()

    # this variable should be received from the riot API _OR_ scraped from the base_url
    # issues when scraped for base_url, consider scrape from API
    # all_champions = ['aatrox', 'ahri']
    all_champions = json.load(open('data/all_champs.json', 'r'))

    # wins_lane = 0
    # loses_lane = 1
    # best_with = 2
    # wins_more_against = 3
    # loses_more_against = 4

    lookup_table = dict()
    time_log = []

    # scrape info for each champs page and save to hash table
    # currently, has issues with names with a space (e.g. tahm kench) or a apostrophe (e.g. kha'zix)
    for champion in all_champions:
        lookup_table[champion] = champ_scrape(driver, champion.lower())

        # add random time to avoid over querying the website (log it as well)
        rand_time = 0.5*random()
        time_log.append(rand_time)
        sleep(rand_time)

    driver.quit()

    f = open('data/champ_data.json', 'w+')

    c = lookup_table

    f.write(json.dumps(c))

    f.close()

    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(json.load(open('data/champ_data.json', 'r')))
    print("Time spent sleeping: ", sum(time_log))
