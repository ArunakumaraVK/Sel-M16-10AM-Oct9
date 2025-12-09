import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.fed_cm import click_dialog_button

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
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

men = take_name = driver.find_element("xpath",'//a[@data-group="men"]')
print(men.text)
time.sleep(2)
women = driver.find_element("xpath",'//a[@data-group="women"]')
time.sleep(1)
print(women.get_attribute('href'))
print(women.get_attribute('data-type'))

