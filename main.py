import requests
from bs4 import BeautifulSoup


url = ["https://news.ycombinator.com/", 
       "https://news.ycombinator.com/?p=2", 
       "https://news.ycombinator.com/?p=3", 
       "https://news.ycombinator.com/?p=4", 
       "https://news.ycombinator.com/?p=5"]


for link in url:
    response = requests.get(link)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    news_titles = soup.find_all("a")
    
    for news in news_titles:
        if "Python" in news.text:
            print(news.text)
            print(news["href"])
            print()
        if "Replit" in news.text:
            print(news.text)
            print(news["href"])
            print()
        if "JavaScript" in news.text:
            print(news.text)
            print(news["href"])
            print()
        if "CSS" in news.text:
            print(news.text)
            print(news["href"])
            print()
        if "programmer" in news.text:
            print(news.text)
            print(news["href"])
            print()
        if "developer" in news.text:
            print(news.text)
            print(news["href"])
            print()
        if "software" in news.text:
            print(news.text)            
            print(news["href"])
            print()
        if "Heat" in news.text:
            print(news.text)
            print(news["href"])
            print()



    