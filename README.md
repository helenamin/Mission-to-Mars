# web-scraping-challenge
This project is about building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 


## Step 1 - Scraping
To create the scraping script, Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter are used. These are the items have been scraped:

* NASA Mars News - visit the [Mars News Site](https://redplanetscience.com) and collect the latest News Title and Paragraph Text.

* JPL Mars Space Images - visit [here](https://spaceimages-mars.com) and use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Mars Facts - visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Then convert the data to a HTML table string using panadas.

* Mars Hemispheres - visit the Astrogeology site [here](https://marshemispheres.com) to obtain full resolution images for each of Mar's hemispheres. 


## Step 2 - MongoDB and Flask Application
In order to display all of the information that was scraped from the URLs above, a new HTML page has been created using  MongoDB with Flask templating.

* Python script called `scrape_mars.py` created by converting codes inside Jupyter notebook and adding them inside a function called `scrape` that execute all of scraping code from above and return one Python dictionary containing all of the scraped data.

* Inside the 'app.py', a route created called `/scrape` that imports `scrape_mars.py` script and call `scrape` function and stores the return value in Mongo as Pyhton dictionary.

* Root route `/` in 'app.py' query Mongo database and pass the mars data into an HTML template to display the data.

* Finally a template HTML file created called `index.html` that takes the mars data dictionary and display all of the data in the appropriate HTML elements. The final product looks like below.

![final_app_part1.png](screenshots/final_app_part1.png)
![final_app_part2.png](screenshots/final_app_part2.png)