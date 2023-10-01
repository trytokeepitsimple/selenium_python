from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.select import Select


class WebElements():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10);

        #elements selection
        selecttagelement = driver.find_element(By.ID,"carselect")
        print("element got captured")
        selelm = Select(selecttagelement)


        #select by value -
        a = selelm.select_by_value("benz")
        print("Benz is selected")
        time.sleep(2)


        #select by FaceValue

        b=selelm.select_by_visible_text("BMW")
        print("BMW is selected via visible text")
        time.sleep(2)


        #select by index

        c = selelm.select_by_index("2")
        print("Honda will be selected by index value in string form")
        time.sleep(2)

        #select by index value - numeric index
        d = selelm.select_by_index(0)
        print("BMW will be selected by numeric index value ")
        time.sleep(2)

run_element_check = WebElements()
run_element_check.run()