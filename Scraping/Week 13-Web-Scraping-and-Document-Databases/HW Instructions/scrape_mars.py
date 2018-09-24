# Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
import re

def scrape():
    
    # Set up splinter browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Create dictionary to store scraped Mars data
    mars_data = {}

    # NASA Mars news url to scrape
    url_mars_news = "https://mars.nasa.gov/news/"

    # Retrieve page with the requests module
    response = requests.get(url_mars_news)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    # Find content titles, store first title
    titles = soup.find_all('div', class_="content_title")
    news_title = titles[0].text.replace('\n', '')

    # Find content description, save first one
    teasers = soup.find_all('div', class_="rollover_description_inner")
    news_p = teasers[0].text.replace('\n', '')

    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p

    # Mars image url to scrape
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    # Save site's html as variable, use beautiful soup to parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find html with article tag using lambda function to search for style that begins with 'background-image'
    extracted_html = soup.find("article", {"style" : lambda L: L and L.startswith('background-image')})

    # Store the style as variable
    extracted_style = extracted_html.attrs['style']

    beg_url = 'https://www.jpl.nasa.gov'

    # Use regular expressions package to search for url

    try:
        found = re.search('url(.+?);', extracted_style).group(1)
    except AttributeError:
        found = ''

    # Create featured image url by combining two strings
    featured_image_url = beg_url + found[2:-2]

    mars_data["featured_image_url"] = featured_image_url


    # url of Mars twitter page
    twitter_url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response = requests.get(twitter_url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = bs(response.text, 'html.parser')

    # Save latest tweet text as string
    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    mars_data["mars_weather"] = mars_weather

    # Mars facts url
    facts_url = 'http://space-facts.com/mars/'

    # Retrieve page with the requests module
    response = requests.get(facts_url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    # Use pandas to read the table from html
    mars_facts = pd.read_html(facts_url)

    # Subset list to get table
    mars_df = mars_facts[0]

    # Name table columns
    mars_df.columns = ['Attribute', 'Value']

    # Convert table to html
    mars_html_table = mars_df.to_html()

    # Remove all html code for new lines
    mars_html_table.replace('\n', '')

    # Save as html table
    mars_info = mars_df.to_html('mars_html_table.html')

    mars_data["mars_table"] = mars_info

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_hemis = []

    for i in range (4):
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = bs(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back()

    mars_data['mars_hemis'] = mars_hemis


    # Return the dictionary
    return mars_data