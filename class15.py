import requests, csv
from bs4 import BeautifulSoup as bs
from googletrans import Translator
translator = Translator()

total_product_scrape = 0
headers = {"Accept-Language": "en-US,en;q=0.5"}
user_input = int(input("How much pages you have to scrape : "))
for page in range(user_input):
    r = requests.get(f'https://www.dsioan.gr/members/home/page:{page}', headers=headers)
    soup = bs(r.content, 'html.parser')
    members_container = soup.find_all('div', attrs={'class' : 'member'})
    for member in members_container:
        total_product_scrape += 1
        print("total Product Scrape : ", total_product_scrape)
        title = member.find('a').text
        detected_language = translator.detect(title)
        title = translator.translate(title, src=detected_language.lang, dest='en')
        title = title.text
        print(title)
        with open('output.csv', 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([title])

