import requests
from bs4 import BeautifulSoup

user_query = input("You query to be scraped? : ")
user_query = user_query.replace(' ','%20')

headers = {
    "Authority" : "jooble.org",
    "Method" : "GET",
    "Path" : f"/SearchResult?ukw={user_query}",
    "Scheme" : "https",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "en-US,en;q=0.9",
}

r = requests.get(f"https://jooble.org/SearchResult?ukw={user_query}")
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)
