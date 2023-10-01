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

        #elements selection
        radioBtns = driver.find_elements(By.XPATH,"//input[@type='radio' and contains(@name,'cars')]")
        size = len(radioBtns)

        for btn in radioBtns:
            selected = btn.is_selected()

            if not selected:
                btn.click()
                time.sleep(3)

run_element_check = WebElements()
run_element_check.run()