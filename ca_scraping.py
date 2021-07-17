#Haiden Gembinski
#Scraping functionality for CryptoAlert

from bs4 import BeautifulSoup
import requests

#get the price of the coin found at the url
def get_price():
    url = "https://coinmarketcap.com/currencies/binance-coin/"
    price = 0
    coinmarketcap = requests.get(url)
    soup = BeautifulSoup(coinmarketcap.content, 'html.parser')
    line = soup.find('div', {'priceValue___11gHJ'}).text

    price = float(line[1:])
    print(price)

get_price()
