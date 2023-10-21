from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
#lib to intercact with file_explorer of system
from pynput.keyboard import Key,Controller

class file_upload:
    def run(self):
        baseURL = 'https://www.plupload.com/examples/'
        service = Service(executable_path='../drivers/chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        element = driver.find_element(By.ID, "uploader_browse")
        element.click()
        #since selenium does not have any control , implict or explict wait would not work
        #that is why we need to add time.sleep() for wait
        time.sleep(5)


        #create keyboard object using controller function
        keyword=Controller()
        #user keyword.type("path_of_file_to_be_selected")
        keyword.type("/home/devslane-75/Pictures/virat_kohli.jpg")
        time.sleep(5)
        #after selecting the file we need to press enter to finish selection
        keyword.press(Key.enter)
        time.sleep(3)
        #because once enter key is pressed , we also need to release it
        keyword.release(Key.enter)
        time.sleep(3)


file_upload = file_upload()
file_upload.run()


