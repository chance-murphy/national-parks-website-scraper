import requests, json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
import pandas as pd
import csv

# "crawling" -- generally -- going to all links from a link ... like a spiderweb
# its specific def'n varies, but this is approximately the case in all situations
# and is like what you may want to do in many cases when scraping

######

# A "simple" example (without much fancy functionality or data processing)

# Constants
START_URL = "https://www.nps.gov/"
FILENAME = "national_sites.json"

# So I can use 1 (one) instance of the Cache tool -- just one for my whole program, even though I'll get data from multiple places
PROGRAM_CACHE = Cache(FILENAME)

# assuming constants exist as such
# use a tool to build functionality here
def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data) # default here with the Cache.set tool is that it will expire in 7 days, which is probs fine, but something to explore
    return data

#######

main_page = access_page_data(START_URL)

# explore... find that there's a <ul> with class 'topics' and I want the links at each list item...

# I've cached this so I can do work on it a bunch
main_soup = BeautifulSoup(main_page, features="html.parser")
# print(main_soup.prettify())

dropdown_list = main_soup.find('ul',{'class':'dropdown-menu SearchBar-keywordSearch'})
# print(dropdown_list) # cool

# for each list item in the unordered list, I want to capture -- and CACHE so I only get it 1 time this week --
# the data at each URL in the list...
states_links = dropdown_list.find_all('a')
# print(states_links) # cool


# Get a list of possible locations for later
# site_states = []
# for i in states_links[:1]:
#     state = i.text
#     site_states.append(state)

# print(site_locations)
# Debugging/thinking code:
# #
# for i in states_links:
#     print(i['href'])

# Just text! I'm not going back to the internet at all anymore since I cached the main page the first time

# This is stuff ^ I'd eventually clean up, but probably not at first as I work through this problem.

states_pages = [] # gotta get all the data in BeautifulSoup objects to work with...
site_states = []
site_names = []
site_types = []
site_descriptions = []
site_locations = []
for i in states_links:
    page_data = access_page_data(START_URL + i['href'])
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    # print(soup_of_page.prettify())
    states_pages.append(soup_of_page)

# print(states_pages[0].prettify())

for state in states_pages:

    site_state = state.find("h1", class_ = "page-title")
    parks_list = state.find_all("div", class_ = "col-md-9 col-sm-9 col-xs-12 table-cell list_left")

    #Get the states
    for i in parks_list:
        site_states.append(site_state.text)

    #Get name of each site
    for i in parks_list:
        name = i.h3.text
        if name == '':
            name = 'N/A'
        site_names.append(name)

    #Type of each site
    for i in parks_list:
        type = i.h2.text
        if type == '':
            type = 'N/A'
        site_types.append(type)

    #Get Description of each site
    for i in parks_list:
        description = i.p.text
        if description == '':
            description = 'N/A'
        site_descriptions.append(description)

    #Get location of each site
    for i in parks_list:
        location = i.h4.text
        if location == '':
            location = 'N/A'
        site_locations.append(location)

# print(site_states)
# print(site_names)
# print(site_types)
# print(site_descriptions)
# print(site_locations)

# print(len(site_states))
# print(len(site_names))
# print(len(site_types))
# print(len(site_descriptions))
# print(len(site_locations))

site_info = pd.DataFrame({'State': site_states,
                       'Location': site_locations,
                       'Name': site_names,
                       'Type': site_types,
                       'Description': site_descriptions,
})

# print(site_info.info())


csv_file_name = "national_sites.csv"

site_info.to_csv(csv_file_name)

##################
# START IGNORING #
##################


    # #Location of each site
    # site_location = []
    # for i in parks_list:
    #     location = i.h4.text
    #     site_location.append(location)
    # # print(site_location)
