# The browser and application speed should be matched if not the synchronization concepts will match the speed.
# Explicit, implicit and custom waits are used to handle this.
# Will get "Noelementinteractable" exception


# time.sleep(): It's not a good approach because it has drawbacks like it waits until the specified sec gets over and specifying repeated time.sleep will consume memory and time.


'''   Implicit Wait   '''
import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver=webdriver.Chrome(opts)
# driver.implicitly_wait(30)      # ImplicitWait will be asking browser to wait until the elements gets loaded, not an application.
#
# driver.get("https://www.moneycontrol.com/")

##################################################################################
# '''  Explicit wait      '''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # To reduce the speed of the driver object we use this.

from selenium.webdriver.support import expected_conditions

 opts=webdriver.ChromeOptions()
 opts.add_experimental_option("detach", True)

 driver=webdriver.Chrome(opts)
 wait_ = WebDriverWait(driver, 30)

 driver.get("https://www.moneycontrol.com/")