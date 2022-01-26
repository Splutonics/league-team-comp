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

    main_content = driver.find_element(
        By.ID, "mainContent").get_attribute('innerHTML')

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


driver = webdriver.Chrome()
lookup_table = dict()
for champion in champions:
    lookup_table[champion] = []
    lookup_table[champion].append(champ_scrape(driver, champion))

driver.quit()


# print(champ_url)
# page = requests.get(champ_url)
# soup = BeautifulSoup(page.content, "html.parser")
# data = soup.find_all(class_='data_table sortable_table')
# time.sleep(1)

# driver.quit()

# print(data)
# file = open('data/', 'w')
# # soup.
# file.write(str(soup))
# file.close()
# print(soup)


# webbrowser.open_new_tab(BASE_URL)
# wait_time = random.random()/50
# time.sleep(wait_time)


# driver = webdriver.Chrome()
# driver.get(champ_url)

# # button = driver.find_element_by_css_selector(
# #     '.btn.btn-primary.w-100.m-1.romdownbtn')
# time.sleep(5)

# # button.click()

# # time.sleep(10)
# driver.quit()
if __name__ == '__main__':
    pass
