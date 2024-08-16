from selenium.webdriver.common.by import By
import time
import login
import duration


xpath_pattern = '//div[contains(@id,"id__")]/div[2]/div/div[3]/a'


start_time = time.time()

# Open a file in write mode
with open('links.txt', 'w') as file:
    while time.time() - start_time < duration.total_duration:
        post_elements = login.driver.find_elements(By.XPATH, xpath_pattern)

        for post_element in post_elements:
            # Extract link and datetime information
            link = post_element.get_attribute("href")
            datetime = post_element.find_element(By.XPATH, './time').get_attribute("datetime")

            # Write the link and datetime information to the file
            # file.write(f"Link: {link}, Datetime: {datetime}\n")
            file.write(f"{link}\n")
            print(f"Link: {link}, Datetime: {datetime}")

        login.driver.execute_script("window.scrollBy(0, 500);") 

        # Wait for a specific duration
        time.sleep(duration.pause_duration)

# Close the file
file.close()

# login.driver.quit()
