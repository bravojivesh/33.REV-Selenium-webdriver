from selenium import webdriver
from selenium.webdriver.common.by import By

#just to keep the browser open. Too much work, I know!
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.amazon.in/Laws-Power-Robert-Greene-Collection-ebook/dp/B0041G68Z0/ref=sr_1_7?crid=3BCCEPV70NGFJ&dib=eyJ2IjoiMSJ9.silKJjwz_lFk4UkfSccTguBvURDEq7tRC40_nX0sLiCxGq2EPGYgylgJFsicna8YSZZKy3R7LZadJAsczUZCvpDv3UMGKfHcPVkTGYcgL59um21zgeG-o_hvilTGj9TBepGjQpFzxzKBCircvBVHmX_edFcfdJE7DDZfn-piKyfzlrx-Z7QA-E8zHblPUdnpoe2V_XA2Mz7kB315CZKzhA-4Z1eKpgH8q_u948iNLM0.PK5In5lTj1Vmhl4foWPX5vkzWqEmIRyBfEuqGrnHvd4&dib_tag=se&keywords=books&qid=1712509678&sprefix=boo%2Caps%2C266&sr=8-7")

# to find elements in the web-page.
price0=driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[3]/div[1]/div[12]/div[1]/div[4]/di"
                                           "v/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/table/tbody/"
                                           "tr[2]/td[2]/span")

#after finding an element, we can access its attributes
price=price0.text

search_box=driver.find_element(By.XPATH,value="/html/body/div[2]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
#accessing some of its attributes.
print (f"attributes of search box: value={search_box.get_attribute('value')}, autocomplete: {search_box.get_attribute('autocomplete')}")


print ("The find element returns this: ",price0)
print (f"While when we use dot notation '.' to access its attributes: {price}")

driver.quit()