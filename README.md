<h1>Chance Murphy 507 Project 4</h1>
<p>
This is a scraping program. This code will scrape information from the website url https://www.nps.gov/ to give the user information on every national site in the United States of America. In order to do this, the program will first scrape information from the main page to get the URLs for each individual state. Once these URLs have been aquired, the content of these URLs will be cached in a JSON so that requests are only made to the website if information needs to be updated or added.

With the individual state URLs now cached, we wil grab the required informaion from each page (State, site location, site name, site type, and a breif description) and store it in a list for each peice of information. Once the lists are gathered, pandas is used to create a table of information and then that table is written to a CSV file using to.csv function of pandas.
<br><br>
Everything needed to successfully run this program is included in the SI507_project4.py and advanced_expiry_caching.py files included in this repository. You will need to download both files and place them in the same folder. To run the program, navigate to the folder they are located in in your terminal window and type "python SI507_project4.py".
<br><br>
<h2>Grade:</h2>
<h3>1000/1000</h3>
I have successfully scraped the pages for the required data and also scraped the data for the state that each national site is located, which was an optional challenge.
</p>
