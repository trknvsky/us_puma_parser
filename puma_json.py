import urllib.request
import requests
from urllib.parse import urlparse
from pprint import pprint
from bs4 import BeautifulSoup
from pprint import pprint
from decimal import Decimal
from puma_constants import *
from puma_choose import *

def get_html(url):
    response = requests.get(url, choose_category())
    contents = response.text
    soup = BeautifulSoup(contents, 'lxml')
    items_data = []
    products = soup.find_all('div', {'class': 'product-tile'})
    count = 0
    for product in products:
        item = {}
        d_none = product.find_all('div', {'class': 'd-none'})
        tile_body = product.find_all('div', {'class': 'product-tile-body'})
        for item_names in d_none:
            names = item_names.find_all('span', {'itemprop': 'name'})
            for name in names:
                item['name'] = name.contents[0]
                print(item)
        for values in tile_body:
            hrefs = values.find_all('a', {'class': 'product-tile-link link'})
            prices = values.find_all('span', {'class': 'sales'})
            for href in hrefs:
                item['href'] = 'https://us.puma.com{}'.format(href.get('href'))
            for price in prices:
                item['price'] = price.get('data-price-value')
                item['currency'] = price.get('data-price-currency')
                if price.get('data-price-value') != '':
                    if Decimal(price.get('data-price-value')) < 50.00:
                        count += 1
                        items_data.append(item)
    print(count)
    return items_data


def main():
    url = 'https://us.puma.com/on/demandware.store/Sites-NA-Site/en_US/Search-UpdateGrid'
    pprint(get_html(url))

if __name__ == '__main__':
    main()