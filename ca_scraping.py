#Haiden Gembinski
#Scraping functionality for CryptoAlert

from bs4 import BeautifulSoup
import requests
import json

#get the price of the coin found at the url
def get_price(url):
    price = 0
    coinmarketcap = requests.get(url)
    soup = BeautifulSoup(coinmarketcap.content, 'html.parser')
    line = soup.find('div', {'class' : 'priceValue'}).text

    price = line[1:]

    try:
        test = float(price)

        if test <= 0:
            return ""
    except:
        return ""
    
    return price
