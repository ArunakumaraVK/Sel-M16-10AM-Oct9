
# Action chain class : mouse and keyboard operations(that is low level operations) like double click, mouse hover, scrolling, drag and drop, right click
#action chains is a class used to perform on the low level operations
# Keys class:

# Doule click: using move_to_element() we will perform mouse hover action in selenium.(here we have to move the cursor on to the elements so er use that move_to_element method.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)
ac_obj = ActionChains(driver)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

copy_ele = driver.find_element("xpath",'//button[text()="Copy Text"]')
ac_obj.double_click(copy_ele).perform()     # double_click() is used to right click operation.
name = driver.find_element('xpath',"//label[text()='Name:']")
ac_obj.double_click(name).perform()
