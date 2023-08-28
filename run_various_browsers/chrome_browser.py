from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CService

# Path to the ChromeDriver executable
chrome_driver_path = '../drivers/chromedriver_linux64/chromedriver'

#old syntax
# driver = webdriver.Chrome(executable_path=chrome_driver_path)


# Create a Chrome WebDriver instance
#selenium 4 syntax
chrome_service = CService(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Navigate to a website
driver.get('https://www.google.com')

driver.implicitly_wait(100)

# Close the WebDriver
driver.quit()
