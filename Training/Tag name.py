import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Edge(opts)
driver.get("https://www.amazon.in/")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.find_element('tag Name','input').send_keys('Arunakumara')
time.sleep(2)
driver.find_element('name','lastname').send_keys('V K')
#time.sleep(2)
driver.find_element('className','form-control').send_keys('arunvasudev656@gmail.com')
time.sleep(2)
driver.find_element('className','form-control').send_keys("9380954655")
time.sleep(2)