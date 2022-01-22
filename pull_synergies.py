import time
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.leagueofgraphs.com/champions/counters'
champions = ['aatrox']
for champion in champions:
    champ_url = BASE_URL + '/' + champion
    print(champ_url)
    page = requests.get(champ_url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find_all(class_='data_table sortable_table')
    # time.sleep(1)


print(data)
# file = open('data/', 'w')
# # soup.
# file.write(str(soup))
# file.close()
# print(soup)


# listt = []
# textfile = open("data/roms_first_5_pages.txt", "w")
# for element in listt:
#     textfile.write(element + "\n")
# textfile.close()

# import webbrowser
# import time
# import random
# import asyncio
# from selenium import webdriver

# BASE_URL = "https://www.retrostic.com"


# def openning():
#     for rom in roms:
#         webbrowser.open_new_tab(BASE_URL + rom)
#         wait_time = random.random()/50
#         time.sleep(wait_time)


# driver = webdriver.Chrome()
# driver.get("https://www.retrostic.com/roms/snes/super-mario-kart-81982")
# button = driver.find_element_by_css_selector(
#     '.btn.btn-primary.w-100.m-1.romdownbtn')
# time.sleep(5)

# button.click()

# time.sleep(10)
# driver.quit()

# if __name__ == '__main__':
#     roms = []
#     rom_list = open("roms_first_5_pages.txt", "r")
#     for rom in rom_list:
#         roms.append(rom)
#         # print(rom)
#     rom_list.close()
#     # print(roms)
