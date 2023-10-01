from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class WebElements():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10);

        element = driver.find_element(By.ID, "name")
        print("element got captured")
        attributes = element.get_attribute("placeholder")
        print("Value which got captured is "+attributes)



run_element_check = WebElements()
run_element_check.run()