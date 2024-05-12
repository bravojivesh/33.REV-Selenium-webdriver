#JH: Core assumptions:
#1) Price for an item is unique. Based on this, the corresponding ID is mapped. And then clicked.

#May 12, 2024:-- looks like the issue is #store div. Coz after buying cursor, 1 appeared. So it is impacting the list.
#"1" became the new item on the list. And logic is trying to de-assemble 1.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time=time.time() #starting point
time_out=start_time+5 #5 seconds ahead

#to leave the window open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

dict0={}
dict={}

while time.time()-start_time < 15: #total time
    cookie_to_click=driver.find_element(By.ID, value="cookie")
    cookie_to_click.click() #keep clicking

    #-------TO go through the items on the right panel------
    #list_to_buy_object=driver.find_elements(By.ID, value="store")
    #-------JH: the above returns ONE object only as ID is always unique. So we have to use by.CSS Selector


    if time_out-time.time() <0: #to check every 5 seconds.
        # DB: print (f"current time is:{time.time()} and timeout is: {time_out}")
        time_out+=5 #if less than 5 seconds, push the check time 5 seconds ahead.
        # print (f"new time out is: {time_out}")
        list_to_buy_object=driver.find_elements(By.CSS_SELECTOR, value="#store b") #returns a list of objects
        print (list_to_buy_object)
        print (len(list_to_buy_object))

        cookie_count_STR = int(driver.find_element(By.ID, value="money").text)
        cookie_count = int(cookie_count_STR)

        price_list = []

        #to extract price from the long string
        for item in list_to_buy_object:
            print("-------Cookie count so far:", cookie_count)

            print ("Current item:", item)
            item_text0=item.text
            item_text= item_text0.replace("\n","")
            ID=item.get_attribute("id")
            print ("item text is:",item_text)
            print (f"the index is: {list_to_buy_object.index(item)}")
            print (f"ID is: {ID}")

            current_element_ID = driver.find_element(By.ID, value=ID)
            if current_element_ID.text == "":
                print("EMPTYYY. NO NEED TO CLICK")
            else:
                print ("Curent element:", current_element_ID.text)
                price= item_text0.split(" - ")[1].split("\n")[0]
                price_without_commma = price.replace(",",
                                                     "")  # for numbers like 2,000, they need to be converted into 2000
                price_int=int(price_without_commma)
                print (f"===the price is {price_int}, and the type is: {type(price_int)}")

                price_list.append(price_int)
                print ("=====the price list:", price_list)
                dict0[current_element_ID]=price_int
                dict[current_element_ID.text]=price_int
                print(f"======the price list is {dict}")

        to_click_VALUE=-1
        to_click_ID=""
        for x,y in dict0.items():
            if cookie_count> y and to_click_VALUE<y:
                to_click_VALUE=y
                to_click_ID=x
        print ("To click", to_click_VALUE)
        print ("to click ID:", to_click_ID)
        print("to click ID TYPE", type(to_click_ID))
        to_click_ID.click()






            #to get the cookie count


            # if item_text!="": #NEED THIS as the last element is empty. So trying to split or replace below will give error
            #     print (" First read after text empty is checked: the item is:", item_text.replace("\n",""))
            #     price= item_text.split(" - ")[1].split("\n")[0]
            # #first split using "-". Then grab the item in [1] index. Split it again using "\n" and gram the first item.This only gives price.
            #     price_without_commma=price.replace(",","") #for numbers like 2,000, they need to be converted into 2000
            #     price_int=int(price_without_commma)
            #     print (f"the price is {price_int}, and the type is: {type(price_int)}")
            #
            #     get_id=item.get_attribute("id")
            #     print (f"Final item after finding ID and price: {item_text.replace("\n","")}, and ID: {get_id} and PRICE IS: {price_int}")
            #
            #    #to get the cookie count
            #     cookie_count=int(driver.find_element(By.ID,value="money").text)
            #
            #     dict[price_int]=get_id
            #     if cookie_count>price_int:
            #         list_of_affordable_prices.append(price_int)
            #
            # else:
            #     print ("=================looks like it is empty:", item_text)
            #
            #
            # print(dict)
            # print ("The list of affordable price: ", list_of_affordable_prices)
            #
            # if len(list_of_affordable_prices)>0:
            #     max1=max(list_of_affordable_prices)
            #     print ("The ID that can be bought is:", dict[max1])
            #     element_to_buy=driver.find_element(By.ID,value=dict[max1])
            #     print (element_to_buy)
            #     element_to_buy.click()
            #     print ("CLICK SUCCESS")

