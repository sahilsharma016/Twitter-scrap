import csv
import duration
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
from login import driver 
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

def scroll_until_end():
    max_scroll_attempts = 20
    current_scroll_position = 0

    for _ in range(max_scroll_attempts):
        # Store the current scroll position
        previous_scroll_position = current_scroll_position

        # Scroll down to the end of the page
        driver.execute_script("window.scrollBy(0,600);")

        # Wait for a short duration to let the content load
        time.sleep(duration.pause_duration_comment)

        # Get the updated scroll position
        current_scroll_position = driver.execute_script("return window.scrollY;")

        # Check if the scroll position changed
        if current_scroll_position != previous_scroll_position:
            # Scroll position changed, content loaded
            continue
        else:
            # Scroll position didn't change after multiple attempts
            print("Scrolling failed, moving to the next URL.")
            return False

    # If the loop completes without breaking, assume content loaded successfully
    return True

with open('dropped_duplicates.txt', 'r') as file:
    content = file.read()

lines = content.split('\n')

with open('comments.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['link', 'comments']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for line in lines:
        # Open a new tab
        driver.execute_script("window.open();")

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        print("Switched")

        # Open the new window and navigate to the specified URL
        new_window_url = "https://twitter.com/home"
        driver.get(new_window_url)
        print("Navigated to", new_window_url)

        if len(driver.window_handles) >3:
            driver.switch_to.window(driver.window_handles[1])  # Switch to the main tab (1st tab)
            driver.close()

            driver.switch_to.window(driver.window_handles[1])  # After closing the 2nd tab, switch to the 3rd tab
            # driver.close()
           
        try:
            if urlparse(line).hostname is not None:  # Check if the line is a valid URL
                driver.get(line)
                print("Navigated to", line)

                time.sleep(4)
                if not scroll_until_end():
                    while True:
                        try:
                            
                            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Show more replies']"))).click()
                            
                            print("Clicked 'Show more replies'")
                        except:
                            break  # No 'Show more replies' button found, stop looking
                else:
                    print("Scrolled to the end of the page.")

                # Continue with your existing code to find and print comments
                find_comment = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
                print("ggjjjjjjjjjjg")
                for comment in find_comment:
                    writer.writerow({'link': line, 'comments': comment.text})
                print("end")
            else:
                print("Invalid URL:", line)

        except Exception as e:
            print("An error occurred:", str(e))

driver.quit()