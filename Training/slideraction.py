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

slider = driver.find_element(By.XPATH, '(//div[@id="slider-range"]/span)[1]')
# Move the slider right by 100 pixels
ac_obj.click_and_hold(slider).move_by_offset(100,0).release().perform()

time.sleep(2)
# Move the slider left by 100 pixels
ac_obj.click_and_hold(slider).move_by_offset(-100,0).release().perform()