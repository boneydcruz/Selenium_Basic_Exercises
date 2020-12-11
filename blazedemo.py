from selenium import webdriver
search_string = input("flight from (Paris/Boston/Portland):")
search_string1 = input("flight to (Rome/London/Berlin):")
browser = webdriver.Firefox()
browser.get('http://www.blazedemo.com/')
browser.find_element_by_name('fromPort').send_keys(search_string)
browser.implicitly_wait(5)
browser.find_element_by_name('toPort').send_keys(search_string1)
browser.implicitly_wait(5)
browser.find_element_by_xpath('/html/body/div[3]/form/div/input').click()
browser.implicitly_wait(5)
browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[1]/input').click()

