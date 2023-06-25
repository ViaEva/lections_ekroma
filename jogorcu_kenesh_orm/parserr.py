# from cgitb import html
# from unittest import result
# import requests
# from bs4 import BeautifulSoup
# from bs4.element import ResultSet,Tag


# class Parser:
#     _HOST = 'http://kenesh.kg/ru/deputy/list/35'

#     def __init__(self) -> None:
#         self.data = []
#         self.soup = lambda html: BeautifulSoup(html,'lxml')
#         last_page = self.get_last_page()
#         for page in range(1, last_page + 1):
#             html = self.get_html(params=f'page={page}')
#             cards = self.get_cards_from_html(html)
#             list_of_deputats = self.parse_data(cards)
#             self.data.extend(list_of_deputats)

#     def get_html(self, params='') -> str:
#         return requests.get(
#             url=self._HOST,
#             params=params
#         ).text

#     def get_cards_from_html(self,html) -> ResultSet:
#         return self.soup(html).find_all('div', class_='dep-item')

#     @staticmethod
#     def parse_data(cards: ResultSet):
#         result = []
#         for card in cards:
#             name = card.find('a', class_='name').text
#             try:
#                 phone = card.find('a', class_='phone-call').find('span').text
#             except:
#                 phone = None
#             try:
#                 email = card.find('a', class_='mail').find('span').text
#             except:
#                 email = None
#             fraction = card.find('div', class_='info').text
#             obj = {
#                 'name': name,
#                 'phone': phone,
#                 'email': email,
#                 'fraction': fraction
#             }
#             result.append(obj)
#         return result

#     def get_last_page(self):
#         html = self.get_html
#         items = self.soup(html).find_all('a', class_='item')
#         return max(map(lambda item: int(item.text.strip()),items))


# if __name__ == '__main__':
#     obj = Parser()
#     print(obj.data)

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet


class Parser:
    __HOST = 'http://kenesh.kg/ru/deputy/list/35'

    def __init__(self):
        self.data = []
        self.soup = lambda html: BeautifulSoup(html, 'html.parser')
        last_page = self.get_last_page()
        for page in range(1, last_page + 1):
            html = self.get_html(params=f'page={page}')
            cards = self.get_cards_from_html(html)
            list_of_deputats = self.parse_data(cards)
            self.data.extend(list_of_deputats)

    def get_html(self, params='') -> str:
        return requests.get(
            url=self.__HOST,
            params=params
        ).text

    def get_cards_from_html(self, html) -> ResultSet:
        return self.soup(html).find_all('div', class_='dep-item')

    @staticmethod
    def parse_data(cards: ResultSet) -> list:
        result = []
        for card in cards:
            name = card.find('a', class_='name').text
            try:
                phone = card.find('a', class_='phone-call').find('span').text
            except:
                phone = None
            try:
                email = card.find('a', class_='mail').find('span').text
            except:
                email = None
            fraction = card.find('div', class_='info').text
            obj = {
                'name': name,
                'phone': phone,
                'email': email,
                'fraction': fraction
            }
            result.append(obj)
        return result

    def get_last_page(self):
        html = self.get_html()
        items = self.soup(html).find_all('a', class_='item')
        return max(map(lambda item: int(item.text.strip()), items))


# if __name__ == '__main__':
#     obj = Parser()
#     print(obj.data)