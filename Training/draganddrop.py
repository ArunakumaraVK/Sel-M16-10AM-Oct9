import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)
ac_obj = ActionChains(driver)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
ele = driver.find_element(By.XPATH, '//h2[text()="SVG Elements"]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

draggable_ele = driver.find_element(By.XPATH, '//div[@id="draggable"]')
droppable_ele = driver.find_element(By.XPATH, '//div[@id="droppable"]')

ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

