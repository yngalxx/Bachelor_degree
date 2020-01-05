def PremierLeagueDataScraper(URL, CSV):

    # These 2 imports are necessary to use selenium
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options

    # Package "time" is using to sleep scraper
    import time

    # to be able to save scraped data to csv file
    import csv

    # To be able to launch and operate on firefox
    opts = Options()
    browser = Firefox(options=opts)

    # Maximal page load time
    browser.set_page_load_timeout(100)

    # Page has few sec to load, then window will be closed
    try:
        browser.get(URL)

    except Exception as e:
        print(getattr(e, 'message', str(e)))
        browser.close()
        quit()

    # Maximize window
    browser.maximize_window()

    # Sleep for a while (0.5 sec)
    time.sleep(2)

    # Scroll down
    browser.execute_script("window.scrollBy(0, 320)")

    # Accept cookies
    browser.find_element_by_xpath(
        '/html/body/section/div/div').click()

    # Click on list position
    browser.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[2]/div[1]/section/div[4]/div[2]').click()

    # Click forward position
    browser.find_element_by_xpath(
        '/html/body/main/div[2]/div/div[2]/div[1]/section/div[4]/ul/li[5]').click()

    # Sleep for a while
    time.sleep(2)

    # Counter
    count = 0

    # Loop to scrape data
    while(True):

        count+=1

        # Try scrape
        try:

            # Sometimes in Xpath the last part of path is 'strong'
            try:
                player = browser.find_element_by_xpath(
                    '/html/body/main/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr['
                    + str(count)+ ']/td[2]/a/strong').text

            # And sometimes is not 'strong' but only 'a'
            except Exception as e:
                player = browser.find_element_by_xpath(
                    '/html/body/main/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr['
                    + str(count)+ ']/td[2]/a').text

            stat = browser.find_element_by_xpath(
                '/html/body/main/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr['
                + str(count)+ ']/td[5]').text

            # Add scraped values to csv
            with open(CSV + '.csv', 'a') as fd:
                filewriter = csv.writer(fd, delimiter=',')
                filewriter.writerow([player, stat])

            # Scroll down
            browser.execute_script("window.scrollBy(0, 45)")

            if count == 20:

                browser.find_element_by_xpath(
                    '/html/body/main/div[2]/div/div[2]/div[1]/div[3]/div[2]').click()
                count = 0

                browser.execute_script("window.scrollBy(0, -1100)")

                time.sleep(2)


        # Except when something is wrong with scraping
        except Exception as e:
            print(getattr(e, 'message', str(e)))
            browser.close()
            browser.quit()

