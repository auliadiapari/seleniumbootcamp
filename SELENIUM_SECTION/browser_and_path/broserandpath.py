
#Calling an web browser/driver instance
from selenium import webdriver

#driver support safari/chrome/edge/opera etc.
#driver = webdriver.Chrome(executable_path=thepath/location for the driver)
driver = webdriver.Chrome()

driver.get("https://google.com")