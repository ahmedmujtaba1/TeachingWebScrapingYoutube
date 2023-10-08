import requests, csv
from bs4 import BeautifulSoup as bs
from googletrans import Translator
translator = Translator()
# r = requests.get("http://books.toscrape.com/catalogue/page-1.html")
# soup = bs(r.content, 'html.parser')
# product_scrape = 0
# page_scrape = 0
# total_product_number = 0
# pagination_text = str(soup.find('li', attrs={"class" : "current"}).text)
# pagination_text = int(pagination_text.split('of')[1].replace(' ', '').replace('\n',''))
# for page in range(pagination_text):
#     product_details_container = soup.find_all("article", attrs={'class' : 'product_pod'})
#     if len(product_details_container) != product_scrape:
#         for product_details in product_details_container:
#             print("Product Scrape : ",  product_scrape)
#             total_product_number += 1
#             print("Total Product Number : ",  total_product_number)
#             product_scrape += 1
#             title = product_details.find('h3').text
#             price = product_details.find('')
#             print(title)
#             print("-------------------------")
#     else:
#         page_scrape += 1
#         print(f"-------Page no {page_scrape}---------")
#         r = requests.get(f"http://books.toscrape.com/catalogue/page-{page_scrape}.html")
#         product_scrape = 0


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

