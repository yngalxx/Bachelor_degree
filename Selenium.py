#Necessary imports

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

#To be able to save data to csv file

import csv

#To operate in a Firefox brwoser

opts = Options()
browser = Firefox(options=opts)

#Open page

browser.get("http://quotes.toscrape.com/page/1/")

#Counter to change number of element in xpath 

count=1

#Loop (range is 10 because are only 10 quotes on one page)

for i in range(10):

    #Try and except (just in case XPath values changeing by counter isn't one by one)
    
    try:
        text = browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div["
                                             + str(count) + "]/span[1]").text

        author = browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div["
                                             + str(count) + "]/span[2]/small").text

       #Adding data to csv file
       
        with open('Quotes.csv', 'a') as fd:
            filewriter = csv.writer(fd, delimiter=',')
            filewriter.writerow([author, text])

    except:
        pass

    count+=1
