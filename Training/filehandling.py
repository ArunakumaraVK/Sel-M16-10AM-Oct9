#file uploading
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(2)
driver.refresh()
time.sleep(2)

#single file uploading
'''file_path = r'D:\ARUN SPACE\A.runa_Automation_Resume.pdf'

driver.find_element('xpath',"//input[@id='singleFileInput']").send_keys(file_path)'''

#Multiple files uploading
file1 = r'D:\ARUN SPACE\A.runa_Automation_Resume.pdf'
file2 = r'D:\ARUN SPACE\EXPERIENCE DOCUMENTS\OpenMind_Internship Completion Letter_Aruna Signed_edited.pdf'
file3 = r'D:\ARUN SPACE\EXPERIENCE DOCUMENTS\Nostrum IT Service PVt Ltd\Hike Letter.pdf'
time.sleep(2)
driver.find_element('xpath',"//input[@id='multipleFilesInput']").send_keys(f'{file1}\n{file2}\n{file3}')