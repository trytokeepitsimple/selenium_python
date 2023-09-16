from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)


#link text should always under anchor tag

element_by_id = driver.find_element(By.CLASS_NAME, "inputs")
if element_by_id is not None:
    print("Element by Class Name Captured Successfully")

element_by_name = driver.find_element(By.TAG_NAME, "a")
if element_by_name is not None:
    print("Element By Tag Name Captured Successfully")

