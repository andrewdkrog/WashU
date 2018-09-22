# Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
import re

# URL to scrape
url = "https://mars.nasa.gov/news/"

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'html.parser')

print(soup.prettify())

# results are returned as an iterable list
titles = soup.find_all('div', class_="content_title")
teasers = soup.find_all('div', class_="rollover_description_inner")

news_title = titles[0].text
news_p = teasers[0].text

# Set up splinter browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Mars image url to scrape
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')

extracted_html = soup.find("article", {"style" : lambda L: L and L.startswith('background-image')})

extracted_style = extracted_html.attrs['style']

beg_url = 'https://www.jpl.nasa.gov'

import re

try:
    found = re.search('url(.+?);', extracted_style).group(1)
except AttributeError:
    found = '' # apply your error handling

# Create featured image url by combining two strings
featured_image_url = beg_url + found[2:-2]

print(featured_image_url)

# url of Mars twitter page
twitter_url = 'https://twitter.com/marswxreport?lang=en'

# Retrieve page with the requests module
response = requests.get(twitter_url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'html.parser')

print(soup.prettify())

# Save latest tweet text as string
mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

print(mars_weather)

# Mars facts url
url = 'http://space-facts.com/mars/'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'html.parser')

# Use pandas to read the table from html
mars_facts = pd.read_html(url)

print(mars_facts)

# Subset list to get table
mars_df = mars_facts[0]

# Name table columns
mars_df.columns = ['Attribute', 'Value']

# Convert table to html
mars_html_table = mars_df.to_html()

# Remove all html code for new lines
mars_html_table.replace('\n', '')

# Save as html table
mars_df.to_html('mars_html_table.html')


# #..Visit the USGS Astrogeology site to obtain hgih resolution images for 
# #....each of Mar's hemispheres
# usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# usgs_req = requests.get(usgs_url)

# #..You will need to click each of the links to the hemispheres in order 
# #....to find full res image
# soup = bs(usgs_req.text, "html.parser")
# hemi_attributes_list = soup.find_all('a', class_="item product-item")

# print(len(hemi_attributes_list))
# print(hemi_attributes_list[1]['href'])

#..Save both the image url string for the full resolution hemisphere image
#...., and the hemisphere title containing the hemisphere name name. Use
#.... a Python dictionary to store the data using keys img_url and title
# hemisphere_image_urls = []
# for hemi_img in hemi_attributes_list:
#     img_title = hemi_img.find('h3').text
#     #print(img_title)
#     link_to_img = "https://astrogeology.usgs.gov/" + hemi_img['href']
#     #print(link_to_img)
#     img_request = req.get(link_to_img)
#     soup = bs(img_request.text, 'lxml')
#     img_tag = soup.find('div', class_='downloads')
#     img_url = img_tag.find('a')['href']
#     hemisphere_image_urls.append({"Title": img_title, "Image_Url": img_url})

# print(hemisphere_image_urls)

#.. Append the dictionary with th eimage url string and the hemisphere
#.... title to a list. This list will contain one dictionary for each 
#.... hemisphere