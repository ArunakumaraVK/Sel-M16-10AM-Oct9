import time
from selenium import webdriver
from selenium.webdriver import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
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

driver.find_element("css selector","input[id='Email']").send_keys("arunvasudev656@gmail.com")
time.sleep(3)
driver.find_element("css selector","input[class='password']").send_keys("Qwertyuiop@321")
time.sleep(3)
driver.find_element("css selector","input[class='button-1 login-button']").click()