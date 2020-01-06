#Imports
import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook

#Using Request library to get a source code of a site
page = requests.get("http://quotes.toscrape.com/page/1/")

#Creating BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#Parsing
html = list(soup.children)[2]
body = list(html.children)[3]

#Creating Excel file
wb = Workbook()
sheet1 = wb.add_sheet('Quotes')
style = xlwt.easyxf('font: bold 1')
sheet1.write(0,0, "Author", style)
sheet1.write(0,1, "Quote", style)

#Scraping and saving data in Excel file
count=1
for quote in body.find_all(class_="quote"):

    author = quote.find(class_="author").text
    text = quote.find(class_="text").text

    sheet1.write(count, 0, author)
    sheet1.write(count, 1, text)

    count+=1

#Save Excel file
wb.save('Quotes.xls')
