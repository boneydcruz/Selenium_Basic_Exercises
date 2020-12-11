from selenium import webdriver

# Taking input from user
search_string = input("Input the URL or string you want to search for:")

browser = webdriver.Firefox()
browser.get('http://www.google.com/')

matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=")
browser.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3/span').click()
browser.implicitly_wait(3000)
#browser.quit()
