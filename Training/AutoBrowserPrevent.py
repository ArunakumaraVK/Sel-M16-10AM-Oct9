from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
c_driver=webdriver.Edge(opts)
