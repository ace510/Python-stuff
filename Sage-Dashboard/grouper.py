import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time
import os
import asyncio

# driver = webdriver.Chrome()
with open('.token','r') as file:
    for line in file:
        QQQ_url = str(line)



human_names = {
    'BS_SPT_300CRE_SYS_Q_CT'     : '300 CRE',
    'BS_SPT_300CRE_SYSCCB_Q_CT'  : '300 CRE callbacks',
    'BS_SPT_100CON_Tech_CCB_Q_CT': '100 CON',
    'BS_SPT_50C_Install_EN_Q_CT' : '50 Canada',
    'BS_SPT_50US_ICU_Q_CT'       : '50 US',
    'BS_SPT_50US_ICU_CCB_Q_CT'   : '50 US Callback',
}
# print(human_names['BS_SPT_50C_Install_EN_Q_CT'])

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_argument("--window-size=10,10")
options.add_argument("--test-type")
options.add_argument("--disable-extensions")
options.add_argument("--remote-debugging-port=0")



dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

driver = webdriver.Chrome(chrome_options=options, desired_capabilities=dc, executable_path= "C:\\Users\\IaClark\\OneDrive - Sage Software, Inc\\chromedriver_win32\\chromedriver.exe")

def getClipboardText():
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    return root.clipboard_get()

def screen_scrape(url):
    while True:
        driver.get(url)

        driver_text = driver.find_element_by_tag_name('body').text
    
        # driver.find_elements_by_tag_name('body')[0].send_keys(Keys.CONTROL + "a")
        # driver.find_elements_by_tag_name('body')[0].send_keys(Keys.CONTROL + "c")

        # foo = getClipboardText()
        # print(foo)
        # time.sleep(60)
        # driver.quit()
        
        # foo_out = ''
        #for i in foo:
        #    if i not in '\t':
        #        foo_out += i
        #    else:
        #        foo_out += ' '

        foo_list = driver_text.split('\n')
        foo_dict = dict()

        for i in foo_list:
            stump = i.split(' ')
            if len(stump) == 12:
                foo_dict[stump[0]] = stump[1:]

        return foo_dict

def display_data(input_dict):
    for i in input_dict.keys():
        if i in human_names.keys():
                # print(i)
                # print(human_names[i])
                print('there are %s calls in the %s queue' % (foo_dict[i][0], human_names[i])) 
        time.sleep(10)


def main():
    foo_dict = ''
    error = False
    foo_dict = screen_scrape(QQQ_url)

    while error == False:
        try:
            display_data(foo_dict)
        except AttributeError:
            print('whoops, didn\'t get the data I needed')
            error = True
        time.sleep(1)
        

        
        



if __name__ == "__main__":
    main()