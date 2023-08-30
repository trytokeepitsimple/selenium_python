from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)


#link text should always under anchor tag

element_by_id = driver.find_element(By.LINK_TEXT, "HOME")
if element_by_id is not None:
    print("Element by Link Text Captured Successfully")

element_by_name = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
if element_by_name is not None:
    print("Element By Partial Link Text Captured Successfully")

