from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv
import undetected_chromedriver as uc

#------------------INIT--------------------#

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Product Title', 'Product URL', 'Data-ASIN','Price','In Stock','Brand Name','Rating','Details',"Shipment"])

#--------------------------------# 
# ----- - - --  --- BOT ------------------- #

options = webdriver.ChromeOptions()

#Maximize Your Window

options.add_argument('--start-maximized')

# Headless --> Open Chrome but you can accessible.
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')

print('[info] Hello, User!')
keyword = input('[details] Please tell me the keyword to scrape? : ')
total_pages = int(input('[details] Please tell me the how many pages to scrape? : '))
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)
print("[+] Getting the url.")
driver.get(f"https://www.amazon.com/s?k={keyword.replace(' ','+')}&ref=nb_sb_noss_2")
time.sleep(4.2)
total_product_no = 0
num = 0
page_no = 1
product_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-component-type="s-search-results"]//div[@data-component-type="s-search-result"]')))
print(f"[info] Product Found : {len(product_list)}")
for x in range(total_pages):
    for producT in product_list:
        total_product_no += 1
        num += 1
        try:
            data_asin = producT.get_attribute('data-asin')
        except:
            data_asin = ''
        product_url = driver.find_element(By.XPATH, f'(//span[@data-component-type="s-search-results"]//div[@data-component-type="s-search-result"]//h2//a)[{num}]').get_attribute('href')
        title = driver.find_element(By.XPATH, f'(//div[@data-component-type="s-search-result"]//h2)[{num}]').text
        try:
            price = str(driver.find_element(By.XPATH, f'(//div[@data-component-type="s-search-result"]//span[@class="a-price"])[{num}]').text).replace("\n",".")
        except: price = ""
        driver.execute_script(f"window.open('{product_url}');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(4.5)
        # in_stock = False
        try:
            text_stock = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='availability']//span"))).text
            if "In Stock" in str(text_stock):
                in_stock = True
            else:
                in_stock = False
        except Exception:
            in_stock = False
        try:
            rating = driver.find_element(By.XPATH,"(//span[@id='acrPopover']//span//span)[1]").text
            rating = f"{rating} out of 5"
        except:
            rating = ''

        review_url = product_url.replace('dp','product-reviews')

        try:
            brand_bio_link= driver.find_element(By.XPATH,"//a[@id='bylineInfo']").text
            brand_name = str(brand_bio_link).split('Visit the')[1].replace(' Store', '').replace(' ','')
        except:
            brand_bio_link = ''
            brand_name= ''
        
        try:
            shipment = driver.find_element(By.XPATH,"(//div[@class='offer-display-feature-text']//span)[1]").text
        except: shipment = ''

        detail_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='feature-bullets']//ul//li")))
        description = []
        y = 0
        for x in range(len(detail_list)):
            y += 1 
            detail = driver.find_element(By.XPATH,f"(//div[@id='feature-bullets']//ul//li//span)[{y}]").text
            description.append(str(detail)+' ')
        description = str(description).replace(',','').replace('[','').replace(']','')
        print(f"[info] Title : ", title)
        print(f"[info] Product URL : ", product_url)
        print(f"[info] Data-Asin : {data_asin}")
        print(f"[info] Price : {price}")
        print(f"[info] In Stock : {in_stock}")
        print(f"[info] Brand Name : {brand_name}")
        print(f"[info] Rating : {rating}")
        print(f"[info] Shipment : {shipment}")
        print(f"[info] Description : {description}")
        with open('output.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([title, product_url, data_asin, price, in_stock, brand_name, rating, description, shipment])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1) 
        print("[+] ------------------------------")
        if num == len(product_list):
            # wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"))).click()
            driver.get(f'https://www.amazon.com/s?k=keyboard&ref=nb_sb_noss&page={page_no}')
            page_no += 1
            num = 0
            print(f"[info] Moving to page no {page_no}")
            time.sleep(2.2)
            break