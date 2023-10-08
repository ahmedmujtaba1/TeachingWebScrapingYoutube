import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://pk.sapphireonline.pk/collections/woman?page=2&gclid=Cj0KCQjwqs6lBhCxARIsAG8YcDjm3EhUXNa6aCm1DC-kFdRf_8D-0wpI6HRPEZsccEEavb8Po21SGToaAg8gEALw_wcB')
soup = bs(r.content, 'html.parser')
# print(soup)

title_list = soup.find_all('h3', {'class' : "t4s-product-title"})
price_list = soup.find_all('div', {'class' : "t4s-product-price"})
print(len(price_list),len(title_list))
for i in range(len(title_list)):
    product_title = title_list[i].find('a').text
    print("Title : ",product_title)
    product_price = price_list[i].find('span').text
    print("Price : ", product_price)