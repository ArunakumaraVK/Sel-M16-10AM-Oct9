import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.instagram.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.refresh()
time.sleep(2)
#driver.find_element(By.NAME, "username").click()
#time.sleep(2)

