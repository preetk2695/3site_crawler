from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
driver = webdriver.Chrome()
driver.get("http://www.snapdeal.com")

product_name = input('enter product query')

elem = driver.find_element_by_name("keyword")
elem.clear()
elem.send_keys(product_name)
elem.send_keys(Keys.RETURN)
sleep(5)
result_list = driver.find_elements_by_class_name("product-tuple-listing")


def find_actual_price(product):
    span_tags = product.find_elements_by_tag_name('span')
    for span in span_tags:
        clas = span.get_attribute('class')
        if 'lfloat product-desc-price strike ' in clas:
            return span.text
        else:
            continue
    return 0

all_contents = []
for product in result_list:
    product_item = product.find_element_by_class_name("product-title ")

    price = product.find_element_by_class_name("product-price")
    actual_price = find_actual_price(product)
    try:
        rating = product.find_element_by_class_name("filled-stars")
        ratingValue = rating.get_attribute('style')
        ratingValue = ratingValue.split()[1]
        ratingValue=ratingValue[0:-1]
    except:
        ratingValue= 0
    print(ratingValue)
    # do more here
    # print(product_item.text, price.text, actual_price)
    product_dic = {"name": product_item.text,"discounted price": price.text,"actualprice":actual_price,"rating":ratingValue}
    all_contents.append(product_dic)

if len(all_contents) >0:
    data = pd.DataFrame(all_contents)
    print(data)
    data.to_csv('snapdeal_'+product_name+"_.csv")


#df=pd.DataFrame(all_contents)
#df.to_csv('snapdeal.csv')
driver.quit()