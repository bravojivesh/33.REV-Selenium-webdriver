from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")


times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li time")
#you need a unique way of identifying an element. Here it is ".event>li>time" (similar to file location in
#the computer)

print(times)
for x in times:
    print(x)
    print(x.text)


driver.quit()
