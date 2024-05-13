#JH:
#May 12, 2024:-- looks like the issue is #store div. Coz after buying cursor, 1 appeared. So it is impacting the list.
#"1" became the new item on the list. And logic is trying to de-assemble 1.
#May 13, 2023:
#=== StaleItemException-- I spent too much time. Revisit later.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start_time=time.time() #starting point
time_out=start_time+5 #5 seconds ahead

#to leave the window open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

obj_text_list=[]
price_list=[]

list_to_buy_object = driver.find_elements(By.CSS_SELECTOR, value="#store div")  # returns a list of objects
print ("length of objects:", len(list_to_buy_object))

for x in list_to_buy_object:
    obj_text_list.append(x.text)
print (obj_text_list)

for item in obj_text_list:
    if item!="":
        price= item.split(" - ")[1].split("\n")[0]
        print (price)
        price_without_commma = int(price.replace(",",""))
        price_list.append(price_without_commma)

    else:
        continue

print (price_list)
print ("length of price list:", len(price_list))

total_time_to_run=time.time()+5

cookie_to_click = driver.find_element(By.ID, value="cookie")

while time.time()< total_time_to_run:
    cookie_to_click.click()  # keep clicking

cookie_count_STR = int(driver.find_element(By.ID, value="money").text)
cookie_count = int(cookie_count_STR)

print(cookie_count)

for x in price_list:
    if cookie_count > x:
        ind=price_list.index(x)
        list_to_buy_object[ind].click()





