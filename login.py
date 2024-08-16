# @Don418767293930

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


# Specify the URL of the login page
login_url = "https://twitter.com/i/flow/login"

# Create a new instance of the Chrome WebDriver (you can use other browsers as well)
driver = webdriver.Chrome()
time.sleep(5)


driver.get(login_url)
time.sleep(5)


username_field = driver.find_element(By.CLASS_NAME,"r-30o5oe") 

time.sleep(5)


username_field.send_keys("@Don418767293930")

driver.implicitly_wait(3)

username_field.send_keys(Keys.RETURN)
time.sleep(5)

password_field = driver.find_element(By.NAME,"password") 


password_field.send_keys("Sahil@123")
time.sleep(3)

 # Submit the login form (assuming pressing "Enter" submits the form)
password_field.send_keys(Keys.RETURN)


# stop browser to quit automatically
# time.sleep(15)

# 

""" or uncomment this

input("Press Enter to close the browser...")
driver.quit()

"""


print(driver.current_url)
