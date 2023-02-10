from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb


driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com')

driver.find_element(By.ID, 'site-header-cart').click()
driver.get('http://demostore.supersqa.com/my-account/')
driver.find_element(By.ID, 'reg_email').send_keys('yorowi1187@breazeim.com')
driver.find_element(By.ID, 'reg_password').send_keys('Riverdale06!')
driver.find_element(By.NAME, 'register').click()

pdb.set_trace()

# NOTE: TO FIND AVAILABLE METHODS JUST DO dir(<variable>)
# Example: dir(driver)
# Example: dir(cart)





