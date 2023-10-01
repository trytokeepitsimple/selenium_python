from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class Radio_CheckBox():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10);


        #bnwradio
        bmwradio = driver.find_element(By.ID, "bmwradio")
        bmwradio.click()
        time.sleep(2)

        benzradio = driver.find_element(By.ID, "benzradio")
        benzradio.click()
        time.sleep(2)



        #bnwcheckbox
        bmwcheck= driver.find_element(By.ID,"bmwcheck")
        bmwcheck.click()

        benzcheck = driver.find_element(By.ID , "benzcheck")
        benzcheck.click()



        #check which one's are selected using - isSelected() - This will return True or False

        print("BMW radio is selected ? ", bmwradio.is_selected())
        print("Benz radio is selected ? ", benzradio.is_selected())
        print("BMW Checkbox is selected ? ", bmwcheck.is_selected())
        print("Benz Checkbox is selected ? ", benzcheck.is_selected())



run = Radio_CheckBox()
run.run()