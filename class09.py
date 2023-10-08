import requests
from bs4 import BeautifulSoup

request_to_google = requests.get('https://www.google.com')
# print(request_to_google.status_code)
soup = BeautifulSoup(request_to_google.content, 'html.parser')
print(soup)

# 200 code ----> 