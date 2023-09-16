from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)

#we can captaure elements using contains keyword
# basic syntax is - //tag[contains(@attribute,'value')]

element_one_contains_keyword = driver.find_element(By.XPATH, "//input[contains(@value,'Hide')]")

if element_one_contains_keyword is not None:
    print("Caught it successfully")

#this is very useful in cases where multiple classes are there in a element but we want to apply one class to identify element
element_two_contains_keyword = driver.find_element(By.XPATH, "//div[contains(@class,'navbar-collapse')]")
if element_two_contains_keyword is not None:
    print("Caught 2 successfully")

