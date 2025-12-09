#file uploading
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

prefs={
"download.default_directory":"C:\\Users\arunv\PycharmProjects",
"download.prompt_for_download": False,
"safebrowsing.enabled": True,
"plugins.always_open_pdf_externally": True,
}

opts.add_experimental_option("prefs", prefs)

driver= webdriver.Chrome(opts)

driver.get("https://demoqa.com/upload-download")
time.sleep(2)



driver.find_element('xpath',"//a[text()='Download']").click()