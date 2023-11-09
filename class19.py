from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

#------------------INIT--------------------#



#--------------------------------# 
# ----- - - --  --- BOT ------------------- #

options = uc.ChromeOptions()
# options.headless = False

#Maximize Your Window
options.add_argument('--start-maximized')

# Headless --> Open Chrome but you can accessible.
# options.add_argument('--headless')
print('[+] Hello, User!')
user_input = int(input('[+] How many emails you want? : '))
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get("https://mail.tm/en/")
print("----------BOT STARTING-------------")
time.sleep(7)
for i in range(user_input):
    button = driver.find_element(By.ID,"accounts-menu")
    button.click()
    time.sleep(2)
    print("[+] Clicked the Button !")
    print("[+] Getting the Email")
    email = driver.find_element(By.XPATH,"//div[@id='accounts-list']//div//div//p[2]").text
    email = email.replace(' ','')
    print(f"Email [{i}] : ", email)
    driver.find_element(By.ID,"logout").click()
    driver.find_element(By.ID,"logout").click()
    time.sleep(4)