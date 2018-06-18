from selenium import webdriver
from time import sleep

url = "https://opendata.epa.gov.tw"

# to prevent the alert pop up window
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)

broswer = webdriver.Chrome(chrome_options = chrome_options)
broswer.maximize_window()
broswer.get(url)

sleep(3)
broswer.find_element_by_link_text("大氣").click()

sleep(3)
broswer.find_element_by_link_text("PM2.5化學成分監測數據").click()

sleep(3)
broswer.find_element_by_link_text("JSON").click()