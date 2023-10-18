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
        driver.implicitly_wait(10)

        #find_login_btn
        login_btn  = driver.find_element(By.XPATH,'//a[@href="/login"]')
        login_btn.click()

        user_name = driver.find_element(By.ID,'email')
        password= driver.find_element(By.ID,'login-password')
        user_name.send_keys('test@email.com')
        password.send_keys('abcabc')

        #file where screenshot is going to be saved
        destinationFile = "dslane-75/Deskto/a.png"

        #save_screenshot(destinationfile)
        try:
            driver.save_screenshot(destinationFile)
            print("ScreenShot Captured Sucessfully")
        except NotADirectoryError:
            print("Directory did not present")



run_element_check = WebElements()
run_element_check.run()