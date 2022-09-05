import requests
from bs4 import BeautifulSoup
page = requests.get("https://leetcode.com/problemset/all/")
soup = BeautifulSoup(page.content, 'html.parser')

class siteToScrape:
	def_init_(self):
		self.url= 'https://leetcode.com/problemset/all/'
		divContianer = soup.find('div', role="row", index="0")
		link = divContainer.find('a',
