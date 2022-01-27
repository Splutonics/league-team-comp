import time
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import random
import asyncio
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


BASE_URL = 'https://www.leagueofgraphs.com/champions/counters'
#change to CHAMPIONS
champions = ['aatrox']

# champions = ['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu']


def champ_scrape(driver, champion_name):
    if not driver:
        driver = webdriver.Chrome()
    champ_url = BASE_URL + '/' + champion_name
    driver.get(champ_url)
    time.sleep(2)

    # wait = WebDriverWait(driver, 5)
    # entire_page = wait.until(
    # EC.visibility_of_all_elements_located((By.ID, 'pageContent')))
    
    #extracts all the relevent html content
    main_content = driver.find_element(
        By.ID, "mainContent").get_attribute('innerHTML')

    #begin parsing and breaking down the html into desired subparts
    soup = BeautifulSoup(main_content, features="html.parser")
    data_tables = soup.find_all(class_="data_table sortable_table")

    wins_lane = 0
    loses_lane = 1
    best_with = 2
    wins_more_against = 3
    loses_more_against = 4

    champ_names = [table.find_all(class_="name") for table in data_tables]
    print(champ_names)
    # print(data_tables)
    # print(str(data_tables))
    return str(champion_name)






if __name__ == '__main__':
    #instantiate driver
    #make sure to be runnining chromedriver.exe
    driver = webdriver.Chrome()

    lookup_table = dict()
    #scrape info for each champs page and save to hash table
    for champion in champions:
        lookup_table[champion] = []
        lookup_table[champion].append(champ_scrape(driver, champion))

    driver.quit()
