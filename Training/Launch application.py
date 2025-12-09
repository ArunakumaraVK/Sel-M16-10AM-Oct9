import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.instagram.com/")
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

##print(driver.page_source)
##time.sleep(2)

print(driver.name)
time.sleep(2)

driver.save_screenshot('FB_Loginpage.png') #can use this to take screenshot and stor it inside the same library ie Training

#driver.save_screenshot(r'C:\Users\arunv\PycharmProjects\Selenium_Training\Files_\FB_LoginPage.png') #Create a Directory folder(Files) inside the project name Selenium_Training and right click on the folder(Files) and take absolute path and paste it inside the take screenshort method.

driver.close()

#driver.quit()