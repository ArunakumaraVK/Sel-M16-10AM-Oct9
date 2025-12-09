import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome (opts)
driver.get("https://www.python.org/")

driver.maximize_window()
time.sleep(2)

driver.refresh()
time.sleep(2)


all_links = driver.find_elements('tag Name', 'a')
for link in all_links:
    print(link.get_attribute('href'))


