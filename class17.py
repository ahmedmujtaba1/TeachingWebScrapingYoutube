from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

#------------------INIT--------------------#

sofascore_login = "https://www.sofascore.com/user/login"
path = r"B:\VPNs\Buster"


#--------------------------------# 
# ----- - - --  --- BOT ------------------- #


chrome_options = webdriver.ChromeOptions()
# chrome-states.com 
chrome_options.add_argument(f'--load-extension={path}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")
driver.execute_script(f"window.open('{sofascore_login}');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
time.sleep(5000)