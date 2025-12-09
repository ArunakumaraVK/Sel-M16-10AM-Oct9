import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.find_element('id','user-name').send_keys('standard_user')
time.sleep(2)
driver.find_element('id','password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element('id','login-button').click()
time.sleep(3)
driver.find_element('id','react-burger-menu-btn').click()
time.sleep(3)
driver.find_element('id','logout_sidebar_link').click()
time.sleep(2)
driver.close()
