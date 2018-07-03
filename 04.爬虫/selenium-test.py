from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

node = driver.find_elements_by_class_name('a-b-c')

node.send_keys(Keys.CONTROL, 'a')
node.send_keys(Keys.BACKSPACE)
node.send_keys('order123')

wait = WebDriverWait(driver, 10)
wait.until(
    lambda the_driver: the_driver.find_elements_by_class_name('my_body')
)

time.sleep(1)
print driver.page_source