import time
from selenium import webdriver
from ddt.read_excel import reading_testdata

path = r'C:\Users\arunv\OneDrive\Desktop\demo_testdata.xlsx'
data = reading_testdata(path, sheetname='reg')

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(1)

driver.find_element(by='xpath', value='//a[text()="Register"]').click()
time.sleep(1)

driver.find_element(by='id', value='gender-female').click()
driver.find_element(by='id', value='FirstName').send_keys('Ganga')
driver.find_element(by='id', value='LastName').send_keys('Shintre')
driver.find_element(by='id', value='Email').send_keys('ganga@gmail.com')
driver.find_element(by='id', value='Password').send_keys('ganga@12345')
driver.find_element(by='id', value='ConfirmPassword').send_keys('ganga@12345')