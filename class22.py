from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv
import undetected_chromedriver as uc

#------------------INIT--------------------#

# with open('output/output.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Email'])

#--------------------------------# 
# ----- - - --  --- BOT ------------------- #

options = webdriver.ChromeOptions()

#Maximize Your Window

options.add_argument('--start-maximized')

# Headless --> Open Chrome but you can accessible.
options.add_argument('--headless')
options.add_argument('--log-level=3')

print('[+] Hello, User!')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)
print("[+] Getting the url.")
driver.get("https://www.amazon.com/s?k=keyboard&ref=nb_sb_noss")
time.sleep(4.2)
total_product_no = 0
num = 0
page_no = 1
product_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-component-type="s-search-results"]//div[@data-component-type="s-search-result"]')))
print(f"[+] Product Found : {len(product_list)}")
for x in range(50):
    for producT in product_list:
        total_product_no += 1
        num += 1
        try:
            data_asin = producT.get_attribute('data-asin')
        except:
            data_asin = ''
        title = driver.find_element(By.XPATH, f'(//div[@data-component-type="s-search-result"]//h2)[{num}]').text
        try:
            price = driver.find_element(By.XPATH, f'(//div[@data-component-type="s-search-result"]//span[@class="a-price"])[{num}]').text
        except: price = ""
        print(f"[+] Title : ", title)
        print(f"[+] Data-Asin : {data_asin}")
        print(f"[+] Price : {price}")
        print("[+] ------------------------------")
        if num == len(product_list):
            # wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"))).click()
            driver.get(f'https://www.amazon.com/s?k=keyboard&ref=nb_sb_noss&page={page_no}')
            page_no += 1
            num = 0
            print(f"[+] Moving to page no {page_no}")
            time.sleep(2.2)
            break