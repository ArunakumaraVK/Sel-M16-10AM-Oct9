import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
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

driver.find_element("xpath","//a[text()='Register']").click() #text() function
time.sleep(3)
driver.find_element("xpath","//input[@id='gender-female']").click()
time.sleep(2)
driver.find_element("xpath","//input[@name='FirstName']").send_keys("Arunakumara")
time.sleep(2)
driver.find_element("xpath","//input[@id='LastName']").send_keys("V K")
time.sleep(2)
driver.find_element("xpath","//input[@name='Email']").send_keys("arunvasudev656@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='register-button']").click()
time.sleep(2)
driver.find_element("xpath","//span[text()='Wishlist']").click() #text() function

