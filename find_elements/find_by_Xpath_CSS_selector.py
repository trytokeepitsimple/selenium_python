from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)

element_by_id = driver.find_element(By.XPATH, "//input[@id='alertbtn']")
if element_by_id is not None:
    print("Element by XPath Captured Successfully")

element_by_name = driver.find_element(By.CSS_SELECTOR, "#confirmbtn")
if element_by_name is not None:
    print("Element By CSS Selector Captured Successfully")

