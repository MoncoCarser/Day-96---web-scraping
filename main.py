import requests
from bs4 import BeautifulSoup


url = "https://www.yelp.co.uk/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA%2C+United+States"

response = requests.get(url)
html = response.text

print(html)