from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

#------------------INIT--------------------#

rapid_api_signup = "https://rapidapi.com/auth/sign-up?referral=/hub"
path = r"B:\VPNs\Buster"

#--------------------------------# 
# ----- - - --  --- BOT ------------------- #


chrome_options = webdriver.ChromeOptions()
# chrome-states.com 
chrome_options.add_argument(f'--load-extension={path}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get(rapid_api_signup)
time.sleep(12)
driver.find_element(By.ID,"signup-form_username").send_keys("ahmedowowkeoelkel")
time.sleep(1)
driver.find_element(By.ID,"signup-form_email").send_keys("ahmedowowkeoelkel@gmail.com")
time.sleep(1)
driver.find_element(By.ID,"signup-form_password").send_keys("ahmedowowkeoelkel12@SS")
# driver.execute_script(f"window.open('{sofascore_login}');")
driver.find_element(By.XPATH,"//span[text()='Sign Up']/..").click()
# # Switch to the new window
# driver.switch_to.window(driver.window_handles[1])
time.sleep(5000)