import pickle
import pprint
from time import sleep
from random import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from get_all_champions import get_all_champions

BASE_URL = 'https://www.leagueofgraphs.com/champions/counters'


def champ_scrape(driver, champion_name):
    if not driver:
        driver = webdriver.Chrome()
    champ_url = BASE_URL + '/' + champion_name
    driver.get(champ_url)
    # time.sleep(2)

    # wait = WebDriverWait(driver, 5)
    # entire_page = wait.until(
    # EC.visibility_of_all_elements_located((By.ID, 'pageContent')))

    # extracts all the relevent html content
    main_content = driver.find_element(
        By.ID, "mainContent").get_attribute('innerHTML')

    # begin parsing and breaking down the html into desired subparts
    soup = BeautifulSoup(main_content, features="html.parser")
    data_tables = soup.find_all(class_="data_table sortable_table")
    print(data_tables)

    champ_hash = dict()
    for idx, table in enumerate(data_tables):
        champ_names_html = table.find_all(class_="name")
        champ_names = [champ.string for champ in champ_names_html]

        champ_values_html = table.find_all(class_="progressBarTxt")
        champ_values = [champ.string for champ in champ_values_html]

        champ_hash[idx] = list(zip(champ_names, champ_values))

    return champ_hash


if __name__ == '__main__':

    # instantiate driver
    # make sure to be runnining chromedriver.exe
    driver = webdriver.Chrome()

    # this variable should be received from the riot API _OR_ scraped from the base_url
    all_champions = ['aatrox']
    # all_champions = pickle.load(open('data/all_champs.pkl', 'rb')

    # all_champions = ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu']

    wins_lane = 0
    loses_lane = 1
    best_with = 2
    wins_more_against = 3
    loses_more_against = 4

    lookup_table = dict()
    time_log = []
    # scrape info for each champs page and save to hash table
    for champion in all_champions:
        lookup_table[champion] = champ_scrape(driver, champion)

        # add random time to avoid over querying the website (log it as well)
        rand_time = 2*random.random()
        time_log.append(rand_time)
        sleep(rand_time)

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(lookup_table)
    print("Time spent sleeping: ", sum(time_log))
    driver.quit()
