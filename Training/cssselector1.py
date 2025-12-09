import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.facebook.com/signup")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

##driver.minimize_window()
##time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

print(driver.current_url)
time.sleep(2)

print(driver.title)
time.sleep(1)

#print(driver.page_source)
#time.sleep(2)

print(driver.name)
time.sleep(1)

driver.find_element("css selector","input[name='firstname']").send_keys("arun")
time.sleep(3)
driver.find_element("css selector","input[name='lastname']").send_keys("V K")
time.sleep(3)
driver.find_element("css selector","input[value='2']").send_keys("V K")
time.sleep(3)
driver.find_element("css selector","input[name='reg_email__']").send_keys("9380954655")
time.sleep(3)
driver.find_element("css selector","input[id='password_step_input']").send_keys("Qwertyuiop@431")
time.sleep(2)
driver.find_element("css selector","button[name='websubmit']").click()