# Install the Selenium library first
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace 'your_url' with the actual URL of your website
url = ''

# Set up the Chrome WebDriver (make sure chromedriver.exe is in your system path or specify its path)
driver = webdriver.Chrome(executable_path='"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"')  # Update with the correct path

try:
    # Open the website
    driver.get(url)

    # Simulate some user interactions
    search_box = driver.find_element("name", "q")  # Replace "q" with the actual name attribute of the search box
    search_box.send_keys("Selenium testing")
    search_box.send_keys(Keys.RETURN)

    # You can add more interactions as needed...

    # Wait for a few seconds (optional)
    time.sleep(5)

finally:
    # Close the browser window
    driver.quit()
