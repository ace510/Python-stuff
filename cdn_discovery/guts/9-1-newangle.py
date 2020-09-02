from confidential import new_preamble
import requests
# import bs4
import selenium
# webby = requests.get(new_preamble)
# BeautySoup = bs4.BeautifulSoup(webby.text,"html5lib")
# print(BeautySoup.prettify())

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--window-size=10,10")
options.add_argument("--test-type")
options.add_argument("--remote-debugging-port=0")
options.add_argument("--headless")

dc = DesiredCapabilities.CHROME
dc["loggingPrefs"] = {"driver": "OFF", "server": "OFF", "browser": "OFF"}

driver = webdriver.Chrome(
    chrome_options=options,
    desired_capabilities=dc,
    executable_path=r"D:\\chromedriver\\chromedriver.exe",
)

driver.get(new_preamble)
