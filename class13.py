# # import requests

# # url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"

# # querystring = {"query":"fiverr","match_email_domain":"true"}

# # headers = {
# # 	"X-RapidAPI-Key": "8da795aa71msh3cee0f5a50328e0p10aa59jsne899580ef625",
# # 	"X-RapidAPI-Host": "website-contacts-scraper.p.rapidapi.com"
# # }

# # response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())

# import requests

# url = "https://twitter135.p.rapidapi.com/AutoComplete/"

# querystring = {"q":"Elon"}

# headers = {
# 	"X-RapidAPI-Key": "8da795aa71msh3cee0f5a50328e0p10aa59jsne899580ef625",
# 	"X-RapidAPI-Host": "twitter135.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())







##################################################################















import requests
from bs4 import BeautifulSoup

headers = {
    "Method" : "GET",
    "Authority" : "www.bikedekho.com",
    "Path" : "/tvs-bikes",
    "Scheme" :  "https" ,
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "max-age" : "0",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0",
}

r = requests.get("https://www.bikedekho.com/tvs-bikes", headers=headers)
if int(r.status_code) == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    bikelist_container =  soup.find('ul', attrs={'class' : 'bikelist'})
    print(bikelist_container)

