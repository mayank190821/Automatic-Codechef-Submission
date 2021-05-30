from selenium import webdriver
from getpass import getpass

# open browser
browser = webdriver.Chrome()
browser.get("http://www.codechef.com")
# enter user name and password
user_name = input("Enter euser name")
passwd=browser.find_element_by_id("edit-pass")
user = browser.find_element_by_id("edit-name")
user.send_keys(user_name)
passwd.send_keys(getpass("enter passwd"))
browser.find_element_by_id("edit-submit").click()
browser.get("http://www.codechef.com/submit/TEST")
browser.find_element_by_xpath('//*[@id="edit-submit"]').click()
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()
with open("arrayAndPeaks.cpp","r") as f:
    code  = f.read()
code_element=browser.find_element_by_id("edit-program")
browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]').click()
code_element.send_keys(code)
browser.find_element_by_id("edit-submit").click()
browser.find_element_by_xpath('//*[@id="ember353"]/div/div[1]/div[2]/div/button').click()