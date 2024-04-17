from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time=time.time()

#to leave the window open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

while time.time()-start_time < 2: #total time
    cookie_to_click=driver.find_element(By.ID, value="cookie")
    cookie_to_click.click() #keep clicking

time.sleep(0.5) #sometimes count is off by 1. So keeping this to make sure the count is correct.
cookie_count=driver.find_element(By.ID, value="money")

#-------TO go through the items on the right panel------

#list_to_buy_object=driver.find_elements(By.ID, value="store")
#-------JH: the above returns ONE object only as ID is always unique. So we have to use by.CSS Selector

list_to_buy_object=driver.find_elements(By.CSS_SELECTOR, value="#store div") #returns a list of objects

#To create a list based on the list of objects above, and access text attribute of of the object.
list_to_buy_human=[]
for item in list_to_buy_object:
    list_to_buy_human.append(item.text)

print(list_to_buy_human)

#to extract price from the long string
for item0 in list_to_buy_human:
    if item0 !="": #NEED THIS as the last element is empty. So trying to split or replace below will give error
        price= item0.split(" - ")[1].split("\n")[0]
    #first split using "-". Then grab the item in [1] index. Split it again using "\n" and gram the first item.This only gives price.
        price_without_commma=price.replace(",","")
        price_int=int(price_without_commma)
        print(f"the type so far is: {type(price_without_commma)}", price_without_commma)
        print (f"the type NOW is: {type(price_int)}",price_int)



# print ("Cookie score:", cookie_count.text)
# print ("Start time was:", start_time)
# print ("Current time is:", time.time())
# print ("Cookie/second is:", int(cookie_count.text)/12)
# print(f"length of the object is : {len(list_to_buy_object)}")