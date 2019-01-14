from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

#NOTE: you must download the chromedriver and place it in the 'usr/bin' folder
#address to download: https://sites.google.com/a/chromium.org/chromedriver/downloads

df = pd.read_csv('individual_urls.csv')

listy = df['colummn'].tolist()

def scraper(lst, start, stop):
    listings = []
    for i in lst[start:stop]:

        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(i)

        try:
            xpath_wine = r'//*[@id="review"]/div[1]/div[1]'
            wine = driver.find_element_by_xpath(xpath_wine).text
        except (NoSuchElementException, ValueError):
            wine = 'n/a'
        
        try:
            xpath_review = r'//*[@id="review"]/div[2]/div[3]/p'
            review = driver.find_element_by_xpath(xpath_review).text
        except (NoSuchElementException, ValueError):
            review = 'n/a'
            
        try:
            xpath_points = r'//*[@id="points"]'
            points = int(driver.find_element_by_xpath(xpath_points).text)
        except (NoSuchElementException, ValueError):
            review = 'n/a'
            
        try:
            xpath_price = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[1]/li[1]/div[2]/span/span'
            price = driver.find_element_by_xpath(xpath_price).text
        except (NoSuchElementException, ValueError):
            price = 'n/a'

        try:
            xpath_variety = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[1]/li[3]/div[2]/span/a'
            variety = driver.find_element_by_xpath(xpath_variety).text
        except (NoSuchElementException, ValueError):
            variety = 'n/a'

        try:
            xpath_appellation = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[1]/li[4]/div[2]'
            appellation = driver.find_element_by_xpath(xpath_appellation).text
        except (NoSuchElementException, ValueError):
            appellation = 'n/a'

        xpath_winery4 = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[1]/li[4]/div[2]/span/span/a'
        xpath_winery5 = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[1]/li[5]/div[2]/span/span/a'
        try:
            winery = driver.find_element_by_xpath(xpath_winery4).text
        except (NoSuchElementException, ValueError):
            try:
                winery = driver.find_element_by_xpath(xpath_winery5).text
            except (NoSuchElementException, ValueError):
                winery = 'n/a'

        try:
            xpath_alcohol = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[2]/li[1]/div[2]/span/span'
            alcohol = driver.find_element_by_xpath(xpath_alcohol).text
        except (NoSuchElementException, ValueError):
            alcohol = 'n/a'

        try:
            xpath_bottlesize = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[2]/li[2]/div[2]/span/span'
            bottlesize = driver.find_element_by_xpath(xpath_bottlesize).text
        except (NoSuchElementException, ValueError):
            bottlesize = 'n/a'
        
        try:
            xpath_category = r'//*[@id="review"]/div[2]/div[3]/div[2]/div[1]/ul[2]/li[3]/div[2]/span/span'
            category = driver.find_element_by_xpath(xpath_category).text
        except (NoSuchElementException, ValueError):
            category = 'n/a'

        keys = ['Wine', 'Review', 'Points', 'Price', 'Variety', 'Appellation',  'Winery', 'Alcohol', 'Bottlesize', 'Category', 'Url']
        values = [wine, review, points, price, variety, appellation, winery, alcohol, bottlesize, category, i]
        listings.append(dict(zip(keys, values)))

        driver.close()
    return listings
