#My import was like this
from C3BDWS.C3BDWS import PremierLeagueDataScraper

#List of URLs from which I want to scrape data
CSVlist = ['https://www.premierleague.com/stats/top/players/goals',
           'https://www.premierleague.com/stats/top/players/appearances',
           'https://www.premierleague.com/stats/top/players/mins_played',
           'https://www.premierleague.com/stats/top/players/goal_assist',
           'https://www.premierleague.com/stats/top/players/corner_taken',
           'https://www.premierleague.com/stats/top/players/total_cross',
           'https://www.premierleague.com/stats/top/players/total_through_ball',
           'https://www.premierleague.com/stats/top/players/total_pass',
           'https://www.premierleague.com/stats/top/players/touches',
           'https://www.premierleague.com/stats/top/players/total_offside',
           'https://www.premierleague.com/stats/top/players/att_freekick_goal',
           'https://www.premierleague.com/stats/top/players/att_pen_goal',
           'https://www.premierleague.com/stats/top/players/att_hd_goal',
           'https://www.premierleague.com/stats/top/players/hit_woodwork',
           'https://www.premierleague.com/stats/top/players/ontarget_scoring_att',
           'https://www.premierleague.com/stats/top/players/total_scoring_att',
           'https://www.premierleague.com/stats/top/players/aerial_won',
           'https://www.premierleague.com/stats/top/players/aerial_lost']

#Program will be working until latest element in a list
while len(CSVlist) > 0:

    try:
        #Take the first URL from the list
        URL = CSVlist[0]
        
        #This is in order to automate naming csv files depending on which data we are scraping. 
        #I separate inside of url on 'https://www.premierleague.com/stats/top/players/' and the ending. 
        #The ending is a name of csv file.
        CSV = CSVlist[0].partition("https://www.premierleague.com/stats/top/players/")[2]
        PremierLeagueDataScraper(URL, CSV)

    except:
        #When all data will be scraped, the first URL from a list is removing
        CSVlist.pop(0)
