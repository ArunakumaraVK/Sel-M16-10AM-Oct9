import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys  # If want to see Keys varibales first select this statement and clrt+k and ctrl+click on Keys.

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)
ac_obj = ActionChains(driver)
driver.get("https://www.myntra.com/")
time.sleep(2)
ac_obj.send_keys(Keys.END).perform()      #Scroll down
time.sleep(2)
ac_obj.send_keys(Keys.HOME).perform()   #Scroll up