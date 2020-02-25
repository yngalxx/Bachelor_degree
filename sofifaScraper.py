from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time

opts = Options()
browser = Firefox(options=opts)

browser.get('https://sofifa.com')

search_player_field = browser.find_element_by_name("keyword")

names = pd.read_csv('path to csv with only players names')
names['Age'] = ""


for row in names.index:
    search_player_field.send_keys(names['Player'][row])
    search_player_field.submit()
    time.sleep(1)

    try:
        age = browser.find_element_by_css_selector(
            '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)'
        ).text

    except:
        age = 'lack'

    print(names['Player'][row], age)
    names.loc[row, 'Age'] = age
    #print(names)
    search_player_field.clear()
    time.sleep(1)

names.to_csv('/Users/alexdrozdz/PycharmProjects/doLicka/wiek_zawodnikow.csv')
