from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class Switch_to_window():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver-linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)


        #click on open window
        time.sleep(2)
        element = driver.find_element(By.ID,"openwindow")
        element.click()
        #to know the handle of current opened winoow
        parentHandle = driver.current_window_handle
        print("Parent Windows is " ,parentHandle)


        #see all available window handles

        handles = driver.window_handles

        for handle in handles:
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                time.sleep(2)
                print("Second Window Handle" ,handle)
                print(driver.current_window_handle)
                element2 = driver.find_element(By.XPATH,"//input[@id='search']")
                element2.send_keys("python")
                time.sleep(2)
                driver.close()
                break
        # switch between windows using handles
        driver.switch_to.window(parentHandle)
        print("Switched back to parent window ",parentHandle,driver.current_window_handle)
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("test executed as intended")




sc = Switch_to_window()
sc.run()