from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)


#link text should always under anchor tag

elements_by_class_name = driver.find_elements(By.CLASS_NAME, "inputs")
length = len(elements_by_class_name)
if elements_by_class_name is not None:
    print("Element by Class Name Captured Successfully "+str(length))

elements_by_tag_name = driver.find_elements(By.TAG_NAME, "a")
length2 = len(elements_by_tag_name)
if elements_by_tag_name is not None:
    print("Element By Tag Name Captured Successfully "+str(length2))

