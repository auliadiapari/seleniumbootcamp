from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdb

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com')
time.sleep(3)

## BY CSS
#cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
## BY XPATH
cart = driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a')
cart.click()
time.sleep(2)

## BY CSS
#sample_page = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-2.focus > a')
## BY XPATH
sample_page = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[5]/a')
sample_page.click()
time.sleep(2)

## BY CSS
#my_account = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
## BY XPATH
my_account = driver.find_element(By.XPATH,'//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
my_account.click()
time.sleep(2)

## USERNAME
driver.find_element(By.ID, 'username').click()
time.sleep(1)
driver.find_element(By.ID, 'username').send_keys('auliardd@gmail.com')
time.sleep(1)

## PASSWORD
#driver.find_element(By.ID, 'password').click()
#show_password = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(2) > span > span')
#show_password.click()
#driver.find_element(By.ID, 'username').send_keys('SuperSQA123!')


pdb.set_trace()

#time.sleep(3)
#driver.quit()