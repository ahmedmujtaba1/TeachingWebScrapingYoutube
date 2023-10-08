import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://pk.sapphireonline.pk/collections/woman?page=2&gclid=Cj0KCQjwqs6lBhCxARIsAG8YcDjm3EhUXNa6aCm1DC-kFdRf_8D-0wpI6HRPEZsccEEavb8Po21SGToaAg8gEALw_wcB')
soup = bs(r.content, 'html.parser')
# print(soup)

title_list = soup.find_all('h3', {'class' : "t4s-product-title"})
price_list = soup.find_all('div', {'class' : "t4s-product-price"})
product_url_list = soup.find_all('div', {'class': 't4s-product-wrapper'})
print(len(price_list),len(title_list),len(product_url_list))
for i in range(len(title_list)):
    product_title = title_list[i].find('a').text
    print("Title : ",product_title)
    product_price = price_list[i].find('span').text
    print("Price : ", product_price)
    product_url = product_url_list[i].find('a')['href'] 
    product_url = "https://pk.sapphireonline.pk/collections/woman/" + str(product_url)
    print("Product Url : ", product_url)
    r2 = requests.get(url=product_url)
    soup2 = bs(r2.content, 'html.parser')
    sku_list = soup2.find_all('div', { 'class' : "t4s-sku-wrapper" })
    product_details_list = soup2.find_all('section' , {'id' : "content1"})
    for x in range(len(sku_list)):
        sku = sku_list[x].find('h3').text
        print("SKU : ", sku)
        product_details = []
        for c in product_details_list:
            product_details.append(c.text)
        product_details = str(product_details).replace('[','')
        product_details = str(product_details).replace(']','')
        product_details = str(product_details).replace("'",'')
        print("Product Details : ", product_details)
        
    