import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk

def getClipboardText():
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    return root.clipboard_get()

driver = webdriver.Chrome()
driver.get('http://gaqpriisbar01.gs.adinternal.com/Reports/CiscoRealtime')

driver.find_elements_by_tag_name('body')[0].send_keys(Keys.CONTROL + "a")
driver.find_elements_by_tag_name('body')[0].send_keys(Keys.CONTROL + "c")

foo = getClipboardText()
# print(foo)
driver.quit()
foo_out = ''

for i in foo:
    if i not in '\t':
        foo_out += i
    else:
        foo_out += ' '

foo_list = foo_out.split('\n')
foo_dict = dict()

for i in foo_list:
    stump = i.split(' ')
    foo_dict[stump[0]] = stump[1:]

print(foo_dict['BS_SPT_300CRE_SYS_Q_CT'])