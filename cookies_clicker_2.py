#JH: Core assumptions:
#1) Price for an item is unique. Based on this, the corresponding ID is mapped. And then clicked.

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

list_of_affordable_prices = []
dict={}
while time.time()-start_time < 15: #total time
    cookie_to_click=driver.find_element(By.ID, value="cookie")
    cookie_to_click.click() #keep clicking

    #-------TO go through the items on the right panel------
    #list_to_buy_object=driver.find_elements(By.ID, value="store")
    #-------JH: the above returns ONE object only as ID is always unique. So we have to use by.CSS Selector


    if time_out-time.time() <5: #to check every 5 seconds.
        # print (f"current time is:{time.time()} and timeout is: {time_out}")
        time_out+=5 #if less than 5 seconds, push the check time 5 seconds ahead.
        # print (f"new time out is: {time_out}")
        list_to_buy_object=driver.find_elements(By.CSS_SELECTOR, value="#store div") #returns a list of objects
        print (list_to_buy_object)

        #To create a human readable list based on the list of objects above, and access text attribute of of the object.
        list_to_buy_human=[]
        for item in list_to_buy_object:
            list_to_buy_human.append(item.text)
        print(list_to_buy_human)


        #to extract price from the long string
        for item0 in list_to_buy_human:
            print ("raw item is:", item0.replace("\n",""))

            if item0 !="": #NEED THIS as the last element is empty. So trying to split or replace below will give error
                print (" First read: the item is:", item0.replace("\n",""))
                price= item0.split(" - ")[1].split("\n")[0]
            #first split using "-". Then grab the item in [1] index. Split it again using "\n" and gram the first item.This only gives price.
                price_without_commma=price.replace(",","") #for numbers like 2,000, they need to be converted into 2000
                price_int=int(price_without_commma)
                print ("the price is: ", price_int)
                get_id=list_to_buy_object[list_to_buy_human.index(item0)].get_attribute("id")
                print (f"Final item: {item0.replace("\n","")}, and ID: {get_id} and PRICE IS: {price_int}")
                cookie_count=int(driver.find_element(By.ID,value="money").text)
                dict[price_int]=get_id
                if cookie_count>price_int:
                    list_of_affordable_prices.append(price_int)

            else:
                print ("=================looks like it is empty:", item0)


            print(dict)
            print ("The list of affordable price: ", list_of_affordable_prices)

            if len(list_of_affordable_prices)>0:
                max1=max(list_of_affordable_prices)
                print ("The ID that can be bought is:", dict[max1])
                element_to_buy=driver.find_element(By.ID,value=dict[max1])
                print (element_to_buy)
                element_to_buy.click()

