from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class WindowSize():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        #driver.maximize_window()
        driver.implicitly_wait(10)

        #find height and width

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Width of screen is " +str(width) + " and Height is "+str(height))

        driver.quit()



window_size = WindowSize()
window_size.run()