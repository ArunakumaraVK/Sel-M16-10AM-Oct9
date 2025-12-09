import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
#
# def handling_windows():
#     return driver.window_handles
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys('Google pixel9')
#         time.sleep(2)
#         driver.switch_to.window(handling_windows()[0])
#         time.sleep(1)
#
#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'x.com' in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()

#===========================================================================








