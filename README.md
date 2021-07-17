# Bachelor_degree
Codes of scrapers from my Bachelor thesis

## Files:
First_Steps_In_BS4.py, Selenium.py and Scrapy.py are only to present basics of those methods. 

## Main part
Main part of my BA thesis is PremierLeagueDataScraper which scrapes data from premierleague.com/stats about appearances of forwards in English Premier League in current season (In my case it was 2019/20). I created this scraper in order to collect data to subsequent analysis to find the most universal attacker in the league. It's an example of using web scraping in football scouting process. To open web scraper You have to run Initialize_PremierLeagueDataScraper.py.

### DataCleaner.py
Merging lots of csv files containing scraped data to one, cleaning scraped data etc.

## Addition (files: sofifaScraper.py & sofifaCleaner.py):
I also wanted to have age of players, so I had to build another scraper (from sofifa.com) and another data cleaner to get and clean it. I took a list of players names (in another csv) from my first scraped data and I used search field to find all of them on Sofifa page and scraped their age. 
