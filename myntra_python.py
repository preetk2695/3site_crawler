from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait

driver = webdriver.Chrome()
driver.get("http://www.myntra.com")


elem = driver.find_element_by_class_name("desktop-searchBar")
elem.clear()
elem.send_keys("shoes")
elem.send_keys(Keys.RETURN)
wait(driver,10)
result_list = driver.find_element_by_id("desktopSearchResults")
print(result_list.text)
