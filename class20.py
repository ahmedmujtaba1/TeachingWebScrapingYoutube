from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv
import undetected_chromedriver as uc

#------------------INIT--------------------#

with open('output/output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Email'])

#--------------------------------# 
# ----- - - --  --- BOT ------------------- #

options = webdriver.ChromeOptions()

#Maximize Your Window

options.add_argument('--start-maximized')

# Headless --> Open Chrome but you can accessible.
options.add_argument('--headless')
options.add_argument('--log-level=3')

print('[+] Hello, User!')
user_input = int(input('[+] How many emails you want? : '))
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)
driver.get("https://mail.tm/en/")
print("----------BOT STARTING-------------")
time.sleep(1.2)
for i in range(user_input):
    button = wait.until(EC.presence_of_element_located((By.ID,"accounts-menu")))
    button.click()
    # time.sleep(2)
    print("[+] Clicked the Button !")
    print("[+] Getting the Email")
    flag = True
    email = ''
    tries = 0
    while flag:
        time.sleep(0.2)
        try:
            email = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='accounts-list']//div//div//p[2]"))).text
        except:
            button = wait.until(EC.presence_of_element_located((By.ID,"accounts-menu")))
            button.click()
            email = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='accounts-list']//div//div//p[2]"))).text
        email = str(email).replace(' ','')
        if "Password:" not in email:
            flag = False
            break
        else:
            tries += 1
            time.sleep(0.3)
            if tries == 3:
                driver.find_element(By.XPATH,'(//div[@aria-labelledby="accounts-menu"]//a/..)[4]').click()

    print(f"Email [{i}] : ", email)
    with open('output/output.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([email])
    try:
        driver.find_element(By.XPATH,'(//div[@aria-labelledby="accounts-menu"]//a/..)[4]').click()
    except:pass
    time.sleep(4)