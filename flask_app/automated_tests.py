from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("http://127.0.0.1:5000 ")
driver.maximize_window()
# driver.implicitly_wait(20)
print(driver.title)
# continue_link = driver.find_element(By.TAG_NAME, "article")

home_link = driver.find_element(By.LINK_TEXT, 'Home')
home_link.click()

driver.implicitly_wait(20)
print(home_link)
driver.close()

