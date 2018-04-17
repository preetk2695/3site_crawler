from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait

driver = webdriver.Chrome()
driver.get("http://www.snapdeal.com")


elem = driver.find_element_by_name("keyword")
elem.clear()
elem.send_keys("shoes")
elem.send_keys(Keys.RETURN)
wait(driver,10)
result_list = driver.find_element_by_class_name("ref-freeze-reference-point")
name = result_list.find_elements_by_class_name("product-title")
for names in name:
    print(names.text)
