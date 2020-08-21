import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

payload_raw = 'https://support.na.sage.com/selfservice/viewdocument.do?noCount=true&externalId=64650&sliceId=1&isLoadPublishedVer=&docType=kc&docTypeID=DT_Article&stateId=3641&cmd=displayKC&dialogID=140247&ViewedDocsListHelper=com.kanisa.apps.common.BaseViewedDocsListHelperImpl&openedFromSearchResults=true'
payload = 'https://support.na.sage.com/selfservice/viewdocument.do?noCount=true&externalId=64650'
payload_ween = "https://www.google.com/ncr"

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--window-size=10,10")
options.add_argument("--test-type")
options.add_argument("--remote-debugging-port=0")
options.add_argument("--headless")

dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

driver = webdriver.Chrome(chrome_options=options, desired_capabilities=dc, executable_path= r'D:\\chromedriver\\chromedriver.exe')


def scrape_page(url):
    driver.get(url) # Load page
    time.sleep(5)

    element = driver.find_element_by_tag_name("body")
    print(element)
    print(element.get_attribute('innerHTML'))

driver.maximize_window()
driver.get("https://www.google.com/ncr")
print (driver.find_element_by_tag_name("body").text)