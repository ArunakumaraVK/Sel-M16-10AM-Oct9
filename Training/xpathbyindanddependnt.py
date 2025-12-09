'''import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.fed_cm import click_dialog_button

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.makemytrip.com/")
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

driver.find_element("xpath",'//span[text()="Departure"]').click()
while True:
    try:
        driver.find_element("xpath",'//div[text()="August 2026"]/../..//p[text()="15"]').click()
    except:
        driver.find_element('xpath','//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click()'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Setup Chrome
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# Open MakeMyTrip
driver.get("https://www.makemytrip.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(4)

# --- Step 1: Close login popup (overlay) ---
# This popup blocks clicks on "Departure"
ActionChains(driver).move_by_offset(10, 10).click().perform()
time.sleep(2)

# --- Step 2: Print some info ---
print("Current URL:", driver.current_url)
print("Title:", driver.title)
print("Browser Name:", driver.name)
time.sleep(1)

# --- Step 3: Click on Departure ---
departure = driver.find_element(By.XPATH, '//span[text()="Departure"]')
driver.execute_script("arguments[0].click();", departure)
time.sleep(2)

# --- Step 4: Select date (15 August 2026) ---
while True:
    try:
        date_to_select = driver.find_element(By.XPATH, '//div[text()="August 2026"]/../..//p[text()="15"]')
        date_to_select.click()
        print("✅ Selected 15 August 2026")
        break
    except:
        next_btn = driver.find_element(By.XPATH, '//span[@aria-label="Next Month"]')
        next_btn.click()
        time.sleep(1)

# --- Step 5: Optional browser actions ---
time.sleep(3)
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)

print("✅ Script executed successfully!")
driver.quit()



