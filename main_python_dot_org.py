from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li time")
names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
#you need a unique way of identifying an element. Here it is ".event>li>time" (similar to file location in
#the computer)

# #====this block is to show that .find elements reutrns a "list of objects" (webelement)=======
# print (times)
# print (times[0].text) #this will return the first object's text. Note: just doing [0] will return an object
# #we need its text, and not the object.
# print(names[0].text)
# #======================================

#===========way1: using dictionary comprehension
dict1={x:{"time":times[x].text,"name":names[x].text} for x in range(len(times))}

#===========way2: using for loop outside
dict2={}
for x in range(len(times)):
    dict2[x]={"time":times[x].text,"name":names[x].text}

#--
for x in range(len(times)):
    dict2={x:{"time":times[x].text,"name":names[x].text}}

print ("using way1",dict1)
print ("using way2",dict2)

driver.quit()
