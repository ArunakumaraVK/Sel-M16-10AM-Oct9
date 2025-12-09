import time
from selenium import webdriver
from selenium.webdriver import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.udemy.com/")
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
time.sleep(2)

#print(driver.page_source)
#time.sleep(2)

print(driver.name)
time.sleep(2)


driver.find_element("link text","Sign up").click()
time.sleep(2)
driver.find_element("id","form-group--1").send_keys("arunakumara")
time.sleep(2)
driver.find_element("id","form-group--3").send_keys("arunakumara@gmail.com")
time.sleep(2)
driver.find_element("class name","ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-otp-verification-form--submit-button--ovzq1").click()