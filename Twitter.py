from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import login






xpath_pattern = '//*[contains(@id, "id__")]/div[1]/div/a/div/div[1]/span/span'


account_elements = login.driver.find_elements(By.XPATH, xpath_pattern)

names_list = []


for account_element in account_elements:
    name = account_element.text.strip()
    names_list.append(name)
    
print(names_list)




login.time.sleep(10)

login.driver.quit()