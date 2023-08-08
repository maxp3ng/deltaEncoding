# Max Peng 2023
# Delta Encoding
# Trends Minnow

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup as bs
from pytrends.request import TrendReq
import random






def getRandomTopCompanyTrends():
    # Using BS webscraper to grab list of top 100 companies in US by revenue

    keywords = []

    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    headers = {'User-Agent': 'maxPengResearchEncoder/Minnow (https://waut.dev; waut@waut.dev)'}

    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    for row in table.findAll('tr')[1:]:
        company = row.findAll('td')[1].text
        keywords.append(company[:-1])

    #choose random company
    randomIndex = random.randint(0,len(keywords)-1)
    payload = [keywords[randomIndex]]

    #pytrends setup

    pytrends = TrendReq(hl='en-US', tz=360)

    # time_range = '2023-07-01 2023-08-01'
    time_range = 'today 5-y'

    pytrends.build_payload(
        kw_list=payload,
        cat=0,
        timeframe=time_range,
        geo='',
        gprop=''
    )

    data = pytrends.interest_over_time()

    return data


