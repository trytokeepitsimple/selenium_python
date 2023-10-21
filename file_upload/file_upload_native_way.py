from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class FileUpload():

    def run(self):
        baseURL = 'https://www.file.io/'
        service = Service(executable_path='../drivers/chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(1)

        #pick element
        element = driver.find_element(By.ID , "upload-button")
        #file path using send keys
        element.send_keys("/home/devslane-75/Pictures/download.jpeg")
        time.sleep(10)
        driver.quit()



sc = FileUpload()
sc.run()