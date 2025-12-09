
# Action chain class: mouse and keyboard operations(that is low level operations) like double click, mouse hover, scrolling(up and down), drag and drop, right click, page up and page down
#action chains is a class used to perform on the low level operations
# Keys class: Is used to define the keyboard operations. variables are define inside this class called class variables

# Mouse hovering operation: using move_to_element() we will perform mouse hover action in selenium.(here we have to move the cursor on to the elements so er use that move_to_element method.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import Act


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)
ac_obj = ActionChains(driver)
driver.get("https://www.myntra.com/")
time.sleep(2)

Women = driver.find_element("xpath",'//a[text()="Women"][1]')
ac_obj.move_to_element(Women).perform()
time.sleep(2)
Kids = driver.find_element("xpath",'//a[text()="Kids"][1]')
ac_obj.move_to_element(Kids).perform()

# write code for hovering cursor on multiple elements bu using loop

