from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait

driver = webdriver.Chrome()
driver.get("http://www.amazon.in")


elem = driver.find_element_by_name("field-keywords")
elem.clear()
elem.send_keys("mobiles")
elem.send_keys(Keys.RETURN)
wait(driver,10)
result_list = driver.find_element_by_id("s-results-list-atf")
print(result_list.text)



