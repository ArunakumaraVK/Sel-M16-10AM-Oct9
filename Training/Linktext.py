import time
from selenium import webdriver
from selenium.webdriver import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
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

'''driver.find_element("id","email").send_keys("arunvasudev656@gmail.com")
time.sleep(2)
driver.find_element("name","pass").send_keys("Qwertyuiop@321")
time.sleep(2)
driver.find_element("name","login").click()
time.sleep(6)
driver.close()

#driver.quit()'''

#driver.find_element("name","q").send_keys("Picachu")
#time.sleep(2)
driver.find_element("link text","Flight Bookings").click() #link text()