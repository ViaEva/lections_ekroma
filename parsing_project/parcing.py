import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())
    pages_ul = soup.find('div', class_="vm-pagination").find('ul')
    last_page = pages_ul.find_all('li')[-3]
    total_page = last_page.find('a').get('href').split(',')
    return total_page[-1]

# def get_page_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     product_list = soup.find('div', class_="product vm-col vm-col-1 ")
    

def main():
    nootebooks_url = 'https://enter.kg/computers/noutbuki_bishkek'
    pages = 'results,'
    re = pages + str(get_total_pages(get_html(nootebooks_url)))
    return nootebooks_url + re

lo = BeautifulSoup(main(),'html.parser')
print(lo.prettify())
