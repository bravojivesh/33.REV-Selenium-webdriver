from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time=time.time()

#to leave the window open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#
driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

while time.time()-start_time < 12:
    cookie_to_click=driver.find_element(By.ID, value="cookie")
    cookie_to_click.click()

time.sleep(1)
cookie_count=driver.find_element(By.ID, value="money")
print ("Cookie score:", cookie_count.text)
print ("Start time was:", start_time)
print ("Current time is:", time.time())
print ("Cookie/second is:", int(cookie_count.text)/12)