import time
from selenium import webdriver
from selenium.webdriver import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

for trr in range(2,8):
    for tdd in range(1,5):

        data =  driver.find_element("xpath",f'//table[@name="BookTable"]//tr[{trr}]/td[{tdd}]')
        print(data.text, end=" ")



