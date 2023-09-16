from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

baseURL = 'https://www.letskodeit.com/practice'
service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(baseURL)


#link text should always under anchor tag

#elements_by_xpath = driver.find_element(By.XPATH, "//a[text()='ALL COURSES']").click()
elements_by_xpath = driver.find_element(By.XPATH, "//h1[text()='Practice Page']")

if elements_by_xpath is not None:
    print("Element by Xpath Text Captured Successfully")


