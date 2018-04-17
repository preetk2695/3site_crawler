from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait

driver = webdriver.Chrome()
driver.get("http://www.snapdeal.in")


elem = driver.find_element_by_name("keyword")
elem.clear()
elem.send_keys("mobiles")
elem.send_keys(Keys.RETURN)
wait(driver,10)
result_list = driver.find_elements_by_class_name("comp comp-right-wrapper ref-freeze-reference-point clear")
print(result_list.text)
