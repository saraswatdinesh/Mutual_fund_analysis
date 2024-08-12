# Import libraries.
import requests
import re
import time  # Import the time module
from urllib.request import urlopen
import urllib.request 
import urllib.parse
import urllib.error
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
import random
import pandas as pd



class webScrapper:
    def __init__(self):
        # initialize the ssl connection request
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'
            'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
            ]

    def scrape_link(self, link):
        # Function to call the url and extract the webpage and return an html object stored in a variable
        usr_agent = random.choice(self.user_agents)
        url = link

        try:
            req = Request(url,headers={'User-Agent':usr_agent})
            webpage = urlopen(req, context = self.ctx).read()
            soup = BS(webpage,'html.parser')
            return soup
        except Exception as e:
            print("An error has occurred :", str(e))
            print("This is the user agent used", usr_agent)
    

class YahooFinanceData:
    def __init__(self,soup):
        self.soup = soup
    
    def parse_table(self):
        table_rows = self.soup.find_all("tr",{"class":"yf-ewueuo"})
        data = {
            'dates':[],
            'open_price':[],
            'high_price':[],
            'low_price':[],
            'close_price':[],
            'volume':[]
        }

        for row in table_rows:
            items = row.find_all("td",{"class":"yf-ewueuo"})
            if len(items)!=0:
                try:
                    data['dates'].append(items[0].text)
                    data['open_price'].append(float(items[1].text.replace(',', '')))
                    data['high_price'].append(float(items[2].text.replace(',', '')))
                    data['low_price'].append(float(items[3].text.replace(',', '')))
                    data['close_price'].append(float(items[4].text.replace(',', '')))
                    data['volume'].append(float(items[6].text.replace(',', '').replace('-','0')))
                except ValueError as e:
                    print(f"Value Error :{e} in row : {items}")
        return pd.DataFrame(data)
    
    # define the function to calculate the returns fields 

    def monthly_returns(self, data):
        data['dates']= pd.to_datetime(data['dates'], errors = 'coerce')
        data['return'] = ((data['close_price'] - data['open_price'])/data['open_price'])*100
        return data[['dates','return']]


def main():
    url = "https://finance.yahoo.com/quote/%5EBSESN/history/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACAmBcx-zko10K-Q2XBcMk35C4KO6GkkqcoC3RP9v5ra2qcxOjr3IgUNfBhsUgCIC9aN2SLvgRCOQEl3VI9JlDI0e8_iYjWus2rap9plE8WGKcs80R9mrQuIweJQ_Z5TNroINNblLN_EDWo0TaNbuKZKgpoIbzoKkAEWxFzxGtnQ&period1=867728700&period2=1722457285&frequency=1mo"
    scrapper = webScrapper()
    soup = scrapper.scrape_link(url)

    if soup:
        parser = YahooFinanceData(soup)
        data = parser.parse_table() 

        # Calculate the returns 

        returns_data = parser.monthly_returns(data)
        print(returns_data)
    
    else:
        print("Failed to retrive or parse the data ")


if __name__ == "__main__":
    main()




