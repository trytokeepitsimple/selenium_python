from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class A():

    def method(self):
     baseURL = 'https://www.letskodeit.com/practice'
     service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
     driver = webdriver.Chrome(service=service)
     driver.get(baseURL)
     driver.maximize_window()
     driver.implicitly_wait(10);

    #login btn
     LoginBtn = driver.find_element(By.XPATH,"//a[@href='/login']")
     LoginBtn.click()


     #email field
     email_field = driver.find_element(By.ID, 'email')
    #password field
     password_field = driver.find_element(By.ID, 'login-password')


     email_field.send_keys('test')
     time.sleep(3)
     password_field.send_keys('password')
     time.sleep(3)


     email_field.clear()
     time.sleep(3)
     password_field.clear()
     time.sleep(3)

     driver.quit()


run_class = A()
run_class.method()

