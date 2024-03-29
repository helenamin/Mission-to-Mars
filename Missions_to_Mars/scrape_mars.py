# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



def scrape():


    #Part 1 -  Scrape NASA Mars News

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of Mars News Site page to be scraped
    url_1 = 'https://redplanetscience.com/'

    #Browse Mars News Site page
    browser.visit(url_1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # scrape news title
    news_title = soup.find_all('div', class_="content_title")[0].text

    # scrape news paragraph
    news_p = soup.find_all('div', class_="article_teaser_body")[0].text

    #close the browser
    browser.quit()


    # Part 2 - Scrape JPL Mars Space Images - Featured Image

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)    

    # URL of spaceimages-mars page to be scraped
    url_2 = 'https://spaceimages-mars.com/'

    #Browse spaceimages-mars page
    browser.visit(url_2)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the src for the current Featured Mars  image
    # relative_image_path = soup.find_all('img',class_='headerimage')[0]["src"]
    relative_image_path = soup.find_all('a',class_='showimg')[0]["href"]
    featured_image_url = url_2 + relative_image_path

    #close the browser
    browser.quit()


    #Part 3 - Scrape Mars Facts

    url_3 = "https://galaxyfacts-mars.com/"

    tables = pd.read_html(url_3)

    df = tables[0]

    #grab the first row for the header
    new_header = df.iloc[0] 
    #take the data less the header row
    df = df[1:]
    #set the header row as the df header
    df.columns = new_header 

    # set the index to the `Mars - Earth Comparison` column
    df.set_index('Mars - Earth Comparison', inplace=True)

    #Generate HTML tables string from DataFrame
    html_table = df.to_html()
    
    #strip unwanted newlines to clean up the table
    html_table = html_table.replace('\n', '')


    # Part 4 - Scrape Mars Hemispheres

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url_4 = 'https://marshemispheres.com/'
    browser.visit(url_4)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('div', class_='item')

    #Define lists for image links and titles
    img_urls = []
    titles = []
    i=0

    #Scrabe image links and titles
    for item in items:
        
        
        browser.find_by_css('a.itemLink h3')[i].click()
    
        img_url = browser.find_link_by_text("Sample").first['href']
        img_urls.append(img_url)
        
        browser.back()
        
        title = item.find('h3').text
        title_text = title.split('E')[0]
        titles.append(title_text)
    
        i=i+1

    #close the browser
    browser.quit()

    

    # Create hemisphere_image_urls objet which is a list of dictionaries 
    hemispheres =[]
    hemispheres = [{'title': title, 'img_url': img_url} for title,img_url in zip(titles,img_urls)]


    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "hemispheres": hemispheres
    }

    # Return results
    return mars_data

