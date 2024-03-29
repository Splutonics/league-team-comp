# not used, use api_get_all_champions.py instead

import json
from time import sleep
from random import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_all_champions(driver, url):
    if not driver:
        driver = webdriver.Chrome()
    driver.get(url)
    champ_list = driver.find_element(
        By.ID, 'drop-champions').get_attribute('innerHTML')

    # begin parsing and breaking down the html into desired subparts
    soup = BeautifulSoup(champ_list, features="html.parser")
    champs_html = soup.find_all('li')
    # print(champs_html)
    all_champions = []
    for champ in champs_html:
        try:
            all_champions.append(champ['data-name'].lower())
        except:
            pass

    return(all_champions)


if __name__ == '__main__':

    BASE_URL = 'https://www.leagueofgraphs.com/champions/counters'

    f = open('data/all_champs.json', 'w+')

    # instantiate driver
    # make sure to be runnining chromedriver.exe
    driver = webdriver.Chrome()

    c = get_all_champions(driver, BASE_URL)

    driver.quit()

    f.write(json.dumps(c))

    f.close()

    print(json.load(open('data/all_champs.json', 'r')))
