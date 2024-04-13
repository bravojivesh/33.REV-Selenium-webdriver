from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")


article_count1=driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
article_count2=driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

#---JH:Unlike in the course videos, the search bar was not readily available. So I had to write this code to click on the symbol first, before we send text for searching.
search_SYMBOL=driver.find_element(By.CSS_SELECTOR, ".vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
search_SYMBOL.click()
#-- we can do better and write a code TO only do the above if search bar is missing. But it will more complex than
#needed. In course video the above itself is NOT needed.

search_input=driver.find_element(By.NAME, "search")
search_input.send_keys("Jose",Keys.ENTER)

#time.sleep(3) #i added this on my own. It will wait for 5 seconds right before clicking the link




print ("way1:", article_count1.text)
print ("way2:", article_count2.text)

#driver.quit()
