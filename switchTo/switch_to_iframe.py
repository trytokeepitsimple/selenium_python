from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class Switch_to_iframe():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)


        #scroll it down
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(5)
        print("step 1 : scroll till last")

        #switch to iframe using ID - ID which is aligned to iframe Tag
        #driver.switch_to.frame("courses-iframe")


        #switch to iframe using name - Name which is aligned to iframe
        #driver.switch_to.frame("iframe-name")

        # switch to iframe using number - we need to pass numbers like we pass for array index and it starts from zero
        # if one iframe is there then we can access it by 0 , if three frames are there then we need to pass 2 to switch to 3rd iframe
        driver.switch_to.frame(0)
        print("Step 2 : Switched into Iframe Window")

        #find element inside the frame
        element = driver.find_element(By.XPATH , "//input[@id='search']")
        time.sleep(2)
        element.send_keys("python")

        #Switch to parent frame
        driver.switch_to.default_content()
        print("Step 3 : Switched back to parent top window")
        driver.execute_script("window.scrollBy(0,-1000);")

        element2 = driver.find_element(By.ID, "name")
        time.sleep(2)
        element2.send_keys("test executed successfully")
        time.sleep(2)
        print("Step 4 : Everything executed as expected")



sc = Switch_to_iframe()
sc.run()