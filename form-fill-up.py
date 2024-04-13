from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name_element=driver.find_element(By.NAME, value="fName")
first_name_element.send_keys("Jivesh")

last_name_element=driver.find_element(By.NAME, value="lName")
last_name_element.send_keys("Hamal")

email_element=driver.find_element(By.NAME, value="email")
email_element.send_keys("ggg@gmail.com")

button=driver.find_element(By.CLASS_NAME, value="btn-primary")
button.click()
