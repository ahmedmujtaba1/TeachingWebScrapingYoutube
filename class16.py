# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# CHrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/ahmedmujtaba1")
time.sleep(3)
username = driver.find_element(By.XPATH,"//span[@class='p-nickname vcard-username d-block']").text
try:
    bio = driver.find_element(By.XPATH,"//div[@class='p-note user-profile-bio mb-3 js-user-profile-bio f4']").text
except:
    bio = ""

try:
    pronouns = driver.find_element(By.XPATH,"//span[@itemprop='pronouns']").text
except:
    pronouns = ""

try:
    followers = driver.find_element(By.XPATH,"//span[@itemprop='pronouns']").text
except:
    followers = ""



print("Username : ",username)
print("Bio : ", bio)
print("Pronouns : ", pronouns)
time.sleep(5000)
