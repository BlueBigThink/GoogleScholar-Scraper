import os
import requests
import csv
import asyncio
from bs4 import BeautifulSoup
from colorama import Fore, Back

class Scraper:
    def __init__(self):
        self.keys = []
        self.query = ''
        self.page = 0
        self.count = 20
        try:
            os.mkdir('output')
        except FileExistsError:
            pass

    def add_key(self, key : str) -> None:
        self.keys.append(key)

    def build_query(self) -> None:
        query = 'https://scholar.google.com/scholar?hl=en&as_sdt={}%2C5&q='
        insertQuery = ''
        idx = 0
        for key in self.keys:
            idx += 1
            insertQuery += key
            if idx != len(self.keys):
                insertQuery += '+'
        query += insertQuery
        query += '&hl=en&as_sdt=0,5'
        self.query = query

    def get_data(self, page:int = 0) -> None:
        self.page = page
        while(self.count > 0):
            query = self.query.format(self.page * 10)
            self.page += 1
            print(Fore.GREEN + query)
            self.count -= 1

async def main():
    scraper = Scraper()
    scraper.add_key('carbon')
    scraper.add_key('footprint')
    scraper.add_key('of')
    scraper.add_key('Silicone')
    scraper.build_query()
    scraper.get_data(1)

if __name__ == '__main__':
    asyncio.run(main())