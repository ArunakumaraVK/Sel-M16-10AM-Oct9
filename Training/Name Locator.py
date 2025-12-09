import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login%20Oct%2015%2C%2011%3A48%20AM")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.find_element('name','firstname').send_keys('Arunakumara')
time.sleep(2)
driver.find_element('name','lastname').send_keys('V K')
time.sleep(2)
driver.find_element('name','reg_email__').send_keys('arunvasudev656@gmail.com')
time.sleep(2)
driver.find_element('name','reg_passwd__').send_keys("Qwertyuiop@123")
time.sleep(2)
driver.close()