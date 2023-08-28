from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)


element_by_id = driver.find_element(By.ID, "radio-btn-example")
if element_by_id is not None:
    print("Element by ID Captured Successfully")

element_by_name = driver.find_element(By.NAME, "enter-name")
if element_by_name is not None:
    print("Element By Name Captured Successfully")

    