import time
from selenium import webdriver
from selenium.webdriver import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.amazon.in/")
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

'''driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("cricket bat")
time.sleep(3)
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()'''

driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("cricket bat")

